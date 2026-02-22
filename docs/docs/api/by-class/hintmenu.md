# HintMenu

*class* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 430)


A hint menu. This same class can be used for the top-level hints menu and for sub-menus within the hints menu.


**Superclass chain:** [MenuItem](menuitem.md) > [MenuObject](menuobject.md) > `object` > [HintMenuObject](hintmenuobject.md) > **HintMenuSubclasses:** [TopHintMenu](tophintmenu.md)


## Properties


### `allContents`

Defined in hintsys.t, line 485

our list of all of our sub-items (some of which may not be active, in which case they'll appear in this list but not in our 'contents' list, which contains only active contents)


### `isActiveInMenu`

Defined in hintsys.t, line 460

we're active in a menu if we have any active contents


### `title` *(overridden)*

Defined in hintsys.t, line 432

the menu's title


## Inherited Properties


*From [MenuItem](menuitem.md):* [`bgcolor`](menuitem.md#bgcolor), [`curKeyList`](menuitem.md#curKeyList), [`curMenu`](menuitem.md#curMenu), [`fgcolor`](menuitem.md#fgcolor), [`fullScreenMode`](menuitem.md#fullScreenMode), [`heading`](menuitem.md#heading), [`indent`](menuitem.md#indent), [`isOpen`](menuitem.md#isOpen), [`keyList`](menuitem.md#keyList), [`prevMenuLink`](menuitem.md#prevMenuLink), [`topbarbg`](menuitem.md#topbarbg), [`topbarfg`](menuitem.md#topbarfg), [`topMenu`](menuitem.md#topMenu)


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


*From [HintMenuObject](hintmenuobject.md):* [`topicOrder`](hintmenuobject.md#topicOrder)


## Methods


### `addToContents(obj)` *(overridden)*

Defined in hintsys.t, line 463

add a sub-item to our contents


### `initializeContents` *(overridden)*

Defined in hintsys.t, line 473

initialize our contents list


### `updateContents` *(overridden)*

Defined in hintsys.t, line 435

update our contents


## Inherited Methods


*From [MenuItem](menuitem.md):* [`display`](menuitem.md#display), [`enterSubMenu`](menuitem.md#enterSubMenu), [`formatXML`](menuitem.md#formatXML), [`getChildIndex`](menuitem.md#getChildIndex), [`getKeysXML`](menuitem.md#getKeysXML), [`getNextMenu`](menuitem.md#getNextMenu), [`getPrevMenu`](menuitem.md#getPrevMenu), [`getXML`](menuitem.md#getXML), [`refreshTopMenuBanner`](menuitem.md#refreshTopMenuBanner), [`removeStatusLine`](menuitem.md#removeStatusLine), [`removeTopMenuBanner`](menuitem.md#removeTopMenuBanner), [`showMenu`](menuitem.md#showMenu), [`showMenuHtml`](menuitem.md#showMenuHtml), [`showMenuText`](menuitem.md#showMenuText), [`showTopMenuBanner`](menuitem.md#showTopMenuBanner)


*From [MenuObject](menuobject.md):* [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`execute`](menuobject.md#execute), [`initializeLocation`](menuobject.md#initializeLocation)


*From [HintMenuObject](hintmenuobject.md):* [`compareForTopicSort`](hintmenuobject.md#compareForTopicSort)
