#!/usr/bin/env python3
"""
Convert remaining TADS 3 HTML documentation to Markdown (Phase 5).

Covers three source directories:
  - htmltads/  → docs/html-tads/     (HTML TADS UI & formatting docs)
  - wb/        → docs/tools/workbench/ (Workbench IDE docs)
  - root-level → docs/getting-started/, docs/appendices/
"""

import sys
import shutil
from pathlib import Path
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from convert_utils import (
    T3DOC, DOCS_OUT, SCRIPTS_DIR,
    load_html, extract_title, strip_navigation,
    convert_element, rewrite_links_in_markdown, clean_markdown,
    load_link_registry, save_link_registry,
)


def load_html_fixed(filepath):
    """Load HTML with lxml after fixing unclosed <a name=...> anchor tags.

    The htmltads files use unclosed <a name=...> anchor tags. lxml
    auto-closes these by wrapping subsequent content inside them,
    destroying the document structure. We pre-process the HTML to
    self-close these anchors before parsing.
    """
    import re
    with open(filepath, "rb") as f:
        raw = f.read()
    try:
        html = raw.decode("utf-8")
    except UnicodeDecodeError:
        html = raw.decode("cp1252")

    # Self-close <a name="..."> or <A name=...> anchors that have no href
    # Match: <a name=X> where X is quoted or unquoted, with optional whitespace
    # Replace with: <a name="X"></a>
    # But NOT <a name=X href=...> (those are real links)
    def fix_anchor(m):
        full = m.group(0)
        # If it has an href, leave it alone
        if "href" in full.lower():
            return full
        name_val = m.group(1) or m.group(2)
        return f'<a name="{name_val}"></a>'

    html = re.sub(
        r'<[Aa]\s+[Nn][Aa][Mm][Ee]\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|(\S+))\s*>',
        lambda m: f'<a name="{m.group(1) or m.group(2) or m.group(3)}"></a>',
        html
    )

    return BeautifulSoup(html, "lxml")

HTMLTADS_DIR = T3DOC / "htmltads"
WB_DIR = T3DOC / "wb"

# ---------- File Maps ----------

HTMLTADS_MAP = {
    "intro.htm": "html-tads/introduction.md",
    "START.HTM": "html-tads/getting-started-with-html.md",
    "banners.htm": "html-tads/banners.md",
    "charmode.htm": "html-tads/character-mode.md",
    "convert.htm": "html-tads/converting-games.md",
    "deviate.htm": "html-tads/deviations.md",
    "dist.htm": "html-tads/distributing.md",
    "latin2.htm": "html-tads/latin2.md",
    "linebrk.htm": "html-tads/line-breaking.md",
    "porting.htm": "html-tads/porting.md",
    "res.htm": "html-tads/resources.md",
    "sound.htm": "html-tads/sound.md",
    "tables.htm": "html-tads/tables.md",
}

WB_MAP = {
    "tadswb.htm": "tools/workbench/overview.md",
    "newgame.htm": "tools/workbench/creating-game.md",
    "custom.htm": "tools/workbench/customizing.md",
    "editor.htm": "tools/workbench/editor.md",
    "exts.htm": "tools/workbench/extensions.md",
    "helptdb.htm": "tools/workbench/debugger.md",
    "script.htm": "tools/workbench/scripting.md",
    "wbcmd.htm": "tools/workbench/commands.md",
    "HELPCOMP.HTM": "tools/workbench/compiling.md",
    "HELPED.HTM": "tools/workbench/external-editor.md",
    "DOCKWIN.HTM": "tools/workbench/docking-windows.md",
    # Skipped:
    "WBCONT.HTM": None,    # TOC page (content absorbed into index)
    "getmanuals.htm": None,  # Download links page
}

ROOT_MAP = {
    "t3QuickStart.htm": "getting-started/quickstart.md",
    "compat.htm": "appendices/compatibility.md",
    # Skipped:
    "changes.htm": None,     # Historical changelog
    "t3changes.htm": None,   # Historical changelog
    "index.htm": None,       # Replaced by mkdocs site index
    "indexwb.htm": None,     # Replaced by mkdocs site index
    "nodoc.htm": None,       # Stub
    "nolibref.htm": None,    # Stub
}


def strip_wb_chrome(soup):
    """Remove Workbench-specific navigation chrome."""
    # Remove breadcrumb nav: <font size=-1>Help Topics > ...</font>
    for font in soup.find_all("font", attrs={"size": "-1"}):
        text = font.get_text()
        if "Help Topics" in text or "Table of Contents" in text:
            # Also remove trailing <br> tags
            for sibling in list(font.next_siblings):
                if hasattr(sibling, "name") and sibling.name == "br":
                    sibling.decompose()
                else:
                    break
            font.decompose()

    # Remove decorative <center> blocks with just images/headings
    for center in soup.find_all("center"):
        center.decompose()

    # Remove copyright footer: <font size=-1>Copyright...</font>
    for font in soup.find_all("font", attrs={"size": "-1"}):
        text = font.get_text()
        if "Copyright" in text:
            font.decompose()


