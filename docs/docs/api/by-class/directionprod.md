# DirectionProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 640)


Base class for "direction" productions. Each direction (the compass directions, the vertical directions, the shipboard directions, and so on) must have an associated grammar rule, which must produce one of these. This should be subclassed with grammar rules like this:


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **DirectionProd**


<details><summary>Subclasses (16)</summary>

- [directionName(aft)](directionname%28aft%29.md)
- [directionName(down)](directionname%28down%29.md)
- [directionName(east)](directionname%28east%29.md)
- [directionName(fore)](directionname%28fore%29.md)
- [directionName(in)](directionname%28in%29.md)
- [directionName(north)](directionname%28north%29.md)
- [directionName(northeast)](directionname%28northeast%29.md)
- [directionName(northwest)](directionname%28northwest%29.md)
- [directionName(out)](directionname%28out%29.md)
- [directionName(port)](directionname%28port%29.md)
- [directionName(south)](directionname%28south%29.md)
- [directionName(southeast)](directionname%28southeast%29.md)
- [directionName(southwest)](directionname%28southwest%29.md)
- [directionName(starboard)](directionname%28starboard%29.md)
- [directionName(up)](directionname%28up%29.md)
- [directionName(west)](directionname%28west%29.md)

</details>


## Properties


### `dir`

Defined in parser.t, line 646

Each direction-specific grammar rule subclass must set this property to the associated direction object (northDirection, etc).


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
