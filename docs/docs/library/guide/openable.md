# Openable

Openable: [BasicOpenable](basicopenable.md)

Most objects that are lockable are also likely to be openable - after all, there's not a lot of point in locking or unlocking an object that can't be open or closed. However, since most of the objects that are openable and closable tend to be container-like objects or door-like objects, in practice one tends to use classes like [Door](door.md) and [OpenableContainer](openablecontainer.md) rather more than a bare Openable. We are not yet ready to introduce an example of a bare Openable in our test game, but there is one later, the [tardisPanel](presentlater.md)object.

The Openable class inherits all the behaviour of [BasicOpenable](basicopenable.md) and the mainly adds handling (or at least additional preconditions) for a number of common verbs (OPEN, CLOSE, PUT IN, POUR INTO, LOCK, LOCK WITH, GET OUT OF, and BOARD).

Openable also defines **lockStatusReportable** to be (!isOpen); for a fuller explanation see [Lockable](lockable.md). Finally it defines an **openStatus**() method which returns a sentence like "it's open" or "it's closed" (without punctuation) which can be added to the description of an object to indicate whether it's open or closed. The library defaults are usually fine, but you may, for example, want to suppress "it's closed" either for aesthetic reasons or to disguise the fact that something is openable, in which case you might write something like:

`openStatus { return isOpen ? inherited : ''; }`

If you do that, however, the punctuation will look a bit wayward when the object is closed, so you also have to tweak the description of the object from something like:

`"It's red and square. "`

To

`"It's red and square"`

And then write your openStatus method thus:

```tads3
 openStatus = (isOpen ? ' . It\'s open' : '')
```

Note that the final full stop (or period) and space have been removed from the end of the object description and added instead to the start of the "It's open" message.
