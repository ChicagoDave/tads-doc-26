#!/usr/bin/env python3
"""
Convert TADS 3 System Manual HTML pages to Markdown.

Reads from: tads-sources/t3doc/sysman/
Writes to:  docs/docs/language/, docs/docs/intrinsics/, docs/docs/tools/
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from convert_utils import (
    T3DOC, DOCS_OUT, convert_sysman_page, load_link_registry,
    save_link_registry, load_html
)

SYSMAN_DIR = T3DOC / "sysman"

# Map sysman .htm files to output locations.
# Part I: Opening Moves -> language/
# Part II: The Tools -> tools/
# Part III: The Language -> language/
# Part IV: The Intrinsics -> intrinsics/
# Part V: The System Library -> language/ (system lib)
# Part VI: The User Interface -> language/ (UI)
# Part VII: Playing on the Web -> language/ (web)
# Part VIII: Translating -> appendices/

FILE_MAP = {
    # Part I: Opening Moves
    "intro.htm": "language/intro.md",
    "syntax.htm": "language/syntax.md",
    "naming.htm": "language/naming.md",
    "hello.htm": "language/hello.md",

    # Part II: The Tools
    "build.htm": "tools/build.md",
    "univpath.htm": "tools/univpath.md",
    "aloneexe.htm": "tools/aloneexe.md",
    "terp.htm": "tools/terp.md",

    # Part III: The Language
    "progstru.htm": "language/progstru.md",
    "charmap.htm": "language/charmap.md",
    "preproc.htm": "language/preproc.md",
    "types.htm": "language/types.md",
    "strlit.htm": "language/strlit.md",
    "enum.htm": "language/enum.md",
    "startup.htm": "language/startup.md",
    "inherit.htm": "language/inherit.md",
    "objdef.htm": "language/objdef.md",
    "inlineobj.htm": "language/inlineobj.md",
    "opoverload.htm": "language/opoverload.md",
    "multmeth.htm": "language/multmeth.md",
    "dynobj.htm": "language/dynobj.md",
    "gc.htm": "language/gc.md",
    "expr.htm": "language/expr.md",
    "proccode.htm": "language/proccode.md",
    "optparams.htm": "language/optparams.md",
    "namedargs.htm": "language/namedargs.md",
    "except.htm": "language/except.md",
    "anonfn.htm": "language/anonfn.md",
    "undef.htm": "language/undef.md",
    "reflect.htm": "language/reflect.md",
    "icext.htm": "language/icext.md",
    "export.htm": "language/export.md",
    "errmsg.htm": "language/errmsg.md",

    # Part IV: The Intrinsics - Function Sets
    "t3vm.htm": "intrinsics/functions/t3vm.md",
    "tadsgen.htm": "intrinsics/functions/tadsgen.md",
    "regex.htm": "intrinsics/functions/regex.md",
    "tadsio.htm": "intrinsics/functions/tadsio.md",
    "tadsnet.htm": "intrinsics/functions/tadsnet.md",
    "netsec.htm": "intrinsics/functions/netsec.md",
    "scripts.htm": "intrinsics/functions/scripts.md",
    "pack.htm": "intrinsics/functions/pack.md",

    # Part IV: The Intrinsics - Classes
    "bignum.htm": "intrinsics/classes/bignum.md",
    "bytearr.htm": "intrinsics/classes/bytearr.md",
    "charset.htm": "intrinsics/classes/charset.md",
    "collect.htm": "intrinsics/classes/collect.md",
    "date.htm": "intrinsics/classes/date.md",
    "dict.htm": "intrinsics/classes/dict.md",
    "dynfunc.htm": "intrinsics/classes/dynfunc.md",
    "file.htm": "intrinsics/classes/file.md",
    "filename.htm": "intrinsics/classes/filename.md",
    "gramprod.htm": "intrinsics/classes/gramprod.md",
    "httpreq.htm": "intrinsics/classes/httpreq.md",
    "httpsrv.htm": "intrinsics/classes/httpsrv.md",
    "icic.htm": "intrinsics/classes/icic.md",
    "iter.htm": "intrinsics/classes/iter.md",
    "list.htm": "intrinsics/classes/list.md",
    "lookup.htm": "intrinsics/classes/lookup.md",
    "objic.htm": "intrinsics/classes/objic.md",
    "rexpat.htm": "intrinsics/classes/rexpat.md",
    "framedesc.htm": "intrinsics/classes/framedesc.md",
    "string.htm": "intrinsics/classes/string.md",
    "strbuf.htm": "intrinsics/classes/strbuf.md",
    "strcomp.htm": "intrinsics/classes/strcomp.md",
    "tadsobj.htm": "intrinsics/classes/tadsobj.md",
    "tempfile.htm": "intrinsics/classes/tempfile.md",
    "timezone.htm": "intrinsics/classes/timezone.md",
    "vector.htm": "intrinsics/classes/vector.md",
    "wlookup.htm": "intrinsics/classes/wlookup.md",

    # Part V: The System Library
    "init.htm": "language/init.md",
    "tok.htm": "language/tok.md",
    "libmisc.htm": "language/libmisc.md",
    "nodef.htm": "language/nodef.md",

    # Part VI: The User Interface
    "fmt.htm": "language/fmt.md",
    "dispfn.htm": "language/dispfn.md",
    "banners.htm": "language/banners.md",

    # Part VII: Playing on the Web
    "webui.htm": "language/webui.md",
    "webdeploy.htm": "language/webdeploy.md",
    "webhost.htm": "language/webhost.md",

    # Part VIII: Translating and Localizing
    "errtrans.htm": "appendices/errtrans.md",
    "cmap.htm": "appendices/cmap.md",

    # Section intro/cover pages
    "begin.htm": "language/begin.md",
    "tools.htm": "tools/overview.md",
    "langsec.htm": "language/langsec.md",
    "builtins.htm": "intrinsics/builtins.md",
    "lib.htm": "language/lib.md",
    "ui.htm": "language/ui.md",
    "web.htm": "language/web.md",
    "local.htm": "appendices/local.md",

    # TOC and cover
    "toc.htm": None,  # Skip - we generate our own nav
    "cover.htm": None,  # Skip - we have our own landing page
}


def build_link_registry():
    """Build a mapping of old HTML filenames to new Markdown paths."""
    registry = {}
    for old_name, new_path in FILE_MAP.items():
        if new_path:
            registry[old_name] = new_path
    return registry


def convert_all():
    """Convert all System Manual pages."""
    link_registry = build_link_registry()

    converted = 0
    skipped = 0
    errors = []

    for htm_file, out_path in FILE_MAP.items():
        if out_path is None:
            skipped += 1
            continue

        src = SYSMAN_DIR / htm_file
        if not src.exists():
            print(f"  WARNING: Source file not found: {src}")
            errors.append(htm_file)
            continue

        dst = DOCS_OUT / out_path
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            title, markdown = convert_sysman_page(src, link_registry, output_path=out_path)
            with open(dst, "w", encoding="utf-8") as f:
                f.write(markdown)
            converted += 1
            print(f"  OK: {htm_file} -> {out_path}")
        except Exception as e:
            print(f"  ERROR: {htm_file}: {e}")
            errors.append(htm_file)

    # Check for any .htm files we missed
    all_htm = set(f.name for f in SYSMAN_DIR.glob("*.htm"))
    mapped_htm = set(FILE_MAP.keys())
    unmapped = all_htm - mapped_htm
    if unmapped:
        print(f"\n  WARNING: {len(unmapped)} unmapped files:")
        for f in sorted(unmapped):
            print(f"    {f}")

    # Save the link registry
    save_link_registry(link_registry)

    print(f"\nDone: {converted} converted, {skipped} skipped, {len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors)}")

    return converted, errors


if __name__ == "__main__":
    print("Converting TADS 3 System Manual...")
    convert_all()
