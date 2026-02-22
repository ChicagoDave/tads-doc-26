# commentPreParser

*object* — defined in [input.t](../by-file/input.t.md) (line 958)


The "comment" pre-parser. If the command line starts with a special prefix string (by default, "*", but this can be changed via our commentPrefix property), this pre-parser intercepts the command, treating it as a comment from the player and otherwise ignoring the entire input line. The main purpose is to give players a way to put comments into recorded transcripts, as notes to themselves when later reviewing the transcripts or as notes to the author when submitting play-testing feedback.


**Superclass chain:** [StringPreParser](stringpreparser.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **commentPreParser**


## Properties


### `commentPrefix`

Defined in input.t, line 1005

The comment prefix. You can change this to any character, or to any sequence of characters (longer sequences, such as '//', will work fine). If a command line starts with this exact string (or starts with whitespace followed by this string), we'll consider the line to be a comment.


### `leadPat`

Defined in input.t, line 1017

The leading-whitespace pattern. We skip any text that matches this pattern at the start of a command line before looking for the comment prefix.


### `runOrder` *(overridden)*

Defined in input.t, line 1034

Use a lower execution order than the default, so that we run before most other pre-parsers. Most other pre-parsers are written to handle actual commands, so it's usually just a waste of time to have them look at comments at all - and can occasionally be problematic, since the free-form text of a comment could confuse a pre-parser that's expecting a more conventional command format. When the comment pre-parser detects a comment, it halts any further processing of the command - so by running ahead of other pre-parsers, we'll effectively bypass other pre-parsers when we detect a comment.


### `warningCount`

Defined in input.t, line 1020

warning count for entering comments without SCRIPT in effect


## Inherited Properties


*From [StringPreParser](stringpreparser.md):* [`regList`](stringpreparser.md#regList), [`regListSorted`](stringpreparser.md#regListSorted)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `doParsing(str, which)` *(overridden)*

Defined in input.t, line 959


## Inherited Methods


*From [StringPreParser](stringpreparser.md):* [`construct`](stringpreparser.md#construct), [`execute`](stringpreparser.md#execute), [`registerPreParser`](stringpreparser.md#registerPreParser), [`runAll`](stringpreparser.md#runAll)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
