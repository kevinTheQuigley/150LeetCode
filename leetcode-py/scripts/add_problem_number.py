#!/usr/bin/env python3
"""Rename problem folders to include their LeetCode problem number as a prefix."""

import argparse
import re
import sys
from pathlib import Path


def get_problem_number(readme_path: Path) -> int | None:
    """Extract the problem number from a README.md file."""
    try:
        content = readme_path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r"\*\*LeetCode:\*\*\s*\[Problem\s+(\d+)\]", content)
    if match:
        return int(match.group(1))
    return None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename problem folders to include their LeetCode problem number as a prefix."
    )
    parser.add_argument(
        "--folder",
        "-f",
        required=True,
        help="Path to the parent folder containing problem subdirectories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be renamed without actually renaming.",
    )
    args = parser.parse_args()

    parent = Path(args.folder).resolve()
    if not parent.is_dir():
        print(f"❌ Not a directory: {parent}", file=sys.stderr)
        sys.exit(1)

    renamed = 0
    skipped = 0
    errors = 0

    for subdir in sorted(parent.iterdir()):
        if not subdir.is_dir():
            continue

        name = subdir.name
        readme = subdir / "README.md"

        if not readme.exists():
            print(f"  ⚠️  No README.md in '{name}' — skipping")
            skipped += 1
            continue

        number = get_problem_number(readme)
        if number is None:
            print(f"  ⚠️  Could not find problem number in '{name}/README.md' — skipping")
            skipped += 1
            continue

        # Skip folders that already have the correct prefix
        expected_prefix = f"{number}_"
        if name.startswith(expected_prefix):
            skipped += 1
            continue

        new_name = f"{number}_{name}"
        new_path = parent / new_name

        if new_path.exists():
            print(f"  ❌  Target already exists: '{new_name}' — skipping '{name}'")
            errors += 1
            continue

        if args.dry_run:
            print(f"  [dry-run] {name}  →  {new_name}")
        else:
            subdir.rename(new_path)
            print(f"  ✅ {name}  →  {new_name}")
        renamed += 1

    print(f"\nDone. Renamed: {renamed}, Skipped: {skipped}, Errors: {errors}")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
