# DynamicProd

*class* — defined in [gramprod.t](../by-file/gramprod.t.md) (line 156)


Dynamic match object interface. This is a mix-in class that should be used as a superclass for any class used as the match object when creating new alternatives dynamically with GrammarProd.addAlt().


**Superclass chain:** `object` > **DynamicProd**


## Properties


### `grammarAltProps`

Defined in gramprod.t, line 180

grammarAltProps - the list of "->" properties used in all of the alternatives associated with this match object. addAlts() stores this list automatically - there's no need to create it manually.


### `grammarTag`

Defined in gramprod.t, line 173

grammarTag - the name for the collection of alternatives associated with the match object. This name is primarily for debugging purposes; it appears as the first element of the grammarInfo() result list.


## Methods


### `grammarInfo`

Defined in gramprod.t, line 162

Generate match information. This returns the same information that grammarInfo() returns for match objects that the compiler generates for static 'grammar' statements.
