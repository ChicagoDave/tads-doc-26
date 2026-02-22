# Tip

*class* — defined in [tips.t](../by-file/tips.t.md) (line 96)


The Tip class. Each actual tip should be represented by an instance of this class. To show the tip, just call tipName.showTip(). If the tip has already been shown, or if the tips have been turned off completely, then nothing will be displayed.


**Superclass chain:** `object` > **TipGlobal objects:** [exitsTip](exitstip.md), [footnotesTip](footnotestip.md), [fullScoreTip](fullscoretip.md), [oopsTip](oopstip.md), [scoreChangeTip](scorechangetip.md), [undoTip](undotip.md)


## Properties


### `desc`

Defined in tips.t, line 102

The actual text to display when this tip is shown. We'll wrap it in <.tip> tags automatically, and also add a paragraph break before it.


### `shown`

Defined in tips.t, line 163

flag: has this tip been shown before?


## Methods


### `makeShown`

Defined in tips.t, line 153

Mark this tip as shown. This method can be called by outside code before the tip has been triggered. If the tip informs the player of a certain command, for instance, then it would become redundant if the player has already used that command.


### `shouldShowTip`

Defined in tips.t, line 135

should we show this tip when asked to?


### `showTip`

Defined in tips.t, line 105

show this tip


### `showTipDesc`

Defined in tips.t, line 122

display our tip description, I.E. the actual tip
