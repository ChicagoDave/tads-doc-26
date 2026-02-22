# KeyedContainer

KeyedContainer : [LockableWithKey](lockablewithkey.md), [OpenableContainer](openablecontainer.md)

A KeyedContainer is a Container that can be opened and closed, and also locked and unlocked with a key. As an example we'll put a large, heavy trunk in mainCave:

```tads3
trunk : KeyedContainer, Heavy 'large black trunk' 'large black trunk' @mainCave
  initSpecialDesc = "A large black trunk rests in the middle of the cave. "
  initiallyLocked = true
  keyList = [brassKey]
;
```

Note that we have to set **initiallyLocked** to true if we want the trunk to start locked, and that **keyList** needs to be set to the list of keys that can lock and unlock this container. Clearly, we also need to define the key, which is entirely straightforward:

```tads3
brassKey : Key 'small brass key' 'brass key' @roundCave;
```

Note that even if it is listed in another objects' keyList, to function as a key an object must be of class Key and not simply Thing; the Key class contains a number of specializations, of which the most important is overriding verifyIobjLockWith() and verifyIobjUnlockWith() to make it logical (which implies possible) for a Key to be used as the indirect object of these commands.

The trunk will obviously be more interesting if there's something inside when it's opened, so let's put the glass jar and the fake golden banana inside:

```tads3
fakeTreasure : Thing 'huge great golden gold banana/treasure'
    'golden banana' @trunk
   ...
;
glassJar : BasicContainer 'glass jar' 'glass jar' @trunk
   ...
;
```

You'll also need to delete fakeTreasure's initSpecialDesc, which is no longer appropriate.

<a name="bentkey"></a>
```tads3
trunk : KeyedContainer, Heavy 'large black trunk' 'large black trunk' @mainCave
  initSpecialDesc = "A large black trunk rests in the middle of the cave. "
  initiallyLocked = true
  keyList = [brassKey]
  lockOrUnlockAction(lock)
  {
    if(gIobj.isBent)
       reportFailure('{The iobj/he} fits the lock but won\'t quite turn in it. ');
    else
      inherited(lock);
  }
;
brassKey : Key 'small brass key' 'brass key' @roundCave
  "It<<isBent ? ' looks slightly bent' : '\'s been straightened'>>. "
  isBent = true
;
```

We now need to find a way to straighten the brass key so that it'll open the trunk. Among things players might try is hitting the key with various objects, or trying to put in the flame of the torch, and we should probably provide suitable responses to such attempts or even make some of them work. But for now, we'll adopt a more exotic solution, a futuristic Autorectifier (a device that straightens any bent device placed in it), which will eventually be discovered aboard a space station (once we've constructed the space station and a means of getting there). We've already defined the basic cylinder that's the core of the device, here's the complete definition along with its components:

```tads3
autoRectifier : ComplexContainer 'silver cylinder' 'silver cylinder' @mainCave
  "It's about a foot high and five inches in diameter. A black ring surrounds
   the opening at one end. The only other feature of interest are a conspicuous
   orange button and the manufacturer's name inscribed just below the ring. "
   subContainer : ComplexComponent, SingleContainer {  bulkCapacity = 3 }
   bulk = 4
   weight = 3
;
+ Component 'black ring' 'black ring'
  "The black ring appears to made of some kind of rubbery plastic, but the material
   is unfamiliar to you, as is its function. "
;
+ Component 'manufacturer\'s name' 'manufacturer\'s name'
  "According to the inscription this device was manufactured
   by ALDEBARAN AUTORECTIFIERS INTERPLANETARY CORP."
;
+ Button, Component 'orange button' 'orange button'
  "It's a large round button on one side of the cylinder. "
  dobjFor(Push)
  {
    action()
    {
      "When you push the button the cylinder starts to hum, and its interior glows
       with a light that starts orange, then changes to yellow, then finally
       a dazzling white, as the hum steadily rises in pitch. Suddenly the hum
       stops and the light inside goes out. ";
       foreach(local cur in autoRectifier.subContainer.contents)
           if(cur.isBent) cur.isBent = nil;
    }
  }
;
```

Note how we specify the contents of the cylinder in the button's actionDobjPush method, and that this method will set isBent to nil on anything placed in the cylinder (if it is not nil already); this will allow the device to be usable on any other bent objects we care to introduce into the game.
