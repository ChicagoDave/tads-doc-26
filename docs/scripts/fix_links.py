"""
Link fixer for the TADS 3 documentation site.

Fixes broken links across all Markdown files:
  A. Parenthesized filenames — URL-encode parens in hrefs
  B. VM-spec cross-references — map old filenames to new ones
  C. Old section paths — remap libref/sysman/techman/gsg/tourguide refs
  D. Malformed external URLs — strip errant ../ prefixes
  E. Missing by-class refs — un-link references to non-existent API pages

Usage:
    python3 docs/scripts/fix_links.py [--dry-run]
"""

import re
import os
import sys
import json
from pathlib import Path
from urllib.parse import quote

DOCS_ROOT = Path(__file__).parent.parent / "docs"
SCRIPTS_DIR = Path(__file__).parent

# ---------- Fix A: Parenthesized filenames ----------

def build_paren_filename_set():
    """Collect all filenames containing parentheses under docs/."""
    paren_files = set()
    for md in DOCS_ROOT.rglob("*.md"):
        name = md.name
        if "(" in name:
            paren_files.add(name)
    return paren_files


def fix_parenthesized_links(content, paren_files):
    """URL-encode parentheses in links to files with parens in their names.

    In raw markdown, [text](predicate(about).md) is mis-parsed.
    We replace the inner ( and ) with %28 and %29 so the link works.
    """
    changes = 0
    for fname in paren_files:
        if fname not in content:
            continue
        # URL-encode parens in the filename
        encoded = fname.replace("(", "%28").replace(")", "%29")
        old = fname
        new = encoded
        if old != new and old in content:
            content = content.replace(old, new)
            changes += 1

    # Also fix broken links where the path was wrong AND had parens.
    # E.g., ](../../lever(2).md) in library/guide/ should be ](lever%282%29.md)
    # These show up as truncated: [text](../../lever(2) with .md) left over
    # Fix by finding the raw pattern in the source text.
    paren_link_re = re.compile(
        r'\[([^\]]*)\]\('       # [text](
        r'([^)]*?)'             # path prefix (non-greedy)
        r'([a-zA-Z0-9_]+)'     # filename base
        r'\((\w+)\)'            # (inner) — gets consumed as link close
        r'(\.md(?:#[^)]*)?)\)'  # .md or .md#fragment) — trailing
    )
    def fix_paren_link(m):
        nonlocal changes
        text, prefix, base, inner, ext_frag = m.groups()
        encoded_name = f"{base}%28{inner}%29{ext_frag}"
        changes += 1
        return f"[{text}]({prefix}{encoded_name})"

    content = paren_link_re.sub(fix_paren_link, content)
    return content, changes


# ---------- Fix B: VM-spec cross-references ----------

VMSPEC_REMAP = {
    "../model.md": "machine-model.md",
    "../format.md": "image-format.md",
    "../debug.md": "debug-records.md",
    "../opcode.md": "bytecode.md",
    "../bincode.md": "binary-encoding.md",
    "../metacl.md": "metaclasses.md",
    "../metalist.md": "metaclass-ids.md",
    "../save.md": "save-restore.md",
    "../philos.md": "philosophy.md",
    "../fnset_t3.md": "function-set.md",
    "../tadsspch.md": "special-characters.md",
    "../goals.md": "goals.md",
    "../notation.md": "notation.md",
}


def fix_vmspec_links(content, rel_path):
    """Fix vm-spec internal cross-references using old filenames."""
    if not rel_path.startswith("vm-spec/"):
        return content, 0
    changes = 0
    for old_href, new_href in VMSPEC_REMAP.items():
        # Match with optional fragment: ](../model.md#something)
        pattern = re.compile(
            r'\](\(' + re.escape(old_href) + r'(#[^)]*)?)\)'
        )
        def replacer(m):
            frag = m.group(2) or ""
            return f"]({new_href}{frag})"
        new_content = pattern.sub(replacer, content)
        if new_content != content:
            changes += 1
            content = new_content
    # Also remove broken logo image references
    content_new = re.sub(
        r'\[([^\]]*)\]\(\.\./t3logo\.gif\)',
        '',
        content
    )
    if content_new != content:
        changes += 1
        content = content_new
    return content, changes


# ---------- Fix C: Old section paths ----------

# Maps old section href prefixes to correct new section roots.
OLD_SECTION_MAP = {
    "libref/index.md": "api/by-class/index.md",
    "libref/source/": "api/by-file/",
    "sysman/cover.md": "language/index.md",
    "techman/cover.md": "library/index.md",
    "gsg/index.md": "getting-started/tutorial/index.md",
    "gsg/": "getting-started/tutorial/",
    "tourguide/index.md": "library/guide/index.md",
    "tourguide/": "library/guide/",
    "learning/": "getting-started/tutorial/",
}

