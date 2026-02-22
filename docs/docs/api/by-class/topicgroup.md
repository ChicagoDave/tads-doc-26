# TopicGroup

*class* — defined in [actor.t](../by-file/actor.t.md) (line 2587)


A TopicGroup is an abstract container for a set of TopicEntry objects. The purpose of the group object is to apply a common "is active" condition to all of the topics within the group.


**Superclass chain:** `object` > **TopicGroup**


## Properties


### `isActive`

Defined in actor.t, line 2593

The group "active" condition - each instance should override this to specify the condition that applies to all of the TopicEntry objects within the group.


### `matchScoreAdjustment`

Defined in actor.t, line 2600

The *adjustment* to the match score for topic entries contained within this group. This is usually a positive number, so that it boosts the match strength of the child topics.


### `topicGroupScoreAdjustment`

Defined in actor.t, line 2622

Get my score adjustment. We'll return our own basic score adjustment plus the cumulative adjustment for our containers.


## Methods


### `addSuggestedTopic(topic)`

Defined in actor.t, line 2629

add a suggested topic - we'll pass this up to our container


### `addTopic(topic)`

Defined in actor.t, line 2626

add a topic - we'll simply add the topic directly to our container


### `getTopicOwner`

Defined in actor.t, line 2606

the topic owner for any topic entries within the group is the topic owner taken from the group's own location


### `topicGroupActive`

Defined in actor.t, line 2609

are TopicEntry objects within the group active?
