# ListGroupPrefixSuffix

*class* — defined in [lister.t](../by-file/lister.t.md) (line 2178)


List Group implementation: simple prefix/suffix lister. Shows a prefix message, then shows the list, then shows a suffix message.


**Superclass chain:** [ListGroupSorted](listgroupsorted.md) > [ListGroup](listgroup.md) > `object` > **ListGroupPrefixSuffixSubclasses:** [SuggestionListGroup](suggestionlistgroup.md)


## Properties


### `groupPrefix`

Defined in lister.t, line 2216

The prefix and suffix messages. The showGroupPrefix and showGroupSuffix methods simply show these message properties. We go through this two-step procedure for convenience: if the subclass doesn't need the POV and list parameters, it's less typing to just override these parameterless properties. If the subclass needs to vary the message according to the POV or what's in the list, it can override the showGroupXxx methods instead.


### `groupSuffix`

Defined in lister.t, line 2217


## Inherited Properties


*From [ListGroup](listgroup.md):* [`groupDisplaysSublist`](listgroup.md#groupDisplaysSublist), [`minGroupSize`](listgroup.md#minGroupSize)


## Methods


### `showGroupList(pov, lister, lst, options, indent, infoTab)` *(overridden)*

Defined in lister.t, line 2179


### `showGroupPrefix(pov, lst)`

Defined in lister.t, line 2202

show the prefix - we just show the groupPrefix message by default


### `showGroupSuffix(pov, lst)`

Defined in lister.t, line 2205

show the suffix - we just show the groupSuffix message by default


## Inherited Methods


*From [ListGroupSorted](listgroupsorted.md):* [`compareGroupItems`](listgroupsorted.md#compareGroupItems), [`sortListGroup`](listgroupsorted.md#sortListGroup)


*From [ListGroup](listgroup.md):* [`createGroupSublister`](listgroup.md#createGroupSublister), [`groupCardinality`](listgroup.md#groupCardinality), [`groupNounPhraseCount`](listgroup.md#groupNounPhraseCount), [`showGroupItem`](listgroup.md#showGroupItem), [`showGroupItemCounted`](listgroup.md#showGroupItemCounted)
