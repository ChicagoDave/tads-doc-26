# Thing

*class* — defined in [thing.t](../by-file/thing.t.md) (line 1075)


Thing: the basic class for game objects. An object of this class represents a physical object in the simulation.


**Superclass chain:** [VocabObject](vocabobject.md) > `object` > **Thing**


<details><summary>Subclasses (118)</summary>

- [Actor](actor.md)
- [UntakeableActor](untakeableactor.md)
- [Person](person.md)
- [BasicLocation](basiclocation.md)
- [NestedRoom](nestedroom.md)
- [BasicChair](basicchair.md)
- [BasicBed](basicbed.md)
- [BasicPlatform](basicplatform.md)
- [Booth](booth.md)
- [Platform](platform.md)
- [NominalPlatform](nominalplatform.md)
- [Bed](bed.md)
- [Chair](chair.md)
- [HighNestedRoom](highnestedroom.md)
- [Vehicle](vehicle.md)
- [Room](room.md)
- [DarkRoom](darkroom.md)
- [FloorlessRoom](floorlessroom.md)
- [OutdoorRoom](outdoorroom.md)
- [ShipboardRoom](shipboardroom.md)
- [BulkLimiter](bulklimiter.md)
- [BasicContainer](basiccontainer.md)
- [Container](container.md)
- [Dispenser](dispenser.md)
- [Matchbook](matchbook.md)
- [OpenableContainer](openablecontainer.md)
- [KeyedContainer](keyedcontainer.md)
- [LockableContainer](lockablecontainer.md)
- [RestrictedContainer](restrictedcontainer.md)
- [SingleContainer](singlecontainer.md)
- [StretchyContainer](stretchycontainer.md)
- [SpaceOverlay](spaceoverlay.md)
- [RearContainer](rearcontainer.md)
- [RearSurface](rearsurface.md)
- [RestrictedRearSurface](restrictedrearsurface.md)
- [RestrictedRearContainer](restrictedrearcontainer.md)
- [Underside](underside.md)
- [RestrictedUnderside](restrictedunderside.md)
- [Surface](surface.md)
- [RestrictedSurface](restrictedsurface.md)
- [Button](button.md)
- [CollectiveGroup](collectivegroup.md)
- [ItemizingCollectiveGroup](itemizingcollectivegroup.md)
- [ComplexContainer](complexcontainer.md)
- [Consultable](consultable.md)
- [Dispensable](dispensable.md)
- [FillMedium](fillmedium.md)
- [Food](food.md)
- [Hidden](hidden.md)
- [Intangible](intangible.md)
- [DistanceConnector](distanceconnector.md)
- [SensoryEmanation](sensoryemanation.md)
- [Noise](noise.md)
- [SimpleNoise](simplenoise.md)
- [Odor](odor.md)
- [SimpleOdor](simpleodor.md)
- [Vaporous](vaporous.md)
- [Key](key.md)
- [Keyring](keyring.md)
- [Lever](lever.md)
- [SpringLever](springlever.md)
- [LightSource](lightsource.md)
- [Flashlight](flashlight.md)
- [FueledLightSource](fueledlightsource.md)
- [Candle](candle.md)
- [Matchstick](matchstick.md)
- [NonPortable](nonportable.md)
- [Fixture](fixture.md)
- [Component](component.md)
- [ComplexComponent](complexcomponent.md)
- [ContainerDoor](containerdoor.md)
- [CustomFixture](customfixture.md)
- [Decoration](decoration.md)
- [Unthing](unthing.md)
- [Distant](distant.md)
- [Enterable](enterable.md)
- [EntryPortal](entryportal.md)
- [Exitable](exitable.md)
- [ExitPortal](exitportal.md)
- [NestedRoomFloor](nestedroomfloor.md)
- [Passage](passage.md)
- [Stairway](stairway.md)
- [StairwayDown](stairwaydown.md)
- [StairwayUp](stairwayup.md)
- [ThroughPassage](throughpassage.md)
- [BasicDoor](basicdoor.md)
- [Door](door.md)
- [AutoClosingDoor](autoclosingdoor.md)
- [SecretDoor](secretdoor.md)
- [HiddenDoor](hiddendoor.md)
- [ExitOnlyPassage](exitonlypassage.md)
- [PathPassage](pathpassage.md)
- [RoomPart](roompart.md)
- [DefaultWall](defaultwall.md)
- [Floor](floor.md)
- [SecretFixture](secretfixture.md)
- [Immovable](immovable.md)
- [CustomImmovable](customimmovable.md)
- [Heavy](heavy.md)
- [TravelPushable](travelpushable.md)
- [OnOffControl](onoffcontrol.md)
- [Switch](switch.md)
- [Readable](readable.md)
- [Settable](settable.md)
- [Dial](dial.md)
- [LabeledDial](labeleddial.md)
- [NumberedDial](numbereddial.md)
- [TravelConnector](travelconnector.md)
- [AskConnector](askconnector.md)
- [DefaultAskConnector](defaultaskconnector.md)
- [RoomConnector](roomconnector.md)
- [OneWayRoomConnector](onewayroomconnector.md)
- [RoomAutoConnector](roomautoconnector.md)
- [TravelMessage](travelmessage.md)
- [DeadEndConnector](deadendconnector.md)
- [NoTravelMessage](notravelmessage.md)
- [FakeConnector](fakeconnector.md)
- [Wearable](wearable.md)

</details>


**Global objects:** [lightProbe](lightprobe.md)


## Properties


### `actorInAName`

Defined in en_us.t, line 1269


### `actorInName`

Defined in en_us.t, line 1268

describe an actor as being in/being removed from/being moved into this location


### `actorInPrep`

Defined in en_us.t, line 1250

Default preposition to use when an actor is in/on this object (as a nested location), and full prepositional phrase, with no article and with an indefinite article. By default, we use the objInPrep for actors as well.


### `actorIntoName`

Defined in en_us.t, line 1271


### `actorOutOfName`

Defined in en_us.t, line 1270


### `actorOutOfPrep`

Defined in en_us.t, line 1253

preposition to use when an actor is being removed from this location


### `aDisambigName`

Defined in en_us.t, line 903

The indefinite-article name for disambiguation prompts. We use the same logic here as in theDisambigName.


### `allStates`

Defined in thing.t, line 2153

Get a list of all of our possible states. For an object that can assume varying states as represented by getState, this should return the list of all possible states that the object can assume.


### `aName`

Defined in en_us.t, line 1472

My name with an indefinite article. By default, we figure out which article to use (a, an, some) automatically.


### `brightness`

Defined in thing.t, line 4396

The strength of the light the object is giving off, if indeed it is giving off light. This value should be one of the following:


### `bulk`

Defined in thing.t, line 3737


### `canBeHeard`

Defined in thing.t, line 6681


### `canBeSeen`

Defined in thing.t, line 6680

can the player character see/hear/smell/touch me?


### `canBeSmelled`

Defined in thing.t, line 6682


### `canBeTouched`

Defined in thing.t, line 6683


### `canMatchHer`

Defined in en_us.t, line 737


### `canMatchHim`

Defined in en_us.t, line 736

Test to see if we can match the pronouns 'him', 'her', 'it', and 'them'. By default, these simply test the corresponding isXxx flags (except 'canMatchThem', which tests 'isPlural' to see if the name has plural usage).


### `canMatchIt`

Defined in en_us.t, line 738


### `canMatchThem`

Defined in en_us.t, line 739


### `circularlyInMessage`

Defined in thing.t, line 7841

my message indicating that another object x cannot be put into me because I'm already in x


### `collectiveGroup`

Defined in thing.t, line 2513

Our collective group. Note - this property is obsolescent; it's supported only for compatibility with old code. New games should use 'collectiveGroups' instead.


### `collectiveGroups`

Defined in thing.t, line 2506

My associated "collective group" objects. A collective group is an abstract object, not part of the simulation (i.e, not directly manipulable by characters as a separate object) that can stand in for an entire group of related objects in some actions. For example, we might have a collective "money" object that stands in for any group of coins and paper bills for "examine" commands, so that when the player says something like "look at money" or "count money," we use the single collective money object to handle the command rather than running the command iteratively on each of the individual coins and bills present.


### `contents`

Defined in thing.t, line 4802

My contents. This is a list of the objects that this object directly contains.


### `contentsListed`

Defined in thing.t, line 1875

Determine if my contents are to be listed when I'm shown in a listing (in a room description, inventory list, or a description of my container).


### `contentsListedInExamine`

Defined in thing.t, line 1883

Determine if my contents are to be listed when I'm directly examined (with an EXAMINE/LOOK AT command). By default, we *always* list our contents when we're directly examined.


### `contentsListedSeparately`

Defined in thing.t, line 1907

Determine if my contents are listed separately from my own list entry. If this is true, then my contents will be listed in a separate sentence from my own listing; for example, if 'self' is a box, we'll be listed like so:


### `contentsLister`

Defined in thing.t, line 4444

My "contents lister." This is a Lister object that we use to display the contents of this object for room descriptions, inventories, and the like.


### `descContentsLister`

Defined in thing.t, line 4450

the Lister to use when showing my contents as part of my own description (i.e., for Examine commands)


### `described`

Defined in thing.t, line 1564

Flag: I've been desribed. This is nil by default; we set this to true whenever the player explicitly examines the object.


### `disambigEquivName`

Defined in en_us.t, line 947

The name of the object, for the purposes of disambiguation prompts to disambiguation among this object and basic equivalents of this object (i.e., objects of the same class marked with isEquivalent=true).


### `disambigName`

Defined in en_us.t, line 842

The name of the object, for the purposes of disambiguation prompts. This should almost always be the object's ordinary name, so we return self.name by default.


### `// distantDesc`

Defined in thing.t, line 2207

The default "distant" description. If this is defined for an object, then we evaluate it to display the description when an actor explicitly examines this object from a point of view where we have a "distant" sight path to the object.


### `distantInitSpecialDesc`

Defined in thing.t, line 1460


### `distantSpecialDesc`

Defined in thing.t, line 1195

The special descriptions to use under obscured and distant viewing conditions. By default, these simply display the normal special description, but these can be overridden if desired to show different messages under these viewing conditions.


### `distinguishers`

Defined in thing.t, line 2343

My Distinguisher list. This is a list of Distinguisher objects that can be used to distinguish this object from other objects.


### `dummyName`

Defined in en_us.t, line 1920

Dummy name - this simply displays nothing; it's used for cases where messageBuilder substitutions want to refer to an object (for internal bookkeeping) without actually showing the name of the object in the output text. This should always simply return an empty string.


### `effectiveFollowLocation`

Defined in thing.t, line 3776

Get the effective location of an actor directly within me, for the purposes of a "follow" command. To follow someone, we must have the same effective follow location that the target had when we last observed the target leaving.


### `equivalenceKey`

Defined in en_us.t, line 855

The "equivalence key" is the value we use to group equivalent objects. Note that we can only treat objects as equivalent when they're explicitly marked with isEquivalent=true, so the equivalence key is irrelevant for objects not so marked.


### `equivalentGrouper`

Defined in thing.t, line 4796

Our equivalent item grouper. During initialization, we will create an equivalent grouper and store it in this property for each class object that has instances marked with isEquivalent. Note that this is stored with the class, because we want each of our equivalent instances to share the same grouper object so that they are listed together as a group.


### `equivalentGrouperClass`

Defined in thing.t, line 4786

my equivalence grouper class - when we initialize, we'll create a grouper of this class and store it in equivalentGrouper


### `equivalentGrouperTable`

Defined in thing.t, line 4780

A static game-wide table of equivalence groups. This has a table of ListGroupEquivalent-derived objects, keyed by equivalence name. Each group of objects with the same equivalence name is listed in the same group and so has the same grouper object.


### `esEndingPat`

Defined in en_us.t, line 1145


### `explicitVisualSenseInfo`

Defined in thing.t, line 6577

current explicit visual sense information overriding live value


### `getState`

Defined in thing.t, line 2145

Get our state - returns a ThingState object describing the state. By default, we don't have varying states, so we simply return nil.


### `globalParamName`

Defined in thing.t, line 1132

My global parameter name. This is a name that can be used in {xxx} parameters in messages to refer directly to this object. This is nil by default, which means we have no global parameter name. Define this to a single-quoted string to set a global parameter name.


### `holdingIndex`

Defined in thing.t, line 3729

When an actor takes me, the actor will assign me a holding index value, which is simply a serial number indicating the order in which I was picked up. This lets the actor determine which items have been held longest: the item with the lowest holding index has been held the longest.


### `iesEndingPat`

Defined in en_us.t, line 1144

verb-ending patterns for figuring out which '-s' ending to add


### `initDesc`

Defined in thing.t, line 1472

If we define a non-nil initDesc, and the object is in its initial description state (as indicated by isInInitState), then we'll use this property instead of "desc" to describe the object when examined. This can be used to customize the description the player sees in parallel to initSpecialDesc.


### `initNominalRoomPartLocation`

Defined in thing.t, line 1832

