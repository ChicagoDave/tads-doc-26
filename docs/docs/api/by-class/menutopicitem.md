# MenuTopicItem

*class* — defined in [menusys.t](../by-file/menusys.t.md) (line 421)


MenuTopicItem displays a series of entries successively. This is intended to be used for displaying something like a list of hints for a topic. Set menuContents to be a list of strings to be displayed.


**Superclass chain:** [MenuItem](menuitem.md) > [MenuObject](menuobject.md) > `object` > **MenuTopicItemSubclasses:** [Goal](goal.md)


## Properties


### `chunkSize`

Defined in menusys.t, line 447

The maximum number of our sub-items that we'll display at once. This is only used on interpreters with banner capabilities, and is ignored in full-screen mode.


### `heading` *(overridden)*

Defined in menusys.t, line 426

heading, displayed while we're showing this topic list


### `lastDisplayed`

Defined in menusys.t, line 440

the index of the last item we displayed from our menuContents list


### `menuContents`

Defined in menusys.t, line 437

A list of strings and/or MenuTopicSubItem items. Each one of these is meant to be something like a single hint on our topic. We display these items one at a time when our menu item is selected.


### `menuTopicListEnd`

Defined in menusys.t, line 450

we'll display this after we've shown all of our items


### `nextMenuTopicLink`

Defined in menusys.t, line 429

hyperlink text for showing the next menu


### `title` *(overridden)*

Defined in menusys.t, line 423

the name of this topic, as it appears in our parent menu


## Inherited Properties


*From [MenuItem](menuitem.md):* [`bgcolor`](menuitem.md#bgcolor), [`curKeyList`](menuitem.md#curKeyList), [`curMenu`](menuitem.md#curMenu), [`fgcolor`](menuitem.md#fgcolor), [`fullScreenMode`](menuitem.md#fullScreenMode), [`indent`](menuitem.md#indent), [`isOpen`](menuitem.md#isOpen), [`keyList`](menuitem.md#keyList), [`prevMenuLink`](menuitem.md#prevMenuLink), [`topbarbg`](menuitem.md#topbarbg), [`topbarfg`](menuitem.md#topbarfg), [`topMenu`](menuitem.md#topMenu)


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


## Methods


### `displaySubItem(idx, lastBeforeInput, eol)`

Defined in menucon.t, line 875

Display an item from our list. 'idx' is the index in our list of the item to display. 'lastBeforeInput' indicates whether or not this is the last item we're going to show before pausing for user input. 'eol' gives the newline sequence to display at the end of the line.


### `getNextTopicXML`

Defined in menuweb.t, line 270

get the next topic, in XML format


### `getTopicXML(i)`

Defined in menuweb.t, line 281

get the XML formatted description of the item at the given index


### `getXML(from)` *(overridden)*

Defined in menuweb.t, line 242

get the XML description of my menu list


### `redrawWinHtml(topIdx)`

Defined in menucon.t, line 782

redraw the window in HTML mode, starting with the given item at the top of the window


### `showMenuHtml(topMenu)` *(overridden)*

Defined in menucon.t, line 654

Display and run our menu in HTML mode.


### `showMenuText(topMenu)` *(overridden)*

Defined in menucon.t, line 594

Display and run our menu in text mode.


## Inherited Methods


*From [MenuItem](menuitem.md):* [`display`](menuitem.md#display), [`enterSubMenu`](menuitem.md#enterSubMenu), [`formatXML`](menuitem.md#formatXML), [`getChildIndex`](menuitem.md#getChildIndex), [`getKeysXML`](menuitem.md#getKeysXML), [`getNextMenu`](menuitem.md#getNextMenu), [`getPrevMenu`](menuitem.md#getPrevMenu), [`refreshTopMenuBanner`](menuitem.md#refreshTopMenuBanner), [`removeStatusLine`](menuitem.md#removeStatusLine), [`removeTopMenuBanner`](menuitem.md#removeTopMenuBanner), [`showMenu`](menuitem.md#showMenu), [`showTopMenuBanner`](menuitem.md#showTopMenuBanner), [`updateContents`](menuitem.md#updateContents)


*From [MenuObject](menuobject.md):* [`addToContents`](menuobject.md#addToContents), [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`execute`](menuobject.md#execute), [`initializeContents`](menuobject.md#initializeContents), [`initializeLocation`](menuobject.md#initializeLocation)
