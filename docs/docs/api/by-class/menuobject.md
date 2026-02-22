# MenuObject

*class* — defined in [menusys.t](../by-file/menusys.t.md) (line 141)


A basic menu object. This is an abstract base class that encapsulates some behavior common to different menu classes, and allows the use of the + syntax (like "+ MenuItem") to define containment.


**Superclass chain:** `object` > **MenuObjectSubclasses:** [MenuItem](menuitem.md), [HintMenu](hintmenu.md), [TopHintMenu](tophintmenu.md), [MenuLongTopicItem](menulongtopicitem.md), [HintLongTopicItem](hintlongtopicitem.md), [MenuTopicItem](menutopicitem.md), [Goal](goal.md)


## Properties


### `contents`

Defined in menusys.t, line 143

our contents list


### `menuOrder`

Defined in menusys.t, line 204

The menu order. When we're about to show a list of menu items, we'll sort the list in ascending order of this property, then in ascending order of title. By default, we set this order value to be equal to the menu item's sourceTextOrder. This makes the menu order default to the order of objects as defined in the source. If some other basis is desired, override topicOrder.


## Methods


### `addToContents(obj)`

Defined in menusys.t, line 156

add a menu item


### `compareForMenuSort(other)`

Defined in menusys.t, line 215

Compare this menu object to another, for the purposes of sorting a list of menu items. Returns a positive number if this menu item sorts after the other one, a negative number if this menu item sorts before the other one, 0 if the relative order is arbitrary.


### `execute`

Defined in menusys.t, line 255

This preinit object makes sure the MenuObjects all have their contents initialized properly.


### `initializeContents`

Defined in menusys.t, line 242

Finish initializing our contents list. This will be called on each MenuObject *after* we've called initializeLocation() on every object. In other words, every menu will already have been added to its parent's contents; this can do anything else that's needed to initialize the contents list. For example, some subclasses might want to sort their contents here, so that they list their menus in a defined order. By default, we sort the menu items by menuOrder; subclasses can override this as needed.


### `initializeLocation`

Defined in menusys.t, line 149

Since we're inheriting from object, but need to use the "+" syntax, we need to set up the contents appropriately
