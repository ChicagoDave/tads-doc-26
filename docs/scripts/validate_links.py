"""
Link validator for the TADS 3 documentation site.

Scans all Markdown files under docs/docs/, extracts markdown links,
resolves each target path, and reports broken links categorized by type.

Usage:
    python3 docs/scripts/validate_links.py [--json]
"""

import re
import os
import sys
import json
from pathlib import Path
from urllib.parse import unquote

DOCS_ROOT = Path(__file__).parent.parent / "docs"
REPORT_PATH = Path(__file__).parent / "link_report.json"

# Regex to find markdown links: [text](href)
# Uses a balanced-paren aware pattern to handle filenames with parens
LINK_RE = re.compile(
    r'\[([^\]]*)\]'       # [text]
    r'\('                  # opening (
    r'([^)\s]+(?:\([^)]*\)[^)\s]*)*)'  # href, allowing balanced parens
    r'\)'                  # closing )
)

# Regions to skip (fenced code blocks)
FENCED_CODE_RE = re.compile(r'```.*?```', re.DOTALL)


def extract_links(content, filepath):
    """Extract all markdown links from content, skipping code blocks."""
    # Remove fenced code blocks
    cleaned = FENCED_CODE_RE.sub('', content)

    links = []
    for match in LINK_RE.finditer(cleaned):
        text = match.group(1)
        href = match.group(2)
        # Find line number in original content
        pos = match.start()
        # Approximate line number (from cleaned content)
        line_no = cleaned[:pos].count('\n') + 1
        links.append((text, href, line_no))
    return links


def classify_href(href):
    """Classify a link href by type."""
    if href.startswith(('http://', 'https://', 'mailto:', 'ftp://', 'news:', 'urn:')):
        return 'external'
    if href.startswith('#'):
        return 'fragment'
    return 'internal'


def resolve_link(md_file, href):
    """Resolve an internal link relative to the markdown file's location.

    Returns (resolved_path, fragment) where resolved_path is absolute.
    """
    # Strip fragment
    base, _, fragment = href.partition('#')
    if not base:
        return None, fragment  # fragment-only

    # URL-decode
    base = unquote(base)

    # Resolve relative to the file's directory
    file_dir = md_file.parent
    resolved = (file_dir / base).resolve()
    return resolved, fragment


def categorize_broken(md_file, href, resolved):
    """Categorize why a link is broken."""
    rel = str(md_file.relative_to(DOCS_ROOT))

    # Malformed external URL embedded in relative path
    if re.search(r'https?:/', href) or re.search(r'ftp:/', href):
        return 'malformed_url'

    # Old path references
    if 'libref/' in href or 'sysman/' in href and '../sysman' not in rel:
        return 'old_path'
    if 'techman/' in href:
        return 'old_path'

    # Parenthesized filename issue
    if '(' in href or ')' in href:
        return 'parenthesized'

    # Extension issues
    if href.endswith('.htm') or href.endswith('.html'):
        return 'unconverted_extension'

    return 'missing_target'


def validate_all():
    """Validate all links across all markdown files."""
    results = {
        'total_files': 0,
        'total_links': 0,
        'external_links': 0,
        'fragment_links': 0,
        'internal_links': 0,
        'ok_links': 0,
        'broken_links': 0,
        'broken_by_category': {
            'parenthesized': [],
            'old_path': [],
            'malformed_url': [],
            'unconverted_extension': [],
            'missing_target': [],
        },
    }

    md_files = sorted(DOCS_ROOT.rglob('*.md'))
    results['total_files'] = len(md_files)

    for md_file in md_files:
        content = md_file.read_text(errors='replace')
        links = extract_links(content, md_file)

        for text, href, line_no in links:
            results['total_links'] += 1
            kind = classify_href(href)

            if kind == 'external':
                results['external_links'] += 1
                continue
            if kind == 'fragment':
                results['fragment_links'] += 1
                continue

            results['internal_links'] += 1
            resolved, fragment = resolve_link(md_file, href)

            if resolved is None:
                continue  # fragment-only, already counted

            if resolved.exists():
                results['ok_links'] += 1
            else:
                results['broken_links'] += 1
                rel_file = str(md_file.relative_to(DOCS_ROOT))
                category = categorize_broken(md_file, href, resolved)
                results['broken_by_category'][category].append({
                    'file': rel_file,
                    'line': line_no,
                    'text': text,
                    'href': href,
                })

    return results


def print_report(results):
    """Print a human-readable summary."""
    print("=" * 60)
    print("TADS 3 Documentation - Link Validation Report")
    print("=" * 60)
    print(f"Files scanned:    {results['total_files']}")
    print(f"Total links:      {results['total_links']}")
    print(f"  External:       {results['external_links']}")
    print(f"  Fragment-only:  {results['fragment_links']}")
    print(f"  Internal:       {results['internal_links']}")
    print(f"    OK:           {results['ok_links']}")
    print(f"    Broken:       {results['broken_links']}")
    print()

    for category, items in results['broken_by_category'].items():
        if items:
            print(f"--- {category} ({len(items)} links) ---")
            # Show first 5 examples
            for entry in items[:5]:
                print(f"  {entry['file']}:{entry['line']}")
                print(f"    [{entry['text']}]({entry['href']})")
            if len(items) > 5:
                print(f"  ... and {len(items) - 5} more")
            print()


def main():
    json_output = '--json' in sys.argv
    results = validate_all()

    if json_output:
        # Serialize to JSON
        print(json.dumps(results, indent=2))
    else:
        print_report(results)

    # Always save JSON report
    with open(REPORT_PATH, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Full report saved to: {REPORT_PATH}")

    return 1 if results['broken_links'] > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
