# MenuLongTopicItem

*class* — defined in [menusys.t](../by-file/menusys.t.md) (line 474)


Long Topic Items are used to print out big long gobs of text on a subject. Use it for printing long treatises on your design philosophy and the like.


**Superclass chain:** [MenuItem](menuitem.md) > [MenuObject](menuobject.md) > `object` > **MenuLongTopicItemSubclasses:** [HintLongTopicItem](hintlongtopicitem.md)


## Properties


### `heading` *(overridden)*

Defined in menusys.t, line 479

the heading, shown while we're displaying our contents


### `isChapterMenu`

Defined in menusys.t, line 490

Flag - this is a "chapter" in a list of chapters. If this is set to true, then we'll offer the options to proceed directly to the next and previous chapters. If this is nil, we'll simply wait for acknowledgment and return to the parent menu.


### `menuContents`

Defined in menusys.t, line 482

either a string to be displayed, or a method returning a string


### `menuLongTopicEnd`

Defined in menusys.t, line 493

the message we display at the end of our text


### `title` *(overridden)*

Defined in menusys.t, line 476

the title of the menu, shown in parent menus


## Inherited Properties


*From [MenuItem](menuitem.md):* [`bgcolor`](menuitem.md#bgcolor), [`curKeyList`](menuitem.md#curKeyList), [`curMenu`](menuitem.md#curMenu), [`fgcolor`](menuitem.md#fgcolor), [`fullScreenMode`](menuitem.md#fullScreenMode), [`indent`](menuitem.md#indent), [`isOpen`](menuitem.md#isOpen), [`keyList`](menuitem.md#keyList), [`prevMenuLink`](menuitem.md#prevMenuLink), [`topbarbg`](menuitem.md#topbarbg), [`topbarfg`](menuitem.md#topbarfg), [`topMenu`](menuitem.md#topMenu)


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


## Methods


### `getXML(from)` *(overridden)*

Defined in menuweb.t, line 301

get my XML description


### `showMenuCommon(topMenu)`

Defined in menucon.t, line 1060

show our contents - common handler for text and HTML modes


### `showMenuHtml(topMenu)` *(overridden)*

Defined in menucon.t, line 938

display and run our menu in HTML mode


### `showMenuText(topMenu)` *(overridden)*

Defined in menucon.t, line 917

display and run our menu in text mode


## Inherited Methods


*From [MenuItem](menuitem.md):* [`display`](menuitem.md#display), [`enterSubMenu`](menuitem.md#enterSubMenu), [`formatXML`](menuitem.md#formatXML), [`getChildIndex`](menuitem.md#getChildIndex), [`getKeysXML`](menuitem.md#getKeysXML), [`getNextMenu`](menuitem.md#getNextMenu), [`getPrevMenu`](menuitem.md#getPrevMenu), [`refreshTopMenuBanner`](menuitem.md#refreshTopMenuBanner), [`removeStatusLine`](menuitem.md#removeStatusLine), [`removeTopMenuBanner`](menuitem.md#removeTopMenuBanner), [`showMenu`](menuitem.md#showMenu), [`showTopMenuBanner`](menuitem.md#showTopMenuBanner), [`updateContents`](menuitem.md#updateContents)


*From [MenuObject](menuobject.md):* [`addToContents`](menuobject.md#addToContents), [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`execute`](menuobject.md#execute), [`initializeContents`](menuobject.md#initializeContents), [`initializeLocation`](menuobject.md#initializeLocation)
