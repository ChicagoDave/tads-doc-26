# Goal

*class* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 105)


A Goal represents an open task: something that the player is trying to achieve. A Goal is an abstract object, not part of the simulated world of the game.


**Superclass chain:** [MenuTopicItem](menutopicitem.md) > [MenuItem](menuitem.md) > [MenuObject](menuobject.md) > `object` > [HintMenuObject](hintmenuobject.md) > **Goal**


## Properties


### `closeWhen`

Defined in hintsys.t, line 247

Determine if there's any condition that should close this goal. We'll check closeWhenSeen, closeWhenDescribed, and all of the other closeWhenXxx conditions; if any of these return true, then we'll return true.


### `closeWhenAchieved`

Defined in hintsys.t, line 181

An optional Achievement object that closes this goal. Once the achievement is completed, this goal's state will automatically be set to Closed. This makes it easy to associate the goal with a puzzle: once the puzzle is solved, there's no need to show hints for the goal any more.


### `closeWhenDescribed`

Defined in hintsys.t, line 162

close the goal when the given object is described


### `closeWhenKnown`

Defined in hintsys.t, line 193

an optional Topic or Thing that closes this goal when known


### `closeWhenRevealed`

Defined in hintsys.t, line 203

an optional <.reveal> tag that closes this goal when revealed


### `closeWhenSeen`

Defined in hintsys.t, line 153

An option object that, when seen by the player character, closes this goal. Many goals will be things like "how do I find the X?", in which case it's nice to close the goal when the X is found.


### `closeWhenTrue`

Defined in hintsys.t, line 215

an optional general-purpose check that closes the goal


### `goalFullyDisplayed`

Defined in hintsys.t, line 271

Has this goal been fully displayed? The hint system automatically sets this to true when the last item in our hint list is displayed.


### `goalState`

Defined in hintsys.t, line 348

This goal's current state. We'll start off undiscovered. When a goal should be open from the very start of the game, this should be overridden and set to OpenGoal.


### `isActiveInMenu`

Defined in hintsys.t, line 341

we're active in our parent menu if our goal state is Open


### `location`

Defined in hintsys.t, line 120

Our parent menu - this is usually a HintMenu object. In very simple hint systems, this could simply be a top-level hint menu container; more typically, the hint system will be structured into a menu tree that organizes the hint topics into several different submenus, for easier navigatino.


### `menuContents` *(overridden)*

Defined in hintsys.t, line 134

The list of hints for this topic. This should be ordered from most general to most specific; we offer the hints in the order they appear in this list, so the earlier hints should give away as little as possible, while the later hints should get progressively closer to just outright giving away the answer.


### `openWhen`

Defined in hintsys.t, line 233

Determine if there's any condition that should open this goal. This checks openWhenSeen, openWhenDescribed, and all of the other openWhenXxx conditions; if any of these return true, then we'll return true.


### `openWhenAchieved`

Defined in hintsys.t, line 172

An optional Achievement object that opens this goal. This goal will be opened automatically once the goal is achieved, if the goal was previously undiscovered. This makes it easy to set up a hint topic that becomes available after a particular puzzle is solved, which is useful when a new puzzle only becomes known to the player after a gating puzzle has been solved.


### `openWhenDescribed`

Defined in hintsys.t, line 159

this is like openWhenSeen, but opens the topic when the given object is described (with EXAMINE)


### `openWhenKnown`

Defined in hintsys.t, line 190

An optional Topic or Thing that opens this goal when the object becomes "known" to the player character. This will open the goal as soon as gPlayerChar.knowsAbout(openWhenKnown) returns true. This makes it easy to open a goal as soon as the player comes across some information in the game.


### `openWhenRevealed`

Defined in hintsys.t, line 200

An optional <.reveal> tag name that opens this goal. If this is set to a non-nil string, we'll automatically open this goal when the tag has been revealed via <.reveal> (or gReveal()).


### `openWhenSeen`

Defined in hintsys.t, line 145

An optional object that, when seen by the player character, opens this goal. It's often convenient to declare a goal open as soon as the player enters a particular area or has encountered a particular object. For such cases, simply set this property to the room or object that opens the goal, and we'll automatically mark the goal as Open the next time the player asks for a hint after seeing the referenced object.