Our initial room part location. By default, we set this to nil, which means that we'll use the nominal drop destination of our actual initial location when asked. If desired, this can be set to another part; for example, if a poster is initially described as being "on the north wall," this should set to the default north wall object.


### `initSpecialDesc`

Defined in thing.t, line 1444

If we define a non-nil initSpecialDesc, this property will be called to describe the object in room listings as long as the object is in its "initial" state (as determined by isInInitState: this is usually true until the object is first moved to a new location). By default, objects don't have initial descriptions.


### `inlineContentsLister`

Defined in thing.t, line 4463

my "in-line" contents lister - this is the Lister object that we'll use to display my contents parenthetically as part of my list entry in a second-level contents listing


### `isEquivalent`

Defined in thing.t, line 2324

"Equivalence" flag. If this flag is set, then all objects with the same immediate superclass will be considered interchangeable; such objects will be listed collectively in messages (so we would display "five coins" rather than "a coin, a coin, a coin, a coin, and a coin"), and will be treated as equivalent in resolving noun phrases to objects in user input.


### `isHer`

Defined in en_us.t, line 714


### `isHim`

Defined in en_us.t, line 713

Flags indicating that the object should be referred to with gendered pronouns (such as 'he' or 'she' rather than 'it').


### `isInInitState`

Defined in thing.t, line 1486

Am I in my "initial state"? This is used to determine if we should show the initial special description (initSpecialDesc) and initial examine description (initDesc) when describing the object. By default, we consider the object to be in its initial state until the first time it's moved.


### `isKnown`

Defined in thing.t, line 1631

Flag: this object is explicitly "known" to actors in the game, even if it's never been seen. This allows the object to be resolved as a topic in ASK ABOUT commands and the like. Sometimes, actors know about an object even before it's been seen - they might simply know about it from background knowledge, or they might hear about it from another character, for example.


### `isLikelyCommandTarget`

Defined in thing.t, line 5704

by default, most objects are not logical targets for commands


### `isListedAboardVehicle`

Defined in thing.t, line 1705

by default, regular objects are not listed when they arrive aboard vehicles (only actors are normally listed in this fashion)


### `isMassNoun`

Defined in en_us.t, line 702

Flag that this is object's name is a "mass noun" - that is, a noun denoting a continuous (effectively infinitely divisible) substance or material, such as water, wood, or popcorn; and certain abstract concepts, such as knowledge or beauty. Mass nouns are never rendered in the plural, and use different determiners than ordinary ("count") nouns: "some popcorn" vs "a kernel", for example.


### `isPlural`

Defined in en_us.t, line 691

Flag that this object's name is rendered as a plural (this applies to both a singular noun with plural usage, such as "pants" or "scissors," and an object used in the world model to represent a collection of real-world objects, such as "shrubs").


### `isProperName`

Defined in en_us.t, line 792

Proper name flag. This indicates that the 'name' property is the name of a person or place. We consider proper names to be fully qualified, so we don't add articles for variations on the name such as 'theName'.


### `isQualifiedName`

Defined in en_us.t, line 802

Qualified name flag. This indicates that the object name, as given by the 'name' property, is already fully qualified, so doesn't need qualification by an article like "the" or "a" when it appears in a sentence. By default, a name is considered qualified if it's a proper name, but this can be overridden to mark a non-proper name as qualified when needed.


### `isThingConstructed`

Defined in thing.t, line 1109

Have we been through Thing.construct() yet for this object? Note that this will only be set for dynamically created instances (i.e., objects created with 'new').


### `isTopLevel`

Defined in thing.t, line 4976

Is this a "top-level" location? A top-level location is an object which doesn't have another container, so its 'location' property is nil, but which is part of the game universe anyway. In most cases, a top-level location is simply a Room, since the network of rooms makes up the game's map.


### `listName`

Defined in en_us.t, line 954

Single-item listing description. This is used to display the item when it appears as a single (non-grouped) item in a list. By default, we just show the indefinite article description.


### `listWith`

Defined in thing.t, line 2543

"List Group" objects. This specifies a list of ListGroup objects that we use to list this object in object listings, such as inventory lists and room contents lists.


### `location`

Defined in thing.t, line 4600

Every Thing has a location, which is the Thing that contains this object. A Thing's location can only be a simple object reference, or nil; it cannot be a list, and it cannot be a method.


### `lookInLister`

Defined in thing.t, line 4456

the Lister to use when showing my contents in response to a LookIn command


### `moved`

Defined in thing.t, line 1516

Flag: I've been moved out of my initial location. Whenever we move the object to a new location, we'll set this to true.


### `name`

Defined in en_us.t, line 812

The name of the object - this is a string giving the object's short description, for constructing sentences that refer to the object by name. Each instance should override this to define the name of the object. This string should not contain any articles; we use this string as the root to generate various forms of the object's name for use in different places in sentences.


### `nameDoes`

Defined in en_us.t, line 1858


### `nameSays`

Defined in en_us.t, line 1865


### `nameSees`

Defined in en_us.t, line 1863


### `notTravelReadyMsg`

Defined in thing.t, line 3432

explain the reason isActorTravelReady() returned nil


### `objectNotifyList`

Defined in thing.t, line 7716

our list of registered notification items


### `objInPrep`

Defined in en_us.t, line 1242

Default preposition to use when an object is in/on this object. By default, we use 'in' as the preposition; subclasses can override to use others (such as 'on' for a surface).


### `obscuredInitSpecialDesc`

Defined in thing.t, line 1459

The initial descriptions to use under obscured and distant viewing conditions. By default, these simply show the plain initSpecialDesc; these can be overridden, if desired, to show alternative messages when viewing conditions are less than ideal.


### `obscuredSpecialDesc`

Defined in thing.t, line 1196


### `owner` *(overridden)*

Defined in thing.t, line 5288

My explicit owner. By default, objects do not have explicit owners, which means that the owner at any given time is determined by the object's location - my innermost container that can own me is my owner.


### `patElevenEighteen`

Defined in en_us.t, line 1697


### `patIsAlpha`

Defined in en_us.t, line 1696


### `patLeadingTagOrQuote`

Defined in en_us.t, line 1692


### `patOfPhrase`

Defined in en_us.t, line 1822


### `patOneLetterAnWord`

Defined in en_us.t, line 1695


### `patOneLetterWord`

Defined in en_us.t, line 1694


### `patSingleApostropheS`

Defined in en_us.t, line 1819

some pre-compiled patterns for pluralName


### `patTagOrQuoteChar`

Defined in en_us.t, line 1691

pre-compile some regular expressions for aName


### `patUpperOrDigit`

Defined in en_us.t, line 1820


### `patVowelY`

Defined in en_us.t, line 1821


### `pluralDisambigName`

Defined in en_us.t, line 920

The plural name for disambiguation prompts. We use the same logic here as in theDisambigName.


### `pluralName`

Defined in en_us.t, line 1710

Get the default plural name. By default, we'll use the algorithmic plural determination, which is based on the spelling of the name.


### `pronounSelector`

Defined in en_us.t, line 995

Get the 'pronoun selector' for the various pronoun methods. This returns:


### `roomDarkName`

Defined in thing.t, line 2610

our interior room name when we're in the dark


### `roomLocation`

Defined in thing.t, line 3624

Get my "room location." If 'self' is capable of holding actors, this should return 'self'; otherwise, it should return the nearest enclosing container that's a room location. By default, we simply return our location's room location.


### `roomName`

Defined in thing.t, line 2561

Our interior room name. This is the status line name we display when an actor is within this object and can't see out to the enclosing room. Since we can't rely on the enclosing room's status line name if we can't see the enclosing room, we must provide one of our own.


### `seen`

Defined in thing.t, line 1532

Flag: I've been seen by the player character. This is nil by default; we set this to true whenever we show a room description from the player character's perspective, and the object is visible. The object doesn't actually have to be mentioned in the room description to be marked as seen - it merely has to be visible to the player character.


### `sightPresence`

Defined in thing.t, line 4434

Determine whether or not the object has a "presence" in each sense. An object has a presence in a sense if an actor immediately adjacent to the object could detect the object by the sense alone. For example, an object has a "hearing presence" if it is making some kind of noise, and does not if it is silent.


### `sightSize`

Defined in thing.t, line 4404

Sense sizes of the object. Each object has an individual size for each sense. By default, objects are medium for all senses; this allows them to be sensed from a distance or through an obscuring medium, but doesn't allow their details to be sensed.


### `smellPresence`

Defined in thing.t, line 4436


### `smellSize`

Defined in thing.t, line 4406


### `soundPresence`

Defined in thing.t, line 4435


### `soundSize`

Defined in thing.t, line 4405


### `specialContentsLister`

Defined in thing.t, line 4471

My "special" contents lister. This is the Lister to use to display the special descriptions for objects that have special descriptions when we're showing a room description for this object.


### `specialDesc`

Defined in thing.t, line 1175

"Special" description. This is the generic place to put a description of the object that should appear in the containing room's full description. If the object defines a special description, the object is NOT listed in the basic contents list of the room, because listing it with the contents would be redundant with the special description.


### `specialDescBeforeContents`

Defined in thing.t, line 1256

Special description phase. We list special descriptions for a room's full description in two phases: one phase before we show the room's portable contents list, and another phase after we show the contents list. This property controls the phase in which we show this item's special description. This only affects special descriptions that are shown with room descriptions; in other cases, such as "examine" descriptions of objects, all of the special descriptions are usually shown together.


### `specialDescListWith`

Defined in thing.t, line 2550

Get the list group for my special description. This works like the ordinary listWith, but is used to group me with other objects showing special descriptions, rather than in ordinary listings.


### `specialDescOrder`

Defined in thing.t, line 1224

List order for the special description. Whenever there's more than one object showing a specialDesc at the same time (in a single room description, for example), we'll use this to order the specialDesc displays. We'll display in ascending order of this value. By default, we use the same value for everything, so listing order is arbitrary; when one specialDesc should appear before or after another, this property can be used to control the relative ordering.


### `specialNominalRoomPartLocation`

Defined in thing.t, line 1851

Our "special" room part location. By default, we set this to nil, which means that we'll use the nominal drop destination of our actual current location when asked.


### `suppressAutoSeen`

Defined in thing.t, line 1558

Flag: suppress the automatic setting of the "seen" status for this object in room and object descriptions. Normally, we'll automatically mark every visible object as seen (by calling gActor.setHasSeen()) whenever we do a LOOK AROUND. We'll also automatically mark as seen every visible object within an object examined explicitly (such as with EXAMINE, LOOK IN, LOOK ON, or OPEN). This property can override this automatic status change: when this property is true, we will NOT mark this object as seen in any of these cases. When this property is true, the game must explicitly mark the object as seen, if and when desired, by calling actor.setHasSeen().


### `takeFromNotInMessage`

Defined in thing.t, line 8782

general message for "take from" when an object isn't in me


### `theDisambigName`

Defined in en_us.t, line 896

The definite-article name for disambiguation prompts.


### `theName`

Defined in en_us.t, line 1157

Get the name with a definite article ("the box"). By default, we use our standard definite article algorithm to apply an article to self.name.


### `theNamePossNoun`

Defined in en_us.t, line 1216

