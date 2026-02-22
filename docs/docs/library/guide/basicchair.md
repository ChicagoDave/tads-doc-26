# BasicChair

BasicChair : [NestedRoom](nestedroom.md)

It is most unlikely that you would need to use the BasicChair class in your game: it would represent something you could sit on but not put anything on. However, it is important to discuss some of the features of BasicChair that are inherited by Chair, Bed and Platform, and are hence common to these classes that you most likely will use.

The important properties to note on BasicChair are:

- **allowedPostures** - a list of the postures that are allowed on this chair (out of a selection of *sitting*, *standing*, and *lying*). For a chair this is normally *sitting* and *standing*, but you could optionally disallow standing (for example, if the chair is the back seat of a car) or allow lying (for example, if the chair is a large settee). Beds and platforms also allow lying by default, but again this can be changed.

- **obviousPostures** - a list of the *obvious* postures for this object. For a chair, this would normally be just sitting, since although you can stand on a chair, this is not the obvious posture to adopt on it.

- **defaultPosture** - the posture adopted by default for this object (in the case of a chair, this would be *sitting*).
