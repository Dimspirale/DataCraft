import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model"


def load(name):
    with (MODEL / name).open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


class AgentToProfileMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profiles = load("profiles.yaml").get("profiles", [])
        cls.capabilities = load("capabilities-migrated.yaml").get("capabilities", [])
        cls.migrations = load("migrations-agents.yaml").get("migrations", [])

    def test_01_profile_exists(self):
        self.assertIn("PROFILE-CAD", {x["handle"] for x in self.profiles})

    def test_02_legacy_agent_is_not_profile_handle(self):
        self.assertNotIn("AG01000_CAD", {x["handle"] for x in self.profiles})

    def test_03_three_capability_candidates_exist(self):
        handles = {x["handle"] for x in self.capabilities}
        self.assertTrue({
            "CAP-INGEST-CAD-DATA",
            "CAP-OPTIMIZE-CAD-DATA",
            "CAP-EXPORT-CAD-DATA",
        }.issubset(handles))

    def test_04_capabilities_reference_profile(self):
        for capability in self.capabilities:
            self.assertEqual("PROFILE-CAD", capability.get("profile"))

    def test_05_capabilities_have_no_invented_provider(self):
        for capability in self.capabilities:
            self.assertIsNone(capability.get("provider"))

    def test_06_migration_source_is_legacy_agent(self):
        mig = next(x for x in self.migrations if x["handle"] == "MIG-AG-CAD-001")
        self.assertEqual("AG01000_CAD", mig["source"]["legacy_id"])
        self.assertEqual("AGENT", mig["source"]["legacy_kind"])

    def test_07_migration_is_explicit_1_to_n(self):
        mig = next(x for x in self.migrations if x["handle"] == "MIG-AG-CAD-001")
        self.assertEqual("LEGACY_1_TO_N", mig["migration_type"])
        target_count = len(mig["targets"]["profiles"] + mig["targets"]["capabilities"])
        self.assertGreater(target_count, 1)

    def test_08_no_skill_is_invented(self):
        mig = next(x for x in self.migrations if x["handle"] == "MIG-AG-CAD-001")
        self.assertEqual([], mig["targets"]["skills"])

    def test_09_no_alias_substitution_is_present(self):
        mig = next(x for x in self.migrations if x["handle"] == "MIG-AG-CAD-001")
        self.assertNotIn("alias", mig)
        self.assertIn("NO_ALIAS_FOR_1_TO_N", mig["invariants"])

    def test_10_no_implicit_authority(self):
        profile = next(x for x in self.profiles if x["handle"] == "PROFILE-CAD")
        self.assertNotIn("authority", profile)
        for capability in self.capabilities:
            self.assertNotIn("authority", capability)

    def test_11_no_ad_hoc_profile_or_capability_status(self):
        profile = next(x for x in self.profiles if x["handle"] == "PROFILE-CAD")
        self.assertNotIn("profile_status", profile)
        for capability in self.capabilities:
            self.assertNotIn("capability_status", capability)


if __name__ == "__main__":
    unittest.main()
