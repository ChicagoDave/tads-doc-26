# BannerUIWindow

*class* — defined in [banner.t](../by-file/banner.t.md) (line 754)


A BannerUIWindow object. This keeps track of the transient UI state of a banner window while it appears on the screen. We create only transient instances of this class, since it tracks what's actually displayed at any given time.


**Superclass chain:** `object` > **BannerUIWindow**


## Properties


### `align_`

Defined in banner.t, line 786


### `handle_`

Defined in banner.t, line 769

the system-level banner handle


### `id_`

Defined in banner.t, line 772

the banner's ID


### `outputStream_`

Defined in banner.t, line 782

The banner's output stream. Output streams are always transient, so hang on to each active banner's stream so that we can plug it back in on restore.


### `parentID_`

Defined in banner.t, line 775

the parent banner's ID (nil if this is a top-level banner)


### `styleFlags_`

Defined in banner.t, line 787


### `win_`

Defined in banner.t, line 794

Scratch-pad for our association to our BannerWindow object. We only use this during the RESTORE process, to tie the transient object back to the proper persistent object.


### `windowType_`

Defined in banner.t, line 785

creation parameters of the banner


## Methods


### `construct(handle, ostr, id, parentID, windowType, align, styleFlags)`

Defined in banner.t, line 756

construct
