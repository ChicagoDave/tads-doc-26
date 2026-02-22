# TopHintMenu

*class* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 504)


Top-level hint menu. As a convenience, an object defined of this class will automatically register itself as the top-level hint menu during pre-initialization.


**Superclass chain:** [HintMenu](hintmenu.md) > [MenuItem](menuitem.md) > [MenuObject](menuobject.md) > `object` > [HintMenuObject](hintmenuobject.md) > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **TopHintMenu**


## Inherited Properties


*From [HintMenu](hintmenu.md):* [`allContents`](hintmenu.md#allContents), [`isActiveInMenu`](hintmenu.md#isActiveInMenu), [`title`](hintmenu.md#title)


*From [MenuItem](menuitem.md):* [`bgcolor`](menuitem.md#bgcolor), [`curKeyList`](menuitem.md#curKeyList), [`curMenu`](menuitem.md#curMenu), [`fgcolor`](menuitem.md#fgcolor), [`fullScreenMode`](menuitem.md#fullScreenMode), [`heading`](menuitem.md#heading), [`indent`](menuitem.md#indent), [`isOpen`](menuitem.md#isOpen), [`keyList`](menuitem.md#keyList), [`prevMenuLink`](menuitem.md#prevMenuLink), [`topbarbg`](menuitem.md#topbarbg), [`topbarfg`](menuitem.md#topbarfg), [`topMenu`](menuitem.md#topMenu)


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


*From [HintMenuObject](hintmenuobject.md):* [`topicOrder`](hintmenuobject.md#topicOrder)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in hintsys.t, line 506

register as the top-level hint menu during pre-initialization


## Inherited Methods


*From [HintMenu](hintmenu.md):* [`addToContents`](hintmenu.md#addToContents), [`initializeContents`](hintmenu.md#initializeContents), [`updateContents`](hintmenu.md#updateContents)


*From [MenuItem](menuitem.md):* [`display`](menuitem.md#display), [`enterSubMenu`](menuitem.md#enterSubMenu), [`formatXML`](menuitem.md#formatXML), [`getChildIndex`](menuitem.md#getChildIndex), [`getKeysXML`](menuitem.md#getKeysXML), [`getNextMenu`](menuitem.md#getNextMenu), [`getPrevMenu`](menuitem.md#getPrevMenu), [`getXML`](menuitem.md#getXML), [`refreshTopMenuBanner`](menuitem.md#refreshTopMenuBanner), [`removeStatusLine`](menuitem.md#removeStatusLine), [`removeTopMenuBanner`](menuitem.md#removeTopMenuBanner), [`showMenu`](menuitem.md#showMenu), [`showMenuHtml`](menuitem.md#showMenuHtml), [`showMenuText`](menuitem.md#showMenuText), [`showTopMenuBanner`](menuitem.md#showTopMenuBanner)


*From [MenuObject](menuobject.md):* [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`initializeLocation`](menuobject.md#initializeLocation)


*From [HintMenuObject](hintmenuobject.md):* [`compareForTopicSort`](hintmenuobject.md#compareForTopicSort)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
