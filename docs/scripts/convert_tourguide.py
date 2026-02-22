#!/usr/bin/env python3
"""
Convert TADS 3 Tour Guide and Getting Started Guide HTML pages to Markdown.

These docs use Help & Manual generated HTML with:
- <font face="Courier New"> code blocks (with &nbsp; spaces and <br> newlines)
- Table-based bullet lists (Symbol font &#183;)
- <font> tags for all styling
- Grey navigation header tables

Reads from: tads-sources/t3doc/tourguide/, tads-sources/t3doc/gsg/
Writes to:  docs/docs/library/guide/, docs/docs/getting-started/tutorial/
"""

import re
import sys
import shutil
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, str(Path(__file__).parent))
from convert_utils import (
    T3DOC, DOCS_OUT, SCRIPTS_DIR,
    load_link_registry, save_link_registry,
    rewrite_links_in_markdown, clean_markdown, load_html
)

TOURGUIDE_DIR = T3DOC / "tourguide"
GSG_DIR = T3DOC / "gsg"


# ---------------------------------------------------------------------------
# TOC Parsing
# ---------------------------------------------------------------------------

def parse_toc(toc_path):
    """
    Parse a Help & Manual contpage.htm to extract the hierarchical TOC.

    Returns a list of (level, title, href_or_None) tuples.
    Hierarchy is encoded by the <td width="N"> value:
      24 = level 0, 40 = level 1, 56 = level 2, 72 = level 3
    cicon2.gif = section heading (may or may not have a link)
    cicon9.gif = content page (always has a link)
    """
    soup = load_html(toc_path)
    entries = []

    width_to_level = {24: 0, 40: 1, 56: 2, 72: 3}

    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if not rows:
            continue
        row = rows[0]
        cells = row.find_all("td")
        if len(cells) < 2:
            continue

        # First cell has the icon and width
        first_td = cells[0]
        width_str = first_td.get("width", "24")
        try:
            width = int(width_str)
        except ValueError:
            width = 24
        level = width_to_level.get(width, 0)

        # Second cell has the text/link
        second_td = cells[1]
        link = second_td.find("a")
        if link:
            href = link.get("href", "")
            title = link.get_text().strip()
        else:
            href = None
            title = second_td.get_text().strip()

        if title:
            entries.append((level, title, href))

    return entries


