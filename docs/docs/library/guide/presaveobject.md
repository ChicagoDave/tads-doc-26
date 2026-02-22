# PreSaveObject

PreSaveObject: [ModuleExecObject](moduleexecobject.md)

PreSaveObject - every instance of this class is notified, via its execute() method, just before we save the game. This provides a convenient way to make something happen just before our game is saved. The need for this may not arise very often, but if it should arise it's probably more convenient to define a PreSaveObject than to tinker about trying to modify SaveAction or something it calls.

For example, an author really determined to earn the wrath and indignation of his players might write:

```tads3
PreSaveObject
  execute()
  {
     "You pathetically pusillanimous poltroon! <i>Real</i> adventurers don't need to save!
      To penalize you for this cowardly inanity ten thousand points will be instantly
      deducted from your score.<.p>";
      addToScore(-10000, 'saving the game');
  }
;
```

Of course, we don't recommend you follow such an author's example!
