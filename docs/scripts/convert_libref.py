#!/usr/bin/env python3
"""
Convert TADS 3 Library Reference (libref) HTML pages to Markdown.

The libref contains auto-generated HTML documentation for the adv3 library:
- 1,702 object/class pages in libref/object/
- 77 file pages in libref/file/
- Index pages (ClassIndex, ObjectIndex, ActionIndex, etc.)

HTML format uses consistent CSS classes:
  table.ban    - Banner/header (class name, type, source file)
  div.fdesc    - Full description
  div.mjhd     - Section headers
  table.decl   - Property/method declarations
  div.desc     - Item descriptions
  span.title   - Class/object name
  span.type    - "class"/"object"/"file" label
  span.rem     - Remarks (e.g., "OVERRIDDEN")

Reads from: tads-sources/t3doc/libref/
Writes to:  docs/docs/api/by-class/, docs/docs/api/by-file/
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

sys.path.insert(0, str(Path(__file__).parent))
from convert_utils import (
    T3DOC, DOCS_OUT, SCRIPTS_DIR,
    load_link_registry, save_link_registry,
    clean_markdown,
)


def load_libref_html(filepath):
    """Load libref HTML using html.parser (not lxml) to preserve flat structure."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return BeautifulSoup(f.read(), "html.parser")

LIBREF_DIR = T3DOC / "libref"
OBJECT_DIR = LIBREF_DIR / "object"
FILE_DIR = LIBREF_DIR / "file"
API_OUT = DOCS_OUT / "api"
BY_CLASS_OUT = API_OUT / "by-class"
BY_FILE_OUT = API_OUT / "by-file"


# ---------------------------------------------------------------------------
# HTML Description Extraction
# ---------------------------------------------------------------------------

def extract_desc_text(div):
    """
    Extract description text from a div.desc or div.fdesc element.
    Converts inline HTML to simple Markdown.
    """
    if div is None:
        return ""

    parts = []
    for child in div.children:
        if isinstance(child, NavigableString):
            text = str(child)
            parts.append(text)
        elif isinstance(child, Tag):
            if child.name == "p":
                parts.append("\n\n")
            elif child.name == "br":
                parts.append("  \n")
            elif child.name in ("b", "strong"):
                text = child.get_text().strip()
                if text:
                    parts.append(f"**{text}**")
            elif child.name in ("i", "em"):
                text = child.get_text().strip()
                if text == "no description available":
                    continue  # Skip placeholder text
                if text:
                    parts.append(f"*{text}*")
            elif child.name == "code":
                text = child.get_text().strip()
                if text:
                    parts.append(f"`{text}`")
            elif child.name == "a":
                href = child.get("href", "")
                text = child.get_text().strip()
                if text and href:
                    parts.append(f"[{text}]({href})")
                elif text:
                    parts.append(text)
            elif child.name == "pre":
                text = child.get_text()
                parts.append(f"\n```\n{text}\n```\n")
            elif child.name in ("ul", "ol"):
                items = child.find_all("li")
                for j, item in enumerate(items):
                    prefix = f"{j+1}. " if child.name == "ol" else "- "
                    parts.append(f"\n{prefix}{item.get_text().strip()}")
                parts.append("\n")
            elif child.name == "span":
                cls = child.get("class", [])
                if "rem" in cls:
                    continue  # Skip remark spans
                parts.append(child.get_text())
            elif child.name == "table":
                continue  # Skip embedded tables (inheritance declarations)
            else:
                parts.append(child.get_text())

    text = "".join(parts).strip()
    # Clean up whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


# ---------------------------------------------------------------------------
# Object/Class Page Parsing
# ---------------------------------------------------------------------------