_link_registry_cache = None

def _get_link_registry():
    global _link_registry_cache
    if _link_registry_cache is None:
        registry_path = SCRIPTS_DIR / "link_registry.json"
        with open(registry_path) as f:
            _link_registry_cache = json.load(f)
    return _link_registry_cache


def fix_old_section_links(content, rel_path):
    """Fix links referencing old section paths using the link registry."""
    changes = 0
    registry = _get_link_registry()

    def replace_link(match):
        nonlocal changes
        text = match.group(1)
        href = match.group(2)

        # Strip leading ../ to get the section path
        stripped = href
        while stripped.startswith("../"):
            stripped = stripped[3:]

        # Split fragment
        base, _, fragment = stripped.partition("#")
        frag_suffix = f"#{fragment}" if fragment else ""

        # Strategy 1: Direct prefix match in OLD_SECTION_MAP
        for old_prefix, new_prefix in OLD_SECTION_MAP.items():
            if base == old_prefix or base.startswith(old_prefix):
                suffix = base[len(old_prefix):]
                new_target = new_prefix + suffix
                from_dir = str(Path(rel_path).parent)
                new_href = os.path.relpath(new_target, from_dir)
                changes += 1
                return f"[{text}]({new_href}{frag_suffix})"

        # Strategy 2: Extract filename and look up in link registry
        # Handles libref/object/X.md, sysman/X.md, techman/X.md
        for section in ("libref/object/", "libref/file/", "sysman/", "techman/"):
            if base.startswith(section):
                fname = base[len(section):]
                # Try common HTML extensions for registry lookup
                for ext_pair in [(".md", ".html"), (".md", ".htm")]:
                    old_ext, new_ext = ext_pair
                    if fname.endswith(old_ext):
                        lookup = fname[:-len(old_ext)] + new_ext
                        if lookup in registry:
                            new_target = registry[lookup]
                            from_dir = str(Path(rel_path).parent)
                            new_href = os.path.relpath(new_target, from_dir)
                            changes += 1
                            return f"[{text}]({new_href}{frag_suffix})"
                        # Try case variations
                        lookup_lower = lookup.lower()
                        for key in registry:
                            if key.lower() == lookup_lower:
                                new_target = registry[key]
                                from_dir = str(Path(rel_path).parent)
                                new_href = os.path.relpath(new_target, from_dir)
                                changes += 1
                                return f"[{text}]({new_href}{frag_suffix})"

        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace_link, content)
    return content, changes


# ---------- Fix D: Malformed external URLs ----------

def fix_malformed_urls(content):
    """Fix external URLs that have errant ../ prefixes."""
    changes = 0

    # Pattern: ](../../ http:/url) or ](../ftp:/url)
    def fix_url(match):
        nonlocal changes
        text = match.group(1)
        protocol = match.group(2)
        rest = match.group(3)
        changes += 1
        return f"[{text}]({protocol}//{rest})"

    # Fix http: and https: with space or without
    content = re.sub(
        r'\[([^\]]*)\]\(\.\./(?:\.\./)*\s*(https?:)/+([^)]+)\)',
        fix_url, content
    )
    # Fix ftp:
    content = re.sub(
        r'\[([^\]]*)\]\(\.\./(?:\.\./)*\s*(ftp:)/+([^)]+)\)',
        fix_url, content
    )
    # Fix news: protocol links (news:rec.arts.int-fiction)
    def fix_news(match):
        nonlocal changes
        text = match.group(1)
        uri = match.group(2)
        changes += 1
        return f"[{text}]({uri})"

    content = re.sub(
        r'\[([^\]]*)\]\(\.\./(?:\.\./)*\s*(news:[^)]+)\)',
        fix_news, content
    )
    # Fix urn: protocol links
    content = re.sub(
        r'\[([^\]]*)\]\(\.\./(?:\.\./)*\s*(urn:[^)]+)\)',
        fix_news, content
    )
    return content, changes


# ---------- Fix E: Missing by-class refs ----------

def build_existing_class_pages():
    """Get set of existing api/by-class/ filenames."""
    api_dir = DOCS_ROOT / "api" / "by-class"
    return {f.name for f in api_dir.glob("*.md")}


def fix_missing_class_refs(content, rel_path, existing_pages):
    """Un-link references to non-existent api/by-class/ pages."""
    changes = 0

    def replace_missing(match):
        nonlocal changes
        text = match.group(1)
        href = match.group(2)

        # Only handle links that resolve to api/by-class/
        if "by-class/" not in href:
            return match.group(0)

        # Extract the filename
        fname = href.split("/")[-1]
        base_fname = fname.split("#")[0]

        if base_fname and base_fname not in existing_pages:
            changes += 1
            return text  # Un-link: just keep the text
        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace_missing, content)
    return content, changes


