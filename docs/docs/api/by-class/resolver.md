# Resolver

*class* — defined in [resolver.t](../by-file/resolver.t.md) (line 31)


Basic object resolver. An Action object creates an object resolver to mediate the process of resolving noun phrases to objects.


**Superclass chain:** `object` > **Resolver**


<details><summary>Subclasses (277)</summary>

- [ActorResolver](actorresolver.md)
- [IobjResolver](iobjresolver.md)
- [TAction](taction.md)
- [AttackAction](attackaction.md)
- [predicate(Attack)](predicate%28attack%29.md)
- [BoardAction](boardaction.md)
- [predicate(Board)](predicate%28board%29.md)
- [BreakAction](breakaction.md)
- [predicate(Break)](predicate%28break%29.md)
- [BurnAction](burnaction.md)
- [predicate(Burn)](predicate%28burn%29.md)
- [CleanAction](cleanaction.md)
- [predicate(Clean)](predicate%28clean%29.md)
- [ClimbAction](climbaction.md)
- [predicate(Climb)](predicate%28climb%29.md)
- [ClimbDownAction](climbdownaction.md)
- [predicate(ClimbDown)](predicate%28climbdown%29.md)
- [predicate(ClimbDownWhat)](predicate%28climbdownwhat%29.md)
- [ClimbUpAction](climbupaction.md)
- [predicate(ClimbUp)](predicate%28climbup%29.md)
- [predicate(ClimbUpWhat)](predicate%28climbupwhat%29.md)
- [CloseAction](closeaction.md)
- [predicate(Close)](predicate%28close%29.md)
- [ConsultAction](consultaction.md)
- [predicate(Consult)](predicate%28consult%29.md)
- [CutAction](cutaction.md)
- [DetachAction](detachaction.md)
- [predicate(Detach)](predicate%28detach%29.md)
- [DigAction](digaction.md)
- [predicate(Dig)](predicate%28dig%29.md)
- [DoffAction](doffaction.md)
- [predicate(Doff)](predicate%28doff%29.md)
- [DrinkAction](drinkaction.md)
- [predicate(Drink)](predicate%28drink%29.md)
- [DropAction](dropaction.md)
- [predicate(Drop)](predicate%28drop%29.md)
- [EatAction](eataction.md)
- [predicate(Eat)](predicate%28eat%29.md)
- [EnterAction](enteraction.md)
- [predicate(Enter)](predicate%28enter%29.md)
- [ExamineAction](examineaction.md)
- [predicate(Examine)](predicate%28examine%29.md)
- [ExtinguishAction](extinguishaction.md)
- [predicate(Extinguish)](predicate%28extinguish%29.md)
- [FastenAction](fastenaction.md)
- [predicate(Fasten)](predicate%28fasten%29.md)
- [FeelAction](feelaction.md)
- [predicate(Feel)](predicate%28feel%29.md)
- [FlipAction](flipaction.md)
- [predicate(Flip)](predicate%28flip%29.md)
- [FollowAction](followaction.md)
- [predicate(Follow)](predicate%28follow%29.md)
- [GetOffOfAction](getoffofaction.md)
- [predicate(GetOffOf)](predicate%28getoffof%29.md)
- [GetOutOfAction](getoutofaction.md)
- [predicate(GetOutOf)](predicate%28getoutof%29.md)
- [GoThroughAction](gothroughaction.md)
- [predicate(GoThrough)](predicate%28gothrough%29.md)
- [JumpOffAction](jumpoffaction.md)
- [predicate(JumpOff)](predicate%28jumpoff%29.md)
- [JumpOverAction](jumpoveraction.md)
- [predicate(JumpOver)](predicate%28jumpover%29.md)
- [KissAction](kissaction.md)
- [predicate(Kiss)](predicate%28kiss%29.md)
- [LieOnAction](lieonaction.md)
- [predicate(LieOn)](predicate%28lieon%29.md)
- [LightAction](lightaction.md)
- [predicate(Light)](predicate%28light%29.md)
- [ListenToAction](listentoaction.md)
- [predicate(ListenTo)](predicate%28listento%29.md)
- [LiteralTAction](literaltaction.md)
- [EnterOnAction](enteronaction.md)
- [predicate(EnterOn)](predicate%28enteron%29.md)
- [predicate(EnterOnWhat)](predicate%28enteronwhat%29.md)
- [SetToAction](settoaction.md)
- [predicate(SetTo)](predicate%28setto%29.md)
- [TurnToAction](turntoaction.md)
- [predicate(TurnTo)](predicate%28turnto%29.md)
- [TypeLiteralOnAction](typeliteralonaction.md)
- [predicate(TypeLiteralOn)](predicate%28typeliteralon%29.md)
- [predicate(TypeLiteralOnWhat)](predicate%28typeliteralonwhat%29.md)
- [LockAction](lockaction.md)
- [predicate(Lock)](predicate%28lock%29.md)
- [LookBehindAction](lookbehindaction.md)
- [predicate(LookBehind)](predicate%28lookbehind%29.md)
- [LookInAction](lookinaction.md)
- [predicate(LookIn)](predicate%28lookin%29.md)
- [LookThroughAction](lookthroughaction.md)
- [predicate(LookThrough)](predicate%28lookthrough%29.md)
- [LookUnderAction](lookunderaction.md)
- [predicate(LookUnder)](predicate%28lookunder%29.md)
- [MoveAction](moveaction.md)
- [predicate(Move)](predicate%28move%29.md)
- [OpenAction](openaction.md)
- [predicate(Open)](predicate%28open%29.md)
- [PlugInAction](pluginaction.md)
- [predicate(PlugIn)](predicate%28plugin%29.md)
- [PourAction](pouraction.md)
- [predicate(Pour)](predicate%28pour%29.md)
- [PullAction](pullaction.md)
- [predicate(Pull)](predicate%28pull%29.md)
- [PushAction](pushaction.md)
- [predicate(Push)](predicate%28push%29.md)
- [PushTravelAction](pushtravelaction.md)
- [PushTravelDirAction](pushtraveldiraction.md)
- [predicate(PushTravelDir)](predicate%28pushtraveldir%29.md)
- [PushAftAction](pushaftaction.md)
- [PushDownAction](pushdownaction.md)
- [PushEastAction](pusheastaction.md)
- [PushForeAction](pushforeaction.md)
- [PushInAction](pushinaction.md)
- [PushNorthAction](pushnorthaction.md)
- [PushNortheastAction](pushnortheastaction.md)
- [PushNorthwestAction](pushnorthwestaction.md)
- [PushOutAction](pushoutaction.md)
- [PushPortAction](pushportaction.md)
- [PushSouthAction](pushsouthaction.md)
- [PushSoutheastAction](pushsoutheastaction.md)
- [PushSouthwestAction](pushsouthwestaction.md)
- [PushStarboardAction](pushstarboardaction.md)
- [PushUpAction](pushupaction.md)
- [PushWestAction](pushwestaction.md)
- [PushTravelViaIobjAction](pushtravelviaiobjaction.md)
- [PushTravelClimbDownAction](pushtravelclimbdownaction.md)
- [predicate(PushTravelClimbDown)](predicate%28pushtravelclimbdown%29.md)
- [PushTravelClimbUpAction](pushtravelclimbupaction.md)
- [predicate(PushTravelClimbUp)](predicate%28pushtravelclimbup%29.md)
- [PushTravelEnterAction](pushtravelenteraction.md)
- [predicate(PushTravelEnter)](predicate%28pushtravelenter%29.md)
- [PushTravelGetOutOfAction](pushtravelgetoutofaction.md)
- [predicate(PushTravelGetOutOf)](predicate%28pushtravelgetoutof%29.md)
- [PushTravelThroughAction](pushtravelthroughaction.md)
- [predicate(PushTravelThrough)](predicate%28pushtravelthrough%29.md)
- [ReadAction](readaction.md)
- [predicate(Read)](predicate%28read%29.md)
- [RemoveAction](removeaction.md)
- [predicate(Remove)](predicate%28remove%29.md)
- [ScrewAction](screwaction.md)
- [predicate(Screw)](predicate%28screw%29.md)
- [SearchAction](searchaction.md)
- [predicate(Search)](predicate%28search%29.md)
- [SetAction](setaction.md)
- [predicate(Set)](predicate%28set%29.md)
- [SitOnAction](sitonaction.md)
- [predicate(SitOn)](predicate%28siton%29.md)
- [SmellAction](smellaction.md)
- [predicate(Smell)](predicate%28smell%29.md)
- [StandOnAction](standonaction.md)
- [predicate(StandOn)](predicate%28standon%29.md)
- [StrikeAction](strikeaction.md)
- [predicate(Strike)](predicate%28strike%29.md)
- [SwitchAction](switchaction.md)
- [predicate(Switch)](predicate%28switch%29.md)
- [TakeAction](takeaction.md)
- [predicate(Take)](predicate%28take%29.md)
- [TalkToAction](talktoaction.md)
- [predicate(TalkTo)](predicate%28talkto%29.md)
- [predicate(TalkToWhat)](predicate%28talktowhat%29.md)
- [TasteAction](tasteaction.md)
- [predicate(Taste)](predicate%28taste%29.md)
- [ThrowAction](throwaction.md)
- [predicate(Throw)](predicate%28throw%29.md)
- [ThrowDirAction](throwdiraction.md)
- [predicate(ThrowDir)](predicate%28throwdir%29.md)
- [predicate(ThrowDirDown)](predicate%28throwdirdown%29.md)
- [TIAction](tiaction.md)
- [AttachToAction](attachtoaction.md)
- [predicate(AttachTo)](predicate%28attachto%29.md)
- [predicate(AttachToWhat)](predicate%28attachtowhat%29.md)
- [AttackWithAction](attackwithaction.md)
- [predicate(AttackWith)](predicate%28attackwith%29.md)
- [BurnWithAction](burnwithaction.md)
- [predicate(BurnWith)](predicate%28burnwith%29.md)
- [CleanWithAction](cleanwithaction.md)
- [predicate(CleanWith)](predicate%28cleanwith%29.md)
- [CutWithAction](cutwithaction.md)
- [predicate(CutWith)](predicate%28cutwith%29.md)
- [predicate(CutWithWhat)](predicate%28cutwithwhat%29.md)
- [DetachFromAction](detachfromaction.md)
- [predicate(DetachFrom)](predicate%28detachfrom%29.md)
- [DigWithAction](digwithaction.md)
- [predicate(DigWith)](predicate%28digwith%29.md)
- [FastenToAction](fastentoaction.md)
- [predicate(FastenTo)](predicate%28fastento%29.md)
- [GiveToAction](givetoaction.md)
- [predicate(GiveTo)](predicate%28giveto%29.md)
- [predicate(GiveToType2)](predicate%28givetotype2%29.md)
- [predicate(GiveToWhom)](predicate%28givetowhom%29.md)
- [LockWithAction](lockwithaction.md)
- [predicate(LockWith)](predicate%28lockwith%29.md)
- [MoveToAction](movetoaction.md)
- [predicate(MoveTo)](predicate%28moveto%29.md)
- [MoveWithAction](movewithaction.md)
- [predicate(MoveWith)](predicate%28movewith%29.md)
- [PlugIntoAction](plugintoaction.md)
- [predicate(PlugInto)](predicate%28pluginto%29.md)
- [predicate(PlugIntoWhat)](predicate%28plugintowhat%29.md)
- [PourIntoAction](pourintoaction.md)
- [predicate(PourInto)](predicate%28pourinto%29.md)
- [PourOntoAction](pourontoaction.md)
- [predicate(PourOnto)](predicate%28pouronto%29.md)
- [PutBehindAction](putbehindaction.md)
- [predicate(PutBehind)](predicate%28putbehind%29.md)
- [PutInAction](putinaction.md)
- [predicate(PutIn)](predicate%28putin%29.md)
- [predicate(PutInWhat)](predicate%28putinwhat%29.md)
- [PutOnAction](putonaction.md)
- [predicate(PutOn)](predicate%28puton%29.md)
- [PutUnderAction](putunderaction.md)
- [predicate(PutUnder)](predicate%28putunder%29.md)
- [ScrewWithAction](screwwithaction.md)
- [predicate(ScrewWith)](predicate%28screwwith%29.md)
- [ShowToAction](showtoaction.md)
- [predicate(ShowTo)](predicate%28showto%29.md)
- [predicate(ShowToType2)](predicate%28showtotype2%29.md)
- [predicate(ShowToWhom)](predicate%28showtowhom%29.md)
- [TakeFromAction](takefromaction.md)
- [predicate(TakeFrom)](predicate%28takefrom%29.md)
- [ThrowAtAction](throwataction.md)
- [predicate(ThrowAt)](predicate%28throwat%29.md)
- [ThrowToAction](throwtoaction.md)
- [predicate(ThrowTo)](predicate%28throwto%29.md)
- [predicate(ThrowToType2)](predicate%28throwtotype2%29.md)
- [TurnWithAction](turnwithaction.md)
- [predicate(TurnWith)](predicate%28turnwith%29.md)
- [UnfastenFromAction](unfastenfromaction.md)
- [predicate(UnfastenFrom)](predicate%28unfastenfrom%29.md)
- [UnlockWithAction](unlockwithaction.md)
- [predicate(UnlockWith)](predicate%28unlockwith%29.md)
- [UnplugFromAction](unplugfromaction.md)
- [predicate(UnplugFrom)](predicate%28unplugfrom%29.md)
- [UnscrewWithAction](unscrewwithaction.md)
- [predicate(UnscrewWith)](predicate%28unscrewwith%29.md)
- [TopicTAction](topictaction.md)
- [AskVagueAction](askvagueaction.md)
- [predicate(AskVague)](predicate%28askvague%29.md)
- [predicate(TellVague)](predicate%28tellvague%29.md)
- [ConsultAboutAction](consultaboutaction.md)
- [predicate(ConsultAbout)](predicate%28consultabout%29.md)
- [predicate(ConsultWhatAbout)](predicate%28consultwhatabout%29.md)
- [ConvTopicTAction](convtopictaction.md)
- [AskAboutAction](askaboutaction.md)
- [predicate(AskAbout)](predicate%28askabout%29.md)
- [predicate(AskAboutImplicit)](predicate%28askaboutimplicit%29.md)
- [predicate(AskAboutWhat)](predicate%28askaboutwhat%29.md)
- [AskForAction](askforaction.md)
- [predicate(AskFor)](predicate%28askfor%29.md)
- [predicate(AskWhomFor)](predicate%28askwhomfor%29.md)
- [TellAboutAction](tellaboutaction.md)
- [predicate(TellAbout)](predicate%28tellabout%29.md)
- [predicate(TellAboutImplicit)](predicate%28tellaboutimplicit%29.md)
- [predicate(TellAboutWhat)](predicate%28tellaboutwhat%29.md)
- [TellVagueAction](tellvagueaction.md)
- [TravelViaAction](travelviaaction.md)
- [EnTravelVia](entravelvia.md)
- [TurnAction](turnaction.md)
- [predicate(Turn)](predicate%28turn%29.md)
- [TurnOffAction](turnoffaction.md)
- [predicate(TurnOff)](predicate%28turnoff%29.md)
- [TurnOnAction](turnonaction.md)
- [predicate(TurnOn)](predicate%28turnon%29.md)
- [TypeOnAction](typeonaction.md)
- [predicate(TypeOn)](predicate%28typeon%29.md)
- [UnfastenAction](unfastenaction.md)
- [predicate(Unfasten)](predicate%28unfasten%29.md)
- [UnlockAction](unlockaction.md)
- [predicate(Unlock)](predicate%28unlock%29.md)
- [UnplugAction](unplugaction.md)
- [predicate(Unplug)](predicate%28unplug%29.md)
- [UnscrewAction](unscrewaction.md)
- [predicate(Unscrew)](predicate%28unscrew%29.md)
- [WearAction](wearaction.md)
- [predicate(Wear)](predicate%28wear%29.md)
- [TopicQualifierResolver](topicqualifierresolver.md)
- [TopicResolver](topicresolver.md)
- [ConvTopicResolver](convtopicresolver.md)
- [TActionTopicResolver](tactiontopicresolver.md)

