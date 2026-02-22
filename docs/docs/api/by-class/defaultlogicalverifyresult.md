# defaultLogicalVerifyResult

*object* — defined in [verify.t](../by-file/verify.t.md) (line 417)


Default 'logical' verify result. If a verification result list doesn't have an explicitly set result, this is the default value.


**Superclass chain:** [LogicalVerifyResult](logicalverifyresult.md) > [VerifyResult](verifyresult.md) > [MessageResult](messageresult.md) > `object` > **defaultLogicalVerifyResult**


## Properties


### `keyVal` *(overridden)*

Defined in verify.t, line 422

the default logical result has no message


## Inherited Properties


*From [LogicalVerifyResult](logicalverifyresult.md):* [`likelihood`](logicalverifyresult.md#likelihood), [`listOrder`](logicalverifyresult.md#listOrder), [`resultRank`](logicalverifyresult.md#resultRank)


*From [VerifyResult](verifyresult.md):* [`allowAction`](verifyresult.md#allowAction), [`excludePluralMatches`](verifyresult.md#excludePluralMatches)


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Methods


### `showMessage` *(overridden)*

Defined in verify.t, line 418


## Inherited Methods


*From [LogicalVerifyResult](logicalverifyresult.md):* [`compareTo`](logicalverifyresult.md#compareTo), [`construct`](logicalverifyresult.md#construct), [`identicalTo`](logicalverifyresult.md#identicalTo), [`isWorseThan`](logicalverifyresult.md#isWorseThan), [`shouldInsertBefore`](logicalverifyresult.md#shouldInsertBefore)


*From [MessageResult](messageresult.md):* [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage)