# ---------- Fix F: Misc broken links ----------

def fix_misc_links(content, rel_path):
    """Fix miscellaneous broken links."""
    changes = 0

    # Fix backslash paths (Windows-style): ..\..\techman\t3verb.md -> ../../library/...
    def fix_backslash(match):
        nonlocal changes
        text = match.group(1)
        href = match.group(2)
        fixed = href.replace("\\", "/")
        changes += 1
        return f"[{text}]({fixed})"

    if "\\" in content:
        content = re.sub(
            r'\[([^\]]*)\]\(([^)]*\\[^)]*)\)',
            fix_backslash, content
        )

    # Remove empty-text links to non-existent images: [](../htmltads.jpg)
    def remove_broken_image_link(match):
        nonlocal changes
        text = match.group(1)
        href = match.group(2)
        if not text and href.endswith(('.gif', '.jpg', '.png', '.jpeg')):
            resolved = (DOCS_ROOT / Path(rel_path).parent / href).resolve()
            if not resolved.exists():
                changes += 1
                return ''
        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', remove_broken_image_link, content)

    # Fix same-page fragment links that got wrong paths
    # E.g., [readBytes](../../readBytes) should be [readBytes](#readBytes)
    # These are links that look like relative paths but are actually
    # references to anchors/methods on the same page
    def fix_method_refs(match):
        nonlocal changes
        text = match.group(1)
        href = match.group(2)
        # If href has ../ traversals but the target has no extension,
        # it's likely a broken method/anchor reference
        if href.startswith("../") and "/" in href and "." not in href.split("/")[-1]:
            target = href.split("/")[-1]
            if target and target == text:
                changes += 1
                return f"[{text}](#{target})"
        return match.group(0)

    content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', fix_method_refs, content)

    # Fix links to non-existent pages that we know should be removed
    # (changelogs, license files, authkit welcome, etc.)
    DEAD_LINK_PATTERNS = [
        r'\[([^\]]*)\]\([^)]*changes\.md\)',         # changelog
        r'\[([^\]]*)\]\([^)]*license\.txt\)',         # license file
        r'\[([^\]]*)\]\([^)]*authkit/welcome\.md\)',  # authkit welcome
        r'\[([^\]]*)\]\([^)]*opc_namedargtab\)',      # opcode anchor
    ]
    for pattern in DEAD_LINK_PATTERNS:
        def unlink(match, p=pattern):
            nonlocal changes
            text = match.group(1)
            if text:
                changes += 1
                return text
            changes += 1
            return ''
        content = re.sub(pattern, unlink, content)

    return content, changes


# ---------- Main ----------

def fix_all(dry_run=False):
    """Apply all fixes to all markdown files."""
    paren_files = build_paren_filename_set()
    existing_class_pages = build_existing_class_pages()

    stats = {
        'files_modified': 0,
        'parenthesized': 0,
        'vmspec': 0,
        'old_section': 0,
        'malformed_url': 0,
        'missing_class': 0,
        'misc': 0,
    }

    md_files = sorted(DOCS_ROOT.rglob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(errors='replace')
        original = content
        rel_path = str(md_file.relative_to(DOCS_ROOT))

        # Apply fixes in order
        content, n = fix_parenthesized_links(content, paren_files)
        stats['parenthesized'] += n

        content, n = fix_vmspec_links(content, rel_path)
        stats['vmspec'] += n

        content, n = fix_old_section_links(content, rel_path)
        stats['old_section'] += n

        content, n = fix_malformed_urls(content)
        stats['malformed_url'] += n

        content, n = fix_missing_class_refs(content, rel_path, existing_class_pages)
        stats['missing_class'] += n

        content, n = fix_misc_links(content, rel_path)
        stats['misc'] += n

        if content != original:
            stats['files_modified'] += 1
            if dry_run:
                print(f"  Would modify: {rel_path}")
            else:
                md_file.write_text(content)

    return stats


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN (no files will be modified) ===\n")
    else:
        print("=== Fixing broken links ===\n")

    stats = fix_all(dry_run=dry_run)

    print(f"\nFiles modified:       {stats['files_modified']}")
    print(f"Parenthesized fixes:  {stats['parenthesized']}")
    print(f"VM-spec fixes:        {stats['vmspec']}")
    print(f"Old section fixes:    {stats['old_section']}")
    print(f"Malformed URL fixes:  {stats['malformed_url']}")
    print(f"Missing class fixes:  {stats['missing_class']}")
    print(f"Misc fixes:           {stats['misc']}")

    if dry_run:
        print("\nRe-run without --dry-run to apply changes.")


if __name__ == '__main__':
    main()
