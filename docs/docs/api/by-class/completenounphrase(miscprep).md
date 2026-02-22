# completeNounPhrase(miscPrep)

*grammar* — defined in [en_us.t](../by-file/en_us.t.md) (line 5554)


Slightly better than a purely miscellaneous word list is a pair of otherwise valid noun phrases connected by a preposition that's commonly used in command phrases. This will match commands where the user has assumed a command with a prepositional structure that doesn't exist among the defined commands. Since we have badness, we'll be ignored any time there's a valid command syntax with the same prepositional structure.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **completeNounPhrase(miscPrep)**


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `resolveNouns(resolver, results)`

Defined in en_us.t, line 5560


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
