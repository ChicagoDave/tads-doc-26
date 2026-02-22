# LiteralActionBase

*class* — defined in [action.t](../by-file/action.t.md) (line 5192)


Common base class for actions involving literal phrases. This is a mix-in class that can be combined with Action subclasses to create specific kinds of literal actions.


**Superclass chain:** `object` > **LiteralActionBase**


<details><summary>Subclasses (16)</summary>

- [LiteralAction](literalaction.md)
- [OopsAction](oopsaction.md)
- [predicate(Oops)](predicate%28oops%29.md)
- [SpecialTopicAction](specialtopicaction.md)
- [predicate(SpecialTopic)](predicate%28specialtopic%29.md)
- [LiteralTAction](literaltaction.md)
- [EnterOnAction](enteronaction.md)
- [predicate(EnterOn)](predicate%28enteron%29.md)
- [predicate(EnterOnWhat)](predicate%28enteronwhat%29.md)
- [SetToAction](settoaction.md)
- [predicate(SetTo)](predicate%28setto%29.md)
- [TurnToAction](turntoaction.md)
- [predicate(TurnTo)](predicate%28turnto%29.md)
- [TypeLiteralOnAction](typeliteralonaction.md)
- [predicate(TypeLiteralOn)](predicate%28typeliteralon%29.md)
- [predicate(TypeLiteralOnWhat)](predicate%28typeliteralonwhat%29.md)

</details>


## Properties


### `text_`

Defined in action.t, line 5239

the text of the literal phrase


## Methods


### `getLiteral`

Defined in action.t, line 5236

get the current literal text


### `getMessageParam(objName)`

Defined in action.t, line 5197

Get a message parameter. We define 'literal' as the text of the literal phrase, in addition to inherited targets.


### `setObjectMatches(lit)`

Defined in action.t, line 5219

manually set the pre-resolved match trees


### `setResolvedObjects(txt)`

Defined in action.t, line 5212

manually set the resolved objects
