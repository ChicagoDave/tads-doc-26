# Session Summary: 2026-02-21 - message-system-architecture

## Status: Completed

## Goals
- Create the fifth of six planned deep-dive architecture documents: The Message System
- Integrate it into site navigation and cross-reference it from related documents
- Verify the build completes with no new warnings

## Completed

### New Document: message-system.md

Created `/Users/david/repos/tads3/docs/docs/architecture/message-system.md`, a comprehensive 9-section deep-dive following the template established by the four preceding deep-dives (parser-pipeline, action-resolution, sense-perception, containment-model).

**Section breakdown:**

1. **Message System Overview** — ASCII 3-layer diagram (Definition → Substitution → Dispatch). Source-file-to-role mapping table covering msg_neu.t, output.t, en_us.t, report.t, exec.t, action.t, adv3.h.

2. **The Message Lifecycle** — Complete end-to-end trace of a message from action handler to player display. Two worked examples: simple "Taken." for player, and full parameterized NPC message with substitution. Sets up the mental model before the deep sections.

3. **Message Definition Objects** — Class hierarchy (MessageHelper → libMessages, playerActionMessages → npcActionMessages). ASCII class tree. String vs method message properties. Actor selection via getActionMessageObj(). Coverage of approximately 600 message properties.

4. **The Parameter Substitution Engine** — MessageBuilder (output.t:1070) and langMessageBuilder (en_us.t:3758). The paramList_ five-element structure. ASCII algorithm diagram of generateMessage(). Target object resolution chain. Capitalization handling.

5. **The English Language Layer** — Comprehensive parameter reference tables organized by category: pronouns/articles (14 types), verb conjugation (17+ parameters with present/past forms), spatial prepositions. Reflexive pronoun tracking (lastSubject_/lastSubjectName_, sentence boundary reset). Tense switching ({present|past} syntax, square-bracket-to-brace conversion, tSel(), the ! suffix). The invisible {subj} marker.

6. **Message Dispatch and Override Resolution** — The resolveMessageText() algorithm from exec.t as ASCII decision flow. Stack trace inspection for priority ordering. TypeSString/TypeProp/TypeCode/TypeNil handling. Role-selective overrides (dobjMsg/iobjMsg). Custom named parameters (setMessageParam, gMessageParams, gSynthMessageParam).

7. **The Report and Transcript System** — CommandReport class hierarchy (ASCII tree with 15+ classes). Report macro comparison table (8 macros). Suppression rules: default reports suppressed by full reports, and by implicit actions. Deferred display via CommandTranscript.

8. **Author Customization Patterns** — Six cookbook-style patterns with TADS 3 code examples: per-object override, class-level override, custom parameters, actor-specific message objects, conditional method overrides, past tense narration.

9. **Practical Intervention Points** — Five lookup tables: defining/overriding messages, parameter substitution, report control, tense and person, custom message objects.

### Navigation and Cross-Reference Integration

Updated five existing files to incorporate the new document:

- `docs/mkdocs.yml` — Added nav entry for Message System after Containment Model
- `docs/docs/architecture/index.md` — Added Message System entry with description between Containment Model and IF Development Guide
- `docs/docs/architecture/overview.md` — Added cross-reference to message-system.md after the Output and Display module table
- `docs/docs/architecture/containment-model.md` — Updated footer: replaced development-guide.md link with message-system.md link
- `docs/docs/architecture/action-resolution.md` — Added forward link to message-system.md in footer

### Build Verification

Fixed one anchor mismatch: a tip admonition referenced `#the-executionreporting-phase` which does not exist in action-resolution.md. Corrected to `#the-execution-cycle-doactiononce`. Build completed with zero new warnings.

## Key Decisions

### 1. Top-Down Lifecycle-First Structure
Unlike the containment model (which uses bottom-up layers), the message system is presented top-down — starting with a complete lifecycle trace that the reader can follow, then drilling into each layer. This matches how authors encounter the system: they see a message appear and want to understand how it got there.

### 2. English Layer Unified in One Section
The English language layer handles pronouns, articles, verb conjugation, and tense in a single processing pass via langMessageBuilder. These are presented together rather than split into separate sections to reflect the actual implementation boundary.

### 3. Report System Separated from Dispatch
Message dispatch (which message string to use?) and reporting (when and whether to show it?) are distinct mechanisms. Documenting them in separate sections prevents the common author confusion between "why is my message wrong?" and "why isn't my message appearing?"

### 4. Worked Examples as Entry Point
Section 2 traces two concrete examples end-to-end before any deep section begins. This gives the reader a complete mental model to anchor the detailed sections that follow — especially important for a system with three interacting layers.

## Open Items

### Short Term
- Event Scheduling deep-dive (6 of 6): Schedulable, Daemon, Fuse, turn ordering
  - Source files: events.t, schedule.t, adv3.h

### Long Term
- Once all six deep-dives are complete, review architecture/index.md for coherence as a reading guide
- Consider a cross-cutting "how the systems interact" summary document tying all six together

## Files Modified

**New** (1 file):
- `/Users/david/repos/tads3/docs/docs/architecture/message-system.md` — Full 9-section deep-dive on the TADS 3 message system

**Updated** (5 files):
- `/Users/david/repos/tads3/docs/mkdocs.yml` — Added Message System nav entry
- `/Users/david/repos/tads3/docs/docs/architecture/index.md` — Added entry in deep-dive listing
- `/Users/david/repos/tads3/docs/docs/architecture/overview.md` — Added cross-reference after Output and Display table
- `/Users/david/repos/tads3/docs/docs/architecture/containment-model.md` — Updated footer link from development-guide.md to message-system.md
- `/Users/david/repos/tads3/docs/docs/architecture/action-resolution.md` — Added forward link to message-system.md in footer

## Architectural Notes

The message system is architecturally distinctive as a three-layer design with a clean separation of concerns:

- **Layer 1 (Definition)** is pure data — string properties on singleton objects (libMessages, playerActionMessages, npcActionMessages). No logic, no dependencies.
- **Layer 2 (Substitution)** is a language-independent framework (MessageBuilder in output.t) specialized by the English module (langMessageBuilder in en_us.t). This is where parameter tokens like {the dobj} are resolved to text.
- **Layer 3 (Dispatch)** is where the message system connects to the action system — resolveMessageText() in exec.t is the bridge between "what the action wants to say" and "how it gets said." It inspects the call stack to determine which message object and which override to use.

The report/transcript system adds a fourth orthogonal concern: deferred display with suppression rules. This operates independently of message content. This architecture is why TADS 3 can cleanly handle implicit actions — the "Taken." from an implicit take is suppressed at the transcript level without any special casing in the message definition or substitution layers.

Source files referenced throughout: msg_neu.t, output.t, en_us.t, report.t, exec.t, action.t, adv3.h.

## Notes

**Session duration**: ~1.5 hours

**Approach**: Followed the established deep-dive template (overview → lifecycle → internals → customization → lookup tables). Prioritized author-facing concerns: the worked examples in Section 2 and the cookbook patterns in Section 8 are the most practically useful parts.

**Architecture doc count**: 5 of 6 planned deep-dives complete. 1 remaining (event-scheduling).

---

**Progressive update**: Session completed 2026-02-21 19:20
