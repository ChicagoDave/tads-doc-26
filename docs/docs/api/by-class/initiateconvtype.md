# initiateConvType

*object* — defined in [actor.t](../by-file/actor.t.md) (line 2074)


This type is for NPC-initiated conversations. It's not a normal conversational action, since it doesn't involve handling a player command, but is usually instead triggered by an agenda item, takeTurn(), or other background activity.


**Superclass chain:** [ConvType](convtype.md) > `object` > **initiateConvType**


## Properties


### `topicListProp` *(overridden)*

Defined in actor.t, line 2075


## Inherited Properties


*From [ConvType](convtype.md):* [`defaultResponseProp`](convtype.md#defaultResponseProp), [`unknownMsg`](convtype.md#unknownMsg)


## Inherited Methods


*From [ConvType](convtype.md):* [`afterResponse`](convtype.md#afterResponse), [`defaultResponse`](convtype.md#defaultResponse)
