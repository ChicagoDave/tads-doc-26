# MenuItem

*class* — defined in [menusys.t](../by-file/menusys.t.md) (line 275)


A MenuItem is a given item in the menu tree. In general all you need to do to use menus is create a tree of MenuItems with titles.


**Superclass chain:** [MenuObject](menuobject.md) > `object` > **MenuItemSubclasses:** [HintMenu](hintmenu.md), [TopHintMenu](tophintmenu.md), [MenuLongTopicItem](menulongtopicitem.md), [HintLongTopicItem](hintlongtopicitem.md), [MenuTopicItem](menutopicitem.md), [Goal](goal.md)


## Properties


### `bgcolor`

Defined in menusys.t, line 311


### `curKeyList`

Defined in menusys.t, line 354

the current key list - we'll set this on entry to the start of each showMenuXxx method, so that we keep track of the actual key list in use, as inherited from the top-level menu


### `curMenu`

Defined in menuweb.t, line 41

current menu, and current top-level menu


### `fgcolor`

Defined in menusys.t, line 310

foreground (text) and background colors, as HTML color names


### `fullScreenMode`

Defined in menusys.t, line 328

full-screen mode: make our menu take up the whole screen (apart from the instructions bar, of course)


### `heading`

Defined in menusys.t, line 283

the heading - this is shown when this menu is active; by default, we simply use the title


### `indent`

Defined in menusys.t, line 322

number of spaces to indent the menu's contents


### `isOpen`

Defined in menuweb.t, line 45

is the menu open?


### `keyList`

Defined in menusys.t, line 347

The keys used to navigate the menus, in order:


### `prevMenuLink`

Defined in menusys.t, line 363

Title for the link to the previous menu, if any. If the menu has a parent menu, we'll display this link next to the menu title in the top instructions/title bar. If this is nil, we won't display a link at all. Note that this can contain an HTML fragment; for example, you could use an <IMG> tag to display an icon here.


### `title`

Defined in menusys.t, line 277

the name of the menu; this is listed in the parent menu


### `topbarbg`

Defined in menusys.t, line 319


### `topbarfg`

Defined in menusys.t, line 318

Foreground and background colors for the top instructions bar. By default, we use the color scheme of the parent menu, or the inverse of our main menu color scheme if we're the top menu.


### `topMenu`

Defined in menuweb.t, line 42


## Inherited Properties


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


## Methods


### `display`

Defined in menuweb.t, line 23

Call menu.display when you're ready to show the menu. This should be called on the top-level menu; we run the entire menu display process, and return when the user exits from the menu tree.


### `enterSubMenu(idx)`

Defined in menuweb.t, line 61

navigate into a submenu


### `formatXML(func)`

Defined in menuweb.t, line 146

Prepare a title or content string for our XML output. If 'val' is a string, we'll run it through the output formatter to expand any special <.xxx> sequences. If 'val' is a property, we'll evaluate the property of self, capturing the output if it generates any or capturing the string if it returns one. In all cases, we take the result string and convert TADS special characters to HTML, and finally html-escape the result for inclusion in XML output, and return the resulting string.


### `getChildIndex(child)`

Defined in menusys.t, line 409

get the index in the parent of the given child menu


### `getKeysXML(buf)`

Defined in menuweb.t, line 119

get the XML description of the top-level key list


### `getNextMenu(menu)`

Defined in menusys.t, line 379

Get the next menu in our list following the given menu. Returns nil if we don't find the given menu, or the given menu is the last menu.


### `getPrevMenu(menu)`

Defined in menusys.t, line 396

Get the menu previous tot he given menu. Returns nil if we don't find the given menu or the given menu is the first one.


### `getXML(from)`

Defined in menuweb.t, line 87

Package my menu items as XML, to send to the javascript API. 'from' is the menu we just navigated from, if any. This is nil when we enter the top level menu, since we're not navigating from another menu; when we navigate from a parent to a child, this is the parent; when we return from a child to a parent, this is the child; and when we move directly from sibling to sibling (via a next/previous chapter command), this is the sibling. When we display a new topic in a topic list menu, this is simply 'self'.


### `refreshTopMenuBanner(topMenu)`

Defined in menucon.t, line 486

Refresh the contents of the top bar with the instructions


### `removeStatusLine`

Defined in menucon.t, line 557

Remove the status line banner prior to displaying the menu


### `removeTopMenuBanner`

Defined in menucon.t, line 538

Remove the top banner window


### `showMenu(from)`

Defined in menuweb.t, line 48

show this menu as a submenu


### `showMenuHtml(topMenu)`

Defined in menucon.t, line 262

Show the menu using HTML. Return nil when the user selects QUIT to exit the menu entirely.


### `showMenuText(topMenu)`

Defined in menucon.t, line 129

Display the menu in plain text mode. This is used when the interpreter only supports the old tads2-style text-mode single-line status area.


### `showTopMenuBanner(topMenu)`

Defined in menucon.t, line 457

showTopMenuBanner creates the banner for the menu using the banner API. The banner contains the title of the menu on the left and the navigation keys on the right.


### `updateContents`

Defined in menusys.t, line 371

Update our contents. By default, we'll do nothing; subclasses can override this to manage dynamic menus if desired. This is called just before the menu is displayed, each time it's displayed.


## Inherited Methods


*From [MenuObject](menuobject.md):* [`addToContents`](menuobject.md#addToContents), [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`execute`](menuobject.md#execute), [`initializeContents`](menuobject.md#initializeContents), [`initializeLocation`](menuobject.md#initializeLocation)
