# ResolvedTopic

*class* — defined in [action.t](../by-file/action.t.md) (line 6117)


Resolved Topic object. The topic of a TopicTAction always resolves to one of these objects.


**Superclass chain:** `object` > **ResolvedTopicGlobal objects:** [resolvedTopicNothing](resolvedtopicnothing.md)


## Properties


### `canMatchLiterally`

Defined in action.t, line 6260

Are we allowed to match the topic text literally, for parsing purposes? If this is true, it means that we can match the literal text the player entered against strings, regular expressions, etc.; for example, we can match a TopicMatchTopic's matchPattern regular expression. If this is nil, it means that we can only interpret the meaning of the resolved topic by looking at the various topic match lists (inScopeList, likelyList, otherList).


### `inScopeList`

Defined in action.t, line 6291

Our lists of resolved objects matching the topic phrase, separated by classification.


### `likelyList`

Defined in action.t, line 6292


### `otherList`

Defined in action.t, line 6293


### `resInfoTab`

Defined in action.t, line 6310

ResolveInfo table for the resolved objects. This is a lookup table indexed by simulation object. Each entry in the resolved object lists (inScopeList, etc) has have a key in this table, with the ResolveInfo object as the value for the key. This can be used to recover the ResolveInfo object describing the parser results for this object.


### `topicProd`

Defined in action.t, line 6300

The production match tree object that matched the topic phrase in the command. This can be used to obtain the original tokens of the command or the original text of the phrase.


## Methods


### `canMatchObject(obj)`

Defined in action.t, line 6228

Is the given object among the possible matches for the topic?


### `construct(inScope, likely, others, prod)`

Defined in action.t, line 6118


### `getBestMatch`

Defined in action.t, line 6204

Get the best object match to the topic. This is a default implementation that can be changed by game authors or library extensions to implement different topic-matching strategies. This implementation simply picks an object arbitrarily from the "strongest" of the three lists we build: if there's anything in the inScopeList, we choose an object from that list; otherwise, if there's anything in the likelyList, we choose an object from that list; otherwise we choose an object from the otherList.


### `getResolveInfo(obj)`

Defined in action.t, line 6285

Get the parser ResolveInfo object for a given matched object. This recovers the ResolveInfo describing the parsing result for any object in the resolved object lists (inScopeList, etc).


### `getTopicText`

Defined in action.t, line 6236

get the original text of the topic phrase


### `getTopicTokens`

Defined in action.t, line 6266

get the original tokens of the topic phrase, in canonical tokenizer format


### `getTopicWords`

Defined in action.t, line 6274

get the original word strings of the topic phrase - this is simply a list of the original word strings (in their original case), without any of the extra information of the more complicated canonical tokenizer format


### `wrapActionObject(role)`

Defined in action.t, line 6159

Static method: create a ResolvedTopic to represent an object that's already been resolved to a game object for the current action. 'role' is the object role to wrap (DirectObject, IndirectObject, etc).


### `wrapObject(obj)`

Defined in action.t, line 6180

Static method: create a ResolvedTopic to represent the given object.
