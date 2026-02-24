#!/usr/bin/env python3
"""
Validate text content in converted TADS 3 Markdown against original HTML sources.

Extracts visible text from both HTML and Markdown, normalizes it, and compares
at the sentence level using fuzzy matching. Also detects encoding issues.

Usage:
    python3 docs/scripts/validate_text.py [--source NAME] [--all] [--verbose]
"""

import sys
import re
from pathlib import Path
from difflib import SequenceMatcher

sys.path.insert(0, str(Path(__file__).parent))
from validate_utils import (
    build_file_pairs, build_arg_parser,
    extract_html_text, extract_md_text,
    check_encoding_issues,
    write_json_report, make_report_base, SCRIPTS_DIR, DOCS_OUT,
)

REPORT_PATH = SCRIPTS_DIR / "text_validation_report.json"
MATCH_THRESHOLD = 0.85
MIN_SENTENCE_LEN = 20  # Ignore very short fragments


def split_sentences(text):
    """Split normalized text into sentence-like units for comparison."""
    # Split on sentence-ending punctuation followed by space, or on double-space
    parts = re.split(r'(?<=[.!?:;])\s+', text)
    return [p.strip() for p in parts if len(p.strip()) >= MIN_SENTENCE_LEN]


def compare_texts(html_text, md_text, threshold=MATCH_THRESHOLD):
    """
    Compare HTML and MD text at the sentence level.
    Returns (missing_from_md, extra_in_md) lists.
    """
    html_sentences = split_sentences(html_text)
    md_sentences = split_sentences(md_text)

    if not html_sentences:
        return [], []

    missing = []
    extra = []

    # Build set for fast exact matching
    md_set = set(md_sentences)
    html_set = set(html_sentences)

    # Find sentences in HTML not in MD
    unmatched_html = []
    for hs in html_sentences:
        if hs in md_set:
            continue
        unmatched_html.append(hs)

    # Fuzzy match unmatched HTML sentences
    for hs in unmatched_html:
        best_ratio = 0
        if md_sentences:
            for ms in md_sentences:
                ratio = SequenceMatcher(None, hs, ms).quick_ratio()
                if ratio > best_ratio:
                    # Only compute full ratio for promising candidates
                    if ratio > threshold * 0.9:
                        ratio = SequenceMatcher(None, hs, ms).ratio()
                    best_ratio = ratio
                if best_ratio >= threshold:
                    break
        if best_ratio < threshold:
            missing.append(hs)

    # Find sentences in MD not in HTML (less critical)
    unmatched_md = []
    for ms in md_sentences:
        if ms in html_set:
            continue
        unmatched_md.append(ms)

    for ms in unmatched_md:
        best_ratio = 0
        if html_sentences:
            for hs in html_sentences:
                ratio = SequenceMatcher(None, ms, hs).quick_ratio()
                if ratio > best_ratio:
                    if ratio > threshold * 0.9:
                        ratio = SequenceMatcher(None, ms, hs).ratio()
                    best_ratio = ratio
                if best_ratio >= threshold:
                    break
        if best_ratio < threshold:
            extra.append(ms)

    return missing, extra


def validate_file(file_pair, verbose=False):
    """Validate text content in a single file pair."""
    try:
        html_text = extract_html_text(file_pair)
        md_text = extract_md_text(file_pair.output_path)
    except Exception as e:
        return {"error": str(e)}

    if not html_text.strip():
        return None  # Empty source — nothing to validate

    # Compare texts
    missing, extra = compare_texts(html_text, md_text)

    # Check encoding issues in the markdown file
    raw_md = Path(file_pair.output_path).read_text(encoding="utf-8", errors="replace")
    enc_issues = check_encoding_issues(raw_md)

    has_issues = missing or extra or enc_issues

    if has_issues or verbose:
        result = {
            "source": file_pair.source_name,
            "format": file_pair.format_type,
            "html_text_len": len(html_text),
            "md_text_len": len(md_text),
        }
        if missing:
            result["missing_sentences"] = missing[:20]  # Cap at 20
            result["missing_count"] = len(missing)
        if extra:
            result["extra_sentences"] = extra[:20]
            result["extra_count"] = len(extra)
        if enc_issues:
            result["encoding_issues"] = enc_issues
        return result

    return None  # Clean