def parse_object_page(filepath):
    """
    Parse a libref object/class HTML page into a structured dict.
    """
    soup = load_libref_html(filepath)
    data = {
        "name": "",
        "type": "class",  # "class" or "object"
        "source_file": "",
        "source_line": "",
        "description": "",
        "superclasses": [],
        "subclasses": [],
        "global_objects": [],
        "direct_properties": [],
        "inherited_properties": {},  # {parent_class: [prop_names]}
        "direct_methods": [],
        "inherited_methods": {},  # {parent_class: [method_names]}
    }

    # --- Header (table.ban) ---
    ban = soup.find("table", class_="ban")
    if ban:
        title_span = ban.find("span", class_="title")
        if title_span:
            data["name"] = title_span.get_text().strip()

        type_span = ban.find("span", class_="type")
        if type_span:
            data["type"] = type_span.get_text().strip()

        # Source file link
        right_td = ban.find("td", align="right")
        if right_td:
            file_link = right_td.find("a")
            if file_link:
                href = file_link.get("href", "")
                fname = file_link.get_text().strip()
                data["source_file"] = fname
            # Line number
            links = right_td.find_all("a")
            for link in links:
                text = link.get_text().strip()
                if text.isdigit():
                    data["source_line"] = text
                    break

    # --- Description (div.fdesc) ---
    fdesc = soup.find("div", class_="fdesc")
    if fdesc:
        data["description"] = extract_desc_text(fdesc)

    # --- Superclass Tree ---
    super_anchor = soup.find("a", attrs={"name": "_SuperClassTree_"})
    if super_anchor:
        data["superclasses"] = parse_class_tree(super_anchor)

    # --- Subclass Tree ---
    sub_anchor = soup.find("a", attrs={"name": "_SubClassTree_"})
    if sub_anchor:
        data["subclasses"] = parse_class_tree(sub_anchor)

    # --- Global Objects ---
    obj_anchor = soup.find("a", attrs={"name": "_ObjectSummary_"})
    if obj_anchor:
        data["global_objects"] = parse_summary_list(obj_anchor)

    # --- Property Summary ---
    prop_anchor = soup.find("a", attrs={"name": "_PropSummary_"})
    if prop_anchor:
        direct, inherited = parse_summary_section(prop_anchor)
        data["_prop_summary_direct"] = direct
        data["inherited_properties"] = inherited

    # --- Method Summary ---
    meth_anchor = soup.find("a", attrs={"name": "_MethodSummary_"})
    if meth_anchor:
        direct, inherited = parse_summary_section(meth_anchor)
        data["_meth_summary_direct"] = direct
        data["inherited_methods"] = inherited

    # --- Property Details ---
    prop_detail_anchor = soup.find("a", attrs={"name": "_Properties_"})
    if prop_detail_anchor:
        data["direct_properties"] = parse_detail_section(prop_detail_anchor)

    # --- Method Details ---
    meth_detail_anchor = soup.find("a", attrs={"name": "_Methods_"})
    if meth_detail_anchor:
        data["direct_methods"] = parse_detail_section(meth_detail_anchor)

    return data


def is_section_anchor(tag):
    """Check if a tag is a section boundary anchor like _SuperClassTree_."""
    return (
        isinstance(tag, Tag)
        and tag.name == "a"
        and tag.get("name", "").startswith("_")
    )


def is_footer(tag):
    """Check if a tag is the page footer."""
    return (
        isinstance(tag, Tag)
        and tag.name == "div"
        and "ftr" in tag.get("class", [])
    )


def elements_in_section(anchor):
    """
    Yield all Tag elements between this anchor and the next section anchor.
    Uses find_all_next() to handle arbitrary nesting from html.parser.
    """
    for elem in anchor.find_all_next():
        if elem is anchor:
            continue
        if not isinstance(elem, Tag):
            continue
        if is_section_anchor(elem) or is_footer(elem):
            return
        yield elem


def parse_class_tree(anchor):
    """
    Parse a superclass or subclass tree starting from the anchor.
    Returns list of class names.
    """
    names = []
    for elem in elements_in_section(anchor):
        if elem.name == "a" and elem.get("href"):
            name = elem.get_text().strip()
            if name and name not in names:
                names.append(name)
        elif elem.name == "code":
            text = elem.get_text().strip()
            if text == "object" and "object" not in names:
                names.append("object")
    return names


def parse_summary_list(anchor):
    """
    Parse a simple summary list (e.g., Global Objects).
    Returns list of names.
    """
    names = []
    for elem in elements_in_section(anchor):
        if elem.name == "a" and elem.get("href"):
            name = elem.get_text().strip()
            if name:
                names.append(name)
    return names


