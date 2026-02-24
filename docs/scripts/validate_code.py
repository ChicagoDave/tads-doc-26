#!/usr/bin/env python3
"""
Validate code blocks in converted TADS 3 Markdown against original HTML sources.

Extracts code blocks from both HTML (format-aware) and Markdown (fenced blocks),
matches them in sequence, and reports missing, extra, or different blocks.

Usage:
    python3 docs/scripts/validate_code.py [--source NAME] [--all] [--verbose]
"""

import sys
import difflib
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_utils import (
    build_file_pairs, build_arg_parser,
    extract_html_code_blocks, extract_md_code_blocks,
    clean_code_text, check_encoding_issues,
    write_json_report, make_report_base, SCRIPTS_DIR,
)

REPORT_PATH = SCRIPTS_DIR / "code_validation_report.json"


def normalize_code_for_matching(text):
    """Normalize code for sequence matching (not for display)."""
    return re.sub(r'\s+', ' ', text.strip())


def compare_code_blocks(html_blocks, md_blocks):
    """
    Compare code blocks from HTML and Markdown.
    Uses SequenceMatcher to align blocks, then diffs matched pairs.
    """
    result = {
        "html_count": len(html_blocks),
        "md_count": len(md_blocks),
        "matched": 0,
        "identical": 0,
        "differences": [],
        "missing_from_md": [],
        "extra_in_md": [],
    }

    if not html_blocks and not md_blocks:
        return result

    # Normalize for matching
    html_norm = [normalize_code_for_matching(b) for b in html_blocks]
    md_norm = [normalize_code_for_matching(b) for b in md_blocks]

    matcher = difflib.SequenceMatcher(None, html_norm, md_norm)

    for op, i1, i2, j1, j2 in matcher.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                result["matched"] += 1
                hi = i1 + k
                mi = j1 + k
                if html_blocks[hi].strip() == md_blocks[mi].strip():
                    result["identical"] += 1
                else:
                    diff = list(difflib.unified_diff(
                        html_blocks[hi].splitlines(keepends=True),
                        md_blocks[mi].splitlines(keepends=True),
                        fromfile="html", tofile="markdown", lineterm=""
                    ))
                    result["differences"].append({
                        "html_index": hi,
                        "md_index": mi,
                        "diff": "\n".join(diff[:30]),  # Limit diff size
                        "html_preview": html_blocks[hi][:200],
                        "md_preview": md_blocks[mi][:200],
                    })

        elif op == "delete":
            for k in range(i1, i2):
                result["missing_from_md"].append({
                    "html_index": k,
                    "preview": html_blocks[k][:200],
                })

        elif op == "insert":
            for k in range(j1, j2):
                result["extra_in_md"].append({
                    "md_index": k,
                    "preview": md_blocks[k][:200],
                })

        elif op == "replace":
            # Pair up what we can, report the rest
            pairs = min(i2 - i1, j2 - j1)
            for n in range(pairs):
                hi = i1 + n
                mi = j1 + n
                result["matched"] += 1
                diff = list(difflib.unified_diff(
                    html_blocks[hi].splitlines(keepends=True),
                    md_blocks[mi].splitlines(keepends=True),
                    fromfile="html", tofile="markdown", lineterm=""
                ))
                result["differences"].append({
                    "html_index": hi,
                    "md_index": mi,
                    "diff": "\n".join(diff[:30]),
                    "html_preview": html_blocks[hi][:200],
                    "md_preview": md_blocks[mi][:200],
                })
            # Leftover HTML blocks = missing
            for k in range(i1 + pairs, i2):
                result["missing_from_md"].append({
                    "html_index": k,
                    "preview": html_blocks[k][:200],
                })
            # Leftover MD blocks = extra
            for k in range(j1 + pairs, j2):
                result["extra_in_md"].append({
                    "md_index": k,
                    "preview": md_blocks[k][:200],
                })

    return result


