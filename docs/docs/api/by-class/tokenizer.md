# Tokenizer

*class* — defined in [tok.t](../by-file/tok.t.md) (line 84)


Tokenizer base class


**Superclass chain:** `object` > **TokenizerGlobal objects:** [cmdTokenizer](cmdtokenizer.md)


## Properties


### `rules_`

Defined in tok.t, line 123

Tokenizing rules. The subclass can override this to specify a list that defines different tokenization rules. Each entry in the master rules_ list is one rule. Each rule is a list consisting of the name of the rule; the pattern to match for the rule; the token type (an 'enum token') to use when the rule is matched; the value computation rule; and the value test rule.


## Methods


### `deleteRule(name)`

Defined in tok.t, line 195

Delete a rule by name. This finds the rule with the given name and removes it from the list.


### `deleteRuleAt(idx)`

Defined in tok.t, line 208

delete the rule at the given index


### `insertRule(rule, curName, after)`

Defined in tok.t, line 154

Insert a new rule before or after the existing rule with the name 'curName'. If 'curName' is nil, or rule is found with the given name, we'll insert the new rule at the end of the list. 'rule' must be a list with the standard elements for a tokenizer rule. 'after' is nil to insert the new rule before the given existing rule, true to insert after it.


### `insertRuleAt(rule, idx)`

Defined in tok.t, line 185

Insert a rule at the given index in our rules list. 'rule' must be a list with the standard elements for a tokenizer rule. 'idx' is the index of the new rule; we'll insert before the existing element at this index; so if 'idx' is 1, we'll insert before the first existing rule.


### `tokCvtLower(txt, typ, toks)`

Defined in tok.t, line 215

convert a string to lower-case (for value computation rules)


### `tokCvtSkip(txt, typ, toks)`

Defined in tok.t, line 226

processing routine to skip a match - this is used for whitespace and other text that does not result in any tokens in the result list


### `tokenize(str)`

Defined in tok.t, line 248

Tokenize a string. If we find text that we can't match to any of the rules, we'll throw an exception (TokErrorNoMatch). If we succeed in tokenizing the entire string, we'll return a list with one element per token. Each element of the main list is a sublist with the following elements describing a token:
