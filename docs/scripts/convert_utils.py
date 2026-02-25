"""
Shared conversion utilities for TADS 3 HTML-to-Markdown conversion.

Handles the common patterns across sysman, techman, tourguide, and libref HTML docs.
"""

import re
import os
import json
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

# Paths
TADS_SOURCES = Path("/Users/david/repos/tads3/tads-sources")
T3DOC = TADS_SOURCES / "t3doc"
DOCS_OUT = Path("/Users/david/repos/tads3/docs/docs")
SCRIPTS_DIR = Path("/Users/david/repos/tads3/docs/scripts")

# Link registry: maps old HTML paths to new Markdown paths
LINK_REGISTRY_PATH = SCRIPTS_DIR / "link_registry.json"


def load_html(filepath):
    """Load and parse an HTML file with BeautifulSoup.

    Tries UTF-8 first; falls back to Windows-1252 for legacy TADS docs
    that use cp1252 characters (em-dashes, smart quotes, etc.).
    """
    with open(filepath, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("cp1252")
    return BeautifulSoup(text, "lxml")


def extract_title(soup):
    """Extract the page title from <title> or first <h1>."""
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        return title_tag.string.strip()
    h1 = soup.find("h1")
    if h1:
        return get_text(h1).strip()
    return "Untitled"


def get_text(element):
    """Get clean text content from a BeautifulSoup element."""
    if isinstance(element, NavigableString):
        return str(element)
    return element.get_text()


def strip_navigation(soup):
    """Remove topbar, navigation divs, and footer from sysman/techman pages."""
    for div in soup.find_all("div", class_="topbar"):
        div.decompose()
    for div in soup.find_all("div", class_="nav"):
        div.decompose()
    for div in soup.find_all("div", class_="navb"):
        div.decompose()
    for hr in soup.find_all("hr", class_="navb"):
        hr.decompose()
    for div in soup.find_all("div", class_="footer"):
        div.decompose()


def convert_element(element, depth=0):
    """
    Recursively convert an HTML element to Markdown.
    Returns a string of Markdown text.
    """
    if isinstance(element, NavigableString):
        text = str(element)
        # Escape literal < so it won't be interpreted as HTML in markdown.
        # lxml decodes &lt; entities to <, which would become invisible tags.
        text = text.replace("<", "&lt;")
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
        if src and not src.endswith(("topbar.jpg", "getacro.gif")):
            return f"![{alt}]({src})"
        return ""

    # Code blocks: <div class="code"><pre>...</pre></div>
    if tag == "div" and "code" in element.get("class", []):
        return convert_code_block(element)

    # Command line blocks
    if tag == "div" and "cmdline" in element.get("class", []):
        return convert_code_block(element, lang="console")

    # Syntax diagrams
    if tag == "div" and "syntax" in element.get("class", []):
        return convert_syntax_block(element)

    # Pull quotes
    if tag == "div" and "pullquote" in element.get("class", []):
        content = convert_children(element, depth)
        lines = content.strip().split("\n")
        return "\n" + "\n".join(f"> {line}" for line in lines) + "\n\n"

    # Function/parameter definitions
    if tag == "div" and "fdef" in element.get("class", []):
        content = convert_children(element, depth)
        return "\n" + content + "\n"

    # Error message blocks
    if tag == "div" and "errvb" in element.get("class", []):
        content = convert_children(element, depth)
        return "\n" + content + "\n"

    # Section TOC divs
    if tag == "div" and "sectoc" in element.get("class", []):
        content = convert_children(element, depth)
        return "\n" + content + "\n"

    # Main content div - just recurse
    if tag == "div" and "main" in element.get("class", []):
        return convert_children(element, depth)

    # Generic div - just recurse
    if tag == "div":
        return convert_children(element, depth)

    # Headings
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag[1])
        text = convert_children(element, depth).strip()
        # Clean up any residual inline formatting
        return f"\n{'#' * level} {text}\n\n"

    # Paragraphs
    if tag == "p":
        content = convert_children(element, depth).strip()
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
        content = convert_children(element, depth)
        content = content.strip()
        if not content:
            return ""
        return f"**{content}**"

    # Italic
    if tag in ("i", "em"):
        content = convert_children(element, depth)
        content = content.strip()
        if not content:
            return ""
        return f"*{content}*"

    # Inline code
    if tag == "span" and "code" in element.get("class", []):
        text = get_text(element).strip()
        if text:
            # Escape backticks inside code spans
            if "`" in text:
                return f"`` {text} ``"
            return f"`{text}`"
        return ""

    # Inline code via <tt> or <code>
    if tag in ("tt", "code"):
        # Check if inside a <pre> - if so, don't add backticks
        if element.find_parent("pre"):
            return convert_children(element, depth)
        text = get_text(element).strip()
        if text:
            if "`" in text:
                return f"`` {text} ``"
            return f"`{text}`"
        return ""

    # Syntax literal spans (used in syntax diagrams, handled by parent)
    if tag == "span" and "synLit" in element.get("class", []):
        return get_text(element)
    if tag == "span" and "synPar" in element.get("class", []):
        return get_text(element)
    if tag == "span" and "synMark" in element.get("class", []):
        return get_text(element)

    # Error ID spans
    if tag == "span" and "errid" in element.get("class", []):
        text = get_text(element).strip()
        return f"**{text}**"

    # Generic span
    if tag == "span":
        return convert_children(element, depth)

    # Links
    if tag == "a":
        href = element.get("href", "")
        text = convert_children(element, depth).strip()
        name = element.get("name", "")

        # Anchor targets (named anchors)
        if name and not href:
            # mkdocs generates anchors from headings; for standalone anchors
            # we'll use an HTML anchor
            anchor = f'<a name="{name}"></a>'
            # Preserve children: lxml auto-closes malformed <a name="...">
            # tags by nesting subsequent content as children, which we must
            # not discard
            if text:
                return anchor + text
            return anchor

        if not text:
            return ""

        if href:
            return f"[{text}]({href})"
        return text

    # Unordered lists
    if tag == "ul":
        return "\n" + convert_list(element, ordered=False, depth=depth) + "\n"

    # Ordered lists
    if tag == "ol":
        return "\n" + convert_list(element, ordered=True, depth=depth) + "\n"

    # List items (handled by convert_list)
    if tag == "li":
        return convert_children(element, depth)

    # Definition lists
    if tag == "dl":
        return convert_definition_list(element, depth)
    if tag == "dt":
        content = convert_children(element, depth).strip()
        return f"\n**{content}**\n"
    if tag == "dd":
        content = convert_children(element, depth).strip()
        return f":   {content}\n\n"

    # Tables
    if tag == "table":
        return convert_table(element, depth)

    # Pre-formatted (standalone, not inside div.code)
    if tag == "pre":
        text = get_text(element)
        return f"\n```\n{text}\n```\n\n"

    # Blockquote
    if tag == "blockquote":
        content = convert_children(element, depth)
        lines = content.strip().split("\n")
        return "\n" + "\n".join(f"> {line}" for line in lines) + "\n\n"

    # Center tag (just pass through content)
    if tag == "center":
        return convert_children(element, depth)

    # Font tags (strip, keep content)
    if tag == "font":
        return convert_children(element, depth)

    # Sub/superscript
    if tag == "sub":
        return convert_children(element, depth)
    if tag == "sup":
        return convert_children(element, depth)

    # Default: just recurse into children
    return convert_children(element, depth)


