# DangerousVerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 293)


Verification result - command is logical and allowed, but is dangerous. As with all verify results, this should reflect our best guess as to the player's intentions, so this should only be used when it is meant to be obvious to the player that the action is dangerous.


**Superclass chain:** [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **DangerousVerifyResult**


## Properties


### `allowImplicit`

Defined in verify.t, line 298

don't allow dangerous actions to be undertaken implicitly - we do allow these actions, but only when explicitly requested


### `isDangerous`

Defined in verify.t, line 304

this result indicates danger


### `resultRank` *(overridden)*

Defined in verify.t, line 301

result rank - we're only slightly less approving than 'logical'


## Inherited Properties


*From [VerifyResult](verifyresult.md):* [`allowAction`](verifyresult.md#allowAction), [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Inherited Methods


*From [VerifyResult](verifyresult.md):* [`compareTo`](verifyresult.md#compareTo), [`identicalTo`](verifyresult.md#identicalTo), [`isWorseThan`](verifyresult.md#isWorseThan), [`shouldInsertBefore`](verifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
