# ListImpCtx

*class* — defined in [en_us.t](../by-file/en_us.t.md) (line 8080)


A class for messages appearing in a list. Within a list, we want to keep track of the last direct object, so that we can refer to it with a pronoun later in the list.


**Superclass chain:** [ImplicitAnnouncementContext](implicitannouncementcontext.md) > `object` > [GetVerbPhraseContext](getverbphrasecontext.md) > **ListImpCtx**


## Properties


### `baseCtx`

Defined in en_us.t, line 8112

our base context - we delegate some unoverridden behavior to this


### `getVerbCtx` *(overridden)*

Defined in en_us.t, line 8103

we are our own getVerbPhrase context


### `isInList` *(overridden)*

Defined in en_us.t, line 8100

we're in a list


### `useInfPhrase` *(overridden)*

Defined in en_us.t, line 8106

delegate the phrase format to our underlying announcement context


## Inherited Properties


*From [ImplicitAnnouncementContext](implicitannouncementcontext.md):* [`isInSublist`](implicitannouncementcontext.md#isInSublist)


*From [GetVerbPhraseContext](getverbphrasecontext.md):* [`pronounObj`](getverbphrasecontext.md#pronounObj)


## Methods


### `buildImplicitAnnouncement(txt)` *(overridden)*

Defined in en_us.t, line 8109

build the announcement using our underlying context


### `setBaseCtx(ctx)`

Defined in en_us.t, line 8085

Set the appropriate base context for the given implicit action announcement report (an ImplicitActionAnnouncement object).


## Inherited Methods


*From [GetVerbPhraseContext](getverbphrasecontext.md):* [`isObjPronoun`](getverbphrasecontext.md#isObjPronoun), [`objNameObj`](getverbphrasecontext.md#objNameObj), [`setPronounObj`](getverbphrasecontext.md#setPronounObj)