def convert_page(filepath, link_registry, output_path,
                  strip_extra=None, use_lenient_parser=False):
    """
    Convert a single HTML page to Markdown.
    strip_extra: optional function to call on soup before conversion.
    use_lenient_parser: use html.parser instead of lxml (for unclosed tags).
    """
    if use_lenient_parser:
        soup = load_html_fixed(filepath)
    else:
        soup = load_html(filepath)
    title = extract_title(soup)

    # Strip standard navigation
    strip_navigation(soup)

    # Strip source-specific chrome
    if strip_extra:
        strip_extra(soup)

    # Find content
    main = soup.find("div", class_="main")
    if not main:
        main = soup.find("body")
    if not main:
        # Files without <body> (bare HTML) - parse whole document
        main = soup
    if not main:
        return title, f"# {title}\n\n*Conversion error: no content found.*\n"

    # Convert to markdown
    md = convert_element(main)

    # Ensure title heading is present
    # Some pages (especially wb) lose their h1 during chrome stripping
    md_stripped = md.lstrip()
    if not md_stripped.startswith("# "):
        md = f"# {title}\n\n{md}"

    # Rewrite internal links
    if link_registry:
        md = rewrite_links_in_markdown(md, link_registry, output_path)

    # Clean up
    md = clean_markdown(md)

    return title, md


def build_link_registry():
    """Build link registry with all Phase 5 file mappings."""
    registry = load_link_registry()

    # Register htmltads files
    for old_name, new_path in HTMLTADS_MAP.items():
        if new_path:
            # Bare filename (for intra-directory links)
            registry[old_name] = new_path
            registry[old_name.lower()] = new_path
            # With directory prefix (for cross-directory links from wb/)
            registry[f"../htmltads/{old_name}"] = new_path
            registry[f"../htmltads/{old_name.lower()}"] = new_path
            registry[f"htmltads/{old_name}"] = new_path
            registry[f"htmltads/{old_name.lower()}"] = new_path

    # Register wb files
    for old_name, new_path in WB_MAP.items():
        if new_path:
            registry[old_name] = new_path
            registry[old_name.lower()] = new_path
            registry[f"../wb/{old_name}"] = new_path
            registry[f"../wb/{old_name.lower()}"] = new_path
            registry[f"wb/{old_name}"] = new_path
            registry[f"wb/{old_name.lower()}"] = new_path

    # Also register WBCONT.HTM → workbench index (it's skipped but linked to)
    for variant in ["wbcont.htm", "WBCONT.HTM", "../wb/wbcont.htm", "../wb/WBCONT.HTM",
                     "wb/wbcont.htm", "wb/WBCONT.HTM"]:
        registry[variant] = "tools/workbench/index.md"

    # Register root-level files
    for old_name, new_path in ROOT_MAP.items():
        if new_path:
            registry[old_name] = new_path
            registry[old_name.lower()] = new_path
            registry[f"../{old_name}"] = new_path
            registry[f"../{old_name.lower()}"] = new_path

    return registry


def convert_section(section_name, source_dir, file_map, link_registry,
                     strip_fn=None, use_lenient_parser=False):
    """Convert all files in a section. Returns (converted_count, error_list)."""
    converted = 0
    skipped = 0
    errors = []

    for htm_file, out_path in file_map.items():
        if out_path is None:
            skipped += 1
            continue

        src = source_dir / htm_file
        if not src.exists():
            print(f"  WARNING: Source not found: {src}")
            errors.append(htm_file)
            continue

        dst = DOCS_OUT / out_path
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            title, markdown = convert_page(
                src, link_registry, out_path,
                strip_extra=strip_fn,
                use_lenient_parser=use_lenient_parser,
            )
            with open(dst, "w", encoding="utf-8") as f:
                f.write(markdown)
            converted += 1
            print(f"  OK: {htm_file} -> {out_path}")
        except Exception as e:
            print(f"  ERROR: {htm_file}: {e}")
            import traceback
            traceback.print_exc()
            errors.append(htm_file)

    print(f"  {section_name}: {converted} converted, {skipped} skipped, {len(errors)} errors")
    return converted, errors


def copy_wb_images():
    """Copy Workbench images to output directory."""
    wb_out = DOCS_OUT / "tools" / "workbench"
    wb_out.mkdir(parents=True, exist_ok=True)

    image_exts = (".jpg", ".gif", ".png")
    copied = 0
    for ext in image_exts:
        for img in WB_DIR.glob(f"*{ext}"):
            shutil.copy2(img, wb_out / img.name.lower())
            copied += 1
        # Also check uppercase extensions
        for img in WB_DIR.glob(f"*{ext.upper()}"):
            shutil.copy2(img, wb_out / img.name.lower())
            copied += 1

    print(f"  Copied {copied} images to {wb_out}")


def convert_all():
    """Convert all Phase 5 pages."""
    link_registry = build_link_registry()

    total_converted = 0
    all_errors = []

    # HTML TADS (use html.parser for unclosed <a name=...> tags)
    print("\nConverting HTML TADS docs...")
    c, e = convert_section("htmltads", HTMLTADS_DIR, HTMLTADS_MAP, link_registry,
                            use_lenient_parser=True)
    total_converted += c
    all_errors.extend(e)

    # Workbench
    print("\nConverting Workbench docs...")
    c, e = convert_section("wb", WB_DIR, WB_MAP, link_registry, strip_fn=strip_wb_chrome)
    total_converted += c
    all_errors.extend(e)

    # Copy Workbench images
    print("\nCopying Workbench images...")
    copy_wb_images()

    # Root-level files
    print("\nConverting root-level docs...")
    c, e = convert_section("root", T3DOC, ROOT_MAP, link_registry,
                            use_lenient_parser=True)
    total_converted += c
    all_errors.extend(e)

    # Save registry
    save_link_registry(link_registry)

    print(f"\n{'=' * 50}")
    print(f"Phase 5 complete: {total_converted} pages converted, {len(all_errors)} errors")
    if all_errors:
        print(f"Errors: {', '.join(all_errors)}")

    return total_converted, all_errors


if __name__ == "__main__":
    print("Phase 5: Converting remaining TADS 3 documentation...")
    convert_all()
