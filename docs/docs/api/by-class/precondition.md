# PreCondition

*class* — defined in [precond.t](../by-file/precond.t.md) (line 23)


An action pre-condition object. Each condition of an action is represented by a subclass of this class.


**Superclass chain:** `object` > **PreConditionSubclasses:** [ObjectPreCondition](objectprecondition.md), [ObjOpenCondition](objopencondition.md), [SameLocationCondition](samelocationcondition.md), [TouchObjCondition](touchobjcondition.md), [TravelerDirectlyInRoom](travelerdirectlyinroom.md)


**Global objects:** [actorDirectlyInRoom](actordirectlyinroom.md), [actorReadyToEnterNestedRoom](actorreadytoenternestedroom.md), [actorStanding](actorstanding.md), [actorTravelReady](actortravelready.md), [canTalkToObj](cantalktoobj.md), [dropDestinationIsOuterRoom](dropdestinationisouterroom.md), [nearbyAttachableCond](nearbyattachablecond.md), [objAudible](objaudible.md), [objBurning](objburning.md), [objClosed](objclosed.md), [objEmpty](objempty.md), [objHeld](objheld.md), [objNotAttached](objnotattached.md), [objNotWorn](objnotworn.md), [objSmellable](objsmellable.md), [objUnlocked](objunlocked.md), [objVisible](objvisible.md), [roomToHoldObj](roomtoholdobj.md)


## Properties


### `preCondOrder`

Defined in precond.t, line 67

Precondition execution order. When we execute preconditions for a given action, we'll sort the list of all applicable preconditions in ascending execution order.


## Methods


### `checkPreCondition(obj, allowImplicit)`

Defined in precond.t, line 36

Check the condition on the given object (which may be nil, if this condition doesn't apply specifically to one of the objects in the command). If it is possible to meet the condition with an implicit command, and allowImplicit is true, try to execute the command. If the condition cannot be met, report a failure and use 'exit' to terminate the command.


### `verifyPreCondition(obj)`

Defined in precond.t, line 54

Verify the condition. This is called during the object verification step so that the pre-condition can add verifications of its own. This can be used, for example, to add likelihood to objects that already meet the condition. Note that it is generally not desirable to report illogical for conditions that checkPreCondition() enforces, because doing so will prevent checkPreCondition() from ever being reached and thus will prevent checkPreCondition() from attempting to carry out implicit actions to meet the condition.
