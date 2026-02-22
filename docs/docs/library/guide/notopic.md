# NoTopic

NoTopic : [MiscTopic](misctopic.md)

A NoTopic responds to a NO command directed toward the currently conversing NPC. Like a YesTopic it is most useful inside a [ConvNode](convnode.md).

As an example, add the following immediately after the [YesTopic](yestopic.md) we've just defined:

```tads3
++ NoTopic, SuggestedNoTopic
  "<q>No, on second thoughts I think we'd better leave it for now.</q>
   you reply.\b
   <q>Very well.</q> she sighs. "
;
```