def convert_children(element, depth=0):
    """Convert all children of an element to Markdown."""
    parts = []
    for child in element.children:
        parts.append(convert_element(child, depth))
    return "".join(parts)


def convert_code_block(element, lang="tads3"):
    """Convert a <div class="code"><pre>...</pre></div> to a fenced code block."""
    pre = element.find("pre")
    if pre:
        # Get raw text content, preserving whitespace
        code = get_pre_text(pre)
    else:
        code = get_text(element)

    # Strip leading/trailing blank lines but preserve internal whitespace
    lines = code.split("\n")

    # Remove leading empty lines
    while lines and not lines[0].strip():
        lines.pop(0)
    # Remove trailing empty lines
    while lines and not lines[-1].strip():
        lines.pop()

    code = "\n".join(lines)

    return f"\n```{lang}\n{code}\n```\n\n"


def get_pre_text(pre_element):
    """
    Extract text from a <pre> element, handling inline tags like <b>, <i>, <a>.
    Preserves whitespace structure.
    """
    parts = []
    for child in pre_element.descendants:
        if isinstance(child, NavigableString):
            parts.append(str(child))
    return "".join(parts)


def convert_syntax_block(element):
    """
    Convert a <div class="syntax"> block.
    These use span.synLit (literals), span.synPar (parameters), span.synMark (markers).
    Convert to a fenced block with annotation.
    """
    # Get the text representation
    pre = element.find("pre")
    if pre:
        text = get_pre_text(pre)
    else:
        text = get_text(element)

    lines = text.strip().split("\n")
    # Remove leading/trailing blank lines
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    text = "\n".join(lines)
    return f"\n```\n{text}\n```\n\n"


