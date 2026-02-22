# ResolveAsker

*class* — defined in [parser.t](../by-file/parser.t.md) (line 312)


Noun phrase resolver "asker." This type of object can be passed to certain ResolveResults methods in order to customize the messages that the parser generates for interactive prompting.


**Superclass chain:** `object` > **ResolveAskerSubclasses:** [AskConnector](askconnector.md), [DefaultAskConnector](defaultaskconnector.md)


**Global objects:** [enterOnWhatAsker](enteronwhatasker.md)


## Methods


### `askDisambig(targetActor, promptTxt, curMatchList, fullMatchList, requiredNum, askingAgain, dist)`

Defined in parser.t, line 318

Ask for help disambiguating a noun phrase. This asks which of several possible matching objects was intended. This method has the same parameter list as the equivalent message object method.


### `askMissingObject(targetActor, action, which)`

Defined in parser.t, line 332

Ask for a missing object. This prompts for an object that's structurally required for an action, but which was omitted from the player's command.
