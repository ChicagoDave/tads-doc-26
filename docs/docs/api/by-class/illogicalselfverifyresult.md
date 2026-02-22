# IllogicalSelfVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 363)


Verification result - command is always illogical, because it's trying to use an object on itself in some invalid way, as in PUT BOX IN BOX.


**Superclass chain:** [IllogicalVerifyResult](illogicalverifyresult.md) > [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **IllogicalSelfVerifyResult**


## Properties


### `excludePluralMatches` *(overridden)*

Defined in verify.t, line 365

exclude plural matches when this result type is present


## Inherited Properties


*From [IllogicalVerifyResult](illogicalverifyresult.md):* [`allowAction`](illogicalverifyresult.md#allowAction), [`resultRank`](illogicalverifyresult.md#resultRank)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
