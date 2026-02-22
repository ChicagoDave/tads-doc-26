# Flashlight

Flashlight : [LightSource](lightsource.md), [Switch](switch.md)

A Flashlight is basically a LightSource with a switch that can be used to turn it on and off (just like a flashlight or, as we'd call it in Britain, a torch).

```tads3
blackTorch : Flashlight 'large black flashlight/torch' 'large black torch' @mainCave
  "It looks a serious heavy-duty instrument, with a firm ridged grip and
   a powerful bulb. "
   brightnessOn = 4
   bulk = 2
   weight = 2
;
```

There's no particular reason for setting brightnessOn to 4 here, other than the fact that it's described as a powerful torch and to demonstrate that it can be done. You can try this torch/flashlight out if you like, but we won't be leaving it lying around in mainCave for the player to pick up so easily. Instead we'll put in a storage cabinet aboard the Tardis:

```tads3
tardisLivingQuarters : ShipboardRoom 'Tardis Living Quarters' 'the living quarters'
  "These living quarters are pretty bare right now, but there is a storage cabinet
   fixed to one wall, and a door that leads out. "
  out = tardisLivingQuartersDoor
  fore asExit(out)
;
OpenableContainer, Fixture 'storage cabinet' 'storage cabinet' @tardisLivingQuarters
  "The large cabinet is painted a cream colour and looks securely fixed to the wall. "
;
+ blackTorch : Flashlight 'large black flashlight/torch' 'large black torch'
  "It looks a serious heavy-duty instrument, with a firm ridged grip and
   a powerful bulb. "
   brightnessOn = 4
   bulk = 2
   weight = 2
;
```

This, of course, leaves players with the problem of finding an alternative light source before they can reach the Tardis. We'll deal with that next.
