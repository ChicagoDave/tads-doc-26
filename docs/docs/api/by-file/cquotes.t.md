# cquotes.t


** cquotes: a TADS 3 output filter for making single curly quotes  To use, just add to your project. The PreinitObject at the end ** of this file automatically registers the curly quote output filter.  You may use this module in your own game. You may distribute ** modified versions of this file, though I would prefer you contact ** me first at stephen@granades.com and see about having me add your ** changes to my source.  Version: 0.2 (2 Feb 2004) ** Added in fixes for patIsHTMLTag and patIsFormatTag from ** Matt McGlone ** 0.1 (27 Aug 2002) ** Original release  Copyright (c) 2002, 2004 by Stephen Granade. All Rights Reserved.


## Global Objects

- [cquoteOutputFilter](../by-class/cquoteoutputfilter.md)
- //
- //
- filterText
- if
- if
- if


## Functions


### `//(since, e, ., g, ., ", \, <, font, face, =, ', courier, >, ", isn, ', t, really, an, HTML, tag)`

Defined in cquotes.t, line 66


### `//(Possessive, ', s, is, handled, by, the, contraction, .)`

Defined in cquotes.t, line 83


### `filterText(ostr, val, ., substr, (, ret, [1], +, ret, [2], val, ., length, ()`

Defined in cquotes.t, line 70


### `if(aggressive)`

Defined in cquotes.t, line 76


### `if(ret, =, =, nil)`

Defined in cquotes.t, line 58


### `if(ret, !, =, nil, &, &, (, ret, [1], =, =, 1, |, |, val, ., substr, (, ret, [1], -, 1, 1)`

Defined in cquotes.t, line 67
