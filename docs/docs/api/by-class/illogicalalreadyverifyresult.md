# IllogicalAlreadyVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 335)


Verification result - command is currently illogical, because the state that the command seeks to impose already obtains. For example, we're trying to open a door that's already open, or drop an object that we're not carrying.


**Superclass chain:** [IllogicalNowVerifyResult](illogicalnowverifyresult.md) > [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **IllogicalAlreadyVerifyResult**


## Properties


### `excludePluralMatches` *(overridden)*

Defined in verify.t, line 337

exclude plural matches when this result type is present


## Inherited Properties


*From [IllogicalNowVerifyResult](illogicalnowverifyresult.md):* [`allowAction`](illogicalnowverifyresult.md#allowAction), [`resultRank`](illogicalnowverifyresult.md#resultRank)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
