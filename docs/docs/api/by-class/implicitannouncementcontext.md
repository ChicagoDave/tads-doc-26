# ImplicitAnnouncementContext

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 8007)


Implicit action context. This is passed to the message methods that generate implicit action announcements, to indicate the context in which the message is to be used.


**Superclass chain:** `object` > **ImplicitAnnouncementContextSubclasses:** [ListImpCtx](listimpctx.md)


**Global objects:** [standardImpCtx](standardimpctx.md), [tryingImpCtx](tryingimpctx.md)


## Properties


### `getVerbCtx`

Defined in en_us.t, line 8026

our getVerbPhrase context - by default, don't use one


### `isInList`

Defined in en_us.t, line 8016

is this message going in a list?


### `isInSublist`

Defined in en_us.t, line 8023

Are we in a sublist of 'just trying' or 'just asking' messages? (We can only have sublist groupings one level deep, so we don't need to worry about what kind of sublist we're in.)


### `useInfPhrase`

Defined in en_us.t, line 8013

Should we use the infinitive form of the verb, or the participle form for generating the announcement? By default, use use the participle form: "(first OPENING THE BOX)".


## Methods


### `buildImplicitAnnouncement(txt)`

Defined in en_us.t, line 8029

generate the announcement message given the action description