def parse_summary_section(anchor):
    """
    Parse a property/method summary section.
    Returns (direct_names, {parent: [names]}).
    """
    direct = []
    inherited = {}
    current_parent = None

    for elem in elements_in_section(anchor):
        if elem.name == "a" and elem.get("href"):
            name = elem.get_text().strip()
            if name:
                if current_parent:
                    inherited.setdefault(current_parent, []).append(name)
                else:
                    direct.append(name)
        elif elem.name == "p":
            text = elem.get_text().strip()
            m = re.match(r"Inherited from\s+(\S+)\s*:", text)
            if m:
                current_parent = m.group(1)

    return direct, inherited


def parse_detail_section(anchor):
    """
    Parse a property/method detail section.
    Returns list of dicts: {name, params, source, line, description, overridden}.
    """
    items = []

    for elem in elements_in_section(anchor):
        if elem.name == "table" and "decl" in elem.get("class", []):
            item = parse_decl_table(elem)
            # Look for the div.desc that follows this table
            desc_div = elem.find_next("div", class_="desc")
            if desc_div:
                # Make sure this desc belongs to us (not to a later decl)
                next_decl = elem.find_next("table", class_="decl")
                if next_decl is None or (
                    desc_div.sourceline is not None
                    and next_decl.sourceline is not None
                    and desc_div.sourceline < next_decl.sourceline
                ):
                    item["description"] = extract_desc_text(desc_div)
                elif hasattr(desc_div, 'sourcepos') and hasattr(next_decl, 'sourcepos'):
                    if desc_div.sourcepos < next_decl.sourcepos:
                        item["description"] = extract_desc_text(desc_div)
                else:
                    # Fallback: just use it if it's nearby
                    item["description"] = extract_desc_text(desc_div)
            items.append(item)

    return items


def parse_decl_table(table):
    """
    Parse a declaration table (table.decl).
    Returns {name, params, source, line, overridden}.
    """
    item = {
        "name": "",
        "params": "",
        "source": "",
        "line": "",
        "description": "",
        "overridden": False,
    }

    tds = table.find_all("td")
    if not tds:
        return item

    # First cell: code name + optional params + optional OVERRIDDEN
    first_td = tds[0]
    code = first_td.find("code")
    if code:
        text = code.get_text().strip()
        # Special: dobjFor(Action) and iobjFor(Action) are single names
        m_action = re.match(
            r"(dobjFor|iobjFor)\((\w+)\)\s*$", text
        )
        if m_action:
            item["name"] = f"{m_action.group(1)}({m_action.group(2)})"
        else:
            # Parse method name and params: "methodName (param1, param2)"
            # But not dobjFor/iobjFor which have action names in parens
            m_dobj = re.match(
                r"(dobjFor|iobjFor)\((\w+)\)\s+(.+)", text
            )
            if m_dobj:
                item["name"] = (
                    f"{m_dobj.group(1)}({m_dobj.group(2)})"
                )
                item["params"] = m_dobj.group(3).strip()
            else:
                m = re.match(r"(\S+)\s+\(([^)]*)\)", text)
                if m:
                    item["name"] = m.group(1)
                    item["params"] = m.group(2).strip()
                else:
                    item["name"] = text

    rem = first_td.find("span", class_="rem")
    if rem and "OVERRIDDEN" in rem.get_text():
        item["overridden"] = True

    # Second cell: source file + line
    if len(tds) > 1:
        second_td = tds[1]
        links = second_td.find_all("a")
        for link in links:
            href = link.get("href", "")
            text = link.get_text().strip()
            if "/file/" in href:
                item["source"] = text
            elif text.isdigit():
                item["line"] = text

    return item


# ---------------------------------------------------------------------------
# File Page Parsing
# ---------------------------------------------------------------------------

