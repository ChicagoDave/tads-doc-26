# EmptyNounPhraseProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 4028)


An empty noun phrase production is one that matches, typically with non-zero badness value, as a placeholder when a command is missing a noun phrase where one is required.


**Superclass chain:** [NounPhraseProd](nounphraseprod.md) > [BasicProd](basicprod.md) > `object` > **EmptyNounPhraseProdSubclasses:** [ImpliedActorNounPhraseProd](impliedactornounphraseprod.md), [nounList(empty)](nounlist%28empty%29.md), [singleNoun(empty)](singlenoun%28empty%29.md)


## Properties


### `asker_`

Defined in parser.t, line 4152

The ResolveAsker we use to generate our prompt. Use the base ResolveAsker by default; this can be overridden when the prompt is to be customized.


### `fallbackResponseProd`

Defined in parser.t, line 4145

Our fallback response production - if responseProd is nil, this must be supplied for cases where we can't get the production from the action. This is ignored if responseProd is non-nil.


### `newMatch`

Defined in parser.t, line 4130

the new match, when we get an interactive response to a query for the missing object


### `responseProd`

Defined in parser.t, line 4138

Our "response" production - this is the production we use to parse the player's input in response to our disambiguation prompt. A subclass can leave this as nil, in which case we'll attempt to get the appropriate response production from the action.


## Inherited Properties


*From [NounPhraseProd](nounphraseprod.md):* [`filterForCollectives`](nounphraseprod.md#filterForCollectives)


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getImpliedObject(resolver, results)`

Defined in parser.t, line 4094

Get an implied object to automatically fill in for the missing noun phrase. By default, we simply ask the 'results' object for the missing object.


### `getOrigText` *(overridden)*

Defined in parser.t, line 4115

Get my original text. If I have a new match tree, return the text from the new match tree. Otherwise, we have no original text, since we're an empty phrase.


### `getOrigTokenList` *(overridden)*

Defined in parser.t, line 4105

Get my tokens. If I have a new match tree, return the tokens from the new match tree. Otherwise, we don't have any tokens, since we're empty.


### `isEmptyPhrase`

Defined in parser.t, line 4124

I'm an empty noun phrase, unless I already have a new match object.


### `resolveNouns(resolver, results)`

Defined in parser.t, line 4038

resolve the empty phrase


### `setPrompt(response, asker)`

Defined in parser.t, line 4030

customize the way we generate the prompt and parse the response


## Inherited Methods


*From [NounPhraseProd](nounphraseprod.md):* [`filterTruncations`](nounphraseprod.md#filterTruncations), [`getVerifyKeepers`](nounphraseprod.md#getVerifyKeepers)


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