def print_summary(report):
    """Print human-readable validation summary."""
    print("=" * 70)
    print("TADS 3 Documentation — Text Validation Report")
    print("=" * 70)
    print(f"Files checked:      {report['files_checked']} / {report['total_files']}")
    print(f"Files with issues:  {report['files_with_issues']}")
    print()

    if not report["files"]:
        print("All text content matches. No issues found.")
        print("=" * 70)
        return

    # Categorize
    missing_files = []
    extra_files = []
    encoding_files = []

    for md_path, info in sorted(report["files"].items()):
        if "error" in info:
            print(f"  ERROR: {md_path}: {info['error']}")
            continue
        if info.get("missing_count"):
            missing_files.append((md_path, info))
        if info.get("extra_count"):
            extra_files.append((md_path, info))
        if info.get("encoding_issues"):
            encoding_files.append((md_path, info))

    if encoding_files:
        print(f"--- Encoding Issues ({len(encoding_files)} files) ---")
        for md_path, info in encoding_files:
            for issue in info["encoding_issues"]:
                print(f"  {md_path}: {issue}")
        print()

    if missing_files:
        total = sum(f[1]["missing_count"] for f in missing_files)
        print(f"--- Missing Text ({total} sentences in {len(missing_files)} files) ---")
        for md_path, info in missing_files[:20]:  # Show top 20
            print(f"  {md_path} (from {info['source']}, "
                  f"{info['missing_count']} missing):")
            for s in info.get("missing_sentences", [])[:3]:
                preview = s[:100].replace("\n", " ")
                print(f"    MISSING: \"{preview}...\"")
        if len(missing_files) > 20:
            print(f"  ... and {len(missing_files) - 20} more files")
        print()

    if extra_files:
        total = sum(f[1]["extra_count"] for f in extra_files)
        print(f"--- Extra Text ({total} sentences in {len(extra_files)} files) ---")
        for md_path, info in extra_files[:10]:
            print(f"  {md_path}: {info['extra_count']} extra sentences")
        if len(extra_files) > 10:
            print(f"  ... and {len(extra_files) - 10} more files")
        print()

    print(f"Summary: {report['files_with_issues']} files need review")
    print("=" * 70)


def main():
    parser = build_arg_parser("Validate text content in converted TADS 3 documentation")
    args = parser.parse_args()

    # Build file pairs
    pairs = build_file_pairs(
        sources=args.source,
        include_libref=args.all,
    )

    # Filter to single file if requested
    if args.file:
        target = args.file
        pairs = [p for p in pairs if target in str(p.output_path)]
        if not pairs:
            print(f"No file pair found matching: {target}", file=sys.stderr)
            return 2

    total = len(pairs)
    report = make_report_base("validate_text", total, 0, 0)

    checked = 0
    for pair in pairs:
        result = validate_file(pair, verbose=args.verbose)
        checked += 1
        if result:
            rel_path = str(pair.output_path.relative_to(pair.output_path.parents[2]))
            report["files"][rel_path] = result
            has_issue = (
                result.get("missing_count")
                or result.get("extra_count")
                or result.get("encoding_issues")
                or result.get("error")
            )
            if has_issue:
                report["files_with_issues"] += 1

        # Progress
        if checked % 50 == 0:
            print(f"  Checked {checked}/{total}...", file=sys.stderr)

    report["files_checked"] = checked
    report["files_skipped"] = total - checked

    if args.json:
        import json
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_summary(report)
        write_json_report(report, REPORT_PATH)

    return 1 if report["files_with_issues"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