def parse_file_page(filepath):
    """Parse a libref file documentation page."""
    soup = load_libref_html(filepath)
    data = {
        "filename": "",
        "description": "",
        "classes": [],
        "objects": [],
        "functions": [],
    }

    # Header
    ban = soup.find("table", class_="ban")
    if ban:
        title_span = ban.find("span", class_="title")
        if title_span:
            data["filename"] = title_span.get_text().strip()

    # Description
    fdesc = soup.find("div", class_="fdesc")
    if fdesc:
        data["description"] = extract_desc_text(fdesc)

    # Classes
    cls_anchor = soup.find("a", attrs={"name": "_ClassSummary_"})
    if cls_anchor:
        data["classes"] = parse_summary_list(cls_anchor)

    # Objects
    obj_anchor = soup.find("a", attrs={"name": "_ObjectSummary_"})
    if obj_anchor:
        data["objects"] = parse_summary_list(obj_anchor)

    # Functions
    func_anchor = soup.find("a", attrs={"name": "_Functions_"})
    if func_anchor:
        data["functions"] = parse_detail_section(func_anchor)

    return data


# ---------------------------------------------------------------------------
# Markdown Rendering
# ---------------------------------------------------------------------------

def class_link(name, from_dir="by-class"):
    """Generate a relative link to a class page."""
    slug = name.lower()
    if from_dir == "by-class":
        return f"[{name}]({slug}.md)"
    elif from_dir == "by-file":
        return f"[{name}](../by-class/{slug}.md)"
    return f"[{name}](by-class/{slug}.md)"


def file_link(filename, from_dir="by-class"):
    """Generate a relative link to a file page."""
    slug = filename.lower()
    if from_dir == "by-class":
        return f"[{filename}](../by-file/{slug}.md)"
    elif from_dir == "by-file":
        return f"[{filename}]({slug}.md)"
    return f"[{filename}](by-file/{slug}.md)"


def render_class_page(data):
    """Render a class/object page as Markdown."""
    lines = []
    name = data["name"]
    obj_type = data["type"]

    # Title
    lines.append(f"# {name}\n")

    # Metadata line
    meta_parts = [f"*{obj_type}*"]
    if data["source_file"]:
        src = data["source_file"]
        slug = src.lower()
        meta_parts.append(
            f"defined in [{src}](../by-file/{slug}.md)"
        )
        if data["source_line"]:
            meta_parts[-1] += f" (line {data['source_line']})"
    lines.append(" — ".join(meta_parts) + "\n")

    # Description
    desc = data["description"]
    if desc:
        # Clean up the inheritance declaration line that sometimes appears
        desc = re.sub(
            r"\s*class\s+\*\*\w+\*\*\s*:.*$", "", desc, flags=re.MULTILINE
        )
        desc = desc.strip()
        if desc:
            lines.append(f"\n{desc}\n")

    # Superclass chain
    supers = data["superclasses"]
    if supers:
        # Show as breadcrumb: object > VocabObject > Thing > **ClassName**
        chain = []
        for s in supers:
            if s == name:
                continue
            if s == "object":
                chain.append("`object`")
            else:
                chain.append(class_link(s))
        if chain:
            lines.append(
                f"\n**Superclass chain:** {' > '.join(chain)} > **{name}**\n"
            )

    # Subclasses
    subs = [s for s in data["subclasses"] if s != name]
    if subs:
        if len(subs) <= 10:
            sub_links = ", ".join(class_link(s) for s in subs)
            lines.append(f"\n**Subclasses:** {sub_links}\n")
        else:
            lines.append(f"\n<details><summary>Subclasses ({len(subs)})"
                         f"</summary>\n")
            for s in subs:
                lines.append(f"- {class_link(s)}")
            lines.append(f"\n</details>\n")

    # Global Objects
    objs = data["global_objects"]
    if objs:
        obj_links = ", ".join(class_link(o) for o in objs)
        lines.append(f"\n**Global objects:** {obj_links}\n")

    # Direct Properties
    if data["direct_properties"]:
        lines.append("\n## Properties\n")
        for prop in data["direct_properties"]:
            pname = prop["name"]
            desc = prop.get("description", "")
            overridden = prop.get("overridden", False)
            tag = " *(overridden)*" if overridden else ""
            lines.append(f"\n### `{pname}`{tag}")
            lines.append("")
            if prop.get("source") and prop.get("line"):
                lines.append(
                    f"Defined in {prop['source']}, line {prop['line']}"
                )
                lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")

    # Inherited Properties
    if data["inherited_properties"]:
        lines.append("\n## Inherited Properties\n")
        for parent, props in data["inherited_properties"].items():
            prop_links = ", ".join(
                f"[`{p}`]({parent.lower()}.md#{p})" for p in props
            )
            lines.append(f"\n*From {class_link(parent)}:* {prop_links}\n")

    # Direct Methods
    if data["direct_methods"]:
        lines.append("\n## Methods\n")
        for meth in data["direct_methods"]:
            mname = meth["name"]
            params = meth.get("params", "")
            desc = meth.get("description", "")
            overridden = meth.get("overridden", False)
            tag = " *(overridden)*" if overridden else ""
            sig = f"`{mname}({params})`" if params else f"`{mname}`"
            lines.append(f"\n### {sig}{tag}")
            lines.append("")
            if meth.get("source") and meth.get("line"):
                lines.append(
                    f"Defined in {meth['source']}, line {meth['line']}"
                )
                lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")

    # Inherited Methods
    if data["inherited_methods"]:
        lines.append("\n## Inherited Methods\n")
        for parent, meths in data["inherited_methods"].items():
            meth_links = ", ".join(
                f"[`{m}`]({parent.lower()}.md#{m})" for m in meths
            )
            if len(meths) > 20:
                lines.append(f"\n<details><summary>From "
                             f"{class_link(parent)} ({len(meths)})"
                             f"</summary>\n")
                lines.append(meth_links)
                lines.append(f"\n</details>\n")
            else:
                lines.append(
                    f"\n*From {class_link(parent)}:* {meth_links}\n"
                )

    return "\n".join(lines) + "\n"