def validate_file(file_pair, verbose=False):
    """Validate code blocks in a single file pair. Returns a result dict or None if clean."""
    try:
        html_blocks = extract_html_code_blocks(file_pair)
        md_blocks = extract_md_code_blocks(file_pair.output_path)
    except Exception as e:
        return {"error": str(e)}

    if not html_blocks and not md_blocks:
        return None  # No code blocks to validate

    result = compare_code_blocks(html_blocks, md_blocks)

    # Check for encoding issues in MD code blocks
    enc_issues = []
    for block in md_blocks:
        enc_issues.extend(check_encoding_issues(block))
    if enc_issues:
        result["encoding_issues"] = list(set(enc_issues))

    has_issues = (
        result["differences"]
        or result["missing_from_md"]
        or result["extra_in_md"]
        or enc_issues
    )

    if has_issues or verbose:
        return {
            "source": file_pair.source_name,
            "format": file_pair.format_type,
            **result,
        }

    return None  # Clean


def print_summary(report):
    """Print human-readable validation summary."""
    print("=" * 70)
    print("TADS 3 Documentation — Code Block Validation Report")
    print("=" * 70)
    print(f"Files checked:      {report['files_checked']} / {report['total_files']}")
    print(f"Files with issues:  {report['files_with_issues']}")
    print()

    if not report["files"]:
        print("All code blocks match. No issues found.")
        print("=" * 70)
        return

    # Group issues
    missing_files = []
    extra_files = []
    diff_files = []
    encoding_files = []

    for md_path, info in sorted(report["files"].items()):
        if "error" in info:
            print(f"  ERROR: {md_path}: {info['error']}")
            continue
        if info.get("missing_from_md"):
            missing_files.append((md_path, info))
        if info.get("extra_in_md"):
            extra_files.append((md_path, info))
        if info.get("differences"):
            diff_files.append((md_path, info))
        if info.get("encoding_issues"):
            encoding_files.append((md_path, info))

    if missing_files:
        total = sum(len(f[1]["missing_from_md"]) for f in missing_files)
        print(f"--- Missing Code Blocks ({total} blocks in {len(missing_files)} files) ---")
        for md_path, info in missing_files:
            print(f"  {md_path} (from {info['source']}):")
            for m in info["missing_from_md"]:
                preview = m["preview"].replace("\n", " ")[:80]
                print(f"    MISSING block #{m['html_index']}: {preview}...")
        print()

    if extra_files:
        total = sum(len(f[1]["extra_in_md"]) for f in extra_files)
        print(f"--- Extra Code Blocks ({total} blocks in {len(extra_files)} files) ---")
        for md_path, info in extra_files:
            print(f"  {md_path} (from {info['source']}):")
            for e in info["extra_in_md"]:
                preview = e["preview"].replace("\n", " ")[:80]
                print(f"    EXTRA block #{e['md_index']}: {preview}...")
        print()

    if diff_files:
        total = sum(len(f[1]["differences"]) for f in diff_files)
        print(f"--- Content Differences ({total} blocks in {len(diff_files)} files) ---")
        for md_path, info in diff_files:
            print(f"  {md_path} (from {info['source']}):")
            for d in info["differences"]:
                print(f"    DIFF block html#{d['html_index']} vs md#{d['md_index']}:")
                for line in d["diff"].split("\n")[:10]:
                    print(f"      {line}")
        print()

    if encoding_files:
        print(f"--- Encoding Issues ({len(encoding_files)} files) ---")
        for md_path, info in encoding_files:
            for issue in info["encoding_issues"]:
                print(f"  {md_path}: {issue}")
        print()

    print(f"Summary: {report['files_with_issues']} files need review")
    print("=" * 70)


def main():
    parser = build_arg_parser("Validate code blocks in converted TADS 3 documentation")
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
    report = make_report_base("validate_code", total, 0, 0)

    checked = 0
    for pair in pairs:
        result = validate_file(pair, verbose=args.verbose)
        checked += 1
        if result:
            rel_path = str(pair.output_path.relative_to(pair.output_path.parents[2]))
            report["files"][rel_path] = result
            if result.get("differences") or result.get("missing_from_md") or \
               result.get("extra_in_md") or result.get("encoding_issues"):
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