def convert_list(element, ordered=False, depth=0):
    """Convert a <ul> or <ol> to Markdown list items."""
    items = []
    counter = 1
    for child in element.children:
        if isinstance(child, Tag) and child.name == "li":
            content = convert_children(child, depth + 1).strip()
            # Handle multi-line content in list items
            lines = content.split("\n")
            if ordered:
                prefix = f"{counter}. "
                counter += 1
            else:
                prefix = "- "

            indent = "  " * depth
            first_line = f"{indent}{prefix}{lines[0]}"
            rest = []
            for line in lines[1:]:
                if line.strip():
                    rest.append(f"{indent}  {line}")
                else:
                    rest.append("")

            item = first_line
            if rest:
                item += "\n" + "\n".join(rest)
            items.append(item)

    return "\n".join(items) + "\n"


def convert_definition_list(element, depth=0):
    """Convert a <dl> to Markdown."""
    parts = []
    for child in element.children:
        if isinstance(child, Tag):
            parts.append(convert_element(child, depth))
    return "\n" + "".join(parts)


def convert_table(element, depth=0):
    """
    Convert an HTML table to Markdown table.
    For complex tables, falls back to HTML passthrough.
    """
    rows = element.find_all("tr")
    if not rows:
        return ""

    # Check if this is a simple table we can convert
    # (no rowspan/colspan, consistent column count)
    col_counts = []
    for row in rows:
        cells = row.find_all(["td", "th"])
        has_span = any(
            cell.get("rowspan") or cell.get("colspan")
            for cell in cells
        )
        if has_span:
            # Fall back to HTML passthrough for complex tables
            return f"\n{element}\n\n"
        col_counts.append(len(cells))

    if not col_counts or max(col_counts) == 0:
        return ""

    num_cols = max(col_counts)

    # Build markdown table
    md_rows = []
    for i, row in enumerate(rows):
        cells = row.find_all(["td", "th"])
        cell_texts = []
        for cell in cells:
            text = convert_children(cell, depth).strip()
            # Remove newlines within table cells
            text = re.sub(r"\n+", " ", text)
            cell_texts.append(text)

        # Pad to num_cols
        while len(cell_texts) < num_cols:
            cell_texts.append("")

        md_rows.append("| " + " | ".join(cell_texts) + " |")

        # Add separator after first row (header)
        if i == 0:
            md_rows.append("|" + "|".join(["---"] * num_cols) + "|")

    return "\n" + "\n".join(md_rows) + "\n\n"


