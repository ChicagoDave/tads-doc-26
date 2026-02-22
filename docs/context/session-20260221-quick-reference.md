# Session Summary: 2026-02-21 - Quick Reference Cheat Sheet

## Status: Completed

## Goals
- Create a dense, scannable quick-reference cheat sheet for active TADS 3/adv3 development
- Complement the existing architecture documents (overview, development-guide, design-patterns) with a fast-lookup resource rather than conceptual explanation
- Wire the new page into site navigation and the architecture index

## Completed

### Quick Reference Cheat Sheet (`docs/docs/architecture/quick-reference.md`)
Approximately 480 lines across 12 sections and 17 tables. Every section links back to the relevant detailed pages (overview.md, development-guide.md, design-patterns.md, Tour Guide pages).

**Section breakdown:**

1. **Game Skeleton** — Minimal compilable 4-object game template showing the essential include, gameMain, startRoom, and actor object structure.

2. **Thing Hierarchy** — Six tables covering:
   - Portability classes: Thing / Fixture / Decoration / Distant / Immovable / Heavy
   - Containers and surfaces
   - Interaction types: Readable / Food / Wearable / Switch / etc.
   - Light sources
   - Nested rooms
   - Mix-in classes

3. **Rooms and Travel** — Room types, direction properties, travel connectors (Door / FakeConnector / StairwayUp / etc.), the door pattern, and regions.

4. **Action Handlers** — The four phases (verify / check / action / report), verify macros table (illogical / logicalRank / dangerous / etc.), report functions, redirecting actions, preconditions, and a common actions table covering 30 actions with dobj/iobj roles.

5. **Key Properties** — Tables for Thing (16 properties), Room (12 properties), and Actor (6 properties), each showing type, purpose, and default value.

6. **Object Templates** — Thing, Room, TopicEntry, and Passage template syntax with slot explanations. Includes a tip admonition clarifying single-quote vs double-quote vs `@` vs `->` syntax.

7. **String Syntax** — Single vs double quotes, escape sequences table, embedded expressions, conditional text, and library message tags.

8. **Conversations** — TopicEntry types table (12 types), default topics, the actor state pattern with a full code example, and an agenda items table.

9. **Timed Events** — Creation syntax for Fuse / Daemon / SenseFuse / PromptDaemon, a cleanup pattern example, and a tip admonition about orphaned daemons.

10. **Debugging** — Debug commands table, build commands, common compiler errors table, and conditional compilation syntax.

11. **Modify and Replace** — Side-by-side treatment of `modify`, `replace`, and subclassing with examples and guidance on when to use each.

12. **Scoring** — Simple scoring, achievement objects, and `finishGameMsg`.

**Style choices:**
- Tables over prose throughout (17 tables total)
- Code snippets capped at 5 lines each for scannability
- Navigation bar at the top of the page linking all 12 sections
- Two tip admonitions (template syntax disambiguation; daemon cleanup reminder)

### Architecture Index Update (`docs/docs/architecture/index.md`)
Added Quick Reference card with short description to the existing grid of architecture documents.

### Site Navigation Update (`docs/mkdocs.yml`)
Added nav entry for `architecture/quick-reference.md` under the Architecture section, consistent with the existing entries for overview, development-guide, and design-patterns.

### Build Verification
`mkdocs build` passes with zero new warnings. All internal cross-reference links resolve correctly.

## Key Decisions

### 1. Tables Over Prose
The cheat sheet is intentionally table-heavy. The three existing architecture docs already provide conceptual explanation and narrative; this document's sole job is to surface the right syntax or class name in under 10 seconds of scanning.

### 2. Strict Line Budget Per Snippet
Code examples are capped at 5 lines. Longer patterns belong in development-guide.md or design-patterns.md; the cheat sheet links there rather than reproducing them.

### 3. Section Anchor Navigation Bar
A nav bar at the top of the page links all 12 sections so users can jump directly without scrolling, keeping the document usable even at its full 480-line length.

### 4. Tip Admonitions for Gotchas
Two mkdocs-material `tip` admonitions call out the two most common points of confusion: template slot syntax (single vs double quotes, `@`, `->`) and daemon lifecycle cleanup. These are short "don't get burned" notes that would interrupt the flow of a narrative doc but are appropriate in a reference.

## Open Items

### Short Term
- Consider adding a **Grammar and Parser** section covering custom VerbRule / Grammar definitions — currently absent from the cheat sheet
- Possibly add a one-liner table of the most common `gPlayerChar` / `gActor` / `gDobj` / `gIobj` global shorthand macros

### Long Term
- As Phase 3 (Tour Guide + GSG) conversion progresses, verify that all Tour Guide cross-reference links in the cheat sheet resolve to the correct anchors once those pages are fully converted
- A printable single-page PDF variant could be useful; mkdocs-material has a print stylesheet that may handle this automatically

## Files Modified

**New** (1 file):
- `/Users/david/repos/tads3/docs/docs/architecture/quick-reference.md` — 480-line quick-reference cheat sheet, 12 sections, 17 tables

**Modified** (2 files):
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — added Quick Reference card to architecture index grid
- `/Users/david/repos/tads3/docs/mkdocs.yml` — added nav entry under Architecture section

## Architectural Notes

This document sits at the intersection of Phases 6 and 7 (architecture docs + usability). It does not convert any HTML source material; it is entirely new content synthesized from the adv3 library and the existing architecture docs. Future sessions adding new architecture pages should follow the same pattern: dense tables, short snippets, links out to narrative docs, section nav bar at the top.

The 17-table structure means the page is wide. Verify rendering on narrow viewports if the site ever targets mobile readers.

## Notes

**Session duration**: ~1 hour

**Approach**: Content drafted from adv3 library knowledge and cross-referenced against the three existing architecture documents to avoid duplication and ensure link targets exist. Build verified before closing.

---

**Progressive update**: Session completed 2026-02-21 04:30
