# bannerUITracker

*object* — defined in [banner.t](../by-file/banner.t.md) (line 503)


The banner UI tracker. This object keeps track of the current user interface display state; this object is transient because the interpreter's user interface is not part of the persistence mechanism.


**Superclass chain:** `object` > **bannerUITracker**


## Properties


### `activeBanners_`

Defined in banner.t, line 745

The vector of banners currently on the screen. This is a list of transient BannerUIWindow objects, stored in the same order as the banner layout list.


## Methods


### `addBanner(handle, ostr, id, parentID, where, other, windowType, align, styleFlags)`

Defined in banner.t, line 505

add a banner to the active display list


### `getTracker(win)`

Defined in banner.t, line 652

get the BannerUIWindow tracker object for a given BannerWindow


### `orderMatches(uiWin, where, otherID)`

Defined in banner.t, line 664

check a BannerUIWindow to see if it matches the given layout order


### `removeBanner(id)`

Defined in banner.t, line 618

remove a banner from the active display list


### `skipDescendants(idx)`

Defined in banner.t, line 581

Given an index in our list of active windows, skip the given item and all items whose windows are descended from this window. We'll leave the index positioned on the next entry in the list that isn't a descendant of the window at the given index. Note that this skips not only children but grandchildren (and so on) as well.
