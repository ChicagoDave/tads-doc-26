# DisambigProd

*class* — defined in [parser.t](../by-file/parser.t.md) (line 612)


Basic disambiguation production class


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **DisambigProd**


<details><summary>Subclasses (16)</summary>

- [disambigList(list)](disambiglist%28list%29.md)
- [disambigList(single)](disambiglist%28single%29.md)
- [DisambigOrdProd](disambigordprod.md)
- [disambigListItem(ordinal)](disambiglistitem%28ordinal%29.md)
- [disambigOrdinalList(head)](disambigordinallist%28head%29.md)
- [disambigOrdinalList(tail)](disambigordinallist%28tail%29.md)
- [disambigPhrase(all)](disambigphrase%28all%29.md)
- [disambigPhrase(any)](disambigphrase%28any%29.md)
- [disambigPhrase(both)](disambigphrase%28both%29.md)
- [disambigPhrase(list)](disambigphrase%28list%29.md)
- [disambigPhrase(ordinalList)](disambigphrase%28ordinallist%29.md)
- [DisambigPossessiveProd](disambigpossessiveprod.md)
- [disambigListItem(possessive)](disambiglistitem%28possessive%29.md)
- [DisambigVocabProd](disambigvocabprod.md)
- [disambigListItem(noun)](disambiglistitem%28noun%29.md)
- [disambigListItem(plural)](disambiglistitem%28plural%29.md)

</details>


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `removeAmbigFlags(lst)`

Defined in parser.t, line 618

Remove the "ambiguous" flags from a result list. This can be used to mark the response to a disambiguation query as no longer ambiguous.


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
