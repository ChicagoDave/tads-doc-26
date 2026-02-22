# ExitPortal

ExitPortal : [Exitable](shipboardroom.md#leaveship)

An ExitPortal is just like an [Exitable](shipboardroom.md#leaveship), except that you can go through it as well as exit it. For example:

```tads3
squareCave : DarkRoom 'Square Cave' 'the square cave'
   "This capacious cave is unnaturally square, suggesting that it has been
    artificially hewn out of the rock, an impression further enhanced by
    the carefully-constructed ashlar archway to the west. "
   west = mainCave
   out asExit(west)
;
+ ExitPortal -> mainCave 'ashlar arch/archway' 'archway'
  "The archway is beautifully constructed from dressed stones. "
;
```

Note that ExitPortal is *not* a travel connector; -> mainCave makes mainCave its connector property, not its masterObject property. For the distinction, see further on the [Enterable](enterable.md) class. The template used here is the [Exitable template](exitabletemplate.md).