</details>


## Properties


### `action_`

Defined in resolver.t, line 740

my action


### `actor_`

Defined in resolver.t, line 746

the target actor object


### `equivs_`

Defined in resolver.t, line 753

List of equivalent objects we've resolved so far. We use this to try to return different equivalent objects when multiple noun phrases refer to the same set of equivalents.


### `isGlobalScope`

Defined in resolver.t, line 186

Is this a "global" scope? By default, the scope is local: it's limited to what the actor can see, hear, etc. In some cases, the scope is broader, and extends beyond the senses; we call those cases global scope.


### `isSubResolver`

Defined in resolver.t, line 47

Are we a sub-phrase resolver? This should return true if we're being used to resolve a sub-phrase of the main phrase.


### `issuer_`

Defined in resolver.t, line 743

the issuing actor


### `scope_`

Defined in resolver.t, line 737

The cached scope list, if we have one. Note that this is an internal implementation detail of the base class; subclasses can dispense with the cached scope list if they define their own objInScope() and getScopeList() overrides.


### `whichMessageObject`

Defined in resolver.t, line 723

Get an indication of which object we're resolving, for message generation purposes. By default, we'll indicate direct object; this should be overridden for resolvers of indirect and other types of objects.


### `whichObject`

Defined in resolver.t, line 715

