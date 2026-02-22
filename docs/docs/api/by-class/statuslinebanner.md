# statuslineBanner

*object* — defined in [console.t](../by-file/console.t.md) (line 273)


The banner window for the status line.


**Superclass chain:** [BannerWindow](bannerwindow.md) > [OutputStreamWindow](outputstreamwindow.md) > `object` > **statuslineBanner**


## Inherited Properties


*From [BannerWindow](bannerwindow.md):* [`align_`](bannerwindow.md#align_), [`handle_`](bannerwindow.md#handle_), [`id_`](bannerwindow.md#id_), [`inited_`](bannerwindow.md#inited_), [`parentID_`](bannerwindow.md#parentID_), [`size_`](bannerwindow.md#size_), [`sizeUnits_`](bannerwindow.md#sizeUnits_), [`styleFlags_`](bannerwindow.md#styleFlags_), [`windowType_`](bannerwindow.md#windowType_)


*From [OutputStreamWindow](outputstreamwindow.md):* [`outputStream_`](outputstreamwindow.md#outputStream_)


## Methods


### `initBannerWindow` *(overridden)*

Defined in console.t, line 285

initialize


### `removeBanner` *(overridden)*

Defined in console.t, line 275

close the window


### `setColorScheme`

Defined in console.t, line 306

Set the color scheme. We simply show a <BODY> tag that selects the parameterized colors STATUSBG and STATUSTEXT. (These are called "parameterized" colors because they don't select specific colors, but rather select whatever colors the interpreter wishes to use for the status line. In many cases, the interpreter lets the user select these colors via a Preferences dialog.)


## Inherited Methods


*From [BannerWindow](bannerwindow.md):* [`clearWindow`](bannerwindow.md#clearWindow), [`construct`](bannerwindow.md#construct), [`createOutputStreamObj`](bannerwindow.md#createOutputStreamObj), [`createSystemBanner`](bannerwindow.md#createSystemBanner), [`cursorTo`](bannerwindow.md#cursorTo), [`flushBanner`](bannerwindow.md#flushBanner), [`getBannerID`](bannerwindow.md#getBannerID), [`setScreenColor`](bannerwindow.md#setScreenColor), [`setSize`](bannerwindow.md#setSize), [`setTextColor`](bannerwindow.md#setTextColor), [`showBanner`](bannerwindow.md#showBanner), [`showForRestore`](bannerwindow.md#showForRestore), [`sizeToContents`](bannerwindow.md#sizeToContents), [`updateForRestore`](bannerwindow.md#updateForRestore), [`writeToBanner`](bannerwindow.md#writeToBanner)


*From [OutputStreamWindow](outputstreamwindow.md):* [`captureOutput`](outputstreamwindow.md#captureOutput), [`createOutputStream`](outputstreamwindow.md#createOutputStream), [`setOutputStream`](outputstreamwindow.md#setOutputStream)
