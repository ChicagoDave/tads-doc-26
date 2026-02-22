# langMessageBuilder

*object* — defined in [en_us.t](../by-file/en_us.t.md) (line 3758)


The English-specific message builder.


**Superclass chain:** [MessageBuilder](messagebuilder.md) > [OutputFilter](outputfilter.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **langMessageBuilder**


## Properties


### `fixedTenseProp_`

Defined in en_us.t, line 4249

This property is used to temporarily store either a boolean value indicating whether the last encountered parameter string had an exclamation mark at the end of any word, or a property to be invoked by Thing.propWithPresentMessageBuilder_. This field is for internal use only; authors shouldn't have any reason to access it directly.


### `lastSubject_`

Defined in en_us.t, line 4053

The most recent target object used in the nominative case. We note this so that we can supply reflexive mappings when the same object is re-used in the objective case. This allows us to map things like "you can't take you" to the better-sounding "you can't take yourself".


### `lastSubjectName_`

Defined in en_us.t, line 4056

the parameter name of the last subject ('dobj', 'actor', etc)


### `paramList_` *(overridden)*

Defined in en_us.t, line 3777

The English message substitution parameter table.


### `pastEnding_`

Defined in en_us.t, line 4239

This property is used to temporarily store the past-tense ending of a verb to be displayed by Thing.verbEndingSMessageBuilder_. It's for internal use only; game authors shouldn't have any reason to access it directly.


### `patEndOfSentence`

Defined in en_us.t, line 4125

end-of-sentence match pattern


### `patIdObjApostS`

Defined in en_us.t, line 4159


### `patIdObjSlashIdApostS`

Defined in en_us.t, line 4157

some pre-compiled search patterns we use a lot


### `patParamWithExclam`

Defined in en_us.t, line 4161


### `patSpecial`

Defined in en_us.t, line 4027

Pre-compiled regular expression pattern matching any sequence with a special meaning in a message string.


### `patSSlashLetterEd`

Defined in en_us.t, line 4162


### `patTenseSwitching`

Defined in en_us.t, line 4040

Pre-compiled regular expression pattern matching our special tense-switching syntax.


## Inherited Properties


*From [MessageBuilder](messagebuilder.md):* [`lastParamObj_`](messagebuilder.md#lastParamObj_), [`lastTargetObj_`](messagebuilder.md#lastTargetObj_), [`nameTable_`](messagebuilder.md#nameTable_), [`paramTable_`](messagebuilder.md#paramTable_), [`patAllCaps`](messagebuilder.md#patAllCaps), [`patIdObj`](messagebuilder.md#patIdObj), [`patIdObjSlashId`](messagebuilder.md#patIdObjSlashId), [`patIdSlash`](messagebuilder.md#patIdSlash), [`patUpper`](messagebuilder.md#patUpper)


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `generateMessage(orig)` *(overridden)*

Defined in en_us.t, line 3912

Add a hook to the generateMessage method, which we use to pre-process the source string before expanding the substitution parameters.


### `getTargetProp(targetObj, paramObj, info)` *(overridden)*

Defined in en_us.t, line 4069

Get the target object property mapping. If the target object is the same as the most recent subject object (i.e., the last object used in the nominative case), and this parameter has a reflexive form property, we'll return the reflexive form property. Otherwise, we'll return the standard property mapping.


### `langRewriteParam(paramStr)` *(overridden)*

Defined in en_us.t, line 4184

Rewrite a parameter string for a language-specific syntax extension.


### `processOrig(str)`

Defined in en_us.t, line 3941

Pre-process a source string containing substitution parameters, before generating the expanded message from it.


### `processResult(txt)` *(overridden)*

Defined in en_us.t, line 4130

Process result text.


## Inherited Methods


*From [MessageBuilder](messagebuilder.md):* [`execute`](messagebuilder.md#execute), [`filterText`](messagebuilder.md#filterText), [`genLiteral`](messagebuilder.md#genLiteral), [`quoteMessage`](messagebuilder.md#quoteMessage)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