the role played by this object, if any


## Methods


### `allowAll`

Defined in resolver.t, line 397

Determine if "all" is allowed for the noun phrase we're resolving. By default, we'll just ask the action.


### `cacheScopeList`

Defined in resolver.t, line 108

Cache the scope list for this object. By default, we cache the standard physical scope list for our target actor.


### `construct(action, issuingActor, targetActor)`

Defined in resolver.t, line 32


### `filterAll(lst, whichObj, np)`

Defined in resolver.t, line 427

Filter an 'all' list to remove things that don't belong. We always remove the actor executing the command, as well as any objects explicitly marked as hidden from 'all' lists.


### `filterAmbiguousEquivalents(lst, np)`

Defined in resolver.t, line 545

Filter a list of ambiguous matches ('lst') for a noun phrase, to reduce each set of equivalent items to a single such item, if desired. If no equivalent reduction is desired for this type of resolver, this can simply return the original list.


### `filterAmbiguousNounPhrase(lst, requiredNum, np)`

Defined in resolver.t, line 505

Filter an ambiguous list of objects ('lst') resolving to a noun phrase. If the objects in the list vary in the degree of suitability for the command, returns a list consisting only of the most suitable objects. If the objects are all equally suitable - or equally unsuitable - the whole list should be returned unchanged.


