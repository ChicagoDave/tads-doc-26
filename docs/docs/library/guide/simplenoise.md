# SimpleNoise

SimpleNoise : [Noise](noise.md)

SimpleNoise is simply the sonic equivalent of [SimpleOdor](simpleodor.md). Everything that applies to the one applies to the other, except for the obvious difference that a SimpleNoise response to LISTEN or LISTEN TO SOMETHING commands rather than SMELL and SMELL SOMETHING commands.

Having taken SimpleOdor through its paces and exercised it every which way, one simple example of a SimpleNoise should suffice. Add the following directly after the definition of the cavernEntrance object:

```tads3
++ SimpleNoise 'intermittent muffled deep rumbling sound/sounds' 'sound'
  "An intermittent and slightly muffled deep rumbling echoes through the cavern entrance. "
;
```

In this case there seems to be no need to attach this sound to the red glow as well (one might conceivably smell the glow, but one would not expect to hear it), and besides there is no need to go over essentially the same theme and variations in a closely related key. For more sophisticated sounds, though, you might want to consider using the Noise class.
