#!/usr/bin/env python3
"""
Tag untagged fenced code blocks in TADS 3 documentation markdown files.

Scans all .md files under docs/docs/, identifies untagged code blocks that
contain TADS 3 source code, and adds the `tads3` language tag. Blocks that
contain prose, game transcripts, or other non-code content are left alone.

Usage:
    python3 tag_code_blocks.py           # dry run (report only)
    python3 tag_code_blocks.py --apply   # apply changes
    python3 tag_code_blocks.py --verbose # show block content in dry run
"""

import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"

# --- Heuristics ---

# Patterns that strongly indicate TADS 3 code, with weights.
# Each pattern is tested per-line; first match per pattern counts.
CODE_SIGNALS = [
    # Preprocessor
    (r'^\s*#include\s', 3),
    (r'^\s*#define\s', 2),
    (r'^\s*#ifn?def\s', 2),
    (r'^\s*#endif', 1),
    (r'^\s*#charset\s', 2),

    # TADS 3 object/class definitions
    (r'^\s*\w+\s*:\s*(Thing|Room|Actor|object|Fixture|Decoration|Distant|'
     r'Container|Surface|TopicEntry|Passage|Door|Lockable|Key|Wearable|'
     r'Food|Readable|BasicOpenable|Openable|LockableContainer|OpenableContainer|'
     r'KeyedContainer|RestrictedContainer|RestrictedHolder|'
     r'Consultable|Switch|Lever|Settable|Dial|Button|'
     r'OutdoorRoom|DarkRoom|FloorlessRoom|'
     r'StairwayUp|StairwayDown|ThroughPassage|SecretDoor|HiddenDoor|'
     r'Enterable|Exitable|'
     r'Achievement|SimpleAttachable|'
     r'GameID|GameMainDef|'
     r'TopicGroup|AltTopic|DefaultTopic|'
     r'AskTopic|TellTopic|AskTellTopic|GiveTopic|ShowTopic|'
     r'AskForTopic|InitiateTopic|CommandTopic|'
     r'DefaultAskTopic|DefaultTellTopic|DefaultAskTellTopic|'
     r'DefaultGiveTopic|DefaultShowTopic|'
     r'SpecialTopic|YesTopic|NoTopic|'
     r'InConversationState|ConversationReadyState|ActorState|HermitActorState|'
     r'AgendaItem|ConvAgendaItem|DelayedAgendaItem|'
     r'Fuse|SenseFuse|Daemon|SenseDaemon|PromptDaemon|'
     r'Noise|Odor|SensoryEmanation|'
     r'Vaporous|Hidden|Component|'
     r'MultiLoc|MultiInstance|MultiFaceted|'
     r'Unthing|Collective|'
     r'Region|SenseRegion|'
     r'Precondition|PreCondition|'
     r'PreinitObject|InitObject|'
     r'InputDef|BannerWindow|'
     r'ListGroupCustom|ItemizingCollectiveGroup|'
     r'Mentionable|Matchable|VocabObject|LMentionable|'
     r'TravelConnector|OneWayRoomConnector|RoomConnector|'
     r'Immovable|Heavy|TravelPushable|'
     r'NominalPlatform|BasicPlatform|BasicChair|Chair|Platform|Bed|'
     r'NestedRoom|BasicLocation|Vehicle|'
     r'Flashlight|Candle|FueledLightSource|'
     r'Matchstick|Matchbook|'
     r'ThingState|'
     r'CustomVocab|StringPreParser|'
     r'EventList|ShuffledEventList|CyclicEventList|SyncEventList|'
     r'RandomEventList|StopEventList|ShuffledList|'
     r'StyleTag|'
     r'Tip|TipManager'
     # TADS 2 class names (also appear in docs)
     r'|room|item|thing|actor|deepverb|senseVerb|darkroom)\b', 3),

    # TADS 3 object nesting with + prefix
    (r'^\s*\+{1,4}\s+\w+\s*:', 3),
    (r'^\s*\+{1,4}\s+\w+', 2),

    # modify / replace statements
    (r'^\s*modify\s+\w+', 3),
    (r'^\s*replace\s+\w+', 3),

    # Action handler macros
    (r'dobjFor\s*\(', 3),
    (r'iobjFor\s*\(', 3),
    (r'remapTo\s*\(', 2),
    (r'asDobjFor\s*\(', 2),
    (r'asIobjFor\s*\(', 2),

    # TADS 3 keywords in code context
    (r'inherited\s*\(', 2),
    (r'\blocal\s+\w+\s*[=;,]', 2),
    (r'\bfunction\s+\w+\s*\(', 2),
    (r'\bfunction\s*\([^)]*\)\s*\{', 2),
    (r'failCheck\s*\(', 2),
    (r'reportFailure\s*\(', 2),
    (r'gMessageParams\s*\(', 2),
    (r'gAction\b', 1),
    (r'gDobj\b', 1),
    (r'gIobj\b', 1),
    (r'gActor\b', 1),

    # Control flow keywords (with parens/braces — code context)
    (r'\breturn\b\s+', 1),
    (r'\bif\s*\([^)]+\)', 1),
    (r'\bfor\s*\(', 1),
    (r'\bwhile\s*\(', 1),
    (r'\bswitch\s*\(', 1),
    (r'\bforeach\s*\(', 1),

    # Lines ending with semicolons (code, not prose)
    (r'\w\s*;\s*$', 1),

    # Standalone semicolons (end of object definition)
    (r'^\s*;\s*$', 2),

    # Property definitions: name = 'string' or name = "string"
    (r'^\s{2,}\w+\s*=\s*[\'"]', 1),

    # Braces on their own lines (code formatting)
    (r'^\s*[\{}]\s*$', 1),

    # Embedded expressions in strings <<...>>
    (r'<<[a-zA-Z]', 1),

    # Single-line comments
    (r'^\s*//', 1),

    # Block comments
    (r'^\s*/\*', 1),

    # TADS 3 specific: template syntax with quoted vocab
    (r"^\s*'\w[\w\s/]*'\s*$", 1),

    # Method/property calls common in TADS 3
    (r'\.(desc|name|isIn|isDirectlyIn|moveInto|actionMoveInto)\b', 1),
    (r'\b(addToScore|achievement|finishGameMsg)\b', 1),
    (r'\bsay\s*\(', 1),

    # TADS 3 library globals and macros
    (r'\bgMessageParams\b', 1),
    (r'\b(gTopic|gLiteral|gVerifyList)\b', 1),

    # TADS 3 intrinsic keyword
    (r'\bintrinsic\s+[\'"]', 2),

    # TADS 2 function syntax: name: function
    (r'^\s*\w+\s*:\s*function\b', 2),
]