TheName as a possessive noun (that is Bob's, that is yours). We simply return the possessive adjective name, since the two forms are usually identical in English (except for pronouns, where they sometimes differ: "her" for the adjective vs "hers" for the noun).


### `tmpAmbient_`

Defined in thing.t, line 7512

Scratch-pad for calculating ambient energy level - valid only after calcAmbience and until the game state changes in any way. This is for internal use within the sense propagation methods only.


### `tmpAmbientFill_`

Defined in thing.t, line 7520

Last fill material traversed by the ambient sense energy in tmpAmbient_. We must keep track of this so that we can treat consecutive traversals of the same fill material as equivalent to a single traversal.


### `tmpAmbientWithin_`

Defined in thing.t, line 7541

Scratch-pads for the ambient level, best transparency, and obstructor to our *interior* surface. We keep track of these separately from the exterior data so that we can tell what we look like from the persepctive of an object within us.


### `tmpFillMedium_`

Defined in thing.t, line 7558

My fill medium. We cache this during each sense path calculation, since the fill medium calculation often requires traversing several containment levels.


### `tmpObstructor_`

Defined in thing.t, line 7533

Scratch-pad for the obstructor that contributed to a non-transparent path to this object in tmpTrans_.


### `tmpObstructorWithin_`

Defined in thing.t, line 7543


### `tmpPathIsIn_`

Defined in thing.t, line 7551

Scratch-pad for the sense path direction at this object. If this is true, the sense path is pointing inward - that is, the path from the source object to here is entering from outside me. Otherwise, the sense path is pointing outward.


### `tmpTrans_`

Defined in thing.t, line 7527

Scrach-pad for the best transparency level to this object from the current point of view. This is used during cacheSenseInfo to keep track of the sense path to this object.


### `tmpTransWithin_`

Defined in thing.t, line 7542


### `touchPresence`

Defined in thing.t, line 4437


### `touchSize`

Defined in thing.t, line 4407


### `verbCan`

Defined in en_us.t, line 1867


### `verbCannot`

Defined in en_us.t, line 1868


### `verbCant`

Defined in en_us.t, line 1869


### `verbEndingSD`

Defined in en_us.t, line 1901


### `verbEndingSEd`

Defined in en_us.t, line 1902


### `verbEndingSMessageBuilder_`

Defined in en_us.t, line 1903


### `verbMust`

Defined in en_us.t, line 1866


### `verbToCome`

Defined in en_us.t, line 1860


### `verbToDo`

Defined in en_us.t, line 1857

A few common irregular verbs and name-plus-verb constructs, defined for convenience.


### `verbToGo`

Defined in en_us.t, line 1859


### `verbToLeave`

Defined in en_us.t, line 1861


### `verbToSay`

Defined in en_us.t, line 1864


### `verbToSee`

Defined in en_us.t, line 1862


### `verbWill`

Defined in en_us.t, line 1870


### `verbWont`

Defined in en_us.t, line 1871


### `weight`

Defined in thing.t, line 3736

An object has "weight" and "bulk" specifying how heavy and how large the object is. These are in arbitrary units, and by default everything has a weight of 1 and a bulk of 1.


## Inherited Properties


*From [VocabObject](vocabobject.md):* [`canResolvePossessive`](vocabobject.md#canResolvePossessive), [`disambigPromptOrder`](vocabobject.md#disambigPromptOrder), [`pluralOrder`](vocabobject.md#pluralOrder), [`vocabLikelihood`](vocabobject.md#vocabLikelihood), [`vocabWords`](vocabobject.md#vocabWords), [`weakTokens`](vocabobject.md#weakTokens)


## Methods


### `acceptCommand(issuingActor)`

Defined in thing.t, line 5692

by default, objects don't accept commands


### `addAllContents(vec)`

Defined in thing.t, line 4869

add myself and all of my contents, recursively including contents of contents, to a vector


### `addDirectConnections(tab)`

Defined in thing.t, line 5758

Add this item and its direct containment connections to the lookup table. This must recursively add all connected objects that aren't already in the table.


### `addObjectNotifyItem(obj)`

Defined in thing.t, line 7704

Add an item to our registered notification list for actions involving this object as the direct object, indirect object, and so on.


### `addToContents(obj)`

Defined in thing.t, line 5396

Add an object to my contents.


### `addToSenseInfoTable(sense, tab)`

Defined in thing.t, line 6882

Add myself to a sense info table. This is called by senseInfoTable() for each object connected by containment to the source object 'src', after we've fully traversed the containment tree to initialize our current-sense properties (tmpAmbient_, tmpTrans_, etc).


### `adjustLookAroundTable(tab, pov, actor)`

Defined in thing.t, line 2977

Adjust the sense table a "look around" command. This is called after we calculate the sense info table, but before we start describing any of the room's contents, to give us a chance to remove any items we don't want described (or, conceivably, to add any items we do want described but which won't show up with the normal sense calculations).


### `adjustThrowDestination(thrownObj, path)`

Defined in thing.t, line 3839

Adjust a drop destination chosen in a THROW. This is called on the object that was chosen as the preliminary landing location for the thrown object, as calculated by getHitFallDestination(), to give the preliminary destination a chance to redirect the landing to another object. For example, if the preliminary destination simply isn't a suitable surface or container where a projectile could land, or it's not big enough to hold the projectile, the preliminary destination could override this method to redirect the landing to a more suitable object.


### `afterAction`

Defined in thing.t, line 7648

Receive notification that a command has just been performed. This is called by the same rules as beforeAction(), but under the conditions prevailing after the command has been completed.


### `afterTravel(traveler, connector)`

Defined in thing.t, line 7673

Receive notification that a traveler has just arrived via travelerTravelTo(). This notification is sent to each object connected to the traveler by containment, in its new location, just after the travel completes.


### `allContents`

Defined in thing.t, line 4836

Get a vector of all of my contents, recursively including contents of contents.


### `aNameFrom(str)`

Defined in en_us.t, line 1509

Apply an indefinite article ("a box", "an orange", "some lint") to the given name. We'll try to figure out which indefinite article to use based on what kind of noun phrase we use for our name (singular, plural, or a "mass noun" like "lint"), and our spelling.


### `aNameObj`

Defined in en_us.t, line 1475

the indefinite-article name in the objective case


### `aNameOwnerLoc(ownerPriority)`

Defined in en_us.t, line 1364

Get my name (in various forms) distinguished by my owner or location.


### `announceDefaultObject(whichObj, action, resolvedAllObjects)`

Defined in thing.t, line 3922

Announce myself as a default object for an action. By default, we'll show the standard library message announcing a default.


### `appendHeldContents(vec)`

Defined in thing.t, line 5160

Add to a vector all of my contents that are directly held when I'm being directly held. This is used to add the direct contents of an item to scope when the item itself is being directly held.


### `atmosphereList`

Defined in thing.t, line 3660

Our room atmospheric message list. This can be set to an EventList that provides messages to be displayed while the player character is within this object.


### `baseMoveInto(newContainer)`

Defined in thing.t, line 5506

Base moveInto - this is the low-level containment changer; this routine does not send any notifications to any containers, and does not mark the object as moved. This form should be used only for internal library-initiated state changes, since it bypasses all of the normal side effects of moving an object to a new container.


### `basicExamine`

Defined in thing.t, line 8085

Perform the basic 'examine' action. This shows either the normal or initial long description (the latter only if the object hasn't been moved yet, and it has a special initial examine description), and marks the object as having been described at least once.


### `basicExamineFeel`

Defined in thing.t, line 8397

Basic examination of an object for touch. As with the basic taste examination, we don't use an emanation object or distinguish transparency levels, because feeling an object requires direct physical contact.


### `basicExamineListen(explicit)`

Defined in thing.t, line 8215

Basic examination of the object for sound. If the object has an associated noise object, we'll describe it.


### `basicExamineSmell(explicit)`

Defined in thing.t, line 8298

Basic examination of the object for odor. If the object has an associated odor object, we'll describe it.


### `basicExamineTaste`

Defined in thing.t, line 8385

Basic examination of an object for taste. Unlike the smell/listen examination routines, we don't bother using a separate sensory emanation object for tasting, as tasting is always an explicit action, never passive. Furthermore, since tasting requires direct physical contact with the object, we don't differentiate levels of transparency or distance.


### `beforeAction`

Defined in thing.t, line 7638

Receive notification that a command is about to be performed. This is called on each object connected by containment with the actor performing the command, and on any objects explicitly registered with the actor, the actor's location and its locations up to the outermost container, or the directly involved objects.


### `beforeTravel(traveler, connector)`

Defined in thing.t, line 7665

Receive notification that a traveler (an actor or a vehicle, for example) is about to depart via travelerTravelTo(), OR that an actor is about to move among nested locations via travelWithin(). This notification is sent to each object connected to the traveler by containment, just before the traveler departs.


### `buildContainmentPaths(vec, pathHere, obj)`

Defined in thing.t, line 6334

Service routine for getAllPathsTo: build a vector of the containment paths starting with this object.


### `cacheAmbientInfo(objs, sense)`

Defined in thing.t, line 7006

Cache the ambient energy level at each object in the table. The list must include everything connected by containment.


### `cacheSenseInfo(objs, sense)`

Defined in thing.t, line 6984

Cache sensory information for all objects in the given list from the point of view of self. This caches the ambient energy level at each object, if the sense uses ambient energy, and the transparency and obstructor on the best path in the sense to the object. 'objs' is the connection table, as generated by connectionTable().


### `cacheSensePath(sense)`

Defined in thing.t, line 7300

Cache the sense path for each object reachable from this point of view. Fills in tmpTrans_ and tmpObstructor_ for each object with the best transparency path from the object to me.


### `canBeHeardBy(actor)`

Defined in thing.t, line 6675


### `canBeSeenBy(actor)`

Defined in thing.t, line 6674

can the given actor see/hear/smell/touch me?


### `canBeSensed(sense, trans, ambient)`

Defined in thing.t, line 4489

Determine if I can be sensed under the given conditions. Returns true if the object can be sensed, nil if not. If this method returns nil, this object will not be considered in scope for the current conditions.


### `canBeSmelledBy(actor)`

Defined in thing.t, line 6676


### `canBeTouchedBy(actor)`

Defined in thing.t, line 6677


### `canDetailsBeSensed(sense, info, pov)`

Defined in thing.t, line 4536

Determine if I can be sensed IN DETAIL in the given sense, with the given SenseInfo description. By default, an object's details can be sensed if the sense path is 'transparent' or 'attenuated', OR the object's scale in the sense is 'large'.


### `canHear(obj)`

Defined in thing.t, line 6670


### `canMatchPronounType(typ)`

Defined in en_us.t, line 742

can we match the given PronounXxx pronoun type specifier?


### `canMoveViaPath(obj, dest, op)`

Defined in thing.t, line 6056

Determine if we can traverse this object for moving the given object via a path. Calls checkMoveViaPath(), and returns true if checkMoveViaPath() indicates success, nil if it indicates failure.


### `cannotGoShowExits(actor)`

Defined in thing.t, line 3435

show a list of exits as part of failed travel - defer to location


### `cannotReachObject(obj)`

Defined in thing.t, line 5839

Display a message explaining why we are obstructing a sense path to the given object.


### `cannotSeeSmellSource(obj)`

Defined in thing.t, line 5861

explain why we cannot see the source of an odor


### `cannotSeeSoundSource(obj)`

Defined in thing.t, line 5858

Display a message explaining that the source of a sound cannot be seen because I am visually obstructing it. By default, we show nothing at all; subclasses can override this to provide a better explanation when possible.


### `canOwn(obj)`

Defined in thing.t, line 5331

Can I own the given object? By default, objects cannot own other objects. This can be overridden when ownership is desired.


### `canSee(obj)`

Defined in thing.t, line 6669

Can I see/hear/smell the given object? By default, an object can "see" (or "hear", etc) another if there's a clear path in the corresponding basic sense to the other object. Note that actors override this, because they have a subjective view of the senses: an actor might see in a special infrared vision sense rather than (or in addition to) the normal 'sight' sense, for example.


### `canSmell(obj)`

Defined in thing.t, line 6671


### `canThrowViaPath(obj, dest, op)`

Defined in thing.t, line 6060

determine if we can throw an object via this path


### `canTouch(obj)`

Defined in thing.t, line 5899

Determine if I can touch the given object. By default, we can always touch our immediate container; otherwise, we can touch anything with a touch path that we can traverse.


### `canTouchViaPath(obj, dest, op)`

Defined in thing.t, line 6064

determine if we can reach out and touch an object via this path


### `checkActorOutOfNested(allowImplicit)`

Defined in thing.t, line 3604

Check, using pre-condition rules, that the actor is removed from this nested location and moved to its exit destination.


### `checkBulkChange`

Defined in thing.t, line 4175

Check a proposed change in my bulk. When this is called, the new bulk should already be in effect (the best way to do this when just making a check is via whatIf).


### `checkBulkChangeWithin(changingObj)`

Defined in thing.t, line 4197

Check a bulk change of one of my direct contents, given by obj. When this is called, 'obj' will be (tentatively) set to reflect its proposed new bulk; if this routine doesn't like the new bulk, it should issue a failure report and exit the command, which will cancel the command that would have caused the change and will prevent the proposed change from taking effect.


### `checkMoveViaPath(obj, dest, op)`

Defined in thing.t, line 6020

Determine if we can traverse self for moving the given object in the given manner. This is used to determine if a containment connection path can be used to move an object to a new location. Returns a CheckStatus object indicating success if we can traverse self, failure if not.


### `checkStagingLocation(dest)`

Defined in thing.t, line 5674

Determine if I'm a valid staging location for the given nested room destination 'dest'. This is called when the actor is attempting to enter the nested room 'dest', and the travel handlers find that we're the staging location for the room. (A "staging location" is the location the actor is required to occupy immediately before moving into the destination.)


### `checkThrowViaPath(obj, dest, op)`

Defined in thing.t, line 6030

Determine if we can traverse this object for throwing the given object in the given manner. By default, this returns the same thing as canMoveViaPath, since throwing is in most cases the same as ordinary movement. Objects can override this when throwing an object through this path element should be treated differently from ordinary movement.


### `checkTouchViaPath(obj, dest, op)`

Defined in thing.t, line 6045

Determine if we can traverse self in the given manner for the purposes of 'obj' touching another object. 'obj' is usually an actor; this determines if 'obj' is allowed to reach through this path element on the way to touching another object.


### `checkTravelerDirectlyInRoom(traveler, allowImplicit)`

Defined in thing.t, line 3582

Check that a traveler is directly in this room. By default, a Thing is not a room, so a connector within a Thing actually requires the traveler to be in the Thing's container, not in the Thing itself. So, defer to our container.


### `childInName(childName)`

Defined in en_us.t, line 1308

Get a description of an object within this object, describing the object's location as this object. By default, we'll append "in <theName>" to the given object name.


### `childInNameGen(childName, myName)`

Defined in en_us.t, line 1338

Base routine for generating childInName and related names. Takes the name to use for the child and the name to use for me, and combines them appropriately.


### `childInNameWithOwner(childName)`

Defined in en_us.t, line 1317

Get a description of an object within this object, showing the owner of this object. This is similar to childInName, but explicitly shows the owner of the containing object, if any: "the flashlight in bob's backpack".


### `childInRemoteName(childName, pov)`

Defined in en_us.t, line 1324

get a description of an object within this object, as seen from a remote location


### `clearSenseInfo`

Defined in thing.t, line 7491

Clear the sensory scratch-pad properties, in preparation for a sensory calculation pass.


### `cloneForMultiInstanceContents(loc)`

Defined in thing.t, line 5643

Create a clone for inclusion in MultiInstance contents. We'll recursively clone our own contents.


### `cloneMultiInstanceContents`

Defined in thing.t, line 5621

Clone this object for inclusion in a MultiInstance's contents tree. When we clone an instance object for a MultiInstance, we'll also clone its contents, and their contents, and so on. This routine creates a private copy of all of our contents.


### `conjugateRegularVerb(verb)`

Defined in en_us.t, line 1078

Conjugate a regular verb in the present or past tense for our person and number.


### `connectionTable`

Defined in thing.t, line 5726

Generate a lookup table of all of the objects connected by containment to this object. This table includes all containment connections, even through closed containers and the like.


### `construct` *(overridden)*

Defined in thing.t, line 1080

on constructing a new Thing, initialize it as we would a statically instantiated Thing


### `contentsInFixedIn(loc)`

Defined in thing.t, line 5113

Are my contents within a fixed item that is within the given location? By default, we return nil because we are not ourselves fixed.


### `countDisambigName(cnt)`

Defined in en_us.t, line 909

The counted name for disambiguation prompts. We use the same logic here as in theDisambigName.


### `countListName(equivCount, pov, info)`

Defined in thing.t, line 2079

Single-item counted listing description. This is used to display an item with a count of equivalent items ("four gold coins"). 'info' is the sense information from the current point of view for 'self', which we take to be representative of the sense information for all of the equivalent items.


### `countName(count)`

Defined in en_us.t, line 965

Return a string giving the "counted name" of the object - that is, a phrase describing the given number of the object. For example, for a red book, and a count of 5, we might return "five red books". By default, we use countNameFrom() to construct a phrase from the count and either our regular (singular) 'name' property or our 'pluralName' property, according to whether count is 1 or more than 1.


### `countNameFrom(count, singularStr, pluralStr)`

Defined in en_us.t, line 971

Returns a string giving a count applied to the name string. The name must be given in both singular and plural forms.


### `countNameOwnerLoc(cnt, ownerPriority)`

Defined in en_us.t, line 1408

we have no owner - show as "the item in the location"


### `darkRoomContentsLister`

Defined in thing.t, line 3312

Get my dark room contents lister - this is the Lister object we'll use to display the room's self-illuminating contents when the room is dark.


### `defaultDistantDesc`

Defined in thing.t, line 2210

the default distant description


### `defaultObscuredDesc(obs)`

Defined in thing.t, line 2250

the default obscured description


### `desc`

Defined in thing.t, line 2180

The default long description, which is displayed in response to an explicit player request to examine the object. We'll use a generic library message; most objects should override this to customize the object's desription.


### `directionForConnector(conn, actor)`

Defined in thing.t, line 3540

Find a direction linked to a given connector, for travel by the given actor. Returns the first direction (as a Direction object) we find linked to the connector, or nil if we don't find any direction linked to it.


### `distantSmellDesc`

Defined in thing.t, line 2277

distant smell description


### `distantSoundDesc`

Defined in thing.t, line 2262

distant sound description


### `dobjFor(AskAbout)`

Defined in thing.t, line 9060

"Ask about" action


### `dobjFor(AskFor)`

Defined in thing.t, line 8954

"Ask for" action


### `dobjFor(AskVague)`

Defined in thing.t, line 9079

Vague "ask" and "tell" - these are for syntactically incorrect ASK and TELL phrasings, so that we can provide better error feedback.


### `dobjFor(AttachTo)`

Defined in thing.t, line 9814

"AttachTo" action


### `dobjFor(Attack)`

Defined in thing.t, line 9130

"Attack" action.


### `dobjFor(AttackWith)`

Defined in thing.t, line 9141

"Attack with" action - attack with (presumably) a weapon.


### `dobjFor(Board)`

Defined in thing.t, line 10092

"Board" action


### `dobjFor(Break)`

Defined in thing.t, line 9854

"Break" action


### `dobjFor(Burn)`

Defined in thing.t, line 9767

"Burn". By default, we ask for something to use to burn the object, since most objects are not self-igniting.


### `dobjFor(BurnWith)`

Defined in thing.t, line 9789

"Burn with"


### `dobjFor(Clean)`

Defined in thing.t, line 10037

"Clean" action


### `dobjFor(CleanWith)`

Defined in thing.t, line 10047

"CleanWith" action


### `dobjFor(Climb)`

Defined in thing.t, line 9881

"Climb", "climb up", and "climb down" actions


### `dobjFor(ClimbDown)`

Defined in thing.t, line 9893


### `dobjFor(ClimbUp)`

Defined in thing.t, line 9887


### `dobjFor(Close)`

Defined in thing.t, line 9913

"Close" action


### `dobjFor(Consult)`

Defined in thing.t, line 9667

"Consult" action


### `dobjFor(ConsultAbout)`

Defined in thing.t, line 9673


### `dobjFor(CutWith)`

Defined in thing.t, line 9864

"Cut with" action


### `dobjFor(Detach)`

Defined in thing.t, line 9844

"Detach" action


### `dobjFor(DetachFrom)`

Defined in thing.t, line 9829

"DetachFrom" action


### `dobjFor(Dig)`

Defined in thing.t, line 9508

"Dig" action - by default, simply re-reoute to dig-with, since we generally need a digging implement to dig in anything. Some objects might want to override this to allow digging without any implement; a sandy beach, for example, might allow digging in the sand without a shovel.


### `dobjFor(DigWith)`

Defined in thing.t, line 9519

"DigWith" action


### `dobjFor(Doff)`

Defined in thing.t, line 8934

"Doff" action


### `dobjFor(Drink)`

Defined in thing.t, line 9987

"Drink" action


### `dobjFor(Drop)`

Defined in thing.t, line 8788

"Drop" verb processing


### `dobjFor(Eat)`

Defined in thing.t, line 9973

"Eat" action


### `dobjFor(Enter)`

Defined in thing.t, line 10269

"Enter"


### `dobjFor(EnterOn)`

Defined in thing.t, line 9709

"Enter on" action


### `dobjFor(Examine)`

Defined in thing.t, line 8039

"Examine" action


### `dobjFor(Extinguish)`

Defined in thing.t, line 9804

"Extinguish"


### `dobjFor(Fasten)`

Defined in thing.t, line 10119

"Fasten" action


### `dobjFor(FastenTo)`

Defined in thing.t, line 10129

"Fasten to" action


### `dobjFor(Feel)`

Defined in thing.t, line 8613

"Feel"


### `dobjFor(Flip)`

Defined in thing.t, line 9729

"Flip" action


### `dobjFor(Follow)`

Defined in thing.t, line 9092

"Follow" action


### `dobjFor(GetOffOf)`

Defined in thing.t, line 10110

"Get off of" action


### `dobjFor(GetOutOf)`

Defined in thing.t, line 10102

"Get out of" (unboard) action


### `dobjFor(GiveTo)`

Defined in thing.t, line 8972

"Give to" action


### `dobjFor(GoThrough)`

Defined in thing.t, line 10278

"Go through"


### `dobjFor(JumpOff)`

Defined in thing.t, line 9543

"jump off"


### `dobjFor(JumpOver)`

Defined in thing.t, line 9534

"jump over"


### `dobjFor(Kiss)`

Defined in thing.t, line 8943

"Kiss"


### `dobjFor(LieOn)`

Defined in thing.t, line 10072

"LieOn" action


### `dobjFor(Light)`

Defined in thing.t, line 9760

"Light" action. By default, we treat this as equivalent to "burn".


### `dobjFor(ListenTo)`

Defined in thing.t, line 8560

"Listen to"


### `dobjFor(Lock)`

Defined in thing.t, line 9923

"Lock" action


### `dobjFor(LockWith)`

Defined in thing.t, line 9943

"LockWith" action


### `dobjFor(LookBehind)`

Defined in thing.t, line 8539

"Look behind"


### `dobjFor(LookIn)`

Defined in thing.t, line 8501

"Look in"


### `dobjFor(LookThrough)`

Defined in thing.t, line 8550

"Look through"


### `dobjFor(LookUnder)`

Defined in thing.t, line 8528

"Look under"


### `dobjFor(Move)`

Defined in thing.t, line 9574

"Move" action


### `dobjFor(MoveTo)`

Defined in thing.t, line 9601

"MoveTo" action


### `dobjFor(MoveWith)`

Defined in thing.t, line 9585

"MoveWith" action


### `dobjFor(Open)`

Defined in thing.t, line 9903

"Open" action


### `dobjFor(PlugIn)`

Defined in thing.t, line 10169

"PlugIn" action


### `dobjFor(PlugInto)`

Defined in thing.t, line 10179

"PlugInto" action


### `dobjFor(Pour)`

Defined in thing.t, line 9997

"Pour"


### `dobjFor(PourInto)`

Defined in thing.t, line 10007

"Pour into"


### `dobjFor(PourOnto)`

Defined in thing.t, line 10022

"Pour onto"


### `dobjFor(Pull)`

Defined in thing.t, line 9563

"Pull" action


### `dobjFor(Push)`

Defined in thing.t, line 9552

"Push" action


### `dobjFor(PushTravel)`

Defined in thing.t, line 10289

Push in Direction action - this is for commands like "push boulder north" or "drag sled into cave".


### `dobjFor(PutBehind)`

Defined in thing.t, line 8909

"PutBehind" action


### `dobjFor(PutIn)`

Defined in thing.t, line 8823

"Put In" verb processing. Default objects cannot contain other objects, but they can be put in arbitrary containers.


### `dobjFor(PutOn)`

Defined in thing.t, line 8861

"Put On" processing. Default objects cannot have other objects put on them, but they can be put on surfaces.


### `dobjFor(PutUnder)`

Defined in thing.t, line 8893

"PutUnder" action


### `dobjFor(Read)`

Defined in thing.t, line 8475

"Read"


### `dobjFor(Remove)`

Defined in thing.t, line 8701

"Remove" processing. We'll treat "remove dobj" as meaning "take dobj from <something>", where <something> is elided and must be determined.


### `dobjFor(Screw)`

Defined in thing.t, line 10219

"Screw" action


### `dobjFor(ScrewWith)`

Defined in thing.t, line 10229

"ScrewWith" action


### `dobjFor(Search)`

Defined in thing.t, line 8522

"Search". By default, we make "search obj" do the same thing as "look in obj".


### `dobjFor(Set)`

Defined in thing.t, line 9647

"Set" action


### `dobjFor(SetTo)`

Defined in thing.t, line 9657

"SetTo" action


### `dobjFor(ShowTo)`

Defined in thing.t, line 8998

"Show to" action


### `dobjFor(SitOn)`

Defined in thing.t, line 10062

"SitOn" action


### `dobjFor(Smell)`

Defined in thing.t, line 8575

"Smell"


### `dobjFor(StandOn)`

Defined in thing.t, line 10082

"StandOn" action


### `dobjFor(Strike)`

Defined in en_us.t, line 1949

For the most part, "strike" has the same meaning as "hit", so define this as a synonym for "attack" most objects. There are a few English idioms where "strike" means something different, as in "strike match" or "strike tent."


### `dobjFor(Switch)`

Defined in thing.t, line 9719

"Switch" action


### `dobjFor(Take)`

Defined in thing.t, line 8631

"Take" action


### `dobjFor(TakeFrom)`

Defined in thing.t, line 8717

"Take from" processing


### `dobjFor(TalkTo)`

Defined in thing.t, line 8963

"Talk to"


### `dobjFor(Taste)`

Defined in thing.t, line 8593

"Taste"


### `dobjFor(TellAbout)`

Defined in thing.t, line 9069

"Tell about" action


### `dobjFor(TellVague)`

Defined in thing.t, line 9083


### `dobjFor(Throw)`

Defined in thing.t, line 9169

"Throw" action. By default, we'll simply re-route this to a "throw at" action. Objects that can meaningfully be thrown without any specific target can override this.


### `dobjFor(ThrowAt)`

Defined in thing.t, line 9206

"Throw at" action


### `dobjFor(ThrowDir)`

Defined in thing.t, line 9182

"Throw <direction>". By default, we simply reject this and explain that the command to use is THROW AT. With one exception: we treat THROW <down> as equivalent to THROW AT FLOOR, and use the default library message for that command instead.


### `dobjFor(ThrowTo)`

Defined in thing.t, line 9456

"Throw to" action


### `dobjFor(Turn)`

Defined in thing.t, line 9612

"Turn" action


### `dobjFor(TurnOff)`

Defined in thing.t, line 9749

"TurnOff" action


### `dobjFor(TurnOn)`

Defined in thing.t, line 9739

"TurnOn" action


### `dobjFor(TurnTo)`

Defined in thing.t, line 9622

"Turn to" action


### `dobjFor(TurnWith)`

Defined in thing.t, line 9632

"TurnWith" action


### `dobjFor(TypeLiteralOn)`

Defined in thing.t, line 9699

"Type <literal> on" action


### `dobjFor(TypeOn)`

Defined in thing.t, line 9683

"Type on" action


### `dobjFor(Unfasten)`

Defined in thing.t, line 10144

"Unfasten" action


### `dobjFor(UnfastenFrom)`

Defined in thing.t, line 10154

"Unfasten from" action


### `dobjFor(Unlock)`

Defined in thing.t, line 9933

"Unlock" action


### `dobjFor(UnlockWith)`

Defined in thing.t, line 9958

"UnlockWith" action


### `dobjFor(Unplug)`

Defined in thing.t, line 10194

"Unplug" action


### `dobjFor(UnplugFrom)`

Defined in thing.t, line 10204

"UnplugFrom" action


### `dobjFor(Unscrew)`

Defined in thing.t, line 10244

"Unscrew" action


### `dobjFor(UnscrewWith)`

Defined in thing.t, line 10254

"UnscrewWith" action


### `dobjFor(Wear)`

Defined in thing.t, line 8925

"Wear" action


### `examineListContents`

Defined in thing.t, line 8180

List my contents as part of Examine processing. We'll recursively list contents of contents; this will ensure that even if we have no listable contents, we'll list any listable contents of our contents.


### `examineListContentsWith(lister)`

Defined in thing.t, line 8187

list my contents for an "examine", using the given lister


### `examineSpecialContents`

Defined in thing.t, line 8409

Show the special descriptions of any contents. We'll run through the visible information list for the location; for any visible item inside me that is using its special description, we'll display the special description as a separate paragraph.


### `examineStatus`

Defined in thing.t, line 8168

Show any status associated with the object as part of the full description. This is shown after the basicExamine() message, and is only displayed if we can see full details of the object according to the viewing conditions.


### `failCheck(msg, [params])`

Defined in thing.t, line 8029

Generic "check" failure routine. This displays the given failure message, then performs an 'exit' to cancel the current command. 'msg' is the message to display - it can be a single-quoted string with the message text, or a property pointer. If 'msg' is a property pointer, any necessary message parameters can be supplied as additional 'params' arguments.


### `feelDesc`

Defined in thing.t, line 2296

The "feel description," which is the description displayed when an actor explicitly feels the object. As with taste, we don't distinguish transparency or distance.


### `fillMedium`

Defined in thing.t, line 6654

Get my "fill medium." This is an object of class FillMedium that permeates our interior, such as fog or smoke. This object affects the transmission of senses from one of our children to another, or between our interior and exterior.


### `findOpaqueObstructor(sense, obj)`

Defined in thing.t, line 6738

Find an opaque obstructor. This can be called immediately after calling senseObj() when senseObj() indicates that the object is opaquely obscured. We will find the nearest (by containment) object where the sense status is non-opaque, and we'll return that object.


### `findTouchObstructor(obj)`

Defined in thing.t, line 5958

Find the object that prevents us from touching the given object.


### `forEachConnectedContainer(func, [args])`

Defined in thing.t, line 5594

Call a function on each *connected* container. For most objects, this is the same as forEachContainer, but objects that don't connect their containers for sense purposes would do nothing here.


### `forEachContainer(func, [args])`

Defined in thing.t, line 5581

Call a function on each container. If we have no location, we won't invoke the function at all. We'll invoke the function as follows:


### `fromPOV(actor, pov, propToCall, [args])`

Defined in thing.t, line 4562

Call a method on this object from the given point of view. We'll push the current point of view, call the method, then restore the enclosing point of view.


### `getAllForTakeFrom(scopeList)`

Defined in thing.t, line 4855

Get a list of objects suitable for matching ALL in TAKE ALL FROM <self>. By default, this simply returns the list of everything in scope that's directly inside 'self'.


### `getAllPathsTo(obj)`

Defined in thing.t, line 6299

Build a vector containing all of the possible paths we can traverse to get from me to the given object. The return value is a vector of paths; each path is a list of containment operations needed to get from here to there.


### `getAnnouncementDistinguisher(lst)`

Defined in thing.t, line 2362

Get the distinguisher to use for printing this object's name in an action announcement (such as a multi-object, default object, or vague-match announcement). We check the global option setting to see if we should actually use distinguishers for this; if so, we call getInScopeDistinguisher() to find the correct distinguisher, otherwise we use the "null" distinguisher, which simply lists objects by their base names.


### `getBagAffinities(lst)`

Defined in thing.t, line 4209

Get "bag of holding" affinities for the given list of objects. For each item in the list, we'll get the item's bulk, and get each bag's affinity for containing the item. We'll note the bag with the highest affinity. Once we have the list, we'll put it in descending order of affinity, and return the result as a vector.


### `getBagsOfHolding(vec)`

Defined in thing.t, line 4352

Find all of the bags of holding contained within this object and add them to the given vector. By default, we'll simply recurse into our children so they can add their bags of holding.


### `getBestDistinguisher(lst)`

Defined in thing.t, line 2385

Get a distinguisher that differentiates me from all of the other objects in the given list, if possible, or from as many of the other objects as possible.


### `getBulk`

Defined in thing.t, line 3969

Calculate my total bulk. Most objects have a fixed external shape (and thus bulk) that doesn't vary as contents are added or removed, so our default implementation simply returns our intrinsic bulk without considering any contents.


### `getBulkWithin`

Defined in thing.t, line 3743

Calculate the bulk contained within this object. By default, we'll simply add up the bulks of all of our contents.


### `getCarryingActor`

Defined in thing.t, line 5337

Get the carrying actor. This is the nearest enclosing location that's an actor.


### `getCommonContainer(obj)`

Defined in thing.t, line 4630

Get the container (direct or indirect) we have in common with the object, if any.


### `getCommonDirectContainer(obj)`

Defined in thing.t, line 4607

Get the direct container we have in common with the given object, if any. Returns at most one common container. Returns nil if there is no common location.


### `getConnectedContainers`

Defined in thing.t, line 5604

Get a list of all of my connected containers. This simply returns the list that forEachConnectedContainer() iterates over.


### `getConnectorTo(actor, dest)`

Defined in thing.t, line 3511

Search our direction list for a connector that will lead the given actor to the given destination.


### `getContentsForExamine(lister, infoTab)`

Defined in thing.t, line 4954

Get the listed contents in a direct examination of this object. By default, this simply returns a list of all of our direct contents that are included in the info table.


### `getDestName(actor, origin)`

Defined in thing.t, line 3760

get my "destination name," for travel purposes; by default, we simply defer to our location, if we have one


### `getDropDestination(obj, path)`

Defined in thing.t, line 3813

Get the destination for an object dropped within me. Ordinary objects can't contain actors, so an actor can't directly drop something within a regular Thing, but the same effect could occur if an actor throws a projectile, since the projectile might reach either the target or an intermediate obstruction, then bounce off and land in whatever contains the object hit.


### `getEncumberingBulk(actor)`

Defined in thing.t, line 3988

Calculate the amount of bulk that this object contributes towards encumbering an actor directly holding the item. By default, this simply returns my total bulk.


### `getEncumberingWeight(actor)`

Defined in thing.t, line 4008

Calculate the amount of weight that this object contributes towards encumbering an actor directly holding the item. By default, this simply returns my total weight.


### `getExtraScopeItems(actor)`

Defined in thing.t, line 5715

Get my extra scope items. This is a list of any items that we want to add to command scope (i.e., the set of all items to which an actor is allowed to refer with noun phrases) when we are ourselves in the command scope. Returns a list of the items to add (or just [] if there are no items to add).


### `getHitFallDestination(thrownObj, path)`

Defined in thing.t, line 9370

Get the "hit-and-fall" destination for a thrown object. This is called when we interrupt a thrown object's trajectory because we're in the way of its trajectory.


### `getIdentityObject`

Defined in thing.t, line 4687

Get our "identity" object. This is the object that we appear to be an inseparable part of.


### `getInScopeDistinguisher`

Defined in thing.t, line 2374

Get a distinguisher that differentiates me from all of the other objects in scope, if possible, or at least from some of the other objects in scope.


### `getListedContents(lister, infoTab)`

Defined in thing.t, line 4939

Get my listed contents for recursive object descriptions. This returns the list of the direct contents that we'll mention when we're examining our container's container, a further enclosing container, or the enclosing room.


### `getLocPushTraveler(trav, obj)`

Defined in thing.t, line 3379

Get the "location push traveler" - this is the object that's going to travel for a push-travel action performed by a traveler within this location. This is called by a traveler within this location to find out if the location wants to be involved in the travel, as a vehicle might be. By default, we let our location handle it, if we have one.


### `getLocTraveler(trav, conn)`

Defined in thing.t, line 3362

Get the location traveler - this is the object that's actually going to change location when a traveler within this location performs a travel command to travel via the given connector. By default, we'll indicate what our containing room indicates. (The enclosing room might be a vehicle or an ordinary room; in any case, it'll know what to do, so we merely have to ask it.)


### `getMovePathTo(newLoc)`

Defined in thing.t, line 5971

Get the path for moving this object from its present location to the given new container.


### `getNoise`

Defined in thing.t, line 4808

Get my associated noise object. By default, this looks for an item of class Noise directly within me.


### `getNominalDropDestination`

Defined in thing.t, line 3916

Get the nominal destination for an object dropped into this object. This is used to report where an object ends up when the object is moved into me by some indirect route, such as throwing the object.


### `getNominalOwner` *(overridden)*

Defined in thing.t, line 5306

Get the "nominal owner" of this object. This is the owner that we report for the object if asked to distinguish this object from another via the OwnershipDistinguisher. Note that the nominal owner is not necessarily the only owner, because an object can have multiple owners in some cases; however, the nominal owner must always be an owner, in that isOwnedBy(getNominalOwner()) should always return true.


### `getObjectNotifyList`

Defined in thing.t, line 7689

Get my notification list - this is a list of objects on which we must call beforeAction and afterAction when this object is involved in a command as the direct object, indirect object, or any addition object (other than as the actor performing the command).


### `getOdor`

Defined in thing.t, line 4822

Get my associated odor object. By default, this looks for an item of class Odor directly within me.


### `getOutermostRoom`

Defined in thing.t, line 3318

Get the outermost containing room. We return our container, if we have one, or self if not.


### `getOutermostVisibleRoom(pov)`

Defined in thing.t, line 3325

get the outermost room that's visible from the given point of view


### `getRoomNotifyList`

Defined in thing.t, line 3674

Get the notification list actions performed by actors within this object. Ordinary objects don't have room notification lists, but we might be part of a nested set of objects that includes rooms, so simply look to our container for the notification list.


### `getRoomPartLocation(part)`

Defined in thing.t, line 3632

Get the apparent location of one of our room parts (the floor, the ceiling, etc). By default, we'll simply ask our container about it, since a nested room by default doesn't have any of the standard room parts.


### `getStateWithInfo(info, pov)`

Defined in thing.t, line 2128

Get the "listing state" of the object, given the visual sense information for the object from the point of view for which we're generating the listing. This returns a ThingState object describing the object's state for the purposes of listings. This should return nil if the object doesn't have varying states for listings.


### `getStatuslineExitsHeight`

Defined in thing.t, line 3449

get the status line exit lister height - defer to our location


### `getThrowPathTo(newLoc)`

Defined in thing.t, line 5985

Get the path for throwing this object from its present location to the given target object.


### `getTouchPathTo(obj)`

Defined in thing.t, line 5868

Get the path for this object reaching out and touching the given object. This can be used to determine whether or not an actor can touch the given object.


### `getTravelConnector(dir, actor)`

Defined in thing.t, line 3471

Get the travel connector from this location in the given direction.


### `getVisualSenseInfo`

Defined in thing.t, line 6505

Get the visual sense information for this object from the current global point of view. If we have explicit sense information set with setSenseInfo, we'll return that; otherwise, we'll calculate the current sense information for the given point of view. Returns a SenseInfo object giving the information.


### `getWeight`

Defined in thing.t, line 3934

Calculate my total weight. Weight is generally inclusive of the weights of contents or components, because anything inside an object normally contributes to the object's total weight.


### `hasCollectiveGroup(g)`

Defined in thing.t, line 2519

Are we associated with the given collective group? We do if it's in our collectiveGroups list.


### `hideFromAll(action)`

Defined in thing.t, line 1648

Hide from 'all' for a given action. If this returns true, this object will never be included in 'all' lists for the given action class. This should generally be set only for objects that serve some sort of internal purpose and don't represent physical objects in the model world. By default, objects are not hidden from 'all' lists.


### `hideFromDefault(action)`

Defined in thing.t, line 1655

Hide from defaulting for a given action. By default, we're hidden from being used as a default object for a given action if we're hidden from the action for 'all'.


### `initializeEquivalent`

Defined in thing.t, line 4739

Initialize this class object for listing its instances that are marked with isEquivalent. We'll initialize a list group that lists our equivalent instances as a group.


### `initializeLocation`

Defined in thing.t, line 4722

Initialize my location's contents list - add myself to my container during initialization


### `initializeThing`

Defined in thing.t, line 4700

General initialization - this will be called during preinit so that we can set up the initial values of any derived internal properties.


### `inRoomName(pov)`

Defined in en_us.t, line 1287

A prepositional phrase that can be used to describe things that are in this room as seen from a remote point of view. This should be something along the lines of "in the airlock", "at the end of the alley", or "on the lawn".


### `iobjFor(AttachTo)`

Defined in thing.t, line 9819


### `iobjFor(AttackWith)`

Defined in thing.t, line 9152

it makes as much sense to attack any object as any other, but by default attacking an object has no effect


### `iobjFor(BurnWith)`

Defined in thing.t, line 9794


### `iobjFor(CleanWith)`

Defined in thing.t, line 10052


### `iobjFor(CutWith)`

Defined in thing.t, line 9871


### `iobjFor(DetachFrom)`

Defined in thing.t, line 9834


### `iobjFor(DigWith)`

Defined in thing.t, line 9524


### `iobjFor(FastenTo)`

Defined in thing.t, line 10134


### `iobjFor(GiveTo)`

Defined in thing.t, line 8988

inherit any further processing


### `iobjFor(LockWith)`

Defined in thing.t, line 9948


### `iobjFor(MoveWith)`

Defined in thing.t, line 9591


### `iobjFor(PlugInto)`

Defined in thing.t, line 10184


### `iobjFor(PourInto)`

Defined in thing.t, line 10012


### `iobjFor(PourOnto)`

Defined in thing.t, line 10027


### `iobjFor(PutBehind)`

Defined in thing.t, line 8915


### `iobjFor(PutIn)`

Defined in thing.t, line 8846

verify the transfer


### `iobjFor(PutOn)`

Defined in thing.t, line 8879

verify the transfer


### `iobjFor(PutUnder)`

Defined in thing.t, line 8899


### `iobjFor(ScrewWith)`

Defined in thing.t, line 10234


### `iobjFor(ShowTo)`

Defined in thing.t, line 9051

The actor performing the showing must also be visible to the indirect object, otherwise the actor wouldn't be able to attract the indirect object's attention to do the showing.


### `iobjFor(TakeFrom)`

Defined in thing.t, line 8743

we've passed our checks, so process it as a regular "take"


### `iobjFor(ThrowAt)`

Defined in thing.t, line 9231

process a 'throw' operation, finishing with hitting the target if we get that far


### `iobjFor(ThrowTo)`

Defined in thing.t, line 9477

process a 'throw' operation, finishing with the target trying to catch the object if we get that far


### `iobjFor(TurnWith)`

Defined in thing.t, line 9637


### `iobjFor(UnfastenFrom)`

Defined in thing.t, line 10159


### `iobjFor(UnlockWith)`

Defined in thing.t, line 9963


### `iobjFor(UnplugFrom)`

Defined in thing.t, line 10209


### `iobjFor(UnscrewWith)`

Defined in thing.t, line 10259


### `isActorTravelReady(conn)`

Defined in thing.t, line 3418

Determine if the current gActor, who is directly in this location, is "travel ready." This means that the actor is ready, as far as this location is concerned, to traverse the given connector. By default, we'll defer to our location.


### `isComponentOf(obj)`

Defined in thing.t, line 4693

Am I a component of the given object? The base Thing is not a component of anything, so we'll simply return nil.


### `isDirectlyIn(obj)`

Defined in thing.t, line 5059

Determine if I'm directly inside another Thing. Returns true if this object is contained directly within obj. Returns nil if this object isn't directly within obj, even if it is indirectly in obj (i.e., its container is directly or indirectly in obj).


### `isHeldBy(actor)`

Defined in thing.t, line 5129

Determine if I'm "held" by an actor, for the purposes of being manipulated in an action. In most cases, an object is considered held by an actor if it's directly within the actor's inventory, because the actor's direct inventory represents the contents of the actors hands (or equivalent).


### `isIn(obj)`

Defined in thing.t, line 5000

Determine if I'm is inside another Thing. Returns true if this object is contained within 'obj', directly or indirectly (that is, this returns true if my immediate container is 'obj', OR my immediate container is in 'obj', recursively defined).


### `isInFixedIn(loc)`

Defined in thing.t, line 5099

Determine if this object is contained within an item fixed in place within the given location. We'll check our container to see if its contents are within an object fixed in place in the given location.


### `isListed`

Defined in thing.t, line 1681

Determine if I'm to be listed at all in my room's description, and in descriptions of objects containing my container.


### `isListedInContents`

Defined in thing.t, line 1693

Determine if I'm listed in explicit "examine" and "look in" descriptions of my direct container.


### `isListedInInventory`

Defined in thing.t, line 1699

Determine if I'm listed in inventory listings. By default, we include every item in an inventory list.


### `isListedInRoomPart(part)`

Defined in thing.t, line 1713

Determine if I'm listed as being located in the given room part. We'll first check to make sure the object is nominally contained in the room part; if not, it's not listed in the room part. We'll then ask the room part itself to make the final determination.


### `isLookAroundCeiling(actor, pov)`

Defined in thing.t, line 2738

Are we the "look around ceiling"? If so, it means that a LOOK AROUND for an actor within this location (or from a point of view within this location) will use our own interior description, via lookAroundWithin(). If we're not the ceiling, then we defer to our location, letting it describe its interior.


### `isNominallyIn(obj)`

Defined in thing.t, line 5070

Determine if I'm "nominally" inside the given Thing. Returns true if the object is actually within the given object, OR the object is a room part and I'm nominally in the room part.


### `isNominallyInRoomPart(part)`

Defined in thing.t, line 1744

Determine if we're nominally in the given room part (floor, ceiling, wall, etc). This returns true if we *appear* to be located directly in/on the given room part object.


### `isOccludedBy(occluder, sense, pov)`

Defined in thing.t, line 6693

Am I occluded by the given Occluder when viewed in the given sense from the given point of view? The default Occluder implementation calls this on each object involved in the sense path to determine if it should occlude the object. Returns true if we're occluded by the given Occluder, nil if not. By default, we simply return nil to indicate that we're not occluded.


### `isOrIsIn(obj)`

Defined in thing.t, line 5106

Am I either inside 'obj', or equal to 'obj'?


### `isOwnedBy(obj)` *(overridden)*

Defined in thing.t, line 5197

Determine if I'm "owned" by another object. By default, if we have an explicit owner, then we are owned by 'obj' if and only if 'obj' is our explicit owner; otherwise, if 'obj' is our immediate location, and our immediate location can own us (as reported by obj.canOwn(self)), then 'obj' owns us; otherwise, 'obj' owns us if our immediate location CANNOT own us AND our immediate location is owned by 'obj'. This last case is tricky: it means that if we're inside something other than 'obj' that can own us, such as another actor, then 'obj' doesn't own us because our immediate location does; it also means that if we're inside an object that has an explicit owner rather than an owner based on location, we have the same explicit owner, so a dollar bill inside Bob's wallet which is in turn being carried by Charlie is owned by Bob, not Charlie.


### `isShipboard`

Defined in thing.t, line 3716

Are we aboard a ship? By default, we'll return our location's setting for this property; if we have no location, we'll return nil. In general, this should be overridden in shipboard rooms to return true.


### `isVocabEquivalent(obj)`

Defined in thing.t, line 2473

Determine if I'm equivalent, for the purposes of command vocabulary, to given object.


### `itIs`

Defined in en_us.t, line 1026

get a string with the appropriate pronoun for the object plus the correct conjugation of 'to be'


### `itNom`

Defined in en_us.t, line 1002

get a string with the appropriate pronoun for the object for the nominative case, objective case, possessive adjective, possessive noun


### `itObj`

Defined in en_us.t, line 1003


### `itPossAdj`

Defined in en_us.t, line 1004


### `itPossNoun`

Defined in en_us.t, line 1005


### `itVerb(verb)`

Defined in en_us.t, line 1040

get a string with the appropriate pronoun for the object plus the correct conjugation of the given regular verb for the appropriate person


### `listCardinality(lister)`

Defined in en_us.t, line 784

The grammatical cardinality of this item when it appears in a list. This is used to ensure verb agreement when mentioning the item in a list of items. ("Cardinality" is a fancy word for "how many items does this look like").


### `localDirectionLinkForConnector(conn)`

Defined in thing.t, line 3559

Find the "local" direction link from this object to the given travel connector. We'll only consider our own local direction links; we won't consider enclosing objects.


### `lookAround(actor, verbose)`

Defined in thing.t, line 2659

Look around from the point of view of this object and on behalf of the given actor. This can be used to generate a description as seen from this object by the given actor, and is suitable for cases where the actor can use this object as a sensing device. We simply pass this through to lookAroundPov(), passing 'self' as the point-of-view object.


### `lookAroundPov(actor, pov, verbose)`

Defined in thing.t, line 2692

Look around from within this object, looking from the given point of view and on behalf of the given actor.


### `lookAroundWithin(actor, pov, verbose)`

Defined in thing.t, line 2781

Provide a "room description" of the interior of this object. This routine is primarily intended as a subroutine of lookAround() and lookAroundPov() - most game code shouldn't need to call this routine directly. Note that if you *do* call this routine directly, you *must* set the global point-of-view variables, which you can do most easily by calling this routine indirectly through the fromPOV() method.


### `lookAroundWithinContents(actor, illum, infoTab)`

Defined in thing.t, line 3079

Show my room contents for a "look around" description within this object.


### `lookAroundWithinDesc(actor, illum)`

Defined in thing.t, line 3032

Show our "look around" long description. This is used to display the location's full description when we're providing the room description - that is, when the actor doing the looking is inside me. This displays only the room-specific portion of the room's description; it does not display the status line or anything about the room's dynamic contents.


### `lookAroundWithinName(actor, illum)`

Defined in thing.t, line 3003

Show my name for a "look around" command. This is used to display the location name when we're providing the room description. 'illum' is the ambient visual sense level at the point of view.


### `lookAroundWithinSense(actor, pov, sense, lister)`

Defined in thing.t, line 3233

Add to the room description a list of things we notice through a specific sense. This is used to add things we can hear and smell to a room description.


### `lookAroundWithinShowExits(actor, illum)`

Defined in thing.t, line 3267

Show the exits from this room as part of a description of the room, if applicable. By default, if we have an exit lister object, we'll invoke it to show the exits.


### `lookInDesc`

Defined in thing.t, line 2187

Our LOOK IN description. This is shown when we explicitly LOOK IN the object. By default, we just report that there's nothing unusual inside.


### `mainExamine`

Defined in thing.t, line 8062

Main examination processing. This is called with the current global POV set to the actor performing the 'examine' command.


### `mainMoveInto(newContainer)`

Defined in thing.t, line 5479

Main moveInto - this is the mid-level containment changer; this routine sends notifications to the old and new container, but doesn't notify anything along the connecting sense path.


### `mapPushTravelHandlers(PushTravelThrough, GoThrough)`

Defined in thing.t, line 10301

For all of the two-object forms, map these using our general push-travel mapping. We do all of this mapping here, rather than in the action definition, so that individual objects can change the meanings of these verbs for special cases as appropriate.


### `mapPushTravelHandlers(PushTravelEnter, Enter)`

Defined in thing.t, line 10302


### `mapPushTravelHandlers(PushTravelGetOutOf, GetOutOf)`

Defined in thing.t, line 10303


### `mapPushTravelHandlers(PushTravelClimbUp, ClimbUp)`

Defined in thing.t, line 10304


### `mapPushTravelHandlers(PushTravelClimbDown, ClimbDown)`

Defined in thing.t, line 10305


### `meetsObjHeld(actor)`

Defined in thing.t, line 5147

Are we being held by the given actor for the purposes of the objHeld precondition? By default, and in almost all cases, this simply returns isHeldBy(). In some rare cases, it might make sense to consider an object to meet the objHeld condition even if isHeldBy returns nil; for example, an actor's hands and other body parts can't be considered to be held, but they also don't need to be for any command operating on them.


### `mergeSenseInfo(a, b)`

Defined in thing.t, line 7592

Merge two SenseInfo items. Chooses the "better" of the two items and returns it, where "better" is defined as more transparent, or, transparencies being equal, brighter in ambient energy.


### `mergeSenseInfoTable(a, b)`

Defined in thing.t, line 7569

Merge two senseInfoTable tables. Merges the second table into the first. If an object appears only in the first table, the entry is left unchanged; if an object appears only in the second table, the entry is added to the first table. If an object appears in both tables, we'll keep the one with better detail or brightness, adding it to the first table if it's the one in the second table.


### `moveInto(newContainer)`

Defined in thing.t, line 5448

Move this object to a new container. Before the move is actually performed, we notify the items in the movement path of the change, then we send notifyRemove and notifyInsert messages to the old and new containment trees, respectively.


### `moveIntoForTravel(newContainer)`

Defined in thing.t, line 5465

Move this object to a new container as part of travel. This is almost the same as the regular moveInto(), but does not attempt to calculate and notify the sense path to the new location. We omit the path notification because travel is done via travel connections, which are not necessarily the same as sense connections.


### `moveIntoNotifyPath(newContainer)`

Defined in thing.t, line 5526

Notify each element of the move path of a moveInto operation.


### `mustMoveObjInto(obj)`

Defined in thing.t, line 5385

Report a failure of the condition that tryMovingObjInto tries to bring into effect. By default, this simply says that the object must be in 'self'. Some objects might want to override this when they describe containment specially; for example, an actor might want to say that the actor "must be carrying" the object.


### `nameIs`

Defined in en_us.t, line 1826

get my name plus a being verb ("the box is")


### `nameIsnt`

Defined in en_us.t, line 1829

get my name plus a negative being verb ("the box isn't")


### `nameVerb(verb)`

Defined in en_us.t, line 1839

My name with the given regular verb in agreement: in the present tense, if my name has singular usage, we'll add 's' to the verb, otherwise we won't. In the past tense, we'll add 'd' (or 'ed'). This can't be used with irregular verbs, or with regular verbs that have the last consonant repeated before the past -ed ending, such as "deter".


### `normalizePath(path)`

Defined in thing.t, line 6441

"Normalize" a containment path to remove redundant containment traversals.


### `notePromptByOwnerLoc(ownerPriority)`

Defined in en_us.t, line 1433

Note that I'm being used in a disambiguation prompt by owner/location. If we're showing the owner, we'll set the antecedent for the owner's pronoun, if the owner is a 'him' or 'her'; this allows the player to refer back to our prompt text with appropriate pronouns.


### `notePromptByPossAdj`

Defined in en_us.t, line 1452

Note that we're being used in a prompt question with our possessive adjective. If we're a 'him' or a 'her', set our pronoun antecedent so that the player's response to the prompt question can refer back to the prompt text by pronoun.


### `noteSeenBy(actor, prop)`

Defined in thing.t, line 1612

Note that I've been seen by the given actor, setting the given "seen" property. This routine notifies the object that it's just been observed by the given actor, allowing it to take any special action it wants to take in such cases.


### `notifyInsert(obj, newCont)`

Defined in thing.t, line 7869

Receive notification that we are about to insert a new object into this container. 'obj' is the object being moved, and 'newCont' is the new direct container (which might be a child of ours). This is normally called during the action() phase.


### `notifyMoveInto(newCont)`

Defined in thing.t, line 7889

Receive notification that I'm about to be moved to a new container. By default, we do nothing; subclasses can override this to do any special processing when this object is moved. This is normally called during the action() phase.


### `notifyMoveViaPath(obj, dest, op)`

Defined in thing.t, line 6078

Check moving an object through this container via a path. This method is called during moveInto to notify each element along a move path that the movement is about to occur. We call checkMoveViaPath(); if it indicates failure, we'll report the failure encoded in the status object and terminate the command with 'exit'.


### `notifyRemove(obj)`

Defined in thing.t, line 7854

Receive notification that we are about to remove an object from this container. This is normally called during the action() phase.


### `// obscuredDesc (obs)`

Defined in thing.t, line 2233

The "obscured" description. If this is defined for an object, then we call it to display the description when an actor explicitly examines this object from a point of view where we have an "obscured" sight path to the object.


### `obscuredSmellDesc(obs)`

Defined in thing.t, line 2280

obscured smell description


### `obscuredSoundDesc(obs)`

Defined in thing.t, line 2265

obscured sound description


### `pluralNameFrom(str)`

Defined in en_us.t, line 1725

Get the plural form of the given name string. If the name ends in anything other than 'y', we'll add an 's'; otherwise we'll replace the 'y' with 'ies'. We also handle abbreviations and individual letters specially.


### `processThrow(target, hitProp)`

Defined in thing.t, line 9244

Process a 'throw' command. This is common handling that can be used for any sort of throwing (throw at, throw to, throw in, etc). The projectile is self, and 'target' is the thing we're throwing at or to. 'hitProp' is the property to call on 'target' if we reach the target.


### `propHidesProp(prop1, prop2)`

Defined in thing.t, line 7911

Determine if one property on this object effectively "hides" another. This is a sort of override check for two distinct properties.


### `propWithPresent(prop, [args])`

Defined in en_us.t, line 1927

Invoke a property (with an optional argument list) on this object while temporarily switching to the present tense, and return the result.


### `putInName`

Defined in en_us.t, line 1301

Provide the prepositional phrase for an object being put into me. For a container, for example, this would say "into the box"; for a surface, it would say "onto the table." By default, we return our library message given by our putDestMessage property; this default is suitable for most cases, but individual objects can customize as needed. When customizing this, be sure to make the phrase suitable for use in sentences like "You put the book <<putInName>>" and "The book falls <<putInName>>" - the phrase should be suitable for a verb indicating active motion by the object being received.


### `receiveDrop(obj, desc)`

Defined in thing.t, line 3895

Receive a dropped object. This is called when we are the actual (not nominal) drop destination for an object being dropped, thrown, or otherwise discarded. This routine is responsible for carrying out the drop operation, and reporting the result of the command.


### `// remoteDesc (pov)`

Defined in thing.t, line 2247

The "remote" description. If this is defined for an object, then we call it to display the description when an actor explicitly examines this object from a separate top-level location. That is, when the actor's outermost enclosing room is different from our own outermost enclosing room, we'll use this description.


### `remoteInitSpecialDesc(actor)`

Defined in thing.t, line 1463

the initial remote special description


### `remoteRoomContentsLister(other)`

Defined in thing.t, line 3305

Get my lister for the contents of the given remote room. A remote room is a separate top-level room that an actor can see from its current location; for example, if two top-level rooms are connected by a window, so that an actor standing in one room can see into the other room, then the other room is the remote room, from the actor's perspective.


### `remoteSpecialDesc(actor)`

Defined in thing.t, line 1212

The "remote" special description. This is the special description that will be used when this object is not in the point-of-view actor's current top-level room, but is visible in a connected room. For example, if two top-level rooms are connected by a window, so that an actor in one room can see the objects in the other room, this method will be used to generate the description of the object when the actor is in the other room, viewing this object through the window.


### `removeFromContents(obj)`

Defined in thing.t, line 5409

Remove an object from my contents.


### `removeObjectNotifyItem(obj)`

Defined in thing.t, line 7710

remove an item from the registered notification list


### `restoreLocation(oldLoc)`

Defined in thing.t, line 5432

Restore a previously saved location. Does not trigger any side effects.


### `roomActorThereDesc(actor)`

Defined in thing.t, line 2628

Describe an actor in this location either from the point of view of a separate top-level room, or at a distance. This is called when we're showing a room description (for LOOK AROUND), and the given actor is in a remote room or at a distance visually from the actor doing the looking, and the given actor is contained within this room.


### `roomContentsLister`

Defined in thing.t, line 3279

Get my lighted room contents lister - this is the Lister object that we use to display the room's contents when the room is lit. We'll return the default library room lister.


### `roomDaemon`

Defined in thing.t, line 3644

By default, an object containing the player character will forward the roomDaemon() call up to the container.


### `roomDarkDesc`

Defined in thing.t, line 2613

show our interior description in the dark


### `roomDesc`

Defined in thing.t, line 2582

Show our interior description. We use this to generate the long "look" description for the room when an actor is within this object and cannot see the enclosing room.


### `roomFirstDesc`

Defined in thing.t, line 2591

Show our first-time room description. This is the description we show when the actor is seeing our interior description for the first time. By default, we just show the ordinary room description, but this can be overridden to provide a special description the first time the actor sees the room.


### `roomRemoteDesc(actor)`

Defined in thing.t, line 2607

Show our remote viewing description. This is used when we show a description of a room, via lookAroundWithin, and the actor who's viewing the room is remote. Note that the library never does this itself, since there's no command in the basic library that lets a player view a remote room. However, a game might want to generate such a description to handle a command like LOOK THROUGH KEYHOLE, so we provide this extra description method for the game's use.


### `roomTravelPreCond`

Defined in thing.t, line 3395

Get the travel preconditions for an actor in this location. For ordinary objects, we'll just defer to our container, if we have one.


### `saveLocation`

Defined in thing.t, line 5419

Save my location for later restoration. Returns a value suitable for passing to restoreLocation.


### `selectPathTo(obj, traverseProp)`

Defined in thing.t, line 6106

Choose a path from this object to a given object. If no paths are available, returns nil. If any paths exist, we'll find the shortest usable one, calling the given property on each object in the path to determine if the traversals are allowed.


### `sendNotifyInsert(obj, newCont, msg)`

Defined in thing.t, line 7784

Send the given notification to each direct parent, each of their direct parents, and so forth, stopping when we reach parents that we have in common with our new location. We don't notify parents in common with new location (or their parents).


### `sendNotifyRemove(obj, newLoc, msg)`

Defined in thing.t, line 7751

Send the given notification to each direct parent, each of their direct parents, and so forth, stopping when we reach parents that we have in common with our new location. We don't notify parents in common with new location (or their parents) because we're not actually removing the object from the common parents.


### `senseAmbientMax(senses)`

Defined in thing.t, line 6943

Determine the highest ambient sense level at this object for any of the given senses.


### `senseInfoTable(sense)`

Defined in thing.t, line 6818

Build a list of full information on all of the objects reachable from me through the given sense, along with full information for each object's sense characteristics.


### `senseObj(sense, obj)`

Defined in thing.t, line 6706

Determine how well I can sense the given object. Returns a SenseInfo object describing the sense path from my point of view to the object.


### `sensePathFromWithin(fromChild, sense, trans, obs, fill)`

Defined in thing.t, line 7380

Build a path from an object within me.


### `sensePathFromWithout(fromParent, sense, trans, obs, fill)`

Defined in thing.t, line 7469

Build a path from an object immediately containing me.


### `sensePathToContents(sense, trans, obs, fill)`

Defined in thing.t, line 7332

Build a sense path to my contents


### `sensePathToLoc(sense, trans, obs, fill)`

Defined in thing.t, line 7319

Build a path to my location or locations


### `sensePresenceList(sense)`

Defined in thing.t, line 6916

Build a list of the objects reachable from me through the given sense and with a presence in the sense.


### `setAllSeenBy(infoTab, actor)`

Defined in thing.t, line 1596

Mark everything visible as having been seen. 'infoTab' is a LookupTable of sight information, as returned by visibleInfoTable(). We'll mark everything visible in the table as having been seen by the actor, EXCEPT objects that have suppressAutoSeen set to true.


### `setContentsSeenBy(infoTab, actor)`

Defined in thing.t, line 1576

Mark all visible contents of 'self' as having been seen. 'infoTab' is a LookupTable of sight information, as returned by visibleInfoTable(). This should be called any time an object is examined in such a way that its contents should be considered to have been seen.


### `setGlobalParamName(name)`

Defined in thing.t, line 1147

Set the global parameter name dynamically. If you need to add a new global parameter name at run-time, call this rather than setting the property directly, to ensure that the name is added to the message builder's name table. You can also use this to delete an object's global parameter name, by passing nil for the new name.


### `setVisualSenseInfo(info)`

Defined in thing.t, line 6562

Set the explicit visual sense information; if this is not nil, getVisualSenseInfo() will return this rather than calculating the live value. Returns the old value, which is a SenseInfo or nil.


### `shineFromWithin(fromChild, sense, ambient, fill)`

Defined in thing.t, line 7194

Transmit ambient energy from an object within me. This transmits to my outer surface, and also to my own immediate children - in other words, to the peers of the child shining on us. We need to transmit to the source's peers right now, because it might degrade the ambient energy to go out through our surface.


### `shineFromWithout(fromParent, sense, level, fill)`

Defined in thing.t, line 7281

Transmit ambient energy from an object immediately containing me.


### `shineOnContents(sense, ambient, fill)`

Defined in thing.t, line 7127

Shine ambient energy at my surface onto my contents.


### `shineOnLoc(sense, ambient, fill)`

Defined in thing.t, line 7114

Transmit ambient energy to my location or locations.


### `showDistantSpecialDesc`

Defined in thing.t, line 1336

show the special description under distant viewing conditions


### `showDistantSpecialDescInContents(actor, cont)`

Defined in thing.t, line 1424


### `showInventoryContents(pov, lister, options, indent, infoTab)`

Defined in thing.t, line 4924

Show the contents of this object as part of an inventory listing. By default, we simply use the same listing we do for the normal contents listing.


### `showInventoryItem(options, pov, infoTab)`

Defined in thing.t, line 2088

Show this item as part of an inventory list. By default, we'll show the regular list item name.


### `showInventoryItemCounted(lst, options, pov, infoTab)`

Defined in thing.t, line 2093

show the item, using the inventory state name


### `showListItem(options, pov, infoTab)`

Defined in thing.t, line 1934

Show this item as part of a list. 'options' is a combination of ListXxx flags indicating the type of listing. 'infoTab' is a lookup table of SenseInfo objects giving the sense information for the point of view.


### `showListItemCounted(lst, options, pov, infoTab)`

Defined in thing.t, line 1977

Show this item as part of a list, grouped with a count of list-equivalent items.


### `showListItemCountedGen(lst, options, pov, infoTab, stateNameProp)`

Defined in thing.t, line 1989

General routine to show this item as part of a list, grouped with a count of list-equivalent items. 'stateNameProp' is the property of any list state object that we should use to obtain the name of the listing state.


### `showListItemGen(options, pov, infoTab, stateNameProp)`

Defined in thing.t, line 1945

General routine to show the item as part of a list. 'stateNameProp' is the property to use in any listing state object to obtain the state name.


### `showObjectContents(pov, lister, options, indent, infoTab)`

Defined in thing.t, line 4909

Show the contents of this object, as part of a recursive listing generated as part of the description of our container, our container's container, or any further enclosing container.


### `showObscuredSpecialDesc`

Defined in thing.t, line 1327

show the special description under obscured viewing conditions


### `showObscuredSpecialDescInContents(actor, cont)`

Defined in thing.t, line 1422


### `showRemoteSpecialDesc(actor)`

Defined in thing.t, line 1345

show the remote special description


### `showRemoteSpecialDescInContents(actor, cont)`

Defined in thing.t, line 1426


### `showSpecialDesc`

Defined in thing.t, line 1314

Show the special description, if we have one. If we are using our initial description, we'll show that; otherwise, if we have a specialDesc property, we'll show that.


### `showSpecialDescInContents(actor, cont)`

Defined in thing.t, line 1420

Show the special description in contents listings under various sense conditions. By default, we'll use the corresponding special descriptions for full room descriptions. These can be overridden to show special versions of the description when we're examining particular containers, if desired. 'actor' is the actor doing the looking.


### `showSpecialDescInContentsWithInfo(info, pov, cont)`

Defined in thing.t, line 1396

Show our special description as part of a parent's full description.


### `showSpecialDescWithInfo(info, pov)`

Defined in thing.t, line 1262

Show my special description, given a SenseInfo object for the visual sense path from the point of view of the description.


### `showStatuslineExits`

Defined in thing.t, line 3442

show exits in the statusline - defer to our location


### `showWornItem(options, pov, infoTab)`

Defined in thing.t, line 2102

Show this item as part of a list of items being worn.


### `showWornItemCounted(lst, options, pov, infoTab)`

Defined in thing.t, line 2107

show the item, using the worn-listing state name


### `smellDesc`

Defined in thing.t, line 2274

The "smell description," which is the description displayed when an actor explicitly smells the object. This is used when we have a transparent sense path to the object, and we have no "emanation" object; when we have an associated emanation object, we use its description instead of this one.


### `smellHereDesc`

Defined in thing.t, line 2310

Show the smell/sound description for the object as part of a room description. These are displayed when the object is in the room and it has a presence in the corresponding sense. By default, these show nothing.


### `soundDesc`

Defined in thing.t, line 2259

The "sound description," which is the description displayed when an actor explicitly listens to the object. This is used when we have a transparent sense path and no associated "emanation" object; when we have an associated emanation object, we use its description instead of this one.


### `soundHereDesc`

Defined in thing.t, line 2311


### `specialDescList(infoTab, cond)`

Defined in thing.t, line 8431

Given a visible object info table (from Actor.visibleInfoTable()), get the list of objects, filtered by the given condition and sorted by specialDescOrder.


### `specialPathFrom(src, vec)`

Defined in thing.t, line 6328

Get a "special" path from the given starting object to me. src.getAllPathsTo(obj) calls this on 'obj' when it can't find any actual containment path from 'src' to 'obj'. If desired, this method should add the path or paths to the vector 'vec'.


### `statusName(actor)`

Defined in thing.t, line 2950

Display the "status line" name of the room. This is normally a brief, single-line description.


### `stopThrowViaPath(projectile, path)`

Defined in thing.t, line 9341

Stop a 'throw' operation along a path. 'self' is the object in the path that is impassable by 'projectile' according to canThrowViaPath(), and 'path' is the getThrowPathTo-style path of objects traversed in the projectile's trajectory.


### `superHidesSuper(s1, s2)`

Defined in thing.t, line 7962

Determine if a given superclass of ours hides another superclass of ours, by being inherited (directly or indirectly) in our class list ahead of the other.


### `tasteDesc`

Defined in thing.t, line 2289

The "taste description," which is the description displayed when an actor explicitly tastes the object. Note that, unlike sound and smell, we don't distinguish levels of transparency or distance with taste, because tasting an object requires direct physical contact with it.


### `thatNom`

Defined in en_us.t, line 1015

demonstrative pronouns ('that' or 'those')


### `thatObj`

Defined in en_us.t, line 1020


### `theNameFrom(str)`

Defined in en_us.t, line 1173

Generate the definite-article name from the given name string. If my name is already qualified, don't add an article; otherwise, add a 'the' as the prefixed definite article.


### `theNameObj`

Defined in en_us.t, line 1166

theName in objective case. In most cases, this is identical to the normal theName, so we use that by default. This must be overridden if theName is a pronoun (which is usually only the case for player character actors; see our language-specific Actor modifications for information on that case).


### `theNameOwnerLoc(ownerPriority)`

Defined in en_us.t, line 1391

we have no owner - show as "an item in the location"


### `theNameWithOwner`

Defined in en_us.t, line 1223

theName with my nominal owner explicitly stated, if we have a nominal owner: "your backpack," "Bob's flashlight." If we have no nominal owner, this is simply my theName.


### `throwTargetCatch(obj, path)`

Defined in thing.t, line 9490

Process the effect of throwing the object 'obj' to the catcher 'self'. By default, we'll simply move the projectile into self.


### `throwTargetHitWith(projectile, path)`

Defined in thing.t, line 9310

Process the effect of throwing the object 'projectile' at the target 'self'. By default, we'll move the projectile to the target's drop location, and display a message saying that there was no effect other than the projectile dropping to the floor (or whatever it drops to). 'path' is the path we took to reach the target, as returned from getThrowPathTo(); this lets us determine how we approached the target.


### `throwViaPath(obj, op, target, path)`

Defined in thing.t, line 9281

Carry out a 'throw' operation along a path. 'self' is the projectile; 'obj' is the path element being traversed, and 'op' is the operation being used to traverse the element. 'target' is the object we're throwing 'self' at. 'path' is the projectile's full path (in getThrowPathTo format).


### `transmitAmbient(sense)`

Defined in thing.t, line 7066

Transmit my radiating energy to everything within reach of the sense.


### `transSensingIn(sense)`

Defined in thing.t, line 6584

Determine how accessible my contents are to a sense. Any items contained within a Thing are considered external features of the Thing, hence they are transparently accessible to all senses.


### `transSensingOut(sense)`

Defined in thing.t, line 6603

Determine how accessible peers of this object are to the contents of this object, via a given sense. This has the same meaning as transSensingIn(), but in the opposite direction: whereas transSensingIn() determines how accessible my contents are from the outside, this determines how accessible the outside is from the contents.


### `traversePath(path, func)`

Defined in thing.t, line 6195

Traverse a containment connection path, calling the given function for each element. In each call to the callback, 'obj' is the container object being traversed, and 'op' is the operation being used to traverse it.


### `tryHolding`

Defined in thing.t, line 5355

Try making the current command's actor hold me. By default, we'll simply try a "take" command on the object.


### `tryImplicitRemoveObstructor(sense, obj)`

Defined in thing.t, line 5829

Try an implicit action that would remove this object as an obstructor to 'obj' from the perspective of the current actor in the given sense. This is invoked when this object is acting as an obstructor between the current actor and 'obj' for the given sense, and the caller wants to perform a command that requires a clear sense path to the given object in the given sense.


### `tryMovingObjInto(obj)`

Defined in thing.t, line 5376

Try moving the given object into this object, with an implied command. By default, since an ordinary Thing doesn't have a way of adding new contents by a player command, this does nothing. Containers and other objects that can hold new contents can override this as appropriate.


### `useInitDesc`

Defined in thing.t, line 1508

Determine if I should be described on EXAMINE using my initial examine description (initDesc). This returns true if I have an initial examine desription that isn't nil, and I'm in my initial state. If this returns nil, we'll show our ordinary description (given by the 'desc' property).


### `useInitSpecialDesc`

Defined in thing.t, line 1498

Determine whether or not I should be mentioned in my containing room's description (on LOOK AROUND) using my initial special description (initSpecialDesc). This returns true if I have an initial description that isn't nil, and I'm in my initial state. If this returns nil, the object should be described in room descriptions using the ordinary generated message (either the specialDesc, if we have one, or the ordinary mention in the list of portable room contents).


### `useSpecialDesc`

Defined in thing.t, line 1358

Determine if we should use a special description. By default, we have a special description if we have either a non-nil specialDesc property, or we have an initial description.


### `useSpecialDescInContents(cont)`

Defined in thing.t, line 1382

Determine if we should use our special description in the given object's contents listings, for the purposes of "examine <cont>" or "look in <cont>". By default, we'll use our special description for a given container if we'd use our special description in general, AND we're actually inside the container being examined.


### `useSpecialDescInRoom(room)`

Defined in thing.t, line 1372

Determine if we should use our special description in the given room's LOOK AROUND description. By default, this simply returns useSpecialDesc().


### `useSpecialDescInRoomPart(part)`

Defined in thing.t, line 1798

Determine if I should show my special description with the description of the given room part (floor, ceiling, wall, etc).


### `verbEndingEs`

Defined in en_us.t, line 1910

Verb endings (present or past) for regular '-es/-ed' and '-y/-ies/-ied' verbs, agreeing with this object as the subject.


### `verbEndingIes`

Defined in en_us.t, line 1911


### `verbEndingS`

Defined in en_us.t, line 1900

Verb endings for regular '-s' verbs, agreeing with this object as the subject. We define several methods each of which handles the past tense differently.


### `verbToHave`

Defined in en_us.t, line 1851

'have' verb agreeing with this object as subject


### `verbWas`

Defined in en_us.t, line 1848

past tense being verb agreeing with object as subject


### `verifyFollowable`

Defined in thing.t, line 9120

Verify that I'm a followable object. By default, it's not logical to follow an arbitrary object. If I'm not followable, this routine will generate an appropriate illogical() explanation and return nil. If I'm followable, we'll return true.


### `verifyInsert(obj, newCont)`

Defined in thing.t, line 7827

Verify insertion of an object into my contents. By default we allow it, unless I'm already inside the other object. This is to be called only during verification.


### `verifyMoveTo(newLoc)`

Defined in thing.t, line 7734

Verify a proposed change of location of this object from its current container hierarchy to the given new container. We'll verify removal from each container up to but not including a parent that's in common with the new container - we stop upon reaching the common parent because the object isn't leaving the common parent, but merely repositioned around within it. We'll also verify insertion into each new parent from the first non-common parent on down to the immediate new container.


### `verifyRemove(obj)`

Defined in thing.t, line 7818

Verify removal of an object from my contents or a child object's contents. By default we allow the removal. This is to be called during verification only, so gVerifyResult is valid when this is called.


### `whatIf(func, [changes])`

Defined in thing.t, line 4043

"What if" test. Make the given changes temporarily, bypassing any side effects that would normally be associated with the changes; invokes the given callback; then remove the changes. Returns the result of calling the callback function.


### `whatIfHeldBy(func, actor)`

Defined in thing.t, line 4143

Run a what-if test to see what would happen if this object were being held directly by the given actor.


### `withVisualSenseInfo(pov, senseInfo, methodToCall, [args])`

Defined in thing.t, line 6528

Call a description method with explicit point-of-view and the related point-of-view sense information. 'pov' is the point of view object, which is usually an actor; 'senseInfo' is a SenseInfo object giving the sense information for this object, which we'll use instead of dynamically calculating the sense information for the duration of the routine called.


## Inherited Methods


*From [VocabObject](vocabobject.md):* [`addToDictionary`](vocabobject.md#addToDictionary), [`expandPronounList`](vocabobject.md#expandPronounList), [`filterResolveList`](vocabobject.md#filterResolveList), [`getFacets`](vocabobject.md#getFacets), [`inheritVocab`](vocabobject.md#inheritVocab), [`initializeVocab`](vocabobject.md#initializeVocab), [`initializeVocabWith`](vocabobject.md#initializeVocabWith), [`matchName`](vocabobject.md#matchName), [`matchNameCommon`](vocabobject.md#matchNameCommon), [`matchNameDisambig`](vocabobject.md#matchNameDisambig), [`throwNoMatchForLocation`](vocabobject.md#throwNoMatchForLocation), [`throwNoMatchForPossessive`](vocabobject.md#throwNoMatchForPossessive), [`throwNothingInLocation`](vocabobject.md#throwNothingInLocation)
