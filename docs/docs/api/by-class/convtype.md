# ConvType

*class* — defined in [actor.t](../by-file/actor.t.md) (line 1950)


A conversational action type descriptor. This descriptor is used in handleConversation() in Actor and ActorState to describe the type of conversational action we're performing. The type descriptor object encapsulates a set of information that tells us how to handle the action.


**Superclass chain:** `object` > **ConvTypeGlobal objects:** [askAboutConvType](askaboutconvtype.md), [askForConvType](askforconvtype.md), [byeConvType](byeconvtype.md), [commandConvType](commandconvtype.md), [consultConvType](consultconvtype.md), [giveConvType](giveconvtype.md), [helloConvType](helloconvtype.md), [initiateConvType](initiateconvtype.md), [noConvType](noconvtype.md), [showConvType](showconvtype.md), [tellAboutConvType](tellaboutconvtype.md), [yesConvType](yesconvtype.md)


## Properties


### `defaultResponseProp`

Defined in actor.t, line 1969

the default response property for this action


### `topicListProp`

Defined in actor.t, line 1966

The TopicDatabase topic-list property. This is the property of the TopicDatabase object that we evaluate to get this list of topic entries to search for a match to the topic.


### `unknownMsg`

Defined in actor.t, line 1959

The unknown interlocutor message property. This is used when we try this conversational action without knowing whom we're talking to. For example, if we just say HELLO, and there's no one around to talk to, we'll use this as the default response. This can be a library message property, or simply a single-quoted string to display.


## Methods


### `afterResponse(actor, otherActor)`

Defined in actor.t, line 1984

Perform any special follow-up action for this type of conversational action.


### `defaultResponse(db, otherActor, topic)`

Defined in actor.t, line 1978

Call the default response property on the given topic database. This invokes the property given by defaultResponseProp(). We have both the property and the method to call the property because this allows us to test for the existence of the property and to call it with the appropriate argument list.
