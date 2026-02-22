# BannerWindow

*class* — defined in [banner.t](../by-file/banner.t.md) (line 40)


A BannerWindow corresponds to an on-screen banner. For each banner window a game wants to display, the game must create an object of this class.


**Superclass chain:** [OutputStreamWindow](outputstreamwindow.md) > `object` > **BannerWindowGlobal objects:** [contentsMenuBanner](contentsmenubanner.md), [longTopicBanner](longtopicbanner.md), [statuslineBanner](statuslinebanner.md), [topMenuBanner](topmenubanner.md)


## Properties


### `align_`

Defined in banner.t, line 450


### `handle_`

Defined in banner.t, line 441

the handle to my system-level banner window


### `id_`

Defined in banner.t, line 438

The creator-assigned ID string to identify the banner persistently. This is only needed for banners created dynamically; for BannerWindow objects defined statically at compile time, simply leave this value as nil, and we'll use the object itself as the identifier.


### `inited_`

Defined in banner.t, line 429

flag: this banner has been initialized with initBannerWindow()


### `parentID_`

Defined in banner.t, line 448

Creation parameters. We store these when we create the banner, and update them as needed when the banner's display attributes are changed.


### `size_`

Defined in banner.t, line 451


### `sizeUnits_`

Defined in banner.t, line 452


### `styleFlags_`

Defined in banner.t, line 453


### `windowType_`

Defined in banner.t, line 449


## Inherited Properties


*From [OutputStreamWindow](outputstreamwindow.md):* [`outputStream_`](outputstreamwindow.md#outputStream_)


## Methods


### `clearWindow`

Defined in banner.t, line 309

Clear my banner window. This clears out all of the contents of our on-screen display area.


### `construct(id)`

Defined in banner.t, line 54

Construct the object.


### `createOutputStreamObj` *(overridden)*

Defined in banner.t, line 375

create our banner output stream


### `createSystemBanner(parent, where, other, windowType, align, size, sizeUnits, styleFlags)`

Defined in banner.t, line 361

Create the system-level banner window. This can be customized as needed, although this default implementation should be suitable for most instances.


### `cursorTo(row, col)`

Defined in banner.t, line 326

Move the cursor to the given row/column position. This can only be used with text-grid banners; for ordinary text banners, this has no effect.


### `flushBanner`

Defined in banner.t, line 267

flush any pending output to the banner


### `getBannerID`

Defined in banner.t, line 334

Get the banner identifier. If our 'id_' property is set to nil, we'll assume that we're a statically-defined object, in which case 'self' is a suitable identifier. Otherwise, we'll return the identifier string.


### `initBannerWindow`

Defined in banner.t, line 422

Initialize the banner window. This is called during initialization (when first starting the game, or when resetting with RESTART). If the banner is to be displayed from the start of the game, this can set up the on-screen display.


### `removeBanner`

Defined in banner.t, line 237

Remove the banner. This removes the banner's on-screen window. The BannerWindow object itself remains valid, but after this method returns, the BannerWindow no longer has an associated display window.


### `setScreenColor(color)`

Defined in banner.t, line 319

set the screen color in the banner window


### `setSize(size, sizeUnits, isAdvisory)`

Defined in banner.t, line 280

Set the banner window to a specific size. 'size' is the new size, in units given by 'sizeUnits', which is a BannerSizeXxx constant.


### `setTextColor(fg, bg)`

Defined in banner.t, line 316

set the text color in the banner


### `showBanner(parent, where, other, windowType, align, size, sizeUnits, styleFlags)`

Defined in banner.t, line 104

Show the banner. The game should call this method when it first wants to display the banner.


### `showForRestore(parent, where, other)`

Defined in banner.t, line 343

Restore this banner. This is called after a RESTORE or UNDO operation that finds that this banner was being displayed at the time the state was saved but is not currently displayed in the active UI. We'll show the banner using the characteristics saved persistently.


### `sizeToContents`

Defined in banner.t, line 299

Size the banner to its current contents. Note that some systems do not support this operation, so callers should always make an advisory call to setSize() first to set a size based on the expected content size.


### `updateForRestore`

Defined in banner.t, line 390

Update my contents after being restored. By default, this does nothing; instances might want to override this to refresh the contents of the banner if the banner is normally updated only in response to specific events. Note that it's not necessary to do anything here if the banner will soon be updated automatically as part of normal processing; for example, the status line banner is updated at each new command line via a prompt-daemon, so there's no need for the status line banner to do anything here.


### `writeToBanner(txt)`

Defined in banner.t, line 260

write the given text to the banner


## Inherited Methods


*From [OutputStreamWindow](outputstreamwindow.md):* [`captureOutput`](outputstreamwindow.md#captureOutput), [`createOutputStream`](outputstreamwindow.md#createOutputStream), [`setOutputStream`](outputstreamwindow.md#setOutputStream)
