#!/usr/bin/env python3
"""DataCraft L1 Schema Validation.

Validates a YAML model definition against a JSON Schema.
This is structural validation only: PASS does not imply ModelValid or
RuntimeAuthorized.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def load_schema(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as stream:
        schema = json.load(stream)
    Draft202012Validator.check_schema(schema)
    return schema


def format_path(parts: list[object]) -> str:
    return ".".join(str(part) for part in parts) or "<root>"


def validate(instance_path: Path, schema_path: Path) -> int:
    try:
        instance = load_yaml(instance_path)
        schema = load_schema(schema_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"L1 ERROR: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )

    if errors:
        print(f"L1 FAIL: {instance_path}")
        for error in errors:
            print(f"- {format_path(list(error.absolute_path))}: {error.message}")
        return 1

    print(f"L1 PASS: {instance_path}")
    print("SchemaValid=true")
    print("ModelValid=NOT_EVALUATED")
    print("RuntimeAuthorized=NOT_EVALUATED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a DataCraft definition at L1.")
    parser.add_argument("instance", type=Path, help="YAML definition to validate")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("model/schema/capability.schema.json"),
        help="JSON Schema path",
    )
    args = parser.parse_args()
    return validate(args.instance, args.schema)


if __name__ == "__main__":
    raise SystemExit(main())