def clean_markdown(text):
    """Clean up generated Markdown text."""
    # Fix multiple consecutive blank lines (max 2)
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    # Fix spaces before/after bold/italic markers
    text = re.sub(r"\*\*\s+\*\*", "", text)  # Empty bold
    text = re.sub(r"\*\s+\*", "", text)  # Empty italic

    # Clean up non-breaking spaces that might have leaked through
    text = text.replace("&nbsp;", " ")

    # Ensure file ends with single newline
    text = text.rstrip() + "\n"

    return text


def rewrite_link(href, link_registry=None):
    """
    Rewrite an HTML link to point to the new Markdown location.
    """
    if not href:
        return href

    # External links - leave as-is
    if href.startswith(("http://", "https://", "mailto:", "ftp://")):
        return href

    # Fragment-only links - leave as-is
    if href.startswith("#"):
        return href

    # Strip any fragment
    base, _, fragment = href.partition("#")

    if link_registry and base in link_registry:
        new_path = link_registry[base]
        if fragment:
            return f"{new_path}#{fragment}"
        return new_path

    # Default: convert .htm/.html to .md
    if base.endswith(".htm"):
        base = base[:-4] + ".md"
    elif base.endswith(".html"):
        base = base[:-5] + ".md"

    if fragment:
        return f"{base}#{fragment}"
    return base


def save_link_registry(registry):
    """Save the link registry to disk."""
    with open(LINK_REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2, sort_keys=True)


def load_link_registry():
    """Load the link registry from disk."""
    if LINK_REGISTRY_PATH.exists():
        with open(LINK_REGISTRY_PATH) as f:
            return json.load(f)
    return {}


def convert_sysman_page(filepath, link_registry=None, output_path=None):
    """
    Convert a single sysman/techman HTML page to Markdown.
    Returns (title, markdown_content).

    output_path: the path of the output .md file relative to docs/ root
                 (e.g. "language/anonfn.md"). Used to compute correct relative links.
    """
    soup = load_html(filepath)
    title = extract_title(soup)

    # Strip navigation and chrome
    strip_navigation(soup)

    # Find main content
    main = soup.find("div", class_="main")
    if not main:
        # Some pages don't have div.main wrapper
        main = soup.find("body")
    if not main:
        return title, f"# {title}\n\n*Conversion error: no content found.*\n"

    # Convert to markdown
    md = convert_element(main)

    # Rewrite internal links
    if link_registry:
        md = rewrite_links_in_markdown(md, link_registry, output_path)

    # Clean up
    md = clean_markdown(md)

    return title, md


def rewrite_links_in_markdown(md, link_registry, current_page_path=None):
    """
    Rewrite [text](link) references in markdown using the link registry.
    current_page_path: path of the current page relative to docs/ root,
                       e.g. "intrinsics/builtins.md"
    """
    def replace_link(match):
        text = match.group(1)
        href = match.group(2)
        new_href = rewrite_link(href, link_registry)

        # If we have a current page path and the link is to a docs-root-relative
        # path (not external, not anchor-only), compute relative path
        if current_page_path and new_href and not new_href.startswith(("http://", "https://", "mailto:", "#")):
            new_href = compute_relative_path(current_page_path, new_href)

        return f"[{text}]({new_href})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", replace_link, md)


def compute_relative_path(from_path, to_path):
    """
    Compute a relative path from one docs page to another.
    Both paths are relative to the docs/ root.
    E.g., from "intrinsics/builtins.md" to "intrinsics/functions/t3vm.md"
    yields "functions/t3vm.md".
    """
    from pathlib import PurePosixPath

    from_dir = str(PurePosixPath(from_path).parent)
    to_parts = PurePosixPath(to_path)

    # Split any fragment
    to_str = str(to_parts)
    base, _, fragment = to_str.partition("#")

    try:
        rel = os.path.relpath(base, from_dir)
    except ValueError:
        rel = base

    if fragment:
        return f"{rel}#{fragment}"
    return rel
