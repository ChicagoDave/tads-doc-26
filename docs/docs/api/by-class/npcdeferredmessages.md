# npcDeferredMessages

*object* — defined in [msg_neu.t](../by-file/msg_neu.t.md) (line 2242)


Deferred NPC messages. We use this to report deferred messages from an NPC to the player. A message is deferred when a parsing error occurs, but the NPC can't talk to the player because there's no sense path to the player. When this happens, the NPC queues the message for eventual delivery; when a sense path appears later that lets the NPC talk to the player, we deliver the message through this object. Since these messages describe conditions that occurred in the past, we use the past tense to phrase the messages.


**Superclass chain:** `object` > **npcDeferredMessages**