def slugify(text):
    """Convert a section title to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[&]", "and", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text


# ---------------------------------------------------------------------------
# Tourguide file map from TOC
# ---------------------------------------------------------------------------

def build_tourguide_file_map():
    """
    Build a mapping of tourguide .htm files to output .md paths.
    All pages go under library/guide/ in a flat structure.
    """
    entries = parse_toc(TOURGUIDE_DIR / "contpage.htm")
    file_map = {}

    for level, title, href in entries:
        if href:
            # Strip target= etc, just get the filename
            htm_name = href.split("#")[0]
            # Output path: library/guide/<filename>.md
            md_name = htm_name.replace(".htm", ".md")
            file_map[htm_name] = f"library/guide/{md_name}"

    # Add files not in contpage.htm but with real content
    extra_tourguide = {
        "changesforv3_0_19.htm": "library/guide/changesforv3_0_19.md",
        "initdesc+initexaminedesc.htm": "library/guide/initdesc+initexaminedesc.md",
        "inputmanager.htm": "library/guide/inputmanager.md",
        "mainoutputstream.htm": "library/guide/mainoutputstream.md",
        "stringpreparser.htm": "library/guide/stringpreparser.md",
        "telltoaction.htm": "library/guide/telltoaction.md",
        "vocabwords_.htm": "library/guide/vocabwords_.md",
        "endconvxxxcodes.htm": "library/guide/endconvxxxcodes.md",
    }
    file_map.update(extra_tourguide)

    return file_map, entries


def build_gsg_file_map():
    """
    Build a mapping of GSG .htm files to output .md paths.
    All pages go under getting-started/tutorial/.
    """
    entries = parse_toc(GSG_DIR / "contpage.htm")
    file_map = {}

    for level, title, href in entries:
        if href:
            htm_name = href.split("#")[0]
            md_name = htm_name.replace(".htm", ".md").replace(".html", ".md")
            file_map[htm_name] = f"getting-started/tutorial/{md_name}"

    # Add files not in contpage.htm but with real content
    extra_gsg = {
        "thebasictools.htm": "getting-started/tutorial/thebasictools.md",
        "whatsinaname.htm": "getting-started/tutorial/whatsinaname.md",
    }
    file_map.update(extra_gsg)

    return file_map, entries


# ---------------------------------------------------------------------------
# HTML Preprocessing for Help & Manual format
# ---------------------------------------------------------------------------

def is_bullet_table(table):
    """Check if a table is a bullet-list table (Symbol font &#183;)."""
    rows = table.find_all("tr")
    if len(rows) != 1:
        return False
    cells = rows[0].find_all("td")
    if len(cells) != 2:
        return False
    first_td = cells[0]
    width = first_td.get("width", "")
    try:
        w = int(width)
    except ValueError:
        return False
    if w != 14:
        return False
    # Check for bullet character
    text = first_td.get_text()
    if "\u00b7" in text or "·" in text:
        return True
    return False


def is_spacer_table(table):
    """Check if a table is a spacer/indentation table (td width ~51, empty first cell)."""
    rows = table.find_all("tr")
    if len(rows) != 1:
        return False
    cells = rows[0].find_all("td")
    if len(cells) < 2:
        return False
    first_td = cells[0]
    width = first_td.get("width", "")
    try:
        w = int(width)
    except ValueError:
        return False
    # Spacer tables have width 51 or 71 and empty/whitespace first cell
    if w in (51, 71):
        text = first_td.get_text().strip()
        if not text:
            return True
    return False


def is_empty_table(table):
    """Check if a table has no meaningful content."""
    text = table.get_text().strip()
    return not text


def is_nav_header(table):
    """Check if a table is the navigation header (grey background)."""
    bgcolor = table.get("bgcolor", "")
    if bgcolor.upper() in ("#C0C0C0", "#808080"):
        return True
    # Also check first row
    for tr in table.find_all("tr"):
        for td in tr.find_all("td"):
            if td.get("bgcolor", "").upper() in ("#C0C0C0", "#808080"):
                return True
    return False


def is_courier_font(tag):
    """Check if a font tag specifies Courier New."""
    if tag.name != "font":
        return False
    face = tag.get("face", "")
    return "courier" in face.lower()


def extract_code_text(font_elem):
    """
    Extract code text from a Courier New font element.
    Converts &nbsp; to spaces, <br> to newlines, strips inner formatting.
    Handles the double-newline issue where <br>\n in HTML produces two newlines.
    """
    parts = []
    prev_was_br = False
    for child in font_elem.children:
        if isinstance(child, NavigableString):
            text = str(child)
            text = text.replace("\xa0", " ")  # &nbsp;
            text = text.replace("&nbsp;", " ")
            # After a <br>, skip the leading newline that HTML source adds
            if prev_was_br and text.startswith("\n"):
                text = text[1:]
            prev_was_br = False
            if text:
                parts.append(text)
        elif isinstance(child, Tag):
            prev_was_br = False
            if child.name == "br":
                parts.append("\n")
                prev_was_br = True
            elif child.name in ("b", "strong"):
                parts.append(extract_code_text(child))
            elif child.name in ("i", "em"):
                parts.append(extract_code_text(child))
            elif child.name == "a":
                parts.append(child.get_text().replace("\xa0", " "))
            elif child.name == "font":
                parts.append(extract_code_text(child))
            else:
                parts.append(child.get_text().replace("\xa0", " "))

    return "".join(parts)


def has_line_breaks(elem):
    """Check if an element contains <br> tags (indicating block-level code)."""
    return len(elem.find_all("br")) > 0


def convert_hm_element(element, in_code=False):
    """
    Recursively convert a Help & Manual HTML element to Markdown.
    """
    if isinstance(element, NavigableString):
        text = str(element)
        if in_code:
            text = text.replace("\xa0", " ")
            return text
        return text

    if not isinstance(element, Tag):
        return ""

    tag = element.name

    # Skip these entirely
    if tag in ("script", "style", "link", "meta", "head"):
        return ""

    # Images
    if tag == "img":
        src = element.get("src", "")
        alt = element.get("alt", "")
        if src and not src.endswith(("topbar.jpg", "getacro.gif",
                                     "cicon2.gif", "cicon9.gif")):
            return f"![{alt}]({src})"
        return ""

    # Navigation header tables - strip
    if tag == "table" and is_nav_header(element):
        return ""

    # Bullet tables -> markdown list items
    if tag == "table" and is_bullet_table(element):
        cells = element.find("tr").find_all("td")
        content_td = cells[1]
        text = convert_hm_children(content_td).strip()
        # Clean up trailing whitespace/breaks
        text = re.sub(r'\s*$', '', text)
        return f"\n- {text}\n"

    # Spacer/indentation tables -> just extract content
    if tag == "table" and is_spacer_table(element):
        cells = element.find("tr").find_all("td")
        # Get content from non-empty cells
        parts = []
        for td in cells[1:]:  # skip the spacer cell
            content = convert_hm_children(td).strip()
            if content:
                parts.append(content)
        result = " ".join(parts)
        if result:
            return "\n" + result + "\n"
        return ""

    # Empty tables - skip
    if tag == "table" and is_empty_table(element):
        return ""

    # Other tables - attempt conversion
    if tag == "table":
        return convert_hm_table(element)

    # Font tags - the core of Help & Manual formatting
    if tag == "font":
        face = element.get("face", "")

        # Courier New = code
        if "courier" in face.lower():
            if has_line_breaks(element):
                # Block-level code
                code = extract_code_text(element)
                # Collapse double newlines from HTML source newline + <br>
                while "\n\n" in code:
                    code = code.replace("\n\n", "\n")
                # Strip leading/trailing blank lines
                lines = code.split("\n")
                while lines and not lines[0].strip():
                    lines.pop(0)
                while lines and not lines[-1].strip():
                    lines.pop()
                code = "\n".join(lines)
                if code.strip():
                    return f"\n```tads3\n{code}\n```\n\n"
                return ""
            else:
                # Inline code
                text = element.get_text().replace("\xa0", " ").strip()
                if text:
                    if "`" in text:
                        return f"`` {text} ``"
                    return f"`{text}`"
                return ""

        # Symbol font (bullets) - handled by bullet table detection
        if "symbol" in face.lower():
            return ""

        # All other fonts - strip tag, keep content
        return convert_hm_children(element)

    # Headings
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        text = convert_hm_children(element).strip()
        return f"\n{'#' * level} {text}\n\n"

    # Paragraphs
    if tag == "p":
        content = convert_hm_children(element).strip()
        if content:
            return f"\n{content}\n\n"
        return "\n"

    # Line breaks
    if tag == "br":
        return "  \n"

    # Horizontal rules
    if tag == "hr":
        return "\n---\n\n"

    # Bold
    if tag in ("b", "strong"):
        content = convert_hm_children(element).strip()
        if not content:
            return ""
        return f"**{content}**"

    # Italic
    if tag in ("i", "em"):
        content = convert_hm_children(element).strip()
        if not content:
            return ""
        return f"*{content}*"

    # Inline code
    if tag in ("tt", "code"):
        if element.find_parent("pre"):
            return convert_hm_children(element)
        text = element.get_text().strip()
        if text:
            if "`" in text:
                return f"`` {text} ``"
            return f"`{text}`"
        return ""

    # Links
    if tag == "a":
        href = element.get("href", "")
        text = convert_hm_children(element).strip()
        name = element.get("name", "")

        if name and not href:
            return f'<a name="{name}"></a>'
        if not text:
            return ""
        if href:
            return f"[{text}]({href})"
        return text

    # Lists (real HTML lists, rare in Help & Manual)
    if tag == "ul":
        return "\n" + convert_hm_list(element, ordered=False) + "\n"
    if tag == "ol":
        return "\n" + convert_hm_list(element, ordered=True) + "\n"
    if tag == "li":
        return convert_hm_children(element)

    # Pre-formatted
    if tag == "pre":
        text = element.get_text()
        return f"\n```\n{text}\n```\n\n"

    # Blockquote
    if tag == "blockquote":
        content = convert_hm_children(element)
        lines = content.strip().split("\n")
        return "\n" + "\n".join(f"> {line}" for line in lines) + "\n\n"

    # Divs
    if tag == "div":
        cls = element.get("class", [])
        if "topbar" in cls:
            return ""  # Skip navigation topbar
        if "main" in cls:
            return convert_hm_children(element)
        return convert_hm_children(element)

    # Center
    if tag == "center":
        return convert_hm_children(element)

    # Sub/superscript
    if tag in ("sub", "sup"):
        return convert_hm_children(element)

    # Default: recurse
    return convert_hm_children(element)


def convert_hm_children(element):
    """Convert all children of an element to Markdown."""
    parts = []
    for child in element.children:
        parts.append(convert_hm_element(child))
    return "".join(parts)


def convert_hm_list(element, ordered=False):
    """Convert a real <ul>/<ol> to Markdown."""
    items = []
    counter = 1
    for child in element.children:
        if isinstance(child, Tag) and child.name == "li":
            content = convert_hm_children(child).strip()
            if ordered:
                items.append(f"{counter}. {content}")
                counter += 1
            else:
                items.append(f"- {content}")
    return "\n".join(items) + "\n"


def convert_hm_table(element):
    """Convert an HTML table to Markdown table (simple cases only)."""
    rows = element.find_all("tr")
    if not rows:
        return ""

    col_counts = []
    for row in rows:
        cells = row.find_all(["td", "th"])
        has_span = any(
            cell.get("rowspan") or cell.get("colspan")
            for cell in cells
        )
        if has_span:
            return f"\n{element}\n\n"
        col_counts.append(len(cells))

    if not col_counts or max(col_counts) == 0:
        return ""

    num_cols = max(col_counts)

    md_rows = []
    for i, row in enumerate(rows):
        cells = row.find_all(["td", "th"])
        cell_texts = []
        for cell in cells:
            text = convert_hm_children(cell).strip()
            text = re.sub(r"\n+", " ", text)
            cell_texts.append(text)
        while len(cell_texts) < num_cols:
            cell_texts.append("")
        md_rows.append("| " + " | ".join(cell_texts) + " |")
        if i == 0:
            md_rows.append("|" + "|".join(["---"] * num_cols) + "|")

    return "\n" + "\n".join(md_rows) + "\n\n"


# ---------------------------------------------------------------------------
# Page Conversion
# ---------------------------------------------------------------------------

def extract_tourguide_title(soup):
    """Extract title from a tourguide page."""
    # Try <title> tag first
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        return title_tag.string.strip()
    # Try first heading
    for h in soup.find_all(["h1", "h2", "h3"]):
        text = h.get_text().strip()
        if text:
            return text
    # Try the nav header (first bold text in grey table)
    for table in soup.find_all("table"):
        if is_nav_header(table):
            b = table.find("b")
            if b:
                text = b.get_text().strip()
                # Clean up "ClassName: SuperClass1, SuperClass2"
                if ":" in text:
                    text = text.split(":")[0].strip()
                return text
    return "Untitled"


def extract_tourguide_header_info(soup):
    """
    Extract the class/superclass info from the tourguide nav header.
    Returns (title, superclasses_markdown) or (title, None).
    """
    for table in soup.find_all("table"):
        if is_nav_header(table):
            b = table.find("b")
            if b:
                # Convert to markdown to preserve links
                header_md = convert_hm_children(b).strip()
                return header_md
    return None


def convert_tourguide_page(filepath, link_registry=None, output_path=None):
    """
    Convert a single tourguide HTML page to Markdown.
    Returns (title, markdown_content).
    """
    soup = load_html(filepath)
    title = extract_tourguide_title(soup)

    # Get the header info (class : SuperClass links)
    header_info = extract_tourguide_header_info(soup)

    # Find body content
    body = soup.find("body")
    if not body:
        return title, f"# {title}\n\n*Conversion error: no content found.*\n"

    # Convert to markdown
    md = convert_hm_element(body)

    # Add title heading if not already present
    if not md.strip().startswith("#"):
        heading = f"# {title}\n\n"
        if header_info and ":" in header_info:
            heading += f"{header_info}\n\n"
        md = heading + md

    # Rewrite internal links
    if link_registry:
        md = rewrite_links_in_markdown(md, link_registry, output_path)

    # Clean up
    md = clean_hm_markdown(md)

    return title, md


def convert_gsg_page(filepath, link_registry=None, output_path=None):
    """
    Convert a single GSG HTML page to Markdown.
    GSG pages have div.topbar and div.main wrappers, plus h1/h2 headings.
    Returns (title, markdown_content).
    """
    soup = load_html(filepath)
    title = extract_tourguide_title(soup)

    # Strip topbar
    for div in soup.find_all("div", class_="topbar"):
        div.decompose()

    # Strip trailing nav (after <HR>)
    for hr in soup.find_all("hr"):
        # Remove everything after the HR
        for sibling in list(hr.find_next_siblings()):
            sibling.decompose()
        hr.decompose()

    # Find main content
    main = soup.find("div", class_="main")
    if not main:
        main = soup.find("body")
    if not main:
        return title, f"# {title}\n\n*Conversion error: no content found.*\n"

    # Strip the initial nav paragraph ([Main] [Previous] [Next])
    for p in main.find_all("p", limit=2):
        text = p.get_text()
        if "[Main]" in text and "[Previous]" in text:
            p.decompose()
            break
        if "[Main]" in text:
            p.decompose()
            break

    # Convert to markdown
    md = convert_hm_element(main)

    # Rewrite internal links
    if link_registry:
        md = rewrite_links_in_markdown(md, link_registry, output_path)

    # Clean up
    md = clean_hm_markdown(md)

    return title, md


def clean_hm_markdown(text):
    """
    Clean up Help & Manual converted Markdown.
    More aggressive whitespace cleanup than the generic clean_markdown.
    """
    # First do standard cleanup
    text = clean_markdown(text)

    # Collapse "  \n" (hard breaks) followed by blank lines into paragraph breaks
    text = re.sub(r'(  \n\s*\n)+', '\n\n', text)

    # Collapse isolated hard breaks between paragraphs into paragraph breaks
    # Pattern: text ending with period/etc, then "  \n\n", then more text
    text = re.sub(r'  \n\n', '\n\n', text)

    # Remove orphan hard breaks (line ending with just "  \n" then normal text)
    # But preserve intentional hard breaks within lists
    text = re.sub(r'(?<=[.!?:;"\'])\s*  \n(?=[A-Z])', '\n\n', text)

    # Fix multiple consecutive blank lines (max 2)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Fix trailing whitespace on lines
    text = re.sub(r' +\n', '\n', text)

    # Fix "  \n" at end of paragraphs (not needed)
    text = re.sub(r'  \n\n', '\n\n', text)

    # Ensure file ends with single newline
    text = text.rstrip() + '\n'

    return text


# ---------------------------------------------------------------------------
# Nav Generation
# ---------------------------------------------------------------------------

def generate_nav_entries(entries, file_map, prefix):
    """Generate mkdocs nav YAML entries from TOC entries."""
    nav = []
    current_section = None
    current_subsection = None
    current_subsubsection = None

    for level, title, href in entries:
        if href and href in file_map:
            md_path = file_map[href]
            entry = {title: md_path}
        elif href:
            continue
        else:
            entry = None

        if level == 0:
            if entry:
                nav.append(entry)
            else:
                current_section = {"title": title, "children": []}
                nav.append(current_section)
                current_subsection = None
                current_subsubsection = None
        elif level == 1:
            if entry:
                if current_section:
                    current_section["children"].append(entry)
                else:
                    nav.append(entry)
            else:
                current_subsection = {"title": title, "children": []}
                if current_section:
                    current_section["children"].append(current_subsection)
                current_subsubsection = None
        elif level == 2:
            if entry:
                if current_subsection:
                    current_subsection["children"].append(entry)
                elif current_section:
                    current_section["children"].append(entry)
                else:
                    nav.append(entry)
            else:
                current_subsubsection = {"title": title, "children": []}
                if current_subsection:
                    current_subsection["children"].append(current_subsubsection)
        elif level == 3:
            if entry:
                if current_subsubsection:
                    current_subsubsection["children"].append(entry)
                elif current_subsection:
                    current_subsection["children"].append(entry)

    return nav


# ---------------------------------------------------------------------------
# Main Conversion
# ---------------------------------------------------------------------------

def convert_all_tourguide():
    """Convert all Tour Guide pages."""
    file_map, toc_entries = build_tourguide_file_map()

    # Merge with existing link registry
    link_registry = load_link_registry()
    for old_name, new_path in file_map.items():
        link_registry[old_name] = new_path

    converted = 0
    skipped = 0
    errors = []

    for htm_file, out_path in file_map.items():
        src = TOURGUIDE_DIR / htm_file
        if not src.exists():
            print(f"  WARNING: Source not found: {src}")
            errors.append(htm_file)
            continue

        dst = DOCS_OUT / out_path
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            title, markdown = convert_tourguide_page(
                src, link_registry, output_path=out_path
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

    # Check for unmapped files
    all_htm = set(f.name for f in TOURGUIDE_DIR.glob("*.htm")
                  if f.name != "contpage.htm")
    mapped = set(file_map.keys())
    unmapped = all_htm - mapped
    if unmapped:
        print(f"\n  WARNING: {len(unmapped)} unmapped tourguide files:")
        for f in sorted(unmapped):
            print(f"    {f}")

    # Save updated registry
    save_link_registry(link_registry)

    print(f"\nTour Guide: {converted} converted, {skipped} skipped, "
          f"{len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors)}")

    return converted, errors, toc_entries, file_map


def convert_all_gsg():
    """Convert all Getting Started Guide pages."""
    file_map, toc_entries = build_gsg_file_map()

    link_registry = load_link_registry()
    for old_name, new_path in file_map.items():
        link_registry[old_name] = new_path

    converted = 0
    errors = []

    for htm_file, out_path in file_map.items():
        src = GSG_DIR / htm_file
        if not src.exists():
            print(f"  WARNING: Source not found: {src}")
            errors.append(htm_file)
            continue

        dst = DOCS_OUT / out_path
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            title, markdown = convert_gsg_page(
                src, link_registry, output_path=out_path
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

    # Copy images
    for img in GSG_DIR.glob("*.png"):
        shutil.copy2(img, DOCS_OUT / "getting-started" / "tutorial")
    for img in GSG_DIR.glob("*.gif"):
        if img.name not in ("cicon2.gif", "cicon9.gif"):
            shutil.copy2(img, DOCS_OUT / "getting-started" / "tutorial")
    for img in GSG_DIR.glob("*.jpg"):
        if img.name != "topbar.jpg":
            shutil.copy2(img, DOCS_OUT / "getting-started" / "tutorial")

    # Check unmapped
    all_htm = set(f.name for f in GSG_DIR.glob("*.htm")
                  if f.name not in ("contpage.htm", "nodoc.htm"))
    mapped = set(file_map.keys())
    unmapped = all_htm - mapped
    if unmapped:
        print(f"\n  WARNING: {len(unmapped)} unmapped GSG files:")
        for f in sorted(unmapped):
            print(f"    {f}")

    save_link_registry(link_registry)

    print(f"\nGSG: {converted} converted, {len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors)}")

    return converted, errors, toc_entries, file_map


if __name__ == "__main__":
    print("=" * 60)
    print("Converting TADS 3 Tour Guide...")
    print("=" * 60)
    tg_converted, tg_errors, tg_toc, tg_map = convert_all_tourguide()

    print()
    print("=" * 60)
    print("Converting TADS 3 Getting Started Guide...")
    print("=" * 60)
    gsg_converted, gsg_errors, gsg_toc, gsg_map = convert_all_gsg()

    print()
    print("=" * 60)
    total = tg_converted + gsg_converted
    total_errors = len(tg_errors) + len(gsg_errors)
    print(f"TOTAL: {total} pages converted, {total_errors} errors")
    print("=" * 60)
