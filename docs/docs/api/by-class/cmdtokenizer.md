# cmdTokenizer

*object* — defined in [en_us.t](../by-file/en_us.t.md) (line 4763)


Command tokenizer for US English. Other language modules should provide their own tokenizers to allow for differences in punctuation and other lexical elements.


**Superclass chain:** [Tokenizer](tokenizer.md) > `object` > **cmdTokenizer**


## Properties


### `patAlphaDashAlpha`

Defined in en_us.t, line 4962

add the part after the hyphen


### `patPunct`

Defined in en_us.t, line 5081


### `patSpelledTens`

Defined in en_us.t, line 5077

some pre-compiled regular expressions


### `patSpelledUnits`

Defined in en_us.t, line 5079


### `rules_` *(overridden)*

Defined in en_us.t, line 4764


## Methods


### `acceptAbbrTok(txt)`

Defined in en_us.t, line 4974

Check to see if we want to accept an abbreviated token - this is a token that ends in a period, which we use for abbreviated words like "Mr." or "Ave." We'll accept the token only if it appears as given - including the period - in the dictionary. Note that we ignore truncated matches, since the only way we'll accept a period in a word token is as the last character; there is thus no way that a token ending in a period could be a truncation of any longer valid token.


### `buildOrigText(toks)`

Defined in en_us.t, line 5013

Given a list of token strings, rebuild the original input string. We can't recover the exact input string, because the tokenization process throws away whitespace information, but we can at least come up with something that will display cleanly and produce the same results when run through the tokenizer.


### `tokCvtAbbr(txt, typ, toks)`

Defined in en_us.t, line 4994

Process an abbreviated token.


### `tokCvtApostropheS(txt, typ, toks)`

Defined in en_us.t, line 4900

Handle an apostrophe-s word. We'll return this as two separate tokens: one for the word preceding the apostrophe-s, and one for the apostrophe-s itself.


### `tokCvtPluralApostrophe(txt, typ, toks)`

Defined in en_us.t, line 4924

Handle a plural apostrophe word ("the smiths' house"). We'll return this as two tokens: one for the plural word, and one for the apostrophe.


### `tokCvtSpelledNumber(txt, typ, toks)`

Defined in en_us.t, line 4948

Handle a spelled-out hyphenated number from 21 to 99. We'll return this as three separate tokens: a word for the tens name, a word for the hyphen, and a word for the units name.


## Inherited Methods


*From [Tokenizer](tokenizer.md):* [`deleteRule`](tokenizer.md#deleteRule), [`deleteRuleAt`](tokenizer.md#deleteRuleAt), [`insertRule`](tokenizer.md#insertRule), [`insertRuleAt`](tokenizer.md#insertRuleAt), [`tokCvtLower`](tokenizer.md#tokCvtLower), [`tokCvtSkip`](tokenizer.md#tokCvtSkip), [`tokenize`](tokenizer.md#tokenize)
