#!/usr/bin/env python3
"""DataCraft L2 Model Validation.

Minimal v0.0.1 checks:
- L2-001: Handle uniqueness
- L2-002: canonical ID uniqueness
- L2-003: known kind
- L2-004: Handle / kind consistency

L2 PASS does not imply RuntimeAuthorized.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

import yaml


KNOWN_KIND_PREFIXES = {
    "CAPABILITY": "hdl:cap:",
}


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as stream:
        data = yaml.safe_load(stream)

    if not isinstance(data, dict):
        raise ValueError(f"{path}: model definition must be a YAML object")

    return data


def discover_definitions(model_root: Path) -> list[Path]:
    return sorted(
        path
        for path in model_root.rglob("*.yaml")
        if "schema" not in path.parts
    )


def validate(model_root: Path) -> int:
    paths = discover_definitions(model_root)

    if not paths:
        print(
            f"L2 ERROR: no YAML definitions found under {model_root}",
            file=sys.stderr,
        )
        return 2

    definitions = []

    try:
        for path in paths:
            definitions.append((path, load_yaml(path)))
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"L2 ERROR: {exc}", file=sys.stderr)
        return 2

    errors = []
    handles = defaultdict(list)
    ids = defaultdict(list)

    for path, definition in definitions:
        handle = definition.get("handle")
        canonical_id = definition.get("id")
        kind = definition.get("kind")

        if isinstance(handle, str):
            handles[handle].append(path)

        if isinstance(canonical_id, str):
            ids[canonical_id].append(path)

        if kind not in KNOWN_KIND_PREFIXES:
            errors.append(
                f"L2-003 {path}: unknown kind {kind!r}"
            )
            continue

        expected_prefix = KNOWN_KIND_PREFIXES[kind]

        if not isinstance(handle, str) or not handle.startswith(expected_prefix):
            errors.append(
                f"L2-004 {path}: kind {kind!r} requires handle prefix "
                f"{expected_prefix!r}, got {handle!r}"
            )

    for handle, duplicate_paths in handles.items():
        if len(duplicate_paths) > 1:
            joined = ", ".join(str(path) for path in duplicate_paths)
            errors.append(
                f"L2-001 duplicate handle {handle!r}: {joined}"
            )

    for canonical_id, duplicate_paths in ids.items():
        if len(duplicate_paths) > 1:
            joined = ", ".join(str(path) for path in duplicate_paths)
            errors.append(
                f"L2-002 duplicate id {canonical_id!r}: {joined}"
            )

    if errors:
        print(f"L2 FAIL: {model_root}")

        for error in sorted(errors):
            print(f"- {error}")

        print("ModelValid=false")
        print("RuntimeAuthorized=NOT_EVALUATED")
        return 1

    print(f"L2 PASS: {model_root}")
    print("ModelValid=true")
    print("RuntimeAuthorized=NOT_EVALUATED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the DataCraft model at L2."
    )

    parser.add_argument(
        "model_root",
        nargs="?",
        type=Path,
        default=Path("model"),
        help="Model directory to validate (default: model)",
    )

    args = parser.parse_args()
    return validate(args.model_root)

if __name__ == "__main__":
    raise SystemExit(main())

