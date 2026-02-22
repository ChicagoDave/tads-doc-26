# GrammarAltTokInfo

*class* — defined in [gramprod.t](../by-file/gramprod.t.md) (line 89)


Grammar rule token descriptor. GrammarProd.getGrammarInfo() instantiates one of these objects to represent each token slot in an alternative; a GrammarAltInfo object's gramTokens property has a list of these objects.


**Superclass chain:** `object` > **GrammarAltTokInfo**


## Properties


### `gramTargetProp`

Defined in gramprod.t, line 114

The target property - this is the property of the *match object* that will store the match information for the token. In a 'grammar' statement, this is the property after the '->' symbol for this token.


### `gramTokenInfo`

Defined in gramprod.t, line 143

Detailed information for the token slot, which depends on the token type:


### `gramTokenType`

Defined in gramprod.t, line 120

The token type. This is one of the GramTokTypeXxx values (see gramprod.h) indicating what kind of token slot this is.


## Methods


### `construct(prop, typ, info, ...)`

Defined in gramprod.t, line 100

Constructor. GrammarProd.getGrammarInfo() calls this once for each token in each alternative in the production, passing in values to fully describe the token slot: the target property (in a 'grammar' statement, this is the property after a '->' symbol); the token type; and extra information that depends on the token type. Note that we use '...' at the end of the argument list so that we'll be compatible with any future changes to GrammarProd that add more arguments to this method.
