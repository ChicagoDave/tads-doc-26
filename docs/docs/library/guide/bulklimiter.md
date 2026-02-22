# BulkLimiter

BulkLimiter : [Thing](thing-thebasics.md)

BulkLimiter is the common base class for containers and surfaces: things that have limited bulk capacities. You probably won't have cause to use this class directly; you'll usually use subclasses such as [Surface](surface.md) and [Container](container.md) instead.

BulkLimiter defines the following properties that are inherited by its subclasses:

- **bulkCapacity** - the total aggregate bulk that can be contained in this object (by default, 10000).

- **maxSingleBulk** - the maximum bulk that any individual item inserted into the BulkLimiter may have (by default 10).

- **revealHiddenItems** - a flag that determines whether any Hidden items will be revealed when this BulkLimiter's interior is examined (i.e. when look in, under, or behind will cause the discover method of any item of class [Hidden](hidden.md) to be called). By default this is true, representing the fact that when we look in, under or behind something we normally see what was there even if we didn't before we looked; if desired this can be set to nil so that [Hidden](hidden.md) items remain hidden.

- **tooFullMsg** - The message that is displayed when adding a new object would exceed the BulkLimiter's bulkCapacity. This may be overridden on subclasses.

- **becomingTooFullMsg** - the message property to use when doing something to one of our contents would cause our overall contents to exceed our capacity.

- **becomingTooLargeMsg** - the message property to use when doing something to one of our contents would make it too large to fit all by itself into this container (that is, it would cause that object's bulk to exceed our maxSingleBulk).

BulkLimiter also overrides the [notifyInsert()](notifyinsert+notifyremove.md) method to check whether an object will fit into BulkContainer (which it won't if either the aggregate bulkCapacity or the individual maxSingleBulk would be exceeded by the insertion).
