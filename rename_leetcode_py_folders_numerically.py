from __future__ import annotations

import argparse
import re
from pathlib import Path


README_NAME = "README.md"
PROBLEM_NUMBER_PATTERN = re.compile(r"\bProblem\s+(\d+)\b", re.IGNORECASE)


def extract_problem_number(readme_path: Path) -> int | None:
	"""Return the LeetCode problem number parsed from a README, if present."""
	try:
		content = readme_path.read_text(encoding="utf-8")
	except UnicodeDecodeError:
		content = readme_path.read_text(encoding="utf-8", errors="ignore")

	match = PROBLEM_NUMBER_PATTERN.search(content)
	if not match:
		return None

	return int(match.group(1))


def build_target_name(current_dir: Path, problem_number: int) -> str:
	"""Create the desired directory name: <number>_<existing_name>."""
	prefix_pattern = re.compile(r"^\d+_")
	if prefix_pattern.match(current_dir.name):
		# Replace the existing numeric prefix to keep reruns idempotent.
		suffix = current_dir.name.split("_", 1)[1]
	else:
		suffix = current_dir.name
	return f"{problem_number}_{suffix}"


def rename_problem_directories(root_dir: Path, dry_run: bool = False) -> tuple[int, int, int]:
	"""Rename immediate child directories using problem numbers from README files."""
	renamed = 0
	skipped = 0
	errors = 0

	for child in sorted(root_dir.iterdir(), key=lambda p: p.name.lower()):
		if not child.is_dir():
			continue

		readme_path = child / README_NAME
		if not readme_path.exists():
			print(f"SKIP: {child} (missing {README_NAME})")
			skipped += 1
			continue

		problem_number = extract_problem_number(readme_path)
		if problem_number is None:
			print(f"SKIP: {child} (could not find 'Problem <number>' in {README_NAME})")
			skipped += 1
			continue

		target_name = build_target_name(child, problem_number)
		target_path = child.with_name(target_name)

		if target_path == child:
			print(f"OK:   {child} (already named correctly)")
			continue

		if target_path.exists():
			print(f"ERROR: cannot rename {child} -> {target_path} (target already exists)")
			errors += 1
			continue

		print(f"RENAME: {child.name} -> {target_name}")
		if not dry_run:
			child.rename(target_path)
		renamed += 1

	return renamed, skipped, errors


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description=(
			"Rename each immediate problem directory to '<problem_number>_<folder_name>' "
			"by reading the problem number from README.md."
		)
	)
	parser.add_argument(
		"directory",
		type=Path,
		help="Directory containing problem folders, e.g. leetcode-py/neetcode-150",
	)
	parser.add_argument(
		"--dry-run",
		action="store_true",
		help="Show what would be renamed without changing anything.",
	)
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	root_dir = args.directory.expanduser().resolve()

	if not root_dir.exists() or not root_dir.is_dir():
		print(f"ERROR: directory does not exist: {root_dir}")
		return 1

	renamed, skipped, errors = rename_problem_directories(root_dir, dry_run=args.dry_run)

	mode = "DRY RUN" if args.dry_run else "DONE"
	print(f"\n{mode}: renamed={renamed}, skipped={skipped}, errors={errors}")
	return 1 if errors else 0


if __name__ == "__main__":
	raise SystemExit(main())
