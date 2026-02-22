# HintMenu

HintMenu : MenuItem, HintMenuObject

Unless your hint system is going to be very simple, you'll probably want to split it into submenus. To do this you use a series of HintMenu objects, which would be located directly in the [TopHintMenu](tophintmenu.md). In the present game we might do this by splitting the hints according to region:

```tads3
TopHintMenu;
+ HintMenu 'In the First Set of Caves'
;
+ HintMenu 'Aboard the ship'
;
+ HintMenu 'The Tardis and its Destinations'
;
+ HintMenu 'On the East Side of the Lake'
;
+ HintMenu 'On the South Side of the Lake'
;
+ HintMenu 'On the West Side of the Lake'
;
```

Note that the Menu template defines the single-quoted string as the title property, so, for example, our first HintMenu could have been defined as:

```tads3
+ HintMenu
    title = 'In the First Set of Caves'
;
```

Note also that each of these menus is only displayed if it contains currently open goals.
