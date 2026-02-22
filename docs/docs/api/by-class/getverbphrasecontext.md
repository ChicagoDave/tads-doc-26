# GetVerbPhraseContext

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 7967)


Context for Action.getVerbPhrase(). This keeps track of pronoun antecedents in cases where we're stringing together a series of verb phrases.


**Superclass chain:** `object` > **GetVerbPhraseContextSubclasses:** [ListImpCtx](listimpctx.md)


**Global objects:** [defaultGetVerbPhraseContext](defaultgetverbphrasecontext.md)


## Properties


### `pronounObj`

Defined in en_us.t, line 7988

the pronoun antecedent


## Methods


### `isObjPronoun(obj)`

Defined in en_us.t, line 7982

are we showing the given object pronomially?


### `objNameObj(obj)`

Defined in en_us.t, line 7969

get the objective form of an object, using a pronoun as appropriate


### `setPronounObj(obj)`

Defined in en_us.t, line 7985

set the pronoun antecedent
