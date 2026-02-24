#!/usr/bin/env python3
"""
Shared validation infrastructure for TADS 3 HTML-to-Markdown content validation.

Provides:
- Unified file pair mapping across all converter sources
- Format-aware HTML text and code block extraction
- Markdown text and code block extraction
- Text normalization and encoding issue detection
- Report generation utilities
"""

import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import namedtuple
from bs4 import BeautifulSoup, Tag

SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

from convert_utils import T3DOC, DOCS_OUT, load_html, strip_navigation, get_pre_text

# Format types
FORMAT_SYSMAN = "sysman"
FORMAT_TOURGUIDE = "tourguide"
FORMAT_LIBREF = "libref"

# File pair: links an HTML source to its Markdown output
FilePair = namedtuple("FilePair", ["source_path", "output_path", "format_type", "source_name"])

# Source directories
SYSMAN_DIR = T3DOC / "sysman"
TECHMAN_DIR = T3DOC / "techman"
TOURGUIDE_DIR = T3DOC / "tourguide"
GSG_DIR = T3DOC / "gsg"
HTMLTADS_DIR = T3DOC / "htmltads"
WB_DIR = T3DOC / "wb"
LIBREF_DIR = T3DOC / "libref"
OBJECT_DIR = LIBREF_DIR / "object"
FILE_DIR = LIBREF_DIR / "file"
BY_CLASS_OUT = DOCS_OUT / "api" / "by-class"
BY_FILE_OUT = DOCS_OUT / "api" / "by-file"


# ---------------------------------------------------------------------------
# File pair building
# ---------------------------------------------------------------------------

def _import_sysman_map():
    from convert_sysman import FILE_MAP
    return FILE_MAP

def _import_techman_map():
    from convert_techman import FILE_MAP
    return FILE_MAP

def _import_phase5_maps():
    from convert_phase5 import HTMLTADS_MAP, WB_MAP, ROOT_MAP
    return HTMLTADS_MAP, WB_MAP, ROOT_MAP

def _import_tourguide_maps():
    from convert_tourguide import build_tourguide_file_map, build_gsg_file_map
    tg_map, _ = build_tourguide_file_map()
    gsg_map, _ = build_gsg_file_map()
    return tg_map, gsg_map


