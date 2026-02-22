# HintLongTopicItem

*class* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 491)


A hint menu version of the long topic menu.


**Superclass chain:** [MenuLongTopicItem](menulongtopicitem.md) > [MenuItem](menuitem.md) > [MenuObject](menuobject.md) > `object` > [HintMenuObject](hintmenuobject.md) > **HintLongTopicItem**


## Properties


### `isActiveInMenu`

Defined in hintsys.t, line 496

presume these are always active - they're usually used for things like hint system instructions that should always be available


## Inherited Properties


*From [MenuLongTopicItem](menulongtopicitem.md):* [`heading`](menulongtopicitem.md#heading), [`isChapterMenu`](menulongtopicitem.md#isChapterMenu), [`menuContents`](menulongtopicitem.md#menuContents), [`menuLongTopicEnd`](menulongtopicitem.md#menuLongTopicEnd), [`title`](menulongtopicitem.md#title)


*From [MenuItem](menuitem.md):* [`bgcolor`](menuitem.md#bgcolor), [`curKeyList`](menuitem.md#curKeyList), [`curMenu`](menuitem.md#curMenu), [`fgcolor`](menuitem.md#fgcolor), [`fullScreenMode`](menuitem.md#fullScreenMode), [`indent`](menuitem.md#indent), [`isOpen`](menuitem.md#isOpen), [`keyList`](menuitem.md#keyList), [`prevMenuLink`](menuitem.md#prevMenuLink), [`topbarbg`](menuitem.md#topbarbg), [`topbarfg`](menuitem.md#topbarfg), [`topMenu`](menuitem.md#topMenu)


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


*From [HintMenuObject](hintmenuobject.md):* [`topicOrder`](hintmenuobject.md#topicOrder)


## Inherited Methods


*From [MenuLongTopicItem](menulongtopicitem.md):* [`getXML`](menulongtopicitem.md#getXML), [`showMenuCommon`](menulongtopicitem.md#showMenuCommon), [`showMenuHtml`](menulongtopicitem.md#showMenuHtml), [`showMenuText`](menulongtopicitem.md#showMenuText)


*From [MenuItem](menuitem.md):* [`display`](menuitem.md#display), [`enterSubMenu`](menuitem.md#enterSubMenu), [`formatXML`](menuitem.md#formatXML), [`getChildIndex`](menuitem.md#getChildIndex), [`getKeysXML`](menuitem.md#getKeysXML), [`getNextMenu`](menuitem.md#getNextMenu), [`getPrevMenu`](menuitem.md#getPrevMenu), [`refreshTopMenuBanner`](menuitem.md#refreshTopMenuBanner), [`removeStatusLine`](menuitem.md#removeStatusLine), [`removeTopMenuBanner`](menuitem.md#removeTopMenuBanner), [`showMenu`](menuitem.md#showMenu), [`showTopMenuBanner`](menuitem.md#showTopMenuBanner), [`updateContents`](menuitem.md#updateContents)


*From [MenuObject](menuobject.md):* [`addToContents`](menuobject.md#addToContents), [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`execute`](menuobject.md#execute), [`initializeContents`](menuobject.md#initializeContents), [`initializeLocation`](menuobject.md#initializeLocation)


*From [HintMenuObject](hintmenuobject.md):* [`compareForTopicSort`](hintmenuobject.md#compareForTopicSort)