def render_file_page(data):
    """Render a file documentation page as Markdown."""
    lines = []
    fname = data["filename"]

    lines.append(f"# {fname}\n")

    if data["description"]:
        lines.append(f"\n{data['description']}\n")

    if data["classes"]:
        lines.append("\n## Classes\n")
        for cls in data["classes"]:
            lines.append(f"- {class_link(cls, 'by-file')}")
        lines.append("")

    if data["objects"]:
        lines.append("\n## Global Objects\n")
        for obj in data["objects"]:
            lines.append(f"- {class_link(obj, 'by-file')}")
        lines.append("")

    if data["functions"]:
        lines.append("\n## Functions\n")
        for func in data["functions"]:
            fname_f = func["name"]
            params = func.get("params", "")
            desc = func.get("description", "")
            sig = f"`{fname_f}({params})`" if params else f"`{fname_f}`"
            lines.append(f"\n### {sig}")
            lines.append("")
            if func.get("source") and func.get("line"):
                lines.append(
                    f"Defined in {func['source']}, line {func['line']}"
                )
                lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Index Generation
# ---------------------------------------------------------------------------

def generate_class_index(all_data):
    """Generate alphabetical class index page."""
    lines = []
    lines.append("# Class Index\n")
    lines.append(
        "All classes and objects in the TADS 3 adv3 library.\n"
    )

    # Sort by name (case-insensitive)
    sorted_data = sorted(all_data, key=lambda d: d["name"].lower())

    # Letter anchors
    letters = sorted(set(
        d["name"][0].upper() for d in sorted_data if d["name"]
    ))
    letter_links = " ".join(f"[{l}](#{l.lower()})" for l in letters)
    lines.append(f"\n{letter_links}\n")

    current_letter = ""
    for d in sorted_data:
        name = d["name"]
        if not name:
            continue
        letter = name[0].upper()
        if letter != current_letter:
            current_letter = letter
            lines.append(f"\n## {letter} {{#{letter.lower()}}}\n")

        obj_type = d["type"]
        slug = name.lower()
        src = d.get("source_file", "")
        desc_preview = d.get("description", "")
        # Truncate description for index
        if desc_preview:
            desc_preview = desc_preview.split("\n")[0][:120]
            if len(desc_preview) == 120:
                desc_preview += "..."

        line = f"- [{name}]({slug}.md)"
        if obj_type == "object":
            line += " *(object)*"
        if desc_preview:
            line += f" — {desc_preview}"
        lines.append(line)

    lines.append(f"\n\n*{len(sorted_data)} entries*\n")
    return "\n".join(lines) + "\n"


