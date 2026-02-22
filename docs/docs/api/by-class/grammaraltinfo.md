# GrammarAltInfo

*class* — defined in [gramprod.t](../by-file/gramprod.t.md) (line 43)


Rule alternative descriptor. This describes one alternative in a grammar production. An alternative is one complete list of matchable tokens.


**Superclass chain:** `object` > **GrammarAltInfo**


## Properties


### `gramBadness`

Defined in gramprod.t, line 66

The 'badness' value associated with the alternative. A value of zero means that there's no badness.


### `gramMatchObj`

Defined in gramprod.t, line 73

the "match object" class - this is the class that GrammarProd.parseTokens() instantiates to represent a match to this alternative in the match list that the method returns


### `gramTokens`

Defined in gramprod.t, line 80

The token descriptor list. This is a list of zero or more GrammarAltTokInfo objects describing the tokens making up this rule.


## Methods


### `construct(score, badness, matchObj, toks, ...)`

Defined in gramprod.t, line 54

Constructor. GrammarProd.getGrammarInfo() calls this once for each alternative making up the production, passing in the values that define the alternative. Note that we have a '...' in our argument list so that we'll be compatible with any future GrammarProd versions that add additional arguments - we won't do anything with the extra arguments, but we'll harmlessly ignore them, so code compiled with this library version will continue to work correctly.
