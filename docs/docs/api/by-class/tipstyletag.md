# tipStyleTag

*object* — defined in [tips.t](../by-file/tips.t.md) (line 171)


A style tag that we enclose tips with. By default, we just use plain parentheses, just like for notifications and parser messages, but this could be overridden if we wanted to display something fancier.


**Superclass chain:** [StyleTag](styletag.md) > `object` > **tipStyleTag**


## Properties


### `closeText` *(overridden)*

Defined in tips.t, line 173


### `openText` *(overridden)*

Defined in tips.t, line 172


## Inherited Properties


*From [StyleTag](styletag.md):* [`tagName`](styletag.md#tagName)


## Methods


### `execute`

Defined in tips.t, line 183

During pre-init, create a PromptDaemon for displaying tips. We don't want to display them directly when the showTip() method is called, to allow tips to be triggered from pretty much anywhere without having to worry about them showing up in the middle of some text.
