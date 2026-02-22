# Button

Button : [Thing](thing-introduction.md)

The Button is the simplest kind of gadget class. It is simply something you can PUSH or PRESS. By default it then simply displays a message saying "Click. ", but you'll nearly always want to override this to do something else. You do so by overriding the action method of its Push handling, i.e. either

```tads3
myButton : Button 'button' 'button'
   dobjFor(Push)
   {
     action()
     {
         /* My button-push handling here */
     }
   }
;
```

Or the functionally identical but cosmetically more compact (though arguably less clear) equivalent:

```tads3
myButton : Button 'button' 'button'
   actionDobjPush
   {
         /* My button-push handling here */
   }
;
```

This is so simple that we have already used a couple of buttons: the first to open the [HiddenDoor](hiddendoor.md#smallbrownbutton) in the main cabin, and the second in the implementation of the [Autorectifying](keyedcontainer.md#orangebutton) device. We'll continue to use buttons on our various contraptions, notably on the [Tardis](dynamiclocations.md) control console, but there's no need to give another specific example here.
