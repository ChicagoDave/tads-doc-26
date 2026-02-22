# GlobalRemapping

*class* — defined in [exec.t](../by-file/exec.t.md) (line 615)


GlobalRemapping makes it possible to transform one action into another globally - as opposed to the remapTo mechanism, which lets an object involved in the command perform a remapping. The key difference between global remappings and remapTo is that the latter can't happen until after the objects are resolved (for fairly obvious reasons: each remapTo mapping is associated with an object, so you can't know which mapping to apply until you know which object is involved). In contrast, global remappings are performed *before* object resolution - this is possible because the mappings don't depend on the objects involved in the action.


**Superclass chain:** [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > `object` > **GlobalRemappingGlobal objects:** [giveMeToAskFor](givemetoaskfor.md)


## Properties


### `allGlobalRemappings`

Defined in exec.t, line 771

Static class property: the master list of remappings. We build this automatically at preinit time, and manipulate it via our constructor.


### `listNeedsSorting`

Defined in exec.t, line 778

static class property: the master list needs to be sorted; this is set to true each time we update the list, so that the list scanner knows to sort it before doing its scan


### `remappingOrder`

Defined in exec.t, line 661

Remapping order - the parser applies global remappings in ascending order of this value. In most cases, the order shouldn't matter, since most remappings should be narrow enough that a given command will only be subject to one remapping rule. However, in some cases you might need to define rules that overlap, so the ordering lets you specify which one goes first. In most cases you'll want to apply the more specific rule first.


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `construct`

Defined in exec.t, line 740

construction: add myself to the master list


### `execute` *(overridden)*

Defined in exec.t, line 733

pre-initialization: add each instance to the master list


### `findGlobalRemapping(issuingActor, targetActor, action)`

Defined in exec.t, line 678

Static class method: look for a remapping. This runs through the master list of mappings, looking for a mapping that applies to the given command. If we find one, we'll replace the command with the remapped version, then start over with a fresh scan of the entire list to see if there's a remapping for the *new* version of the command. We repeat this until we get through the whole list without finding a remapping.


### `getRemapping(issuingActor, targetActor, action)`

Defined in exec.t, line 642

Check for and apply a remapping. This method must be implemented in each GlobalRemapping instance to perform the actual remapping work.


### `registerGlobalRemapping`

Defined in exec.t, line 747

register myself with the global list, making this an active mapping


### `unregisterGlobalRemapping`

Defined in exec.t, line 761

unregister - this removes me from the global list, making this mapping inactive: after being unregistered, the parser won't apply this mapping to new commands


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