### `filterPluralPhrase(lst, np)`

Defined in resolver.t, line 634

Filter a plural phrase to reduce the set to the logical subset, if possible. If there is no logical subset, simply return the original set.


### `filterPossRank(lst, num)`

Defined in resolver.t, line 517

Filter an ambiguous noun phrase list using the strength of possessive qualification, if any. If we have subsets at different possessive strengths, choose the strongest subset that has at least the required number of objects.


### `getAction`

Defined in resolver.t, line 60

get the action we're resolving


### `getAll(np)`

Defined in resolver.t, line 409

Get the "all" list - this is the list of objects that we should use when the object of the command is the special word "all". We'll ask the action to resolve 'all' for the direct object, since we are by default a direct object resolver.


### `getAllDefaults`

Defined in resolver.t, line 465

Get the list of potential default objects. This is simply the basic 'all' list, not filtered for exclusion with hideFromAll.


### `getDefaultObject(np)`

Defined in resolver.t, line 671

Get the default object or objects for this phrase. Returns a list of ResolveInfo objects if a default is available, or nil if no default is available. This routine does not interact with the user; it should merely determine if the command implies a default strongly enough to assume it without asking the user.


### `getPossessiveResolver`

Defined in resolver.t, line 95

Get the resolver for possessive phrases. By default, we return a standard possessive resolver. This can be overridden in contexts wher ethe possesive resolution context is special.