# Words that indicate English prose rather than code
PROSE_INDICATORS = [
    'the ', 'a ', 'an ', 'this ', 'that ', 'these ', 'those ',
    'which ', 'where ', 'when ', 'because ', 'since ', 'however ',
    'also ', 'just ', 'would ', 'could ', 'should ', 'might ',
    'must ', 'cannot ', "doesn't", "isn't", "won't", "can't",
    'we ', 'you ', 'they ', 'note that', 'for example',
    'in other words', 'in this case', 'on the other hand',
]


def score_block(block_text):
    """Score a code block for TADS 3 likelihood. Returns (score, details)."""
    lines = block_text.strip().split('\n')
    if not lines:
        return 0, 'empty'

    non_empty = [l for l in lines if l.strip()]
    if not non_empty:
        return 0, 'empty'

    # Compute prose indicators
    avg_len = sum(len(l) for l in non_empty) / len(non_empty)
    prose_line_count = 0
    for l in non_empty:
        lower = l.lower().strip()
        if any(w in lower for w in PROSE_INDICATORS):
            prose_line_count += 1
    prose_ratio = prose_line_count / len(non_empty)

    # If it's clearly prose (long lines, many English words), reject
    if prose_ratio > 0.4 and avg_len > 55:
        return -1, 'prose'

    # Check for game transcript (lines starting with >)
    transcript_lines = sum(1 for l in non_empty if l.strip().startswith('>'))
    if transcript_lines > 0 and transcript_lines >= len(non_empty) * 0.2:
        return -2, 'transcript'

    # Score code signals
    total_score = 0
    matched = []
    for pattern, weight in CODE_SIGNALS:
        for line in lines:
            if re.search(pattern, line):
                total_score += weight
                matched.append(pattern[:30])
                break

    return total_score, matched