def build_file_pairs(sources=None, include_libref=False):
    """
    Build a unified list of FilePair tuples across all converter sources.

    Args:
        sources: list of source names to include (e.g., ["sysman", "tourguide"]).
                 None = all sources (except libref unless include_libref=True).
        include_libref: if True, include libref even when sources is None.

    Returns:
        list of FilePair tuples.
    """
    all_sources = {"sysman", "techman", "tourguide", "gsg", "htmltads", "wb", "root"}
    if include_libref:
        all_sources.add("libref")

    if sources:
        active = set(sources) & (all_sources | {"libref"})
    else:
        active = all_sources

    pairs = []

    # Sysman
    if "sysman" in active:
        for htm, md_rel in _import_sysman_map().items():
            if md_rel is None:
                continue
            src = SYSMAN_DIR / htm
            out = DOCS_OUT / md_rel
            if src.exists() and out.exists():
                pairs.append(FilePair(src, out, FORMAT_SYSMAN, f"sysman/{htm}"))

    # Techman
    if "techman" in active:
        for htm, md_rel in _import_techman_map().items():
            if md_rel is None:
                continue
            # Techman has some paths with subdirs (e.g., "t3spec/intro.htm")
            src = TECHMAN_DIR / htm
            out = DOCS_OUT / md_rel
            if src.exists() and out.exists():
                pairs.append(FilePair(src, out, FORMAT_SYSMAN, f"techman/{htm}"))

    # Phase 5: htmltads, wb, root
    if any(s in active for s in ("htmltads", "wb", "root")):
        htmltads_map, wb_map, root_map = _import_phase5_maps()

        if "htmltads" in active:
            for htm, md_rel in htmltads_map.items():
                if md_rel is None:
                    continue
                src = HTMLTADS_DIR / htm
                out = DOCS_OUT / md_rel
                if src.exists() and out.exists():
                    pairs.append(FilePair(src, out, FORMAT_SYSMAN, f"htmltads/{htm}"))

        if "wb" in active:
            for htm, md_rel in wb_map.items():
                if md_rel is None:
                    continue
                src = WB_DIR / htm
                out = DOCS_OUT / md_rel
                if src.exists() and out.exists():
                    pairs.append(FilePair(src, out, FORMAT_SYSMAN, f"wb/{htm}"))

        if "root" in active:
            for htm, md_rel in root_map.items():
                if md_rel is None:
                    continue
                src = T3DOC / htm
                out = DOCS_OUT / md_rel
                if src.exists() and out.exists():
                    pairs.append(FilePair(src, out, FORMAT_SYSMAN, f"root/{htm}"))

    # Tourguide
    if "tourguide" in active:
        tg_map, gsg_map = _import_tourguide_maps()
        for htm, md_rel in tg_map.items():
            if md_rel is None:
                continue
            src = TOURGUIDE_DIR / htm
            out = DOCS_OUT / md_rel
            if src.exists() and out.exists():
                pairs.append(FilePair(src, out, FORMAT_TOURGUIDE, f"tourguide/{htm}"))

    # GSG
    if "gsg" in active:
        if "tourguide" not in active:
            _, gsg_map = _import_tourguide_maps()
        else:
            # Already imported above
            pass
        # Re-import to ensure we have gsg_map in scope
        _, gsg_map = _import_tourguide_maps()
        for htm, md_rel in gsg_map.items():
            if md_rel is None:
                continue
            src = GSG_DIR / htm
            out = DOCS_OUT / md_rel
            if src.exists() and out.exists():
                pairs.append(FilePair(src, out, FORMAT_TOURGUIDE, f"gsg/{htm}"))

    # Libref
    if "libref" in active:
        # Object pages
        if OBJECT_DIR.exists() and BY_CLASS_OUT.exists():
            for html_file in sorted(OBJECT_DIR.glob("*.html")):
                md_name = html_file.stem.lower() + ".md"
                md_file = BY_CLASS_OUT / md_name
                if md_file.exists():
                    pairs.append(FilePair(html_file, md_file, FORMAT_LIBREF,
                                         f"libref/object/{html_file.name}"))
        # File pages
        if FILE_DIR.exists() and BY_FILE_OUT.exists():
            for html_file in sorted(FILE_DIR.glob("*.html")):
                md_name = html_file.stem.lower() + ".md"
                md_file = BY_FILE_OUT / md_name
                if md_file.exists():
                    pairs.append(FilePair(html_file, md_file, FORMAT_LIBREF,
                                         f"libref/file/{html_file.name}"))

    return pairs


# ---------------------------------------------------------------------------
# HTML text extraction (format-aware)
# ---------------------------------------------------------------------------

def extract_html_text(file_pair):
    """Extract visible text from HTML, excluding code blocks and navigation."""
    if file_pair.format_type == FORMAT_SYSMAN:
        return _extract_html_text_sysman(file_pair.source_path)
    elif file_pair.format_type == FORMAT_TOURGUIDE:
        return _extract_html_text_tourguide(file_pair.source_path)
    elif file_pair.format_type == FORMAT_LIBREF:
        return _extract_html_text_libref(file_pair.source_path)
    return ""


def _extract_html_text_sysman(filepath):
    """Extract visible text from sysman/techman format HTML."""
    soup = load_html(filepath)
    strip_navigation(soup)

    # Remove code blocks
    for div in soup.find_all("div", class_=["code", "cmdline", "syntax"]):
        div.decompose()
    for pre in soup.find_all("pre"):
        pre.decompose()

    # Remove inline code (matches what extract_md_text does with backtick stripping)
    for code in soup.find_all("code"):
        code.decompose()
    for span in soup.find_all("span", class_="code"):
        span.decompose()

    main = soup.find("div", class_="main") or soup.find("body")
    if not main:
        return ""
    return normalize_text(main.get_text())


def _is_courier_font(tag):
    """Check if a font tag specifies Courier New."""
    if not isinstance(tag, Tag) or tag.name != "font":
        return False
    face = tag.get("face", "")
    return "courier" in face.lower()


def _has_line_breaks(elem):
    """Check if an element contains <br> tags."""
    return len(elem.find_all("br")) > 0


def _is_nav_header(table):
    """Check if a table is the navigation header (grey background)."""
    bgcolor = table.get("bgcolor", "")
    if bgcolor.upper() in ("#C0C0C0", "#808080"):
        return True
    for tr in table.find_all("tr"):
        for td in tr.find_all("td"):
            if td.get("bgcolor", "").upper() in ("#C0C0C0", "#808080"):
                return True
    return False


