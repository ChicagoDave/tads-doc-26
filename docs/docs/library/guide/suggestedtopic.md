# SuggestedTopic

SuggestedTopic : object

Although the player can ASK or TELL NPCs about anything, ASK THEM for anything, or attempt to GIVE or SHOW them anything that's available to be given or shown, only a comparatively few of these topics are likely to be implemented in your game. That may be fine if you want the players to have to guess what to ASK ABOUT etc., or because it should be reasonably obvious, but in some circumstances it may degenerate into a game of "guess the topic" (or even, "guess the wording of the topic"), which players may find simply frustrating.

To avoid this, you can provide players with a list of suggested topics, using subclasses of the SuggestedTopic class:

|  | ```tads3 SuggestedAskTopic ``` |
|---|---|

|  | ```tads3 SuggestedGiveTopic ``` |
|---|---|

|  | ```tads3 SuggestedNoTopic ``` |
|---|---|

|  | ```tads3 SuggestedShowTopic ``` |
|---|---|

|  | ```tads3 SuggestedTellTopic ``` |
|---|---|

|  | ```tads3 SuggestedTopicTree ``` |
|---|---|

|  | ```tads3 SuggestedYesTopic ``` |
|---|---|

Note that there are no composite types of SuggestedTopic (such as SuggestedAskTellTopic), because we shall either Suggest asking or telling, but not both on the same topic (even if it's a composite kind of topic like an AskTellTopic). Which brings us to the point that SuggestedTopic is a *mix-in* class, which means that you add particular type of SuggestedTopic you want to the class list of the TopicEntry in question. For example, to make the TopicEntry for asking Sarah about her diamond ring a SuggestedAskTopic, we can change it to:

```tads3
++ AskTopic, SuggestedAskTopic, StopEventList @diamondRing
  [ '<q>What does your ring look like?</q> you ask.\b
     <q>It\'s a plain platinum band with a solitaire diamond.</q> she tells you. ',
    '<q>This ring - it\'s important to you?</q> you inquire.\b
     <q>Oh yes!</q> {the sarah/she} declares, <q>It\'s not it\'s monetary value, so
     much; it\'s more a sentimental thing - you can\'t replace that with insurance
     money. Besides, I was so <i>incensed</i> when this bloke snatched it off me -
     why should he get away with it?</q>',
     new function {
       "<q>Have you any idea where your ring might be?</q> you ask.\b
       <q>Perhaps he dropped it back in there,</q> she suggests, nodding towards
        the open door,<q>let's go and see.</q><.p>";
        sarah.setCurState(sarahGuide1);
     },
     '<q>And the missing ring...</q> you begin.\b
      <q>... is a plain platinum band with a solitaire diamond.</q> she reminds you. '
  ]
  name = 'the diamond ring'
  timesToSuggest = 3
;
```

Then when player types TALK TO WOMAN to start a conversation, or uses the TOPICS command in the course of a conversation, the game will respond with "You could ask her about the diamond ring. " In this case it will suggest it three times (because we have set timesToSuggest to 3) and then stop.

The properties you may want to set on SuggestedTopic are:

- **name** - the name that will be given to this topic in the list of suggestions, after the phrase "You could ask about/ask for/tell about/show/give" You should *always* supply a value for this property, unless for some reason you override fullName.

- **fullName** - the title of the suggestion, suitable for following after "You could " (e.g. "You could ask about the diamond ring. "). You don't normally need to override this, since the library will construct a suitable phrase from the name property and the type of SuggestedTopic. If, however, you were creating your own custom kind of SuggestedTopic it might be useful to override this.

- **timesToSuggest** - rather than assuming that we have infinite curiosity about any particular topic, the game will assume we've exhausted our curiosity about it, that is it will stop suggesting it, after we have asked/told about (or shown or given) it this number of times. If you want this topic to go on being suggested *ad infinitum*, then set timesToSuggest to nil. By default, it's set to 1.

The default value of timesToSuggest*may* not be what you want where you have mixed in a Script class with a TopicEntry class to provide a list of responses. It may be that the subsequent responses are not significant and are just provided for variety in case the player should raise the topic again. Or it may be that they are sufficiently important that you want the player to work through them all. If the latter predominate among the SpecialTopics in your game, it may become just a little tedious to keep having to count the number of items in all the list and override timesToSuggest with the appropriate number. You may prefer it if the game automatically suggested a topic for the number of times there were fresh items in the list; in other words, instead of having timesToSuggest default to 1, you might prefer it to default to the number of different responses in the topic.

If you could prefer this, you can modify SuggestedTopic accordingly:

```tads3
/* If the TopicEntry associated with a SuggestedTopic is also an EventList
 * keep on suggesting till we've been right through the list - i.e.
 * make timesToSuggest correspond to the length of the list.
 */
modify SuggestedTopic
  timesToSuggest = (ofKind(EventList) ? eventList.length() : 1)
;
```

Bear in mind, though, that this may still not always give the behaviour you want, and that you will probably still need or want to override timesToSuggest manually on at least some SuggestedTopics.

The occasions when the game will display the currently active SuggestedTopics are:

- When the player types a TALK TO, GREET or HELLO command

- When the player issue a TOPICS command

- Inside a [ConvNode](convnode.md) when there is an active [SpecialTopic](specialtopic.md)

- Under programmer control, following the use of a <.topics> tag in any output

- By a call to the NPC's **suggestTopics(explicit)**method (where explicit is either true or nil, as in a TOPICS or a TALK TO command respectively)

It's perfectly feasible to add a new SuggestedTopic class to match a new TopicEntry class. For example, a little while back we showed how to implement a custom [PraiseTopic](misctopic.md). The only problem with it is that the player might never know it's there, or that PRAISE SARAH (for example) is a valid conversational command. The ideal solution to this is to create a SuggestedPraiseTopic that can be mixed in with PraiseTopic so that the player can discover its existence. Here's the definition we need:

```tads3
SuggestedPraiseTopic : SuggestedTopic
  suggestionGroup = [suggestionPraiseGroup]
  fullName = 'praise {it targetActor/him}'
  name = '{it targetActor/him}'
;
suggestionPraiseGroup : SuggestionListGroup
    groupPrefix = "praise "
;
```

Add SuggestedPraiseTopic to the class list of all the PraiseTopics (and any AltTopics associated with them), and you now find 'praise her' among the list of conversational commands you can address to Sarah; for example:

```

```

`++ PraiseTopic, SuggestedPraiseTopic, StopEventList
    [
        '<q>It\'s really very good of you to come with me.</q> you
        tell her.\b
        <q>Not at all,</q> she replies, <q>I\'m just hoping you are
        going to find the way out of here.</q>',
        '<q>I\'m really glad you\'re with me - whatever your reasons.</q>
        you remark, <q>Quite frankly, I\'m glad of your company.</q>\b
        <q>Me too,</q> she admits.',
        '<q>I do like you, you know.</q> you tell her.\b
        <q>Now, don\'t go all sentimental on me!</q> she complains, though
        there\'s a warm twinkle in her eye as she says it.',
        '<q>I\'m afraid I can\'t help finding you very attractive.</q> you
        confess.\b
        <q>I daresay neither of us can help that - what you find attractive,
        I mean.</q> she replies matter-of-factly. ',
        '<q>I really do appreciate having you around.</q> you tell her.\b
        <q>So you keep saying,</q> she observes. '
    ]
    isActive = (getActor.isProperName)
;

+++ AltTopic, SuggestedPraiseTopic, StopEventList
    [
        'You\'ve been pretty brave about that ghost - after all it
        was scary! you remark.\b
        It was, she agrees, and you\'ve been pretty brave too!',

        'You know, I really am glad you\'re with me. you tell her.\b
        Me too! she agrees warmly, giving your arm a little squeeze. '
    ]
    isActive = (getActor.hasSeen(ghost))
;`
