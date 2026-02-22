# VerifyResult

*class* — defined in [verify.t](../by-file/verify.t.md) (line 55)


Verification result class. Verification routines return a verification result describing whether or not an action is allowed, and how much sense the command seems to make. When a verification fails, it must include a message describing why the command isn't allowed.


**Superclass chain:** [MessageResult](messageresult.md) > `object` > **VerifyResultSubclasses:** [DangerousVerifyResult](dangerousverifyresult.md), [IllogicalNowVerifyResult](illogicalnowverifyresult.md), [IllogicalAlreadyVerifyResult](illogicalalreadyverifyresult.md), [IllogicalVerifyResult](illogicalverifyresult.md), [IllogicalSelfVerifyResult](illogicalselfverifyresult.md), [InaccessibleVerifyResult](inaccessibleverifyresult.md), [LogicalVerifyResult](logicalverifyresult.md), [NonObviousVerifyResult](nonobviousverifyresult.md)


## Properties


### `allowAction`

Defined in verify.t, line 60

Is the action allowed? This returns true if the command can be allowed to proceed on the basis of the verification, nil if not.


### `excludePluralMatches`

Defined in verify.t, line 152

Should we exclude plurals from being matched, when this type of result is present? By default, we don't; some illogical types might want to exclude plurals because the result types indicate such obvious illogicalities.


### `resultRank`

Defined in verify.t, line 144

Our result ranking relative to other results. Each result class defines a ranking level so that we can determine whether one result is better (more approving) or worse (more disapproving) than another.


## Inherited Properties


*From [MessageResult](messageresult.md):* [`messageProp_`](messageresult.md#messageProp_), [`messageText_`](messageresult.md#messageText_)


## Methods


### `compareTo(other)`

Defined in verify.t, line 96

compare to another: negative if I'm worse than the other, zero if we're the same, positive if I'm better


### `identicalTo(other)`

Defined in verify.t, line 127

Determine if I'm identical to another result. Note that it's possible for two items to compare the same but not be identical - compareTo() is concerned only with logicalness ranking, but identicalTo() determines if the two items are exactly the same. Some subclasses (such as LogicalVerifyResult) distinguish among items that compare the same but have different reasons for their rankings.


### `isWorseThan(other)`

Defined in verify.t, line 86

Am I worse than another result? Returns true if this result is more disapproving than the other.


### `shouldInsertBefore(other)`

Defined in verify.t, line 108

Determine if I should appear in a result list before the given result object. By default, this is true if I'm worse than the given result, but some types of results use special sorting orders.


## Inherited Methods


*From [MessageResult](messageresult.md):* [`construct`](messageresult.md#construct), [`resolveMessageText`](messageresult.md#resolveMessageText), [`setMessage`](messageresult.md#setMessage), [`showMessage`](messageresult.md#showMessage)
