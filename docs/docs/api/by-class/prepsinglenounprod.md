# PrepSingleNounProd

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 5463)


Prepositionally modified single noun phrases. These can be used in indirect object responses, so allow for interactions like this:


**Superclass chain:** [SingleNounProd](singlenounprod.md) > [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **PrepSingleNounProdSubclasses:** [atSingleNoun(main)](atsinglenoun%28main%29.md), [forSingleNoun(main)](forsinglenoun%28main%29.md), [fromSingleNoun(main)](fromsinglenoun%28main%29.md), [inSingleNoun(main)](insinglenoun%28main%29.md), [onSingleNoun(main)](onsinglenoun%28main%29.md), [outOfSingleNoun(main)](outofsinglenoun%28main%29.md), [throughSingleNoun(main)](throughsinglenoun%28main%29.md), [toSingleNoun(main)](tosinglenoun%28main%29.md), [withSingleNoun(main)](withsinglenoun%28main%29.md)


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `isSpecialResponseMatch`

Defined in en_us.t, line 5473

If the response starts with a preposition, it's pretty clearly a response to the special query rather than a new command.


### `resolveNouns(resolver, results)` *(overridden)*

Defined in en_us.t, line 5464


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
