# typographicalOutputFilter

*object* — defined in [en_us.t](../by-file/en_us.t.md) (line 3669)


Typographical effects output filter. This filter looks for certain sequences in the text and converts them to typographical equivalents. Authors could simply write the HTML for the typographical markups in the first place, but it's easier to write the typewriter-like sequences and let this filter convert to HTML.


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > **typographicalOutputFilter**


## Properties


### `abbreviations`

Defined in en_us.t, line 3751

Common abbreviations. These are excluded from being treated as sentence endings when they appear with a trailing period.


### `abbrevPat`

Defined in en_us.t, line 3739

pattern for abbreviations that were mistaken for sentence endings


### `eosPattern`

Defined in en_us.t, line 3726

The end-of-sentence pattern. This looks a bit complicated, but all we're looking for is a period, exclamation point, or question mark, optionally followed by any number of closing group marks (right parentheses or square brackets, closing HTML tags, or double or single quotes in either straight or curly styles), all followed by an ordinary space.


## Methods


### `filterText(ostr, val)` *(overridden)*

Defined in en_us.t, line 3670