def generate_file_index(all_file_data):
    """Generate file listing index page."""
    lines = []
    lines.append("# Source File Index\n")
    lines.append(
        "All source files in the TADS 3 adv3 library.\n"
    )

    sorted_data = sorted(all_file_data, key=lambda d: d["filename"].lower())

    for d in sorted_data:
        fname = d["filename"]
        slug = fname.lower()
        desc = d.get("description", "")
        if desc:
            desc = desc.split("\n")[0][:120]
            if len(desc) == 120:
                desc += "..."

        line = f"- [{fname}]({slug}.md)"
        if desc:
            line += f" — {desc}"
        lines.append(line)

    lines.append(f"\n\n*{len(sorted_data)} files*\n")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Conversion Pipeline
# ---------------------------------------------------------------------------

def convert_all_objects():
    """Convert all libref object/class pages."""
    BY_CLASS_OUT.mkdir(parents=True, exist_ok=True)

    html_files = sorted(OBJECT_DIR.glob("*.html"))
    print(f"Found {len(html_files)} object pages")

    all_data = []
    converted = 0
    errors = []
    link_registry = load_link_registry()

    for html_file in html_files:
        try:
            data = parse_object_page(html_file)
            name = data["name"]
            if not name:
                print(f"  SKIP: {html_file.name} (no name found)")
                continue

            slug = name.lower()
            out_path = BY_CLASS_OUT / f"{slug}.md"
            md = render_class_page(data)
            md = clean_markdown(md)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)

            # Register in link registry
            old_key = html_file.name  # e.g., "Fixture.html"
            new_path = f"api/by-class/{slug}.md"
            link_registry[old_key] = new_path

            all_data.append(data)
            converted += 1
        except Exception as e:
            print(f"  ERROR: {html_file.name}: {e}")
            import traceback
            traceback.print_exc()
            errors.append(html_file.name)

    # Generate class index
    index_md = generate_class_index(all_data)
    index_md = clean_markdown(index_md)
    with open(BY_CLASS_OUT / "index.md", "w", encoding="utf-8") as f:
        f.write(index_md)

    save_link_registry(link_registry)

    print(f"\nObjects: {converted} converted, {len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors[:20])}")

    return converted, errors, all_data


def convert_all_files():
    """Convert all libref file documentation pages."""
    BY_FILE_OUT.mkdir(parents=True, exist_ok=True)

    html_files = sorted(FILE_DIR.glob("*.html"))
    print(f"Found {len(html_files)} file pages")

    all_file_data = []
    converted = 0
    errors = []
    link_registry = load_link_registry()

    for html_file in html_files:
        try:
            data = parse_file_page(html_file)
            fname = data["filename"]
            if not fname:
                print(f"  SKIP: {html_file.name} (no filename found)")
                continue

            slug = fname.lower()
            out_path = BY_FILE_OUT / f"{slug}.md"
            md = render_file_page(data)
            md = clean_markdown(md)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md)

            # Register
            old_key = html_file.name
            new_path = f"api/by-file/{slug}.md"
            link_registry[old_key] = new_path

            all_file_data.append(data)
            converted += 1
        except Exception as e:
            print(f"  ERROR: {html_file.name}: {e}")
            import traceback
            traceback.print_exc()
            errors.append(html_file.name)

    # Generate file index
    index_md = generate_file_index(all_file_data)
    index_md = clean_markdown(index_md)
    with open(BY_FILE_OUT / "index.md", "w", encoding="utf-8") as f:
        f.write(index_md)

    save_link_registry(link_registry)

    print(f"\nFiles: {converted} converted, {len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors[:20])}")

    return converted, errors, all_file_data


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Converting TADS 3 Library Reference - Object Pages...")
    print("=" * 60)
    obj_converted, obj_errors, all_obj = convert_all_objects()

    print()
    print("=" * 60)
    print("Converting TADS 3 Library Reference - File Pages...")
    print("=" * 60)
    file_converted, file_errors, all_files = convert_all_files()

    print()
    print("=" * 60)
    total = obj_converted + file_converted
    total_errors = len(obj_errors) + len(file_errors)
    print(f"TOTAL: {total} pages converted, {total_errors} errors")
    print("=" * 60)
