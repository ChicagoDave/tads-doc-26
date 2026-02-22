# TopHintMenu

TopHintMenu : [HintMenu](hintmenu.md), PreinitObject

TopHintMenu is a class which defines the top of your hints menu tree. You use it to create an object in which to nest the rest of your hint system, and the library will automatically register it as the root of your hint menus.

In the file where you're going to create your hint system, simply define:

```tads3
TopHintMenu 'Hints';
```
