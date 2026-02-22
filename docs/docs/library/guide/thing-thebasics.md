# Thing - The Basics

The basic properties that apply to almost all Thing objects (and objects using many of the classes inheriting from Thing) are vocabWords, name, location, and desc. These are so common the standard [Thing template](thingtemplate.md) allows them to be defined without naming them, thus:

```tads3
myObject : Thing 'vocabWords_' 'name' @location
   "desc"
;
```

And for the most basic portable objects, this type of definition will often suffice without the need to define any other properties or methods. For example, we shall leave a coin for the player to find in the longCave room (using the [Thing template](thingtemplate.md)):

```tads3
brassCoin : Thing '(small) brass coin/groat*coins' 'small brass coin' @longCave
  "On the obverse is the head of King Freddie the Fat, and on the reverse
   is stamped ONE GROAT. "
;
```

By now, most of these properties should be familiar. The **desc** (description) property is what is displayed in response to an EXAMINE command; the only real complication is that you may sometimes want to define desc as a *method*, in which case it must be explicitly defined as a named method outside the template.

The **name** property is the what will normally appear when the object is listed in the contents of rooms, containers or inventory, or when the parser needs to refer to the object (E.g. "Which coin do you mean, the brass coin or the gold coin?").

For a Thing the **location** is normally the object's physical container, which may be a room, an actor (including the Player Character) who is carrying or wearing the object, or some other form of physical container (such as a jar or the top surface of a table). The location can also be specified by using the + notation; e.g. to put the coin in longCave we could have written

```tads3
longCave : DarkRoom 'Long Cave' ...
  ...
;
```

```tads3
+ brassCoin : Thing '(small) brass coin/groat*coins' 'small brass coin'
  "On the obverse is the head of King Freddie the Fat, and on the reverse
   is stamped ONE GROAT. "
;
```

Note that if both the + notation and the @location notation are used on the same object, the + notation takes precedence. But if the + notation is used with an explicit setting of the location property, the explicitly named location property takes precedence. For example, in the case of the brassCoin with the + notation, if I added `@entranceCave` to the object definition after 'brass coin' the coin would remain in longCave, but if I added `location=entranceCave` the brass coin would start life in the entranceCave, despite the + property. This can sometimes be useful if you have a sequence of objects nested within one another using the + notation and you want to define an object that doesn't belong in the containment hierarchy amongst those that do.

Note also that if location is an expression or method, it must be explicitly defined as a named property outside the template, e.g. `location = (ship.location)`

The [vocabWords](vocabwords.md) property is perhaps the most complex of the four, so we shall discuss it in a separate section.