def _extract_html_text_tourguide(filepath):
    """Extract visible text from tourguide/GSG Help & Manual format HTML."""
    soup = load_html(filepath)

    # Remove nav headers
    for table in list(soup.find_all("table")):
        if _is_nav_header(table):
            table.decompose()

    # Remove topbar div (GSG)
    for div in soup.find_all("div", class_="topbar"):
        div.decompose()

    # Remove code blocks (Courier New with line breaks)
    for font in list(soup.find_all("font")):
        if _is_courier_font(font) and _has_line_breaks(font):
            font.decompose()

    body = soup.find("body")
    if not body:
        return ""
    text = body.get_text()
    text = text.replace("\xa0", " ")
    return normalize_text(text)


def _extract_html_text_libref(filepath):
    """Extract visible text from libref HTML."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for table in soup.find_all("table", class_="nav"):
        table.decompose()
    for div in soup.find_all("div", class_="ftr"):
        div.decompose()

    body = soup.find("body")
    if not body:
        return ""
    return normalize_text(body.get_text())


# ---------------------------------------------------------------------------
# HTML code block extraction (format-aware)
# ---------------------------------------------------------------------------

def extract_html_code_blocks(file_pair):
    """Extract code blocks from HTML source."""
    if file_pair.format_type == FORMAT_SYSMAN:
        return _extract_code_blocks_sysman(file_pair.source_path)
    elif file_pair.format_type == FORMAT_TOURGUIDE:
        return _extract_code_blocks_tourguide(file_pair.source_path)
    elif file_pair.format_type == FORMAT_LIBREF:
        return _extract_code_blocks_libref(file_pair.source_path)
    return []


def _extract_code_blocks_sysman(filepath):
    """Extract code blocks from sysman/techman format HTML."""
    soup = load_html(filepath)
    strip_navigation(soup)
    blocks = []

    for div in soup.find_all("div", class_=["code", "cmdline", "syntax"]):
        pre = div.find("pre")
        if pre:
            text = get_pre_text(pre)
        else:
            text = div.get_text()
        text = clean_code_text(text)
        if text.strip():
            blocks.append(text)
        # Mark as processed so standalone <pre> scan skips it
        div.decompose()

    # Standalone <pre> not inside a code div
    for pre in soup.find_all("pre"):
        text = get_pre_text(pre)
        text = clean_code_text(text)
        if text.strip():
            blocks.append(text)

    return blocks


def _extract_code_text_tourguide(font_elem):
    """Extract code text from a Courier New font element."""
    from convert_tourguide import extract_code_text
    text = extract_code_text(font_elem)
    # Collapse double newlines
    while "\n\n" in text:
        text = text.replace("\n\n", "\n")
    return text


def _extract_code_blocks_tourguide(filepath):
    """Extract code blocks from tourguide/GSG Help & Manual format HTML."""
    soup = load_html(filepath)
    blocks = []

    for font in soup.find_all("font"):
        if _is_courier_font(font) and _has_line_breaks(font):
            text = _extract_code_text_tourguide(font)
            text = clean_code_text(text)
            if text.strip():
                blocks.append(text)

    return blocks


def _extract_code_blocks_libref(filepath):
    """Extract code blocks from libref HTML."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    blocks = []

    for pre in soup.find_all("pre"):
        text = pre.get_text()
        text = clean_code_text(text)
        if text.strip():
            blocks.append(text)

    return blocks


# ---------------------------------------------------------------------------
# Markdown extraction
# ---------------------------------------------------------------------------

def extract_md_text(filepath):
    """Extract visible text from Markdown, excluding code blocks and markup."""
    content = Path(filepath).read_text(encoding="utf-8", errors="replace")

    # Remove fenced code blocks
    content = re.sub(r'```[^\n]*\n.*?```', '', content, flags=re.DOTALL)

    # Remove inline code
    content = re.sub(r'``[^`]+``', '', content)
    content = re.sub(r'`[^`\n]+`', '', content)

    # Remove images
    content = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', content)

    # Remove links but keep text
    content = re.sub(r'\[([^\]]*)\]\([^)]+\)', r'\1', content)

    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Remove heading markers
    content = re.sub(r'^#{1,6}\s+', '', content, flags=re.MULTILINE)

    # Remove bold/italic markers
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
    content = re.sub(r'\*([^*]+)\*', r'\1', content)

    # Remove list markers
    content = re.sub(r'^[-*+]\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\d+\.\s+', '', content, flags=re.MULTILINE)

    # Remove table separators
    content = re.sub(r'^\|[-:| ]+\|$', '', content, flags=re.MULTILINE)

    # Remove horizontal rules
    content = re.sub(r'^---+$', '', content, flags=re.MULTILINE)

    return normalize_text(content)


