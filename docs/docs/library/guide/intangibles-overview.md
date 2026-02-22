# Intangibles - Overview

Intangibles in the TADS 3 library constitute things that have some kind of presence but are not physical objects, such a light, smoke, smells and sounds. The class hierarchy for Intangible is:

```tads3
Intangible
   DistanceConnector
   SensoryEmanation
      Noise
         SimpleNoise
      Odor
         SimpleOdor
   Vaporous
```

```tads3
SenseConnector
   DistanceConnector
While we're looking at intangibles and sensory things, we'll also cover:
SensoryEvent
   SoundEvent
SoundObserver
```
