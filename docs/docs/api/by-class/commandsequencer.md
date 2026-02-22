# commandSequencer

*object* — defined in [output.t](../by-file/output.t.md) (line 1611)


Command Sequencer Filter. This is an output filter that handles the special <.commandsep> tag for visual command separation. This tag has the form of a style tag, but must be processed specially.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > **commandSequencer**


## Properties


### `patNextTag`

Defined in output.t, line 1648

pre-compile our tag sequence pattern


### `state_`

Defined in output.t, line 1862

our current state - start out in before-command mode


## Methods


### `filterText(ostr, txt)` *(overridden)*

Defined in output.t, line 1656

Apply our filter


### `setCommandMode`

Defined in output.t, line 1618

Force the sequencer into mid-command mode. This can be used to defeat the resequencing into before-results mode that occurs if any interactive command-line input must be read in the course of a command's execution.


### `writeThrough(txt)`

Defined in output.t, line 1624

Internal routine: write the given text directly through us, skipping any filtering we'd otherwise apply.
