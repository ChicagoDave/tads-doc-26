# HtmlStyleTag

*class* — defined in [output.t](../by-file/output.t.md) (line 789)


HtmlStyleTag - this is a subclass of StyleTag that provides different rendering depending on whether the interpreter is in HTML mode or not. In HTML mode, we display our htmlOpenText and htmlCloseText; when not in HTML mode, we display our plainOpenText and plainCloseText.


**Superclass chain:** [StyleTag](styletag.md) > `object` > **HtmlStyleTagGlobal objects:** [hyperlinkStyleTag](hyperlinkstyletag.md), [inputlineStyleTag](inputlinestyletag.md), [statusroomStyleTag](statusroomstyletag.md), [statusscoreStyleTag](statusscorestyletag.md)


## Properties


### `closeText` *(overridden)*

Defined in output.t, line 792


### `htmlCloseText`

Defined in output.t, line 796


### `htmlOpenText`

Defined in output.t, line 795

our HTML-mode opening and closing text


### `openText` *(overridden)*

Defined in output.t, line 790


### `plainCloseText`

Defined in output.t, line 800


### `plainOpenText`

Defined in output.t, line 799

our plain (non-HTML) opening and closing text


## Inherited Properties


*From [StyleTag](styletag.md):* [`tagName`](styletag.md#tagName)
