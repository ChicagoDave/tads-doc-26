# The Parser Pipeline

Every turn in a TADS 3 game begins with a string of text and ends with a fully resolved action applied to specific objects. The transformation from text to action is a multi-stage pipeline — tokenization, grammar matching, ranking, noun resolution, disambiguation, and execution — spread across four core source files. This document explains the architecture of that pipeline: the design choices, the class hierarchies, and the places where game authors can intervene.

[Pipeline Overview](#pipeline-overview) | [Entry Points](#entry-points-exect) | [Grammar Matching](#grammar-matching-parsert) | [Command Ranking](#command-ranking) | [Noun Resolution](#noun-resolution-resolvert) | [Disambiguation](#disambiguation-disambigt) | [Intervention Points](#practical-intervention-points)

!!! tip "How this document relates to the Command Execution Cycle"
    Eric Eve's [Command Execution Cycle](../library/advanced/command-execution-cycle.md) walks through what happens step by step, from the player's perspective. This document explains the same system from an architectural perspective — why the classes are shaped the way they are, what design patterns they use, and where you can hook in. Read the Execution Cycle first if you want to follow the flow; read this document when you need to understand or extend the machinery.

---

## Pipeline Overview

The parser pipeline is a sequence of data transformations. Each stage takes a specific input and produces a specific output:

```
Player Input  (string)
     │
     ▼
StringPreParser chain         string → string
     │
     ▼
Tokenizer                     string → token list
     │
     ▼
Grammar Matching              tokens → list of parse trees
     │
     ▼
Action Filtering               parse trees → valid parse trees
     │
     ▼
Command Ranking               parse trees → best interpretation
     │
     ▼
Noun Resolution               noun phrases → ResolveInfo lists
     │
     ▼
Global Remapping              action → possibly different action
     │
     ▼
Disambiguation                ambiguous objects → specific objects
     │
     ▼
Action Execution              resolved action → verify/check/action
```

The pipeline is not a single function call. It is orchestrated by two functions in `exec.t` that hand off to classes in `parser.t`, `resolver.t`, and `disambig.t`:

| Stage | Source | Key entry point |
|-------|--------|-----------------|
| Pre-parsing and tokenization | `input.t` | `readMainCommandTokens()` |
| Grammar matching | `parser.t` | `GrammarProd.parseTokens()` (VM intrinsic) |
| Action filtering | `parser.t` (called from `exec.t`) | `resolveFirstAction()` |
| Ranking | `parser.t` | `CommandRanking.sortByRanking()` |
| Noun resolution | `resolver.t` | `Resolver.matchName()`, `objInScope()` |
| Global remapping | `exec.t` | `GlobalRemapping.findGlobalRemapping()` |
| Disambiguation | `disambig.t` | `Distinguisher.canDistinguish()` |
| Action execution | `exec.t` | `executeAction()` → `action.doAction()` |

The stages before noun resolution deal with **syntactic ambiguity** — which grammar rule fits the input. The stages from noun resolution onward deal with **semantic ambiguity** — which objects the player means. This distinction drives the two-function architecture described next.

---

## Entry Points — exec.t

The pipeline has two entry points, and understanding why there are two is the key to understanding the control flow.

### executeCommand()

`executeCommand(targetActor, issuingActor, toks, firstInSentence)` is the top-level entry point, called once per player command. It receives a token list (already pre-parsed and tokenized by `input.t`) and handles everything up to noun resolution:

1. Calls `parseTokens(toks, cmdDict)` on the appropriate command phrase production (`firstCommandPhrase` for the first command in a sentence, `commandPhrase` for subsequent ones) to match grammar rules
2. Filters matches with `resolveFirstAction()` to discard structurally invalid interpretations
3. Calls `CommandRanking.sortByRanking()` to pick the best interpretation
4. Resolves actor prefixes ("BOB, GO NORTH") if present
5. Calls `executeAction()` with the winning match
6. Queues any leftover tokens (from multi-command input) for subsequent turns

### executeAction()

`executeAction(targetActor, targetActorPhrase, issuingActor, countsAsIssuerTurn, action)` takes a resolved Action and handles the semantic side:

1. Runs `GlobalRemapping` to intercept action-level transforms
2. Calls `action.resolveNouns()` for full noun resolution (catching `RemapActionSignal` for re-resolution)
3. Sets up undo savepoints
4. Checks `obeyCommand()` for NPC-directed commands
5. Calls `action.doAction()` to enter the verify/check/action cycle

### Why two functions?

The separation exists because not all commands enter through the parser. Implicit actions (automatically opening a door before walking through it), nested actions (`nestedAction()`), and programmatic commands (`replaceAction()`) all need to resolve nouns and execute an action, but they already know which action to perform — they do not need grammar matching or ranking. These callers bypass `executeCommand()` entirely and call `executeAction()` or `doAction()` directly.

### Control flow signals

The pipeline uses exception-based signaling for non-local control flow. These are not errors — they are deliberate control signals thrown from deep within the action system:

| Signal | Thrown from | Effect |
|--------|------------|--------|
| `ExitSignal` | Action handlers | Abort the current action's remaining execution; does not prevent processing of additional objects or commands on the same command line |
| `ExitActionSignal` | Action handlers | Abort the current action, skip to afterAction |
| `AbortImplicitSignal` | Implicit action system (when verify shows danger) | Cancel an implicit action silently |
| `RemapActionSignal` | Noun resolution | Restart resolution with a different action |
| `TerminateCommandException` | Parsing | Abandon the current command entirely |
| `RetryCommandTokensException` | Parsing | Re-parse with an edited token list |
| `ReplacementCommandStringException` | Parsing | Re-parse with an entirely new command string |

The last two signals are how the OOPS mechanism works: when the player types OOPS followed by a correction, the parser throws a `RetryCommandTokensException` with the corrected token list, and `executeCommand()` catches it and restarts the parse loop.

---

## Grammar Matching — parser.t

Grammar matching transforms a token list into a list of parse trees. This is where the parser figures out which verb the player typed and which tokens are noun phrases.

### The production hierarchy

Every grammar rule in TADS 3 is a class that extends `BasicProd`. The production hierarchy is both the grammar tree and the action tree — Actions *are* grammar productions:

```
BasicProd
├── CommandProd
│   ├── FirstCommandProd             first command in a sentence
│   ├── CommandProdWithActor         "bob, take ball"
│   └── CommandProdWithDefiniteConj  "take ball and drop it"
│
├── NounPhraseProd                  base for all noun matching
│   ├── SingleNounProd              "red ball"
│   │   └── TopicProd              topic phrases (ASK ABOUT)
│   ├── PluralProd                  "balls", "all red things"
│   └── PronounProd                 "it", "them", "him"
│       └── ReflexivePronounProd   "himself", "herself"
│
├── LiteralProd                     literal text capture
│
└── Action                          base for all actions
    ├── IAction                    no objects (JUMP, SLEEP)
    │   ├── LiteralAction: LiteralActionBase, IAction   (TYPE HELLO)
    │   ├── TopicAction: TopicActionBase, IAction       (THINK ABOUT X)
    │   └── ConvIAction            conversational (HELLO, YES)
    └── TAction: Action, Resolver  one object (TAKE X)
        ├── TIAction               two objects (PUT X IN Y)
        ├── LiteralTAction: LiteralActionBase, TAction  (TYPE X ON Y)
        └── TopicTAction: TopicActionBase, TAction      (ASK X ABOUT Y)
```

The critical insight: when you write a VerbRule, you are creating a grammar production class that *extends* the Action class. The colon in `VerbRule(Take) ... : TakeAction` creates a new class that inherits from `TakeAction`, which inherits from `TAction`, which inherits from `Action`, which inherits from `BasicProd`. This means each VerbRule is both a grammar rule (it knows how to match tokens) and an action (it knows what to do with the matched objects).

### VerbRules and the language module

VerbRules live in the language module (`en_us.t`), not in adv3 proper. Each VerbRule defines a token pattern using slot keywords that map to NounPhraseProd subclasses:

| Slot keyword | Maps to | Example |
|-------------|---------|---------|
| `singleDobj` | Single noun phrase | `TAKE BALL` |
| `dobjList` | Noun list (one or more) | `TAKE BALL AND KEY` |
| `singleIobj` | Single indirect object | `PUT BALL IN BOX` |
| `singleLiteral` | Literal text | `SAY HELLO` |
| `singleTopic` | Topic phrase | `ASK ABOUT WAR` |

The VM intrinsic `GrammarProd.parseTokens()` takes the token list and the game dictionary, and matches tokens against all registered grammar rules simultaneously. It returns a list of every parse tree that successfully matches. A single input like "PUT BALL IN BOX" might produce multiple matches — one for `VerbRule(PutIn)` and one for `VerbRule(PutInWhat)` with "BALL IN BOX" parsed as a single noun phrase.

### The badness mechanism

When a VerbRule is a fallback — it should only match if no better rule fits — you mark it with a `badness` value:

```tads3
VerbRule(PutInWhat)
    [badness 500] ('put' | 'place') dobjList
    : PutInAction
    verbPhrase = 'put/putting (what) (in what)'
;
```

This rule matches "PUT BALL" (missing the "IN X" part) and prompts for the indirect object. The `[badness 500]` ensures that when the player types "PUT BALL IN BOX", the parser prefers the full `VerbRule(PutIn)` over this fallback. The badness value feeds directly into the command ranking system described next.

For the practical syntax of defining VerbRules, see the [Grammar and Custom Verbs](quick-reference.md#grammar-and-custom-verbs) section of the quick reference.

---

## Command Ranking

The grammar matching stage can produce multiple valid parse trees for the same input. The ranking system chooses the best one. Its architecture is one of the most interesting parts of the parser.

### The ranking architecture

The key design decision: **ranking works by attempting a tentative noun resolution and collecting statistics about what goes wrong.** The ranker does not examine the grammar structure in isolation — it actually tries to resolve nouns for each interpretation, and whichever interpretation has fewer resolution problems wins.

This is implemented through a clever use of the `ResolveResults` interface. `CommandRanking` extends `ResolveResults`, which means a `CommandRanking` object can be passed to `resolveNouns()` as the error handler. Instead of displaying error messages, it silently counts problems:

```tads3
class CommandRanking: ResolveResults
    sortByRanking(lst, [resolveArguments])
    {
        local rankings = new Vector(lst.length());
        foreach (local cur in lst)
        {
            local curRank = self.createInstance(cur);
            curRank.calcRanking(resolveArguments);
            rankings.append(curRank);
        }
        return rankings.sort(SortDesc,
            {x, y: x.compareRanking(y)});
    }

    calcRanking(resolveArguments)
    {
        match.resolveNouns(resolveArguments..., self);
    }
;
```

The `resolveNouns()` call is *tentative* — it does not commit to any resolution or display anything to the player. It simply feeds problem counts back to the `CommandRanking` object through the `ResolveResults` callback interface.

### The two-pass comparison

Once every parse tree has been tentatively resolved and scored, `compareRanking()` runs a two-pass comparison:

- **Pass 1 (coarse)**: For each criterion in priority order, check presence vs. absence of the problem. The first criterion that discriminates wins.
- **Pass 2 (fine)**: If pass 1 found no difference, go through again comparing actual counts.

This two-pass design means that *having* a problem is always worse than *not having* it, regardless of how many problems the other interpretation has at lower-priority criteria. Only when both interpretations share the same profile of problem presence/absence does the count matter.

### The criterion list

The ranking criteria are checked in this priority order (most important first):

| Criterion | What it measures |
|-----------|-----------------|
| `rankByVocabNonMatch` | Words matching no vocabulary in the entire game |
| `rankByNonMatch` | Noun phrases matching no in-scope object |
| `rankByNonMatchPoss` | Possessive phrases matching no owner |
| `rankByInsufficient` | Not enough objects to satisfy a quantity |
| `rankByListForSingle` | Noun list used in a single-object slot |
| `rankByEmptyBut` | "All except" that excludes everything |
| `rankByAllExcluded` | ALL yields no objects after filtering |
| `rankByActorSpecified` | Actor clause present vs. absent |
| `rankByUnwantedPlural` | Plural used where singular expected |
| `rankByMiscWordList` | Unmatched miscellaneous words |
| `rankByWeakness` | Badness values from VerbRules |
| `rankByLiteralLength` | Shorter literals preferred |
| `rankByIndefinite` | Indefinite noun phrase vs. specific |
| `rankByPluralTrunc` | Plural truncation count |
| `rankByEndAdj` | Trailing adjective (possible noun) |
| `rankByTrunc` | Vocabulary truncation count |
| `rankByPronoun` | Pronoun vs. explicit noun |
| `rankByMissing` | Structurally omitted noun phrases |
| `rankBySubcommands` | Number of sub-commands consumed |
| `rankByTokenCount` | Total tokens consumed |
| `rankByVerbStructure` | Verb structure quality |
| `rankByAmbiguity` | Remaining ambiguity after filtering |

Game authors influence ranking through two primary mechanisms:

1. **`badness` values on VerbRules** — directly affect `rankByWeakness`
2. **`verify()` handlers on objects** — determine which objects survive the tentative resolution, affecting `rankByNonMatch`, `rankByAmbiguity`, and others

---

## Noun Resolution — resolver.t

Once a single parse tree has been selected, its noun phrases must be resolved to actual game objects. This is where the Resolver strategy pattern comes in.

### The Resolver hierarchy

An Action creates a Resolver for each noun phrase slot. The Resolver encapsulates scope and matching rules, so the same grammar production can be resolved differently depending on whether it fills the direct object, indirect object, or actor slot:

```
Resolver                         base class
├── IobjResolver                 indirect object (different scope methods)
├── TopicQualifierResolver       topic qualifier phrases (global scope)
├── ActorResolver                resolve target actor references
└── (Action itself)              many Actions serve as their own dobj resolver

ProxyResolver                    wraps another resolver, narrowing scope
├── PossessiveResolver           "bob's key" — adds known objects to scope
└── InteractiveResolver          base for interactive disambiguation
    └── DisambigResolver         "which one?" response resolution
```

The base `Resolver` class provides the interface that noun phrase productions call during resolution:

| Method | Purpose |
|--------|---------|
| `cacheScopeList()` | Build the list of in-scope objects (default: actor's sensory scope) |
| `objInScope(obj)` | Test whether a specific object is in scope |
| `getScopeList()` | Return the full scope list (used for ALL and defaults) |
| `matchName(obj, origTokens, adjustedTokens)` | Test whether an object matches the given tokens |
| `getAll(np)` | Return the object list for ALL |
| `filterAmbiguousNounPhrase(lst, requiredNum, np)` | Narrow ambiguous matches using verify results |
| `getDefaultObject(np)` | Supply a default when a noun phrase is omitted |
| `resolvePronounAntecedent(typ, np, results, poss)` | Resolve IT, HIM, HER, THEM |
| `getReflexiveBinding(typ)` | Resolve HIMSELF, HERSELF, ITSELF |

### The resolution process

When a noun phrase like "red ball" is resolved, the following steps occur:

1. **Vocabulary matching** — Every object in scope whose `matchName()` returns true for the tokens enters the candidate list. The dictionary built at compile time maps words to objects, so this is fast.

2. **Facet deduplication** — Objects sharing `getFacets()` (representing the same physical object, like two sides of a door) are reduced to one representative.

3. **filterResolveList()** — Each candidate gets a chance to adjust the list. An object can remove itself, substitute another object, or add objects. This is how remapping works at the object level.

4. **Verification pass** — The action's `verify()` handler runs on each candidate, producing a `VerifyResultList`. Objects with lower logical ranks (illogical, illogicalNow) are discarded in favor of objects with higher ranks. This is the single most important mechanism for disambiguation — the parser picks the object that makes the most sense.

5. **Equivalent reduction** — If multiple candidates have `isEquivalent` set and share the same `equivalenceKey`, they are collapsed to a single representative. Five identical gold coins become one.

6. **Count check** — If the player said "five coins", the resolver verifies that enough candidates survived.

### ResolveInfo

The result of noun resolution is a list of `ResolveInfo` objects, each carrying:

| Property | Type | Meaning |
|----------|------|---------|
| `obj_` | Object | The resolved game object |
| `flags_` | Integer | How matched: `VocabTruncated`, `PluralTruncated`, etc. |
| `np_` | NounPhraseProd | The grammar production that produced this match |
| `possRank_` | Integer | Possessive qualification strength (0, 1, or 2) |
| `pronounType_` | Enum | If matched via pronoun, which pronoun type |

### Pronoun resolution

Pronouns are resolved through the `resolvePronounAntecedent()` method. The resolver checks for a prior noun phrase binding (the antecedent), filters the antecedent list against the current scope, and handles facet switching — if the player referred to a door and then walked through it, the pronoun IT should now refer to the side of the door in the new room, not the side in the old room.

Reflexive pronouns (HIMSELF, HERSELF) use a different binding: `getReflexiveBinding()` returns the anaphoric binding from within the same action, so "ASK BOB ABOUT HIMSELF" correctly binds "himself" to "Bob".

---

## Disambiguation — disambig.t

When noun resolution produces multiple candidates that survive all filtering, and the parser cannot automatically choose, it must ask the player "Which do you mean?" This requires two capabilities: describing the difference between candidates, and parsing the response.

### The Distinguisher hierarchy

Each game object has a `distinguishers` list — a sequence of `Distinguisher` singleton instances that describe how to tell it apart from other objects. The parser walks through the distinguishers to find one that can differentiate the ambiguous candidates:

```
Distinguisher                    base class (defined in disambig.t)
    nullDistinguisher            different display names
    basicDistinguisher           different equivalence classes
    ownershipDistinguisher       different getNominalOwner() or location
    locationDistinguisher        different immediate location
    litUnlitDistinguisher        different isLit state
```

These are singleton instances (note the lowercase names), not subclasses. Each instance implements three methods:

- `canDistinguish(a, b)` — Can this distinguisher tell objects `a` and `b` apart?
- `matchName(obj, origTokens, adjustedTokens, matchList, fullMatchList)` — Can the player's disambiguation response be matched using this distinguisher's knowledge?
- `objInScope(obj, matchList, fullMatchList)` — What counts as "in scope" for disambiguation responses?

The `objInScope()` method is subtle. The ownership distinguisher puts *owners* in scope, so when the parser asks "Which key do you mean, Bob's key or the key on the table?", the player can respond with just "Bob's" — the owner is in scope for the disambiguation response even though it is not the object being disambiguated.

### The disambiguation loop

When disambiguation is needed, the flow is:

1. The parser finds a `Distinguisher` that can tell the ambiguous objects apart
2. It generates a "Which do you mean?" prompt using distinguishing descriptions
3. The player responds
4. The response is parsed using a `DisambigResolver`, which narrows scope to just the ambiguous candidates
5. `DisambigRanking` (a subclass of `CommandRanking` with an extra `rankByDisambigOrdinals` criterion) scores the response
6. If still ambiguous, the loop repeats; if the response matches nothing, an error is displayed

This loop is *iterative*, not recursive — a deliberate design choice to prevent stack overflow if a player repeatedly gives ambiguous answers.

The disambiguation system defines three specific exceptions:

| Exception | When thrown |
|-----------|-----------|
| `StillAmbiguousException` | Response doesn't narrow to a single object |
| `UnmatchedDisambigException` | Response doesn't match any candidate |
| `DisambigOrdinalOutOfRangeException` | "The third one" when there are only two |

---

## Practical Intervention Points

The pipeline provides hooks at every stage. Here is a consolidated reference of the places where game authors can intervene, organized by what you want to accomplish.

### Before parsing

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `StringPreParser` | Subclass, override `doParsing(str, which)` | Transform input before tokenization — strip punctuation, expand abbreviations, intercept special commands |
| `PromptDaemon` | Create with `new PromptDaemon()` | Display messages just before the command prompt appears |

A `StringPreParser` can transform the input string, pass it through unchanged, or consume it entirely (returning `nil` to indicate the command has been fully handled):

```tads3
stripQuestionMark: StringPreParser
    doParsing(str, which)
    {
        return str.findReplace('?', '', ReplaceAll);
    }
;
```

### During grammar matching

| Hook | Mechanism | Use case |
|------|-----------|----------|
| New VerbRules | `VerbRule(Name) ... : ActionClass` | Add entirely new verbs |
| `modify grammar` | Extend existing grammar rules | Add synonyms to existing verbs |
| `replace grammar` | Replace grammar rules entirely | Change how existing verbs parse |
| VerbRule `badness` | `[badness N]` in grammar rule | Deprioritize fallback patterns |

See [Grammar and Custom Verbs](quick-reference.md#grammar-and-custom-verbs) in the quick reference for the syntax, and [Creating New Verbs](../library/actions/creating-verbs.md) for the full walkthrough.

### During noun resolution

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `verify()` handlers | `dobjFor(X) { verify() { ... } }` | Control which objects the parser prefers — the primary disambiguation tool |
| `matchName()` | Override on Thing | Customize which words match an object |
| `matchNameCommon()` | Override on Thing | Customize matching at a lower level |
| `filterResolveList()` | Override on Thing | Remove, substitute, or add objects during resolution |
| `vocabLikelihood` | Property on Thing | Bias disambiguation without changing verify logic |
| `isEquivalent` | Property on Thing | Treat interchangeable objects as one (five gold coins) |
| `objInScope()` | Override on Resolver (TAction serves as its own dobj Resolver) | Expand or restrict what the parser considers reachable |

### During and after action selection

| Hook | Mechanism | Use case |
|------|-----------|----------|
| `GlobalRemapping` | Subclass, override `getRemapping()` | Transform one action into another globally (e.g., GIVE ME X → ASK FOR X) |
| `remapTo()` | In dobjFor/iobjFor blocks | Redirect on a per-object basis |
| `asDobjFor()` / `asIobjFor()` | In dobjFor/iobjFor blocks | Reuse another action's handlers for a specific object |

`GlobalRemapping` operates before nouns are fully resolved — it intercepts at the *action* level. This is its distinguishing feature compared to `remapTo`, which requires knowing the resolved objects. See [Design Patterns](design-patterns.md) for the `remapTo` and `asDobjFor` patterns.

---

*Back to the [Architecture Overview](overview.md) for the big picture, or see [The Command Execution Cycle](../library/advanced/command-execution-cycle.md) for the step-by-step procedural walkthrough. For the action execution phases that follow parsing, see [Action Resolution](action-resolution.md) and [Design Patterns](design-patterns.md).*
