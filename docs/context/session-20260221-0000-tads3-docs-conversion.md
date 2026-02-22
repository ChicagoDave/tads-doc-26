# TADS 3 Documentation Modernization — Progress

## Project Goal

Convert ~2,500 HTML pages of frozen (2016) TADS 3 documentation into a unified, modern, searchable mkdocs-material site. Extract API docs from source code. Write new architectural documentation.

Source: `/Users/david/repos/tads3/tads-sources/`
Output: `/Users/david/repos/tads3/docs/`
Plan: `/Users/david/.claude/plans/adaptive-wandering-book.md`

## Status: Phase 3 in progress

### Completed

**Phase 0: Infrastructure**
- mkdocs-material installed and configured (`docs/mkdocs.yml`)
- Full nav structure with 86+ placeholder pages
- Site builds and serves cleanly

**Phase 1: System Manual (88 pages converted, 0 errors)**
- Converter: `docs/scripts/convert_sysman.py`
- Shared utilities: `docs/scripts/convert_utils.py`
- Source: `tads-sources/t3doc/sysman/*.htm`
- Output: `docs/docs/language/`, `docs/docs/intrinsics/`, `docs/docs/tools/`
- All code blocks fenced as `tads3`, images copied, link paths fixed

**Phase 2: Technical Manual + VM Spec (51 pages converted, 0 errors)**
- Converter: `docs/scripts/convert_techman.py`
- Source: `tads-sources/t3doc/techman/*.htm`, `tads-sources/t3doc/techman/t3spec/*.htm`
- Output: `docs/docs/library/`, `docs/docs/vm-spec/`, `docs/docs/tools/`
- 15 VM spec docs (bytecode, machine model, image format, etc.)
- 36 techman articles (actions, verbs, conversations, NPCs, listers, etc.)

### Current State

- **159 Markdown pages** in docs tree
- **160 HTML pages** in built site (25MB)
- Build warnings are only cross-manual links to not-yet-converted sections (libref, tourguide, gsg)
- Link registry at `docs/scripts/link_registry.json`

### In Progress

**Phase 3: Tour Guide + Getting Started Guide (~372 pages)**
- Needs new converter for Help & Manual HTML format
- Key challenges: `<font>` tags, `&nbsp;`-encoded code blocks, table-based bullet lists using Symbol font `&#183;` characters
- Tourguide source: `tads-sources/t3doc/tourguide/*.htm` (324 pages)
- GSG source: `tads-sources/t3doc/gsg/*.htm` (48 pages)
- Representative pages studied: `basicdoor.htm`, `achievement.htm`

### Remaining Phases

| Phase | What | Est. Pages |
|-------|------|-----------|
| 3 | Tour Guide + GSG conversion | ~372 |
| 4 | API extraction from adv3 source | ~36 .t files → API pages |
| 5 | Libref integration + misc docs | ~1,700+ object pages |
| 6 | New architectural docs | 6 new documents |
| 7 | Syntax highlighting + polish | site-wide |

## Key Files

```
docs/
  mkdocs.yml                        # Site config with full nav
  docs/
    index.md                        # Landing page
    language/*.md                   # 37 pages (sysman Parts I, III, V-VII)
    intrinsics/functions/*.md       # 8 pages
    intrinsics/classes/*.md         # 27 pages
    library/*.md                    # 12 pages (techman articles)
    library/actors/*.md             # 4 pages
    library/actions/*.md            # 5 pages
    library/advanced/*.md           # 9 pages
    vm-spec/*.md                    # 15 pages
    tools/*.md                      # 9 pages
    getting-started/*.md            # 2 pages
    appendices/*.md                 # 4 pages
  scripts/
    convert_utils.py                # Shared conversion library (HTML→MD)
    convert_sysman.py               # System Manual converter
    convert_techman.py              # Technical Manual + VM Spec converter
    link_registry.json              # Old .htm → new .md path mappings
  context/
    progress.md                     # This file
```

## Conversion Architecture

The converter is split into shared utilities + per-section converters because the HTML varies significantly across the documentation:

- **sysman/techman**: Clean semantic HTML with `div.code`, `div.syntax`, `span.synLit/synPar/synMark` CSS classes. ~90% automatable.
- **tourguide/gsg**: Help & Manual generated HTML with `<font face="Courier New">` code blocks, `&nbsp;` space encoding, `<br>` newlines, table-based bullet lists. Hardest conversion.
- **libref**: Auto-generated, extremely regular structure (`table.ban`, `div.fdesc`, `div.mjhd`). Best suited for structural parsing.

## Notes

- The critique in `tads-sources/tads-3-claude-issues.txt` is from another TADS 3 developer about Claude's code generation quality with this codebase
- The repo at `tads-sources/` was cloned from https://github.com/tajmone/tads-sources.git (Tristano Ajmone's preservation project)
- TADS 3 source is copyright Michael J. Roberts, distributed as freeware
- Documentation authored by Michael J. Roberts and Eric Eve
