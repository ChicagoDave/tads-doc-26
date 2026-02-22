# LogicalVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 170)


Verification result - command is logical and allowed.


**Superclass chain:** [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **LogicalVerifyResultGlobal objects:** [defaultLogicalVerifyResult](defaultlogicalverifyresult.md)


## Properties


### `keyVal`

Defined in verify.t, line 281

my key value, to distinguish among different results with the same likelihood ranking


### `likelihood`

Defined in verify.t, line 249

The likelihood of the command - the higher the number, the more likely. We use 100 as the default, so that there's plenty of room for specific rankings above or below the default. Particular actions might want to rank likelihoods based on action-specific factors.


### `listOrder`

Defined in verify.t, line 275

Our list ordering. This establishes how we are entered into the master results list relative to other 'logical' results. Results are entered into the master list in ascending list order, so a lower order number means an earlier place in the list.


### `resultRank` *(overridden)*

Defined in verify.t, line 284

result rank - we're the most approving kind of result


## Inherited Properties


*From [VerifyResult](verifyresult.md):* [`allowAction`](verifyresult.md#allowAction), [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Methods


### `compareTo(other)` *(overridden)*

Defined in verify.t, line 198

compare to another result


### `construct(likelihoodRank, key, ord)` *(overridden)*

Defined in verify.t, line 171


### `identicalTo(other)` *(overridden)*

Defined in verify.t, line 233

determine if I'm identical to another result


### `isWorseThan(other)` *(overridden)*

Defined in verify.t, line 184

am I worse than the other result?


### `shouldInsertBefore(other)` *(overridden)*

Defined in verify.t, line 215

determine if I go in a result list before the given result


## Inherited Methods


*From [MessageResult](messageresult.md):* [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
