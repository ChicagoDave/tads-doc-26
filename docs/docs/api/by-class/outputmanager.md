# outputManager

*object* — defined in [output.t](../by-file/output.t.md) (line 47)


Output Manager. This object contains global code for displaying text on the console.


**Superclass chain:** `object` > **outputManager**


## Properties


### `curOutputStream`

Defined in output.t, line 94

the current output stream - start with the main text stream


### `htmlMode`

Defined in output.t, line 111

Is the UI running in HTML mode? This tells us if we have a full HTML UI or a text-only UI. Full HTML mode applies if we're running on a Multimedia TADS interpreter, or we're using the Web UI, which runs in a separate browser and is thus inherently HTML-capable.


## Methods


### `setOutputStream(ostr)`

Defined in output.t, line 54

Switch to a new active output stream. Returns the previously active output stream, so that the caller can easily restore the old output stream if the new output stream is to be established only for a specific duration.


### `withOutputStream(ostr, func)`

Defined in output.t, line 75

run the given function, using the given output stream as the active default output stream
