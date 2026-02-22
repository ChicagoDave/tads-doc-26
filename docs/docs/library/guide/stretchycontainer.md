# StretchyContainer

StretchyContainer : [Container](container.md)

A StretchyContainer is simply a Container that changes bulk according to its contents. An example might be a sack, which would have virtually no bulk when empty, but becomes bulkier the more is put in it. We can leave one in the squareCave, which could be used for carting things around in:

```tads3
sack : StretchyContainer 'coarse brown sack' 'coarse brown sack' @squareCave
  initSpecialDesc = "A coarse brown sack lies crumpled in the corner. "
  bulkCapacity = 30
  minBulk = 1
;
```

Presumably not even a StretchyContainer is infinitely elastic, so we give it a finite **bulkCapacity**. We can also set a **minBulk** which is the bulk of the sack when empty.

Note that if we want to find out how bulky the sack has become at any point in our game code we need to test its **getBulk()** method, not its bulk property (which never changes).