### `getPronounDefault(typ, np)`

Defined in en_us.t, line 3304

Get the default in-scope object list for a given pronoun. We'll look for a unique object in scope that matches the desired pronoun, and return a ResolveInfo list if we find one. If there aren't any objects in scope that match the pronoun, or multiple objects are in scope, there's no default.


### `getQualifierResolver`

Defined in resolver.t, line 88

Get the resolver for qualifier phrases. By default, this simply returns myself, since the resolver for qualifiers is in most contexts the same as the main resolver.


### `getRawPronounAntecedent(typ)`

Defined in resolver.t, line 301

Get the "raw" pronoun antecedent list for a given pronoun selector. This returns a list of objects matching the pronoun. The list is raw in that it is given as a list of game objects (not ResolveInfo objects), and it isn't filtered for scope.


### `getReflexiveBinding(typ)`

Defined in resolver.t, line 196

Get the binding for a reflexive third-person pronoun (himself, herself, itself, themselves). By default, the reflexive binding is the anaphoric binding from the action - that is, it refers back to the preceding noun phrase in a verb phrase with multiple noun slots (as in ASK BOB ABOUT HIMSELF: 'himself' refers back to 'bob', the previous noun phrase).


### `getScopeList`

Defined in resolver.t, line 168

Get the full list of objects in scope. By default, this simply returns our cached scope list.


