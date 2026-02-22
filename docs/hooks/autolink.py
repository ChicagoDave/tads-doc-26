"""
mkdocs hook: Auto-link class names in prose docs to API reference pages.

At build time, scans prose documentation pages for TADS 3 class names
and converts the first occurrence of each into a link to the corresponding
API reference page.

Only processes pages in prose directories (library/, getting-started/,
language/, intrinsics/, html-tads/, tools/, appendices/, vm-spec/).
Never processes API pages themselves.

Configuration: Add to mkdocs.yml:
    hooks:
      - hooks/autolink.py
"""

import re
import os
import json
import logging
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.autolink")

# --- Configuration ---

# Class names that are too common/ambiguous to auto-link
EXCLUDE_NAMES = {
    "Date", "File", "Hidden", "Script", "Goal", "Hint",
    "Collection", "Iterator", "Dictionary", "Noise",
    "Exception", "Event", "Output", "Grammar",
    "Resolver", "State",
}

# Directories whose pages should receive auto-links
AUTOLINK_DIRS = (
    "library/",
    "getting-started/",
    "language/",
    "intrinsics/",
    "html-tads/",
    "tools/",
    "appendices/",
    "vm-spec/",
)

# Directory containing API pages (never auto-link these)
API_DIR = "api/"

# --- State ---

_class_map = None      # {ClassName: "api/by-class/filename.md"}
_pattern = None         # Compiled alternation regex
_sorted_names = None    # Names sorted longest-first


def _load_class_map():
    """Load the class registry and build the matching pattern."""
    global _class_map, _pattern, _sorted_names

    if _class_map is not None:
        return

    registry_path = Path(__file__).parent.parent / "scripts" / "class_registry.json"
    if not registry_path.exists():
        log.warning("autolink: class_registry.json not found, skipping auto-linking")
        _class_map = {}
        return

    with open(registry_path) as f:
        _class_map = json.load(f)

    # Remove excluded names
    for name in EXCLUDE_NAMES:
        _class_map.pop(name, None)

    if not _class_map:
        return

    # Sort names longest-first to prevent partial matches
    _sorted_names = sorted(_class_map.keys(), key=len, reverse=True)

    # Build a single compiled alternation pattern for efficiency
    escaped = [re.escape(name) for name in _sorted_names]
    _pattern = re.compile(r"\b(" + "|".join(escaped) + r")\b")


# Regex patterns for protected regions
_FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]+`")
_LINK_RE = re.compile(r"\[[^\]]*\]\([^)]+\)")
_HEADING_RE = re.compile(r"^#{1,6}\s+.*$", re.MULTILINE)
_HTML_TAG_RE = re.compile(r"<[^>]+>")
_ADMONITION_RE = re.compile(r"^!!! \w+.*$", re.MULTILINE)


def on_page_markdown(markdown, page, config, files, **kwargs):
    """mkdocs hook: auto-link class names in prose pages."""
    _load_class_map()

    if not _class_map or not _pattern:
        return markdown

    src_path = page.file.src_path

    # Only process prose directories
    if not any(src_path.startswith(d) for d in AUTOLINK_DIRS):
        return markdown

    # Never process API pages
    if src_path.startswith(API_DIR):
        return markdown

    return _apply_autolinks(markdown, src_path)


def _apply_autolinks(markdown, src_path):
    """Apply auto-links while protecting code blocks, inline code, and links."""
    # Phase 1: Mask protected regions with placeholders
    protected = []

    def protect(match):
        idx = len(protected)
        protected.append(match.group(0))
        return f"\x00P{idx}\x00"

    text = markdown

    # Order matters: protect larger structures first
    text = _FENCED_CODE_RE.sub(protect, text)
    text = _INLINE_CODE_RE.sub(protect, text)
    text = _LINK_RE.sub(protect, text)
    text = _HEADING_RE.sub(protect, text)
    text = _HTML_TAG_RE.sub(protect, text)
    text = _ADMONITION_RE.sub(protect, text)

    # Phase 2: Find and link class names (first occurrence only)
    from_dir = str(Path(src_path).parent)
    linked = set()

    def replace_first(match):
        name = match.group(1)
        if name in linked:
            return name  # Already linked this name, leave as-is
        linked.add(name)
        target = _class_map[name]
        rel_path = os.path.relpath(target, from_dir)
        return f"[{name}]({rel_path})"

    text = _pattern.sub(replace_first, text)

    # Phase 3: Restore protected regions (reverse order for nested placeholders)
    for i in range(len(protected) - 1, -1, -1):
        text = text.replace(f"\x00P{i}\x00", protected[i])

    return text
