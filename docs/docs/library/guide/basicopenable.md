# BasicOpenable

BasicOpenable: Linkable

BasicOpenable is the base class for openable items. It defines the basic behaviour for objects that can be opened and closed, but no special handling for commands (such as OPEN and CLOSE) that might commonly be used for openable objects. It is much more likely that you will use subclasses of BasicOpenable (such as [Openable](openable.md), [BasicDoor](basicdoor.md) and their subclasses) than BasicOpenable in game code. It is conceivable that you might want to subclass a custom kind of openable object from BasicOpenable, as it is conceivable that you might want to implement a BasicOpenable object in a game for an object that can be open and closed but not does respond to normal opening and closing commands (e.g. because it can only be opened and closed by pushing a button or pulling a lever), but these are left as exercises for the interested reader. The chief importance of BasicOpenable is that if defines the behaviour common to all its descendants. The important properties and methods to know about are:

- **initiallyOpen**: set this to true if you want the object to start out open. The default is nil.

- **isOpen()**: use this method to determine whether the object is open (true) or closed (nil), but do not overwrite this property in game code to make an object open or closed; call makeOpen instead.

- **makeOpen(stat)**: call this method to open or close the object programmatically, by calling makeOpen(true) or makeOpen(nil). You can also override this method to bring about additional side-effects of opening or closing the object, but if you do so be sure to remember to call inherited(stat) somewhere in your overridden makeOpen(stat).

- **openDesc()**: the method/property that provides an additional description to say whether the object is open or closed; the English library defaults are "open" and "closed", which are good enough for most purposes.
