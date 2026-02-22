# ParagraphManager

*class* — defined in [output.t](../by-file/output.t.md) (line 471)


Paragraph manager. We filter strings as they're about to be sent to the console to convert paragraph markers (represented in the source text using the "style tag" format, <.P>) into a configurable display rendering.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > **ParagraphManagerGlobal objects:** [mainParagraphManager](mainparagraphmanager.md), [menuParagraphManager](menuparagraphmanager.md)


## Properties


### `leadingMultiPat`

Defined in output.t, line 507

pre-compile some regular expression patterns we use a lot


### `leadingSinglePat`

Defined in output.t, line 508


### `renderAfterInput`

Defined in output.t, line 482

Flag: show or hide paragraph breaks immediately after input. By default, we do not show paragraph breaks after an input line.


### `renderText`

Defined in output.t, line 476

Rendering - this is what we display on the console to represent a paragraph break. By default, we'll display a blank line.


### `suppressAfter`

Defined in output.t, line 504

Following suppression. This is a regular expression that we match to individual characters. If the character immediately following a paragraph marker matches this expression, we'll suppress the character. We'll apply this to each character following a paragraph marker in turn until we find one that does not match; we'll suppress all of the characters that do match. By default, we suppress additional blank lines after a paragraph break.


### `suppressBefore`

Defined in output.t, line 492

Preceding suppression. This is a regular expression that we match to individual characters. If the character immediately preceding a paragraph marker matches this expression, we'll suppress the paragraph marker in the output. By default, we'll suppress a paragraph break following a blank line, because the default rendering would add a redundant blank line.


## Methods


### `filterText(ostr, txt)` *(overridden)*

Defined in output.t, line 512

process a string that's about to be written to the console
