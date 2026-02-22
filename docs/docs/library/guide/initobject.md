# InitObject

InitObject: [ModuleExecObject](moduleexecobject.md)

An InitObject is an object that contains an execute() method that is executed at the start of the game, before the first command prompt occurs. In a particular game much the same effect could be achieved by putting the code in gameMain.showIntro(), but there are occasions when you might prefer to use InitObject for a particular task, for example:

- Starting up a Daemon or Fuse, when the InitObject can conveniently be mixed-in with the Daemon or Fuse to form a single object (as in the [OneTimePromptDaemon](onetimepromptdaemon.md) example above).

- Writing code for a library extension, or code that you want to be reusable between games, for which isolating it in a separate object will be far more convenient than placing it in a game-specific gameMain.showIntro() method.

- Writing code for a custom class or object that you want to have initialize itself at startup.

Some control is possible over the order of execution of InitObjects by stipulating a list of InitObjects that must be executed before the current one in the execBeforeMe property, and a list of InitObjects that must be executed after the current one in the execAfterMe property (this mechanism is common to all ModuleExecObjects).

Note that in many cases, however, it may be better to use a [PreinitObject](preinitobject.md) for most of these purposes. One case where you *must* use an InitObject rather than a PreinitObject is when you want the object to set up a Fuse or Daemon. Your code will probably compile if you do this in a PreinitObject, but you'll find that the Fuse or Daemon is not actually set up when the game runs. Another case where you would need to use an InitObject rather than a PreinitObject is where you want its execute method to randomize something at the beginning of the game, e.g.:

```tads3
InitObject
  execute()
  {
     gameMain.villain = rand(moriarty, darthVader, presidentClark, caligula);
     gameMain.villain.moveIntoForTravel(startRoom);
  }
;
```

Although in this example there'd probably be little reason for not putting such code in gameMain.showIntro(). This might be different if we had a class of objects that we wanted to set themselves up in this sort of manner at the start of the game, e.g.:

```tads3
class PredatoryMale: Person, InitObject
  mainTargetOfDesire = nil
  execute()
  {
     mainTargetOfDesire = rand(jane, jill, sandra, mary, virginia);
  }
;
```

The fact that this might allow several predatory males to share the same main target of desire might not matter in the least in this imaginary game (although in this case we could have overridden initializeActor to achieve the same result).