### `getTargetActor`

Defined in resolver.t, line 63

get the target actor


### `matchName(obj, origTokens, adjustedTokens)`

Defined in resolver.t, line 71

Match an object's name. By default, we'll call the object's own matchName method with the given original and adjusted token lists. Subclasses can override this to call different match methods (such as matchNameDisambig).


### `objInScope(obj)`

Defined in resolver.t, line 136

Determine if an object is in scope for the purposes of object resolution. By default, we'll return true if the object is in our cached scope list - this ensures that we produce results that are consistent with getScopeList().


### `resetResolver`

Defined in resolver.t, line 53

Reset the resolver - this can be called if we are to re-use the same resolver to resolve a list of noun phrases again.


### `resolvePronounAntecedent(typ, np, results, poss)`

Defined in resolver.t, line 205

Resolve a pronoun antecedent, given a pronoun selector. This returns a list of ResolveInfo objects, for use in object resolution. 'poss' is true if this is a possessive pronoun (his, her, its, etc), nil if it's an ordinary, non-possessive pronoun (him, her, it, etc).


### `resolveUnknownNounPhrase(tokList)`

Defined in resolver.t, line 696

Resolve a noun phrase involving unknown words, if possible. If it is not possible to resolve such a phrase, return nil; otherwise, return a list of resolved objects. This routine does not interact with the user - "oops" prompting is handled separately.


### `selectIndefinite(results, lst, requiredNumber)`

Defined in resolver.t, line 651

Select a resolution for an indefinite noun phrase ("a coin"), given a list of possible matches. The matches will be given to us sorted from most likely to least likely, as done by filterAmbiguousNounPhrase().


### `withGlobals(func)`

Defined in resolver.t, line 708

Execute a callback function in the global context of our actor and action - we'll set gActor and gAction to our own stored actor and action values, then call the callback, then restore the old globals.
