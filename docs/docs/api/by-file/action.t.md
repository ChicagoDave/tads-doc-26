# action.t


## Classes

- [Action](../by-class/action.md)
- [ActionRemappingTooComplexError](../by-class/actionremappingtoocomplexerror.md)
- [AllAction](../by-class/allaction.md)
- [ConvIAction](../by-class/conviaction.md)
- [ConvTopicResolver](../by-class/convtopicresolver.md)
- [ConvTopicTAction](../by-class/convtopictaction.md)
- [DefaultAction](../by-class/defaultaction.md)
- [IAction](../by-class/iaction.md)
- [LiteralAction](../by-class/literalaction.md)
- [LiteralActionBase](../by-class/literalactionbase.md)
- [LiteralTAction](../by-class/literaltaction.md)
- [PreCondDesc](../by-class/preconddesc.md)
- [ResolvedTopic](../by-class/resolvedtopic.md)
- [SystemAction](../by-class/systemaction.md)
- [TAction](../by-class/taction.md)
- [TActionTopicResolver](../by-class/tactiontopicresolver.md)
- [TentativeResolveResults](../by-class/tentativeresolveresults.md)
- [TIAction](../by-class/tiaction.md)
- [TopicAction](../by-class/topicaction.md)
- [TopicActionBase](../by-class/topicactionbase.md)
- [TopicResolver](../by-class/topicresolver.md)
- [TopicTAction](../by-class/topictaction.md)


## Global Objects

- [dummyTentativeInfo](../by-class/dummytentativeinfo.md)
- [dummyTentativeObject](../by-class/dummytentativeobject.md)
- [objectRelations](../by-class/objectrelations.md)
- [resolvedTopicNothing](../by-class/resolvedtopicnothing.md)
- callRoomAfterAction
- callRoomBeforeAction
- withParserGlobals


## Functions


### `callRoomAfterAction(room)`

Defined in action.t, line 2995

Call the roomAfterAction method on a given room, then on the room's containing rooms.


### `callRoomBeforeAction(room)`

Defined in action.t, line 2982

Call the roomBeforeAction method on a given room's containing rooms, then on the room itself.


### `withParserGlobals(issuer, actor, action, func)`

Defined in action.t, line 89

Invoke the given function with the given values for the parser global variables gActor and gAction.
