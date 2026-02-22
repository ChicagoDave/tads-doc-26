# IllogicalVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 344)


Verification result - command is always illogical, regardless of the state of the object. "Close fish" might fall into this category.


**Superclass chain:** [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **IllogicalVerifyResultSubclasses:** [IllogicalSelfVerifyResult](illogicalselfverifyresult.md)


## Properties


### `allowAction` *(overridden)*

Defined in verify.t, line 346

the command isn't allowed


### `resultRank` *(overridden)*

Defined in verify.t, line 349

result rank - this is the most disapproving of the disapprovals


## Inherited Properties


*From [VerifyResult](verifyresult.md):* [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
