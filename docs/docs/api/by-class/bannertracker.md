# bannerTracker

*object* — defined in [banner.t](../by-file/banner.t.md) (line 811)


The persistent banner tracker. This keeps track of the active banner windows persistently. Whenever we save or restore the game's state, this object will be saved or restored along with the state. When we restore a previously saved state, we can look at this object to determine which banners were active at the time the state was saved, and use this information to restore the same active banners in the user interface.


**Superclass chain:** [PostRestoreObject](postrestoreobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > [PostUndoObject](postundoobject.md) > **bannerTracker**


## Properties


### `activeBanners_`

Defined in banner.t, line 927

The list of active banners. This is a list of BannerWindow objects, stored in banner layout list order.


## Inherited Properties


*From [PostRestoreObject](postrestoreobject.md):* [`restoreCode`](postrestoreobject.md#restoreCode)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `addBanner(win, parent, where, other)`

Defined in banner.t, line 813

add a banner to the active display list


### `execute` *(overridden)*

Defined in banner.t, line 930

receive RESTORE/UNDO notification


### `removeBanner(win)`

Defined in banner.t, line 899

remove a banner from the active list


### `restoreDisplayState(initing)`

Defined in banner.t, line 943

Restore the saved banner display state, so that the banner layout looks the same as it did when we saved the persistent state. This should be called after restoring a saved state, undoing to a savepoint, or initializing (when first starting the game or when restarting).


### `skipDescendants(idx)`

Defined in banner.t, line 872

Skip all descendants of the window at the given index.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