def classify_block(block_text):
    """Classify a block as 'tads3', 'skip', or 'review'."""
    score, details = score_block(block_text)

    if score < 0:
        return 'skip', score, details

    lines = block_text.strip().split('\n')
    non_empty = [l for l in lines if l.strip()]
    if not non_empty:
        return 'skip', 0, 'empty'

    avg_len = sum(len(l) for l in non_empty) / len(non_empty)

    # High confidence: score >= 4
    if score >= 4:
        return 'tads3', score, details

    # Medium confidence: score >= 3 with reasonable line lengths
    if score >= 3 and avg_len < 70:
        return 'tads3', score, details

    # Lower confidence: score >= 2, short lines, low prose
    prose_line_count = 0
    for l in non_empty:
        lower = l.lower().strip()
        if any(w in lower for w in PROSE_INDICATORS):
            prose_line_count += 1
    prose_ratio = prose_line_count / len(non_empty)

    if score >= 2 and avg_len < 55 and prose_ratio < 0.25:
        return 'tads3', score, details

    return 'skip', score, details


def find_code_blocks(content):
    """Parse markdown content and find all fenced code blocks.

    Returns list of (line_number, lang, body) where line_number is 0-indexed
    line of the opening fence.
    """
    lines = content.split('\n')
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith('```'):
            # Opening fence
            fence_indent = len(line) - len(stripped)
            backticks = len(stripped) - len(stripped.lstrip('`'))
            lang = stripped[backticks:].strip()
            open_line = i
            # Collect body until closing fence
            body_lines = []
            i += 1
            while i < len(lines):
                cl = lines[i]
                cl_stripped = cl.strip()
                if cl_stripped.startswith('`' * backticks) and \
                   cl_stripped == '`' * backticks:
                    # Closing fence
                    break
                body_lines.append(lines[i])
                i += 1
            body = '\n'.join(body_lines)
            blocks.append((open_line, lang, body))
        i += 1
    return blocks


def process_file(filepath, apply=False, verbose=False):
    """Process a single markdown file. Returns (tagged_count, skipped_count)."""
    content = filepath.read_text(encoding='utf-8')
    lines = content.split('\n')

    tagged = 0
    skipped = 0
    tag_lines = []  # line numbers where we need to add 'tads3'

    for open_line, lang, body in find_code_blocks(content):
        if lang:
            continue  # already tagged

        classification, score, details = classify_block(body)

        if classification == 'tads3':
            tagged += 1
            tag_lines.append(open_line)
            if verbose:
                preview = body.strip()[:80].replace('\n', '\\n')
                print(f"  TAG  score={score:2d}  {preview}")
        else:
            skipped += 1
            if verbose and score > 0:
                preview = body.strip()[:80].replace('\n', '\\n')
                print(f"  SKIP score={score:2d}  {preview}")

    if apply and tag_lines:
        for line_num in tag_lines:
            old_line = lines[line_num]
            # Replace ``` with ```tads3 preserving indentation
            idx = old_line.index('```')
            lines[line_num] = old_line[:idx] + '```tads3' + old_line[idx + 3:]
        filepath.write_text('\n'.join(lines), encoding='utf-8')

    return tagged, skipped


def main():
    apply = '--apply' in sys.argv
    verbose = '--verbose' in sys.argv

    if apply:
        print("APPLYING changes to markdown files...\n")
    else:
        print("DRY RUN — no files will be modified. Use --apply to commit changes.\n")

    total_tagged = 0
    total_skipped = 0
    files_modified = 0
    file_details = []

    md_files = sorted(DOCS_DIR.rglob('*.md'))
    for filepath in md_files:
        tagged, skipped = process_file(filepath, apply=apply, verbose=verbose)
        if tagged > 0:
            files_modified += 1
            rel = filepath.relative_to(DOCS_DIR)
            file_details.append((str(rel), tagged))
            if not verbose:
                print(f"  {tagged:3d} blocks tagged in {rel}")
        total_tagged += tagged
        total_skipped += skipped

    print(f"\n{'=' * 60}")
    print(f"  Blocks tagged as tads3:  {total_tagged}")
    print(f"  Blocks skipped:          {total_skipped}")
    print(f"  Files {'modified' if apply else 'to modify'}:        {files_modified}")
    print(f"{'=' * 60}")

    if not apply and total_tagged > 0:
        print(f"\nRun with --apply to commit these changes.")


if __name__ == '__main__':
    main()