def extract_md_code_blocks(filepath):
    """Extract fenced code blocks from a Markdown file."""
    content = Path(filepath).read_text(encoding="utf-8", errors="replace")
    blocks = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        stripped = lines[i].lstrip()
        if stripped.startswith('```'):
            backtick_count = len(stripped) - len(stripped.lstrip('`'))
            fence = '`' * backtick_count
            body_lines = []
            i += 1
            while i < len(lines):
                if lines[i].strip() == fence:
                    break
                body_lines.append(lines[i])
                i += 1
            body = '\n'.join(body_lines)
            body = clean_code_text(body)
            if body.strip():
                blocks.append(body)
        i += 1

    return blocks


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def normalize_text(text):
    """Normalize text for comparison: collapse whitespace, decode entities, straighten quotes."""
    # HTML entities
    text = text.replace("&nbsp;", " ")
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&amp;", "&").replace("&quot;", '"')
    text = text.replace("&#183;", "")  # Symbol font bullet

    # Smart quotes → straight
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')

    # Dashes → hyphen
    text = text.replace("\u2014", "-").replace("\u2013", "-")

    # Ellipsis → dots
    text = text.replace("\u2026", "...")

    # Non-breaking space
    text = text.replace("\xa0", " ")

    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def clean_code_text(text):
    """Clean code block text for comparison."""
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&amp;", "&").replace("&quot;", '"')
    text = text.replace("\xa0", " ")

    # Normalize encoding artifacts (replacement char → em-dash, smart quotes)
    text = text.replace("\ufffd", "\u2014")  # Common: replacement char was em-dash
    text = text.replace("\u2014", "-")  # Normalize em-dash to plain dash
    text = text.replace("\u2013", "-")  # Normalize en-dash to plain dash
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')

    # Strip trailing whitespace from each line
    lines = [line.rstrip() for line in text.split("\n")]

    # Strip leading/trailing blank lines
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Encoding issue detection
# ---------------------------------------------------------------------------

def check_encoding_issues(text):
    """Check for encoding problems in text. Returns list of issue descriptions."""
    issues = []

    if "\ufffd" in text:
        count = text.count("\ufffd")
        issues.append(f"Unicode replacement character (U+FFFD) x{count}")

    # Common mojibake patterns
    mojibake = [
        ("\u00c3\u00a2", "UTF-8 mojibake (a-circumflex)"),
        ("\u00c3\u00a9", "UTF-8 mojibake (e-acute)"),
        ("\u00e2\u0080\u0099", "UTF-8 mojibake (smart quote)"),
    ]
    for pattern, desc in mojibake:
        if pattern in text:
            issues.append(desc)

    # Unresolved HTML entities in markdown
    if re.search(r'&#\d+;', text):
        issues.append("Unresolved numeric HTML entity")

    return issues


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def write_json_report(data, path):
    """Write a JSON report to disk."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nJSON report: {path}")


def make_report_base(script_name, total, checked, skipped):
    """Create the base report structure."""
    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "script": script_name,
        "total_files": total,
        "files_checked": checked,
        "files_skipped": skipped,
        "files_with_issues": 0,
        "files": {},
    }


# ---------------------------------------------------------------------------
# CLI helpers
# ---------------------------------------------------------------------------

def build_arg_parser(description):
    """Build a standard argument parser for validation scripts."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--source", action="append",
                        choices=["sysman", "techman", "tourguide", "gsg",
                                 "htmltads", "wb", "root", "libref"],
                        help="Validate only this source (repeatable)")
    parser.add_argument("--all", action="store_true",
                        help="Include libref (excluded by default)")
    parser.add_argument("--file", type=str,
                        help="Validate a single output file (relative to docs/docs/)")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON to stdout")
    parser.add_argument("--verbose", action="store_true",
                        help="Show all comparisons, not just issues")
    return parser
