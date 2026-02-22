# Bed

Bed : BasicBed, [Surface](surface.md)

A Bed is simply a NestedRoom an actor can lie on (or sit on). The likely place for a bed is in a bedroom, and as we'll need to pay King Solomon a visit sometime to collect his legendary purple carbuncle (no you won't find it mentioned in the Bible, but we can always imagine that it's one of the precious stones the Queen of Sheba gave him at 1 Kings 10.10) it may as well be his bedroom.

```tads3
solomonBedroom : Room 'Bedroom' 'the bedroom'
  "This large, square bedchamber is panelled in cedar, with a non-glazed window
   looking out to the north, and a large bed against the east wall. A door leads
   out to the west. "
  west = solBedroomDoor
  out asExit(west)
;
+ solBedroomDoor : Door 'bedroom cedar door' 'bedroom door'
  "It's made of cedar. "
;
+ Bed, Heavy 'large bed' 'large bed'
  "It has a cedar frame and an unsprung mattress. "
;
+ Fixture 'window' 'window'
  "The window is basically an opening in the north wall, comprising
   two rectangular sections each with curved tops. It is unglazed. "
  dobjFor(LookThrough)
  {
    action()
    {
     "The window overlooks a building site where a large team of workers
      are constructing a small temple. ";
    }
  }
;
```
