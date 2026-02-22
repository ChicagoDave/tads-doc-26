# ByeTopic

ByeTopic : [MiscTopic](misctopic.md)

A ByeTopic is usually used in connection with [greeting protocols](greetingprotocols.md), to handle the end of a conversation. As such, it is normally located in the [ConversationReadyState](conversationreadystate.md) to which the actor returns at the conclusion of the conversation.  The ByeTopic handles explicit termination of a conversation (via a BYE command).

In the case of King Solomon, we shall assume that our player character would not be so gauche as to walk out on the king without some attempt at formal leave-taking, so we really want a ByeTopic that handles both implicit and explicit conversation termination.  As with the HelloTopic and the ImpHelloTopic this should go in the solomonExamining ConversationReadyState:

```tads3
+++ ByeTopic, ShuffledEventList
  [
    '<q>Goodbye, your majesty.</q> you say, with a little bow, just to be
      on the safe side.\b
     <q>Farewell, mysterious messenger,</q> the king replies, <q>perhaps
      we shall meet again.</q> ',
     '<q>Well, er, cheerio then, sire.</q> you say.\b
      Solomon cocks one eyebrow, <q>Cheerio? Is that how angels speak?
       Fare thee well.</q>',
     '<q>Goodbye, sir.</q> you bid him farewell.\b
      <q>God be with you too.</q> the king replies formally, before returning
       to his contemplations. '
  ]
;
```

Note the symmetry here between HelloTopic and ByeTopic: while HelloTopic handles both implicit and explicit conversation initiation, ByeTopic handles both explicit and implicit conversation termination.
