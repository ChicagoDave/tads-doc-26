# YesTopic

YesTopic : [MiscTopic](misctopic.md)

A YesTopic simply responds to a YES command typed by the player. It is most useful when placed in a [ConvNode](convnode.md). For now we'll give a single example of a YesTopic we'll use to handle the player's replying YES to the question Sarah's just asked (about cutting open the glass display case). We'll also make it a [SuggestedYesTopic](suggestedyestopic.md) so that it includes saying yes among the things suggested to the player at this point (for reasons that will shortly become apparent). Obviously, this YesTopic should be placed in the ConvNode we've just defined:

```tads3
++ YesTopic, SuggestedYesTopic
  topicResponse
  {
    "<q>Yes, do you think you can manage it?</q> you ask.\b
     <q>Watch me!</q> she replies. ";
     nestedActorAction(sarah, CutWith, bananaCase, diamondRing);
    "<q>There you are!</q> she declares, <q>Easy!</q> ";
  }
;
```
