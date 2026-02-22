# inputManager

*object* — defined in [input.t](../by-file/input.t.md) (line 68)


Keyboard input manager.


**Superclass chain:** [PostRestoreObject](postrestoreobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **inputManager**


## Properties


### `inProgressDefObj`

Defined in input.t, line 761

the InputDef object for the input in progress


### `inputEventInProgress`

Defined in input.t, line 764

flag: keystroke/event input is in progress


### `inputLineInProgress`

Defined in input.t, line 758

Flag: command line input is in progress. If this is set, it means that we interrupted command-line editing by a timeout, so we should not show a prompt the next time we go back to the keyboard for input.


### `noInputTimeout`

Defined in input.t, line 783

Flag: inputLine does not support timeouts on the current platform. We set this when we get an InEvtNoTimeout return code from inputLineTimeout, so that we'll know not to try calling again with a timeout. This applies to the current interpreter only, so we must ignore any value restored from a previously saved game, since the game might have been saved on a different platform.


## Inherited Properties


*From [PostRestoreObject](postrestoreobject.md):* [`restoreCode`](postrestoreobject.md#restoreCode)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `cancelInputInProgress(reset)`

Defined in input.t, line 554

Cancel input in progress.


### `execute` *(overridden)*

Defined in input.t, line 727

receive post-restore notification


### `getEvent(allowRealTime, promptFunc)`

Defined in input.t, line 413

Read an event, processing real-time events while waiting, if desired. 'allowRealTime' and 'promptFunc' work the same way they do with getInputLine().


### `getEventOrKey(allowRealTime, promptFunc, keyOnly)`

Defined in input.t, line 429

Read an event or keystroke. 'allowRealTime' and 'promptFunc' work the same way they do in getInputLine(). If 'keyOnly' is true, then we're only interested in keystroke events, and we'll ignore any other events entered.


### `getInputDialog(icon, prompt, buttons, defaultButton, cancelButton)`

Defined in input.t, line 366

Ask for input through a dialog. Freezes the real-time clock for the duration of the dialog display. The arguments are the same as for the built-in inputDialog() function.


### `getInputFile(prompt, dialogType, fileType, flags)`

Defined in input.t, line 338

Ask for an input file. Freezes the real-time event clock for the duration of reading the event.


### `getInputLine(allowRealTime, promptFunc)`

Defined in input.t, line 90

Read a line of input from the keyboard.


### `getInputLineExt(defObj)`

Defined in input.t, line 102

Read a line of input from the keyboard - extended interface, using the InputDef object to define the input parameters. 'defObj' is an instance of class InputDef, defining how we're to handle the input.


### `getKey(allowRealTime, promptFunc)`

Defined in input.t, line 394

Read a keystroke, processing real-time events while waiting, if desired. 'allowRealTime' and 'promptFunc' work the same way they do with getInputLine().


### `inputBegin(promptFunc)`

Defined in input.t, line 707

Begin generic input. Cancels command report list capture, and shows the prompt if given.


### `inputEventBegin(promptFunc)`

Defined in input.t, line 623

Begin reading key/event input. We'll cancel any report gatherer so that prompt text shows immediately, and show the prompt if desired.


### `inputEventEnd`

Defined in input.t, line 638

End keystroke/event input.


### `inputLineBegin(defObj)`

Defined in input.t, line 652

Begin command line editing. If we're in HTML mode, we'll show the appropriate codes to establish the input font.


### `inputLineEnd`

Defined in input.t, line 678

End command line editing. If we're in HTML mode, we'll show the appropriate codes to close the input font.


### `pauseForMore(freezeRealTime)`

Defined in input.t, line 282

Pause for a MORE prompt. If freezeRealTime is true, we'll stop the real-time clock; otherwise we'll let it keep running. Even if we don't freeze the clock, we won't actually process any real-time events while waiting: the point of the MORE prompt is to allow the player to read and acknowledge the on-screen display before showing anything new, so we don't want to allow any output to result from real-time events that occur while waiting for user input. If any real-time events come due while we're waiting, we'll process them when we're done.


### `processRealTimeEvents(allowRealTime)`

Defined in input.t, line 583

Process any real-time events that are ready to run, and return the timeout until the next real-time event.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
