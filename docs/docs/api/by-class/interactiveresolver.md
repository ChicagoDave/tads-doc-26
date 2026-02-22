# InteractiveResolver

*class* — defined in [disambig.t](../by-file/disambig.t.md) (line 335)


Base class for resolvers used when answering interactive questions. This class doesn't do anything in the library directly, but it provides a structured point for language extensions to hook in as needed with 'modify'.


**Superclass chain:** [ProxyResolver](proxyresolver.md) > `object` > **InteractiveResolverSubclasses:** [DisambigResolver](disambigresolver.md)


## Methods


### `getReflexiveBinding(typ)`

Defined in en_us.t, line 3396

Get the reflexive third-person pronoun binding (himself, herself, itself, themselves). If the target actor isn't the PC, and the gender of the pronoun matches, we'll consider this as referring to the target actor. This allows exchanges of this form:


### `resolvePronounAntecedent(typ, np, results, poss)`

Defined in en_us.t, line 3373

Resolve a pronoun antecedent. We'll resolve a third-person singular pronoun to the target actor if the target actor matches in gender, and the target actor isn't the PC. This allows exchanges like this:


### `resolvePronounAsTargetActor(typ)`

Defined in en_us.t, line 3414

Try matching the given pronoun type to the target actor. If it matches in gender, and the target actor isn't the PC, we'll return a resolve list consisting of the target actor. If we don't have a match, we'll return nil.


## Inherited Methods


*From [ProxyResolver](proxyresolver.md):* [`construct`](proxyresolver.md#construct), [`getPossessiveResolver`](proxyresolver.md#getPossessiveResolver), [`propNotDefined`](proxyresolver.md#propNotDefined)
