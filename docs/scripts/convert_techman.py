#!/usr/bin/env python3
"""
Convert TADS 3 Technical Manual and T3 VM Spec HTML pages to Markdown.

Reads from: tads-sources/t3doc/techman/
Writes to:  docs/docs/library/, docs/docs/vm-spec/
"""

import sys
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from convert_utils import (
    T3DOC, DOCS_OUT, convert_sysman_page, load_link_registry,
    save_link_registry
)

TECHMAN_DIR = T3DOC / "techman"

# Map techman .htm files to output locations.
# Part I: Fundamentals -> library/ or getting-started/
# Part II: TADS 3 In Depth -> library/
# Part III: Advanced Topics -> library/advanced/
# Part IV: T3 VM Technical Documentation -> vm-spec/

FILE_MAP = {
    # Top-level
    "intro.htm": "library/techman-intro.md",
    "cover.htm": None,  # Skip cover page

    # Part I: Fundamentals
    "fund.htm": None,  # Section divider
    "t3start.htm": "getting-started/creating-first-project.md",
    "t3design.htm": "library/game-design.md",
    "t3des1.htm": "library/design-in-practice.md",
    "t3des2.htm": "library/design-in-theory.md",
    "t3oop.htm": "library/oop-overview.md",
    "t3inout.htm": "library/input-output.md",
    "t3build_config.htm": "tools/build-configurations.md",
    "t3inc.htm": "tools/separate-compilation.md",
    "t3iautohot.htm": "tools/autohotkey.md",
    "gameinfo.htm": "tools/gameinfo.md",

    # Part II: TADS 3 In Depth
    "depth.htm": None,  # Section divider
    "t3messages.htm": "library/messages.md",
    "t3res.htm": "library/actions/action-results.md",
    "t3verchk.htm": "library/actions/verify-check.md",
    "t3verb.htm": "library/actions/creating-verbs.md",
    "t3precond.htm": "library/actions/preconditions.md",
    "t3msg.htm": "library/messages-substitutions.md",
    "t3imp_action.htm": "library/actions/implied-actions.md",
    "t3lister.htm": "library/listers.md",
    "t3tips.htm": "library/tips-system.md",
    "t3actor.htm": "library/actors/dynamic-characters.md",
    "convbkg.htm": "library/actors/conversation-systems.md",
    "t3conv.htm": "library/actors/programming-conversations.md",
    "t3npcTravel.htm": "library/actors/npc-travel.md",
    "t3banner.htm": "library/banner-api.md",

    # Part III: Advanced Topics
    "advtop.htm": None,  # Section divider
    "t3banish.htm": "library/advanced/banishing-messages.md",
    "t3cycle.htm": "library/advanced/command-execution-cycle.md",
    "t3transcript.htm": "library/advanced/transcript.md",
    "t3scope.htm": "library/advanced/scope.md",
    "t3mi.htm": "library/advanced/multiple-inheritance.md",
    "t3staging.htm": "library/advanced/staging-locations.md",
    "t3odd_noun.htm": "library/advanced/odd-noun-phrases.md",
    "t3globalremap.htm": "library/advanced/global-remapping.md",
    "t3past.htm": "library/advanced/past-tense.md",
    "mediatypes.htm": "appendices/mediatypes.md",
    "t3projectStarters.htm": "tools/project-starters.md",

    # Part IV: T3 VM Technical Documentation
    "t3spec.htm": None,  # Section divider
    "t3spec/intro.htm": "vm-spec/intro.md",
    "t3spec/philos.htm": "vm-spec/philosophy.md",
    "t3spec/goals.htm": "vm-spec/goals.md",
    "t3spec/notation.htm": "vm-spec/notation.md",
    "t3spec/model.htm": "vm-spec/machine-model.md",
    "t3spec/metacl.htm": "vm-spec/metaclasses.md",
    "t3spec/opcode.htm": "vm-spec/bytecode.md",
    "t3spec/format.htm": "vm-spec/image-format.md",
    "t3spec/bincode.htm": "vm-spec/binary-encoding.md",
    "t3spec/charmap.htm": "vm-spec/character-mapping.md",
    "t3spec/debug.htm": "vm-spec/debug-records.md",
    "t3spec/fnset_t3.htm": "vm-spec/function-set.md",
    "t3spec/metalist.htm": "vm-spec/metaclass-ids.md",
    "t3spec/save.htm": "vm-spec/save-restore.md",
    "t3spec/tadsspch.htm": "vm-spec/special-characters.md",

    # TOC
    "toc.htm": None,
}


def build_link_registry():
    """Build mapping of old HTML filenames to new Markdown paths."""
    registry = load_link_registry()
    for old_name, new_path in FILE_MAP.items():
        if new_path:
            registry[old_name] = new_path
    return registry


def convert_all():
    """Convert all Technical Manual and VM Spec pages."""
    link_registry = build_link_registry()

    converted = 0
    skipped = 0
    errors = []

    for htm_file, out_path in FILE_MAP.items():
        if out_path is None:
            skipped += 1
            continue

        src = TECHMAN_DIR / htm_file
        if not src.exists():
            print(f"  WARNING: Source file not found: {src}")
            errors.append(htm_file)
            continue

        dst = DOCS_OUT / out_path
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            title, markdown = convert_sysman_page(src, link_registry, output_path=out_path)
            with open(dst, "w", encoding="utf-8") as f:
                f.write(markdown)
            converted += 1
            print(f"  OK: {htm_file} -> {out_path}")
        except Exception as e:
            print(f"  ERROR: {htm_file}: {e}")
            import traceback
            traceback.print_exc()
            errors.append(htm_file)

    # Copy images
    images_dir = DOCS_OUT / "assets" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    for img in TECHMAN_DIR.glob("*.gif"):
        shutil.copy2(img, images_dir)
    for img in TECHMAN_DIR.glob("*.jpg"):
        if img.name != "topbar.jpg":
            shutil.copy2(img, images_dir)
    # t3spec images
    t3spec_dir = TECHMAN_DIR / "t3spec"
    if t3spec_dir.exists():
        for img in t3spec_dir.glob("*.gif"):
            shutil.copy2(img, DOCS_OUT / "vm-spec")

    # Check for unmapped files
    all_htm = set()
    for f in TECHMAN_DIR.glob("*.htm"):
        all_htm.add(f.name)
    for f in TECHMAN_DIR.glob("t3spec/*.htm"):
        all_htm.add(f"t3spec/{f.name}")
    mapped = set(FILE_MAP.keys())
    unmapped = all_htm - mapped
    if unmapped:
        print(f"\n  WARNING: {len(unmapped)} unmapped files:")
        for f in sorted(unmapped):
            print(f"    {f}")

    # Save updated registry
    save_link_registry(link_registry)

    print(f"\nDone: {converted} converted, {skipped} skipped, {len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors)}")

    return converted, errors


if __name__ == "__main__":
    print("Converting TADS 3 Technical Manual and VM Spec...")
    convert_all()
