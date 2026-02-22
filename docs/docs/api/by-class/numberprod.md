# NumberProd

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 7639)


A numeric production. These can be either spelled-out numbers (such as "fifty-seven") or numbers entered in digit form (as in "57").


**Superclass chain:** [BasicProd](basicprod.md) > `object` > **NumberProd**


<details><summary>Subclasses (24)</summary>

- [numberPhrase(digits)](numberphrase%28digits%29.md)
- [numberPhrase(spelled)](numberphrase%28spelled%29.md)
- [poundNumberPhrase(main)](poundnumberphrase%28main%29.md)
- [spelledHundred(aHundred)](spelledhundred%28ahundred%29.md)
- [spelledHundred(aHundredPlus)](spelledhundred%28ahundredplus%29.md)
- [spelledHundred(hundreds)](spelledhundred%28hundreds%29.md)
- [spelledHundred(hundredsPlus)](spelledhundred%28hundredsplus%29.md)
- [spelledHundred(small)](spelledhundred%28small%29.md)
- [spelledMillion(aMillion)](spelledmillion%28amillion%29.md)
- [spelledMillion(aMillionAndSmall)](spelledmillion%28amillionandsmall%29.md)
- [spelledMillion(millions)](spelledmillion%28millions%29.md)
- [spelledMillion(millionsAndSmall)](spelledmillion%28millionsandsmall%29.md)
- [spelledMillion(millionsPlus)](spelledmillion%28millionsplus%29.md)
- [spelledNumber(main)](spellednumber%28main%29.md)
- [spelledSmallNumber(digit)](spelledsmallnumber%28digit%29.md)
- [spelledSmallNumber(teen)](spelledsmallnumber%28teen%29.md)
- [spelledSmallNumber(tens)](spelledsmallnumber%28tens%29.md)
- [spelledSmallNumber(tensAndUnits)](spelledsmallnumber%28tensandunits%29.md)
- [spelledSmallNumber(zero)](spelledsmallnumber%28zero%29.md)
- [spelledThousand(aThousand)](spelledthousand%28athousand%29.md)
- [spelledThousand(aThousandAndSmall)](spelledthousand%28athousandandsmall%29.md)
- [spelledThousand(thousands)](spelledthousand%28thousands%29.md)
- [spelledThousand(thousandsAndSmall)](spelledthousand%28thousandsandsmall%29.md)
- [spelledThousand(thousandsPlus)](spelledthousand%28thousandsplus%29.md)

</details>


## Inherited Properties


*From [BasicProd](basicprod.md):* [`firstTokenIndex`](basicprod.md#firstTokenIndex), [`isSpecialResponseMatch`](basicprod.md#isSpecialResponseMatch), [`lastTokenIndex`](basicprod.md#lastTokenIndex)


## Methods


### `getStrVal`

Defined in en_us.t, line 7650

Get the string version of the numeric value. This should return a string, but the string should be in digit form. If the original entry was in digit form, then the original entry should be returned; otherwise, a string should be constructed from the integer value. By default, we'll do the latter.


### `getval`

Defined in en_us.t, line 7641

get the numeric (integer) value


## Inherited Methods


*From [BasicProd](basicprod.md):* [`canResolveTo`](basicprod.md#canResolveTo), [`getOrigText`](basicprod.md#getOrigText), [`getOrigTokenList`](basicprod.md#getOrigTokenList), [`setOrigTokenList`](basicprod.md#setOrigTokenList)
