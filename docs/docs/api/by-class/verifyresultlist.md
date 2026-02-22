# VerifyResultList

*class* — defined in [verify.t](../by-file/verify.t.md) (line 428)


Verification result list.


**Superclass chain:** `object` > **VerifyResultList**


## Properties


### `obj_`

Defined in verify.t, line 694

The ResolveInfo for the object being verified. Note that this isn't saved until AFTER the verification is completed.


### `origOrder`

Defined in verify.t, line 701

The original list index for this result. We use this when sorting a list of results to preserve the original ordering of otherwise equivalent items.


### `remapAction_`

Defined in verify.t, line 684

the action and role of the remapped action


### `remapRole_`

Defined in verify.t, line 685


### `remapTarget_`

Defined in verify.t, line 681

The remapped target object. This will filled in during verification if we decide that we want to remap the nominal object of the command to a different object. This should be set to the ultimate target object after all remappings.


### `results_`

Defined in verify.t, line 688

our list of results


## Methods


### `addResult(result)`

Defined in verify.t, line 438

Add a result to our result list.


### `allowAction`

Defined in verify.t, line 474

Is the action allowed? We return true if we have no results; otherwise, we allow the action if *all* of our results allow it, nil if even one disapproves.


### `allowImplicit`

Defined in verify.t, line 495

Is the action allowed as an implicit action? Returns true if we have no results; otherwise, returns true if *all* of our results allow the implicit action, nil if even one disapproves.


### `compareTo(other)`

Defined in verify.t, line 547

Compare my cumulative result (i.e., my most disapproving result) to that of another result list's cumulative result. Returns a value suitable for sorting: -1 if I'm worse than the other one, 0 if we're the same, and 1 if I'm better than the other one. This can be used to compare the cumulative verification results for two objects to determine which object is more logical.


### `construct`

Defined in verify.t, line 429


### `excludePluralMatches`

Defined in verify.t, line 484

Do we exclude plural matches? We do if we have at least one result that excludes plural matches.


### `getEffectiveResult`

Defined in verify.t, line 525

Get my effective result object. If I have no explicitly-set result object, my effective result is the defaut logical result. Otherwise, we return the most disapproving result in our list.


### `matchForCombineRemapped(other, action, role)`

Defined in verify.t, line 637

Determine if we match another verify result list after remapping. This determines if the other verify result is equivalent to us after considering the effects of remapping. We'll return true if all of the following are true:


### `showMessage`

Defined in verify.t, line 506

Show the message. If I have any results, we'll show the message for the effective (i.e., most disapproving) result; otherwise we show nothing.
