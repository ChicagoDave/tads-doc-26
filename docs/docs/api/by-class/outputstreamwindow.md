# OutputStreamWindow

*class* — defined in [output.t](../by-file/output.t.md) (line 1948)


Output stream window.


**Superclass chain:** `object` > **OutputStreamWindowSubclasses:** [BannerWindow](bannerwindow.md), [WebBannerWin](webbannerwin.md)


## Properties


### `outputStream_`

Defined in output.t, line 2015

My output stream - this is a transient OutputStream instance. Subclasses must create this explicitly by calling createOutputStream() when the underlying UI window is first created.


## Methods


### `captureOutput(func)`

Defined in output.t, line 1955

Invoke the given callback function, setting the default output stream to the window's output stream for the duration of the call. This allows invoking any code that writes to the current default output stream and displaying the result in the window.


### `createOutputStream`

Defined in output.t, line 1990

Create our output stream. We'll create the appropriate output stream subclass and set it up with our default output filters. Subclasses can override this as needed to customize the filters.


### `createOutputStreamObj`

Defined in output.t, line 2007

Create the output stream object. Subclasses can override this to create the appropriate stream subclass. Note that the stream should always be created as a transient object.


### `setOutputStream`

Defined in output.t, line 1979

Make my output stream the default in the output manager. Returns the previous default output stream; the caller can note the return value and use it later to restore the original output stream via a call to outputManager.setOutputStream(), if desired.
