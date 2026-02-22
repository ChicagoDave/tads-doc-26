# Hint

*class* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 362)


A Hint encapsulates one hint from a topic. In many cases, hints can be listed in a topic simply as strings, rather than using Hint objects. Hint objects provide a little more control, though; in particular, a Hint object can specify some additional code to run when the hint is shown, so that it can apply any side effects of showing the hint (for example, when a hint is shown, it could mark another Goal object as Open, which might be desirable if the hint refers to another topic that the player might not yet have encountered).


**Superclass chain:** [MenuTopicSubItem](menutopicsubitem.md) > `object` > **Hint**


## Properties


### `hintText`

Defined in hintsys.t, line 364

the hint text


### `referencedGoals`

Defined in hintsys.t, line 381

A list of other Goal objects that this hint references. By default, when we show this hint for the first time, we'll promote each goal in this list from Undiscovered to Open.


## Methods


### `getItemText` *(overridden)*

Defined in hintsys.t, line 389

Get my hint text. By default, we mark as Open any goals listed in our referencedGoals list, then return our hintText string. Individual Hint objects can override this as desired to apply any additional side effects.
