"""
Build a class name registry from the API reference pages.

Reads all docs/docs/api/by-class/*.md files, extracts the H1 title,
and outputs a JSON mapping of class names to their API page paths.

Usage:
    python3 docs/scripts/build_class_registry.py
"""

import json
from pathlib import Path

DOCS_ROOT = Path(__file__).parent.parent / "docs"
API_DIR = DOCS_ROOT / "api" / "by-class"
OUTPUT_PATH = Path(__file__).parent / "class_registry.json"

# Minimum name length to include (avoids very short names)
MIN_NAME_LENGTH = 4


def build_registry():
    """Build the class name -> API page path mapping."""
    registry = {}
    skipped = {"short": 0, "lowercase": 0, "parenthesized": 0, "index": 0}

    for md_file in sorted(API_DIR.glob("*.md")):
        if md_file.name == "index.md":
            skipped["index"] += 1
            continue

        with open(md_file) as f:
            first_line = f.readline().strip()

        if not first_line.startswith("# "):
            continue

        class_name = first_line[2:].strip()

        # Skip parenthesized names (grammar productions)
        if "(" in class_name:
            skipped["parenthesized"] += 1
            continue

        # Skip lowercase-starting names (singleton objects)
        if class_name and class_name[0].islower():
            skipped["lowercase"] += 1
            continue

        # Skip very short names
        if len(class_name) < MIN_NAME_LENGTH:
            skipped["short"] += 1
            continue

        rel_path = f"api/by-class/{md_file.name}"
        registry[class_name] = rel_path

    return registry, skipped


def main():
    registry, skipped = build_registry()

    with open(OUTPUT_PATH, "w") as f:
        json.dump(registry, f, indent=2, sort_keys=True)

    print(f"Class registry built: {len(registry)} entries")
    print(f"  Skipped short (<{MIN_NAME_LENGTH} chars): {skipped['short']}")
    print(f"  Skipped lowercase: {skipped['lowercase']}")
    print(f"  Skipped parenthesized: {skipped['parenthesized']}")
    print(f"  Skipped index: {skipped['index']}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
