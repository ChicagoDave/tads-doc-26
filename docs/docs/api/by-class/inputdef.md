# InputDef

*class* — defined in [input.t](../by-file/input.t.md) (line 19)


Keyboard input parameter definition.


**Superclass chain:** `object` > **InputDefSubclasses:** [BasicInputDef](basicinputdef.md)


## Properties


### `allowRealTime`

Defined in input.t, line 33

Allow real-time events. If this is true, we'll allow real-time events to interrupt the input; if it's nil, we'll freeze the real-time clock while reading input.


### `promptFunc`

Defined in input.t, line 26

The prompt function. This is a function pointer (which is frequently given as an anonymous function) or nil; if it's nil, we won't show any prompt at all, otherwise we'll call the function pointer to display a prompt as needed.


## Methods


### `beginInputFont`

Defined in input.t, line 41

Begin the input style. This should do anything required to set the font to the desired attributes for the input text. By default, we'll simply display <.inputline> to set up the default input style.


### `endInputFont`

Defined in input.t, line 47

End the input style. By default, we'll close the <.inputline> that we opened in beginInputFont().
