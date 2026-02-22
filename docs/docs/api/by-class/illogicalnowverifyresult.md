# IllogicalNowVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 314)


Verification result - command is currently illogical due to the state of the object, but might be logically applied to the object at other times. For example, "open door" on a door that's already open is illogical at the moment, but makes more sense than opening something that has no evident way to be opened or closed to begin with.


**Superclass chain:** [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **IllogicalNowVerifyResultSubclasses:** [IllogicalAlreadyVerifyResult](illogicalalreadyverifyresult.md)


## Properties


### `allowAction` *(overridden)*

Defined in verify.t, line 316

the command isn't allowed


### `resultRank` *(overridden)*

Defined in verify.t, line 319

result rank


## Inherited Properties


*From [VerifyResult](verifyresult.md):* [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
