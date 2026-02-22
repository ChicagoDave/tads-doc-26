# VocabObject

*class* — defined in [thing.t](../by-file/thing.t.md) (line 532)


Object with vocabulary. This is the base class for any object that can define vocabulary words.


**Superclass chain:** `object` > **VocabObject**


<details><summary>Subclasses (120)</summary>

- [Thing](thing.md)
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
- [Topic](topic.md)

</details>


## Properties


### `canResolvePossessive`

Defined in thing.t, line 893

By default, every object can be used as the resolution of a possessive qualifier phrase (e.g., "bob" in "bob's book"). If this property is set to nil for an object, that object can never be used as a possessive. Note that has nothing to do with establishing ownership relationships between objects; it controls only the resolution of possessive phrases during parsing to concrete game objects.


### `disambigPromptOrder`

Defined in thing.t, line 777

Disambiguation prompt order. When we interactively prompt for help resolving an ambiguous noun phrase, we'll put the list of ambiguous matches in ascending order of this property value.


### `owner`

Defined in thing.t, line 977

our explicit owner, if any


### `pluralOrder`

Defined in thing.t, line 758

Plural resolution order. When a command contains a plural noun phrase, we'll sort the items that match the plural phrase in ascending order of this property value.


### `vocabLikelihood`

Defined in thing.t, line 788

Intrinsic parsing likelihood. During disambiguation, if the parser finds two objects with equivalent logicalness (as determined by the 'verify' process for the particular Action being performed), it will pick the one with the higher intrinsic likelihood value. The default value is zero, which makes all objects equivalent by default. Set a higher value to make the parser prefer this object in cases of ambiguity.


### `vocabWords`

Defined in en_us.t, line 373

The vocabulary initializer string for the object - this string can be initialized (most conveniently via a template) to a string of this format:


### `weakTokens`

Defined in thing.t, line 882

Our list of "weak" tokens. This is a token that is acceptable in our vocabulary, but which we can only use in combination with one or more "strong" tokens. (A token is strong if it's not weak, so we need only keep track of one or the other kind. Weak tokens are much less common than strong tokens, so it takes a lot less space if we store the weak ones instead of the strong ones.)


## Methods


### `addToDictionary(prop)`

Defined in en_us.t, line 393

add the words from a dictionary property to the global dictionary


### `construct`

Defined in en_us.t, line 379

On dynamic construction, initialize our vocabulary words and add them to the dictionary.


### `expandPronounList(typ, lst)`

Defined in thing.t, line 856

Expand a pronoun list. This is essentially complementary to filterResolveList: the function is to "unfilter" a pronoun binding that contains this object so that it restores any objects that would have been filtered out by filterResolveList from the original noun phrase binding.


### `filterResolveList(lst, action, whichObj, np, requiredNum)`

Defined in thing.t, line 815

Filter an ambiguous noun phrase resolution list. The parser calls this method for each object that matches an ambiguous noun phrase or an ALL phrase, to allow the object to modify the resolution list. This method allows the object to act globally on the entire list, so that the filtering can be sensitive to the presence or absence in the list of other objects, and can affect the presence of other objects.


### `getFacets`

Defined in thing.t, line 942

Get a list of the other "facets" of this object. A facet is another program object that to the player looks like the same or part of the same physical object. For example, it's often convenient to represent a door using two game objects - one for each side - but the two really represent the same door from the player's perspective.


### `getNominalOwner`

Defined in thing.t, line 974

Get our nominal owner. This is the owner that we report for this object if we're asked to distinguish this object from another object in a disambiguation prompt. The nominal owner isn't necessarily the only owner. Note that if getNominalOwner() returns a non-nil value, isOwnedBy(getNominalOwner()) should always return true.


### `inheritVocab(target, done)`

Defined in en_us.t, line 421

Inherit vocabulary from this class and its superclasses, adding the words to the given target object. 'target' is the object to which we add our vocabulary words, and 'done' is a vector of classes that have been visited so far.


### `initializeVocab`

Defined in en_us.t, line 401

initialize the vocabulary from vocabWords


### `initializeVocabWith(str)`

Defined in en_us.t, line 464

Initialize our vocabulary from the given string. This parses the given vocabulary initializer string and adds the words defined in the string to the dictionary.


### `isOwnedBy(obj)`

Defined in thing.t, line 962

Ownership: a vocab-object can be marked as owned by a given Thing. This allows command input to refer to the owned object using possessive syntax (such as, in English, "x's y").


### `matchName(origTokens, adjustedTokens)`

Defined in thing.t, line 597

Match a name as used in a noun phrase in a player's command to this object. The parser calls this routine to test this object for a match to a noun phrase when all of the following conditions are true:


### `matchNameCommon(origTokens, adjustedTokens)`

Defined in thing.t, line 718

Common handling for the main matchName() and the disambiguation handler matchNameDisambig(). By default, we'll check with our state object if we have a state object; if not, we'll simply return 'self' to indicate that we do indeed match the given tokens.


### `matchNameDisambig(origTokens, adjustedTokens)`

Defined in thing.t, line 697

Match a name in a disambiguation response. This is similar to matchName(), but is called for each object in an ambiguous object list for which a disambiguation response was provided. As with matchName(), we only call this routine for objects that match the dictionary vocabulary.


### `throwNoMatchForLocation(txt)`

Defined in thing.t, line 915

Throw an appropriate parser error when this object is used in a player command to locationally qualify another object (such as when we're the box in "examine the key in the box"), and there's no object among our contents with the given name. By default, we throw the standard parser error ("You see no key in the box").


### `throwNoMatchForPossessive(txt)`

Defined in thing.t, line 905

Throw an appropriate parser error when this object is used in a player command as a possessive qualifier (such as when 'self' is the "bob" in "take bob's key"), and we don't own anything matching the object name that we qualify. This is only called when 'self' is in scope. By default, we throw the standard parser error ("Bob doesn't appear to have any such thing"). 'txt' is the lower-cased, HTMLified text that of the qualified object name ("key" in "bob's key").


### `throwNothingInLocation`

Defined in thing.t, line 925

Throw an appropriate parser error when this object is used in a player command to locationally qualify "all" (such as when we're the box in "examine everything in the box"), and we have no contents. By default, we throw the standard parser error ("You see nothing unusual in the box").
