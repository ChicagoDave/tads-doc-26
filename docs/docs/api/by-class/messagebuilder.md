# MessageBuilder

*class* — defined in [output.t](../by-file/output.t.md) (line 1070)


MessageBuilder - this object provides a general text substitution mechanism. Text to be substituted is enclosed in {curly braces}. Within the braces, we have the substitution parameter name, which can be in the following formats:


**Superclass chain:** [OutputFilter](outputfilter.md) > `object` > [PreinitObject](preinitobject.md) > [ModuleExecObject](moduleexecobject.md) > **MessageBuilderGlobal objects:** [langMessageBuilder](langmessagebuilder.md)


## Properties


### `lastParamObj_`

Defined in output.t, line 1513

the parameter name of the last target object ('dobj', 'actor', etc)


### `lastTargetObj_`

Defined in output.t, line 1510

The most recent target object. Each time we parse a substitution string, we'll remember the target object here; when a substitution string doesn't imply or specify a target object, we'll use the previous one by default.


### `nameTable_`

Defined in output.t, line 1519

our global name table - a LookupTable we set up during preinit


### `paramList_`

Defined in output.t, line 1581

our parameter list - this should be initialized in the language-specific subclass to a list like this:


### `paramTable_`

Defined in output.t, line 1516

our parameter table - a LookupTable that we set up during preinit


### `patAllCaps`

Defined in output.t, line 1073


### `patIdObj`

Defined in output.t, line 1076


### `patIdObjSlashId`

Defined in output.t, line 1074


### `patIdSlash`

Defined in output.t, line 1077


### `patUpper`

Defined in output.t, line 1072

pre-compile some regular expressions we use a lot


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in output.t, line 1472

execute pre-initialization


### `filterText(ostr, txt)` *(overridden)*

Defined in output.t, line 1498

Our output filter method. We'll run each string written to the display through our parameter substitution method.


### `generateMessage(orig)`

Defined in output.t, line 1084

Given a source string with substitution parameters, generate the expanded message with the appropriate text in place of the parameters.


### `genLiteral(str)`

Defined in output.t, line 1463

Internal routine - generate the literal text for the given source string. We'll remove any stuttered close braces.


### `getTargetProp(targetObj, paramObj, info)`

Defined in output.t, line 1410

Get the property to invoke on the target object for the given parameter information entry. By default, we simply return info[2], which is the standard property to call on the target. This can be overridden by the language-specific subclass to provide a different property if appropriate.


### `langRewriteParam(paramStr)`

Defined in output.t, line 1529

Rewrite the parameter string for any language-specific rules. By default, we'll return the original parameter string unchanged; the language-specific instance can override this to provide any special syntax extensions to the parameter string syntax desired by the language-specific library. The returned string must be in one of the formats recognized by the generic handler.


### `processResult(txt)`

Defined in output.t, line 1442

Process result text. This takes some result text that we're about to add and returns a processed version. This is called for all text as we add it to the result string.


### `quoteMessage(str)`

Defined in output.t, line 1454

"Quote" a message - double each open or close brace, so that braces in the message will be taken literally when run through the substitution replacer. This can be used when a message is expanded prior to being displayed to ensure that braces in the result won't be mistaken as substitution parameters requiring further expansion.


## Inherited Methods


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
