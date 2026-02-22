# TopicActionBase

*class* — defined in [action.t](../by-file/action.t.md) (line 5517)


Base class for actions that include a "topic" phrase. This is a mix-in class that can be used in different types of topic actions. In all cases, the topic phrase must be assigned to the 'topicMatch' property in grammar rules based on this class.


**Superclass chain:** `object` > **TopicActionBase**


<details><summary>Subclasses (21)</summary>

- [TopicAction](topicaction.md)
- [TopicTAction](topictaction.md)
- [AskVagueAction](askvagueaction.md)
- [predicate(AskVague)](predicate%28askvague%29.md)
- [predicate(TellVague)](predicate%28tellvague%29.md)
- [ConsultAboutAction](consultaboutaction.md)
- [predicate(ConsultAbout)](predicate%28consultabout%29.md)
- [predicate(ConsultWhatAbout)](predicate%28consultwhatabout%29.md)
- [ConvTopicTAction](convtopictaction.md)
- [AskAboutAction](askaboutaction.md)
- [predicate(AskAbout)](predicate%28askabout%29.md)
- [predicate(AskAboutImplicit)](predicate%28askaboutimplicit%29.md)
- [predicate(AskAboutWhat)](predicate%28askaboutwhat%29.md)
- [AskForAction](askforaction.md)
- [predicate(AskFor)](predicate%28askfor%29.md)
- [predicate(AskWhomFor)](predicate%28askwhomfor%29.md)
- [TellAboutAction](tellaboutaction.md)
- [predicate(TellAbout)](predicate%28tellabout%29.md)
- [predicate(TellAboutImplicit)](predicate%28tellaboutimplicit%29.md)
- [predicate(TellAboutWhat)](predicate%28tellaboutwhat%29.md)
- [TellVagueAction](tellvagueaction.md)

</details>


## Properties


### `topicList_`

Defined in action.t, line 5708

the resolved topic object list


### `topicQualResolver_`

Defined in action.t, line 5705

the topic qualifier resolver


### `topicResolver_`

Defined in action.t, line 5711

my cached topic resolver


## Methods


### `createTopicResolver(issuingActor, targetActor)`

Defined in action.t, line 5645

Create the topic resolver.


### `getMessageParam(objName)`

Defined in action.t, line 5657

Get a message parameter by name. We'll return the topic for the keyword 'topic', and inherit the default handling for anything else.


### `getTopic`

Defined in action.t, line 5672

get the current topic


### `getTopicQualifierResolver(issuingActor, targetActor, reset)`

Defined in action.t, line 5689

Get the resolver for qualifiers we find in the topic phrase (qualifiers that might need resolution include things like possessive adjectives and locational phrases).


### `getTopicResolver(issuingActor, targetActor, reset)`

Defined in action.t, line 5628

get the topic resolver


### `reparseMatchAsTopic(topic, issuingActor, targetActor)`

Defined in action.t, line 5588

Re-parse a match tree as a topic phrase. Returns a TopicProd match tree, if possible.


### `resolveTopic(issuingActor, targetActor, results)`

Defined in action.t, line 5523

Resolve the topic phrase. This resolves the match tree in out 'topicMatch' property, and stores the result in topicList_. This is for use in resolveNouns().


### `setResolvedTopic(topic)`

Defined in action.t, line 5539

Set the resolved topic to the given object list. This is for use in setResolvedObjects().


### `setTopicMatch(topic)`

Defined in action.t, line 5555

Set the topic match tree. This is for use in setObjectMatches().
