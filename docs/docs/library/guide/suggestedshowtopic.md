# SuggestedShowTopic

SuggestedShowTopic : [SuggestedTopic](suggestedtopic.md)

A SuggestedAskTopic is the particular type of [SuggestedTopic](suggestedtopic.md) that prompts the player to SHOW such-and-such to so-and-so.

For example, if we want to suggest to the player that he might show the green ticket to the curator, we could add the following to the appropriate GiveTopic (previously defined):

```tads3
++ GiveShowTopic, SuggestedShowTopic  @museumTicket
  "<q>Thank you, that's fine.</q> {the curator/he} nods as he inspects your ticket,
   <q>Enjoy the exhibits!</q><.reveal ticket-shown>"
   name = 'the green ticket'
;
```
