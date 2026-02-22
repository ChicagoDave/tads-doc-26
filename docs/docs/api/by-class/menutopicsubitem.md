# MenuTopicSubItem

*class* — defined in [menusys.t](../by-file/menusys.t.md) (line 459)


A menu topic sub-item can be used to represent an item in a MenuTopicItem's list of display items. This can be useful when displaying a topic must trigger a side-effect.


**Superclass chain:** `object` > **MenuTopicSubItemSubclasses:** [Hint](hint.md)


## Methods


### `getItemText`

Defined in menusys.t, line 465

Get the item's text. By default, we just return an empty string. This should be overridden to return the appropriate text, and can also trigger any desired side-effects.
