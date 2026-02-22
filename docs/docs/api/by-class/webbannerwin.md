# WebBannerWin

*class* — defined in [browser.t](../by-file/browser.t.md) (line 737)


Web Banner Window. This is designed as a *partial* drop-in replacement for the BannerWindow class, using Web UI windows as implemented in the core TADS javascript client.


**Superclass chain:** [OutputStreamWindow](outputstreamwindow.md) > `object` > **WebBannerWinGlobal objects:** [statuslineBanner](statuslinebanner.md)


## Inherited Properties


*From [OutputStreamWindow](outputstreamwindow.md):* [`outputStream_`](outputstreamwindow.md#outputStream_)


## Methods


### `createOutputStreamObj` *(overridden)*

Defined in browser.t, line 748

create our output stream subclass


### `flushBanner`

Defined in browser.t, line 754

flush output


### `init`

Defined in browser.t, line 741

Initialize. Call this when first displaying the window in the UI.


### `setSize(siz, units, advisory)`

Defined in browser.t, line 770

Banner window size settings. We simply ignore these; callers must rework their layout logic for the Web UI, since the javascript layout system is so different.


### `sizeToContents`

Defined in browser.t, line 771


### `writeToBanner(txt)`

Defined in browser.t, line 760

write text


## Inherited Methods


*From [OutputStreamWindow](outputstreamwindow.md):* [`captureOutput`](outputstreamwindow.md#captureOutput), [`createOutputStream`](outputstreamwindow.md#createOutputStream), [`setOutputStream`](outputstreamwindow.md#setOutputStream)
