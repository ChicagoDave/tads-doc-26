# NonObviousVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 381)


Verification result - command is logical and allowed, but is non-obvious on this object. This should be used when the command is logical, but should not be obvious to the player. When this verification result is present, the command is allowed when performed explicitly but will never be taken as a default.


**Superclass chain:** [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **NonObviousVerifyResult**


## Properties


### `allowImplicit`

Defined in verify.t, line 386

don't allow non-obvious actions to be undertaken implicitly - we allow these actions, but only when explicitly requested


### `resultRank` *(overridden)*

Defined in verify.t, line 392

non-obvious objects are illogical at first glance, so rank them the same as objects that are actually illogical


## Inherited Properties


*From [VerifyResult](verifyresult.md):* [`allowAction`](verifyresult.md#allowAction), [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
