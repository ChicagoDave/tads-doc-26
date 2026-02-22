# InaccessibleVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 402)


Verification result - object is inaccessible. This should be used when a command is applied to an object that is not accessibile in a sense required for the command; for example, "look at" requires that its target object be visible, so a "look at" command in the dark would fail with this type of result.


**Superclass chain:** [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **InaccessibleVerifyResult**


## Properties


### `allowAction` *(overridden)*

Defined in verify.t, line 404

the command isn't allowed


### `resultRank` *(overridden)*

Defined in verify.t, line 410

This ranks below any illogical result - inaccessibility is a stronger disapproval than mere illogicality.


## Inherited Properties


*From [VerifyResult](verifyresult.md):* [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