### `openWhenTrue`

Defined in hintsys.t, line 212

An optional arbitrary check that opens the goal. If this returns true, we'll open the goal. This check is made in addition to the other checks (openWhenSeen, openWhenDescribed, etc). This can be used for any custom check that doesn't fit into one of the standard openWhenXxx properties.


### `title` *(overridden)*

Defined in hintsys.t, line 111

The topic question associated with the goal. The hint system shows a list of the topics for the goals that are currently open, so that the player can decide what area they want help on.


## Inherited Properties


*From [MenuTopicItem](menutopicitem.md):* [`chunkSize`](menutopicitem.md#chunkSize), [`heading`](menutopicitem.md#heading), [`lastDisplayed`](menutopicitem.md#lastDisplayed), [`menuTopicListEnd`](menutopicitem.md#menuTopicListEnd), [`nextMenuTopicLink`](menutopicitem.md#nextMenuTopicLink)


*From [MenuItem](menuitem.md):* [`bgcolor`](menuitem.md#bgcolor), [`curKeyList`](menuitem.md#curKeyList), [`curMenu`](menuitem.md#curMenu), [`fgcolor`](menuitem.md#fgcolor), [`fullScreenMode`](menuitem.md#fullScreenMode), [`indent`](menuitem.md#indent), [`isOpen`](menuitem.md#isOpen), [`keyList`](menuitem.md#keyList), [`prevMenuLink`](menuitem.md#prevMenuLink), [`topbarbg`](menuitem.md#topbarbg), [`topbarfg`](menuitem.md#topbarfg), [`topMenu`](menuitem.md#topMenu)


*From [MenuObject](menuobject.md):* [`contents`](menuobject.md#contents), [`menuOrder`](menuobject.md#menuOrder)


*From [HintMenuObject](hintmenuobject.md):* [`topicOrder`](hintmenuobject.md#topicOrder)


## Methods


### `displaySubItem(idx, lastBeforeInput, eol)` *(overridden)*

Defined in hintsys.t, line 330

display a sub-item, keeping track of when we've shown them all


### `updateContents` *(overridden)*

Defined in hintsys.t, line 299

Check our menu state and update it if necessary. Each time our parent menu is about to display, it'll call this on its sub-items to let them update their current states. This method can promote the state to Open or Closed if the necessary conditions for the goal have been met.


## Inherited Methods


*From [MenuTopicItem](menutopicitem.md):* [`getNextTopicXML`](menutopicitem.md#getNextTopicXML), [`getTopicXML`](menutopicitem.md#getTopicXML), [`getXML`](menutopicitem.md#getXML), [`redrawWinHtml`](menutopicitem.md#redrawWinHtml), [`showMenuHtml`](menutopicitem.md#showMenuHtml), [`showMenuText`](menutopicitem.md#showMenuText)


*From [MenuItem](menuitem.md):* [`display`](menuitem.md#display), [`enterSubMenu`](menuitem.md#enterSubMenu), [`formatXML`](menuitem.md#formatXML), [`getChildIndex`](menuitem.md#getChildIndex), [`getKeysXML`](menuitem.md#getKeysXML), [`getNextMenu`](menuitem.md#getNextMenu), [`getPrevMenu`](menuitem.md#getPrevMenu), [`refreshTopMenuBanner`](menuitem.md#refreshTopMenuBanner), [`removeStatusLine`](menuitem.md#removeStatusLine), [`removeTopMenuBanner`](menuitem.md#removeTopMenuBanner), [`showMenu`](menuitem.md#showMenu), [`showTopMenuBanner`](menuitem.md#showTopMenuBanner)


*From [MenuObject](menuobject.md):* [`addToContents`](menuobject.md#addToContents), [`compareForMenuSort`](menuobject.md#compareForMenuSort), [`execute`](menuobject.md#execute), [`initializeContents`](menuobject.md#initializeContents), [`initializeLocation`](menuobject.md#initializeLocation)


*From [HintMenuObject](hintmenuobject.md):* [`compareForTopicSort`](hintmenuobject.md#compareForTopicSort)
