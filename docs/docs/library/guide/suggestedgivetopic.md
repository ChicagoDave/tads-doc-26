# SuggestedGiveTopic

SuggestedGiveTopic : [SuggestedTopic](suggestedtopic.md)

A SuggestedAskTopic is the particular type of [SuggestedTopic](suggestedtopic.md) that suggests to the player that s/he could Give such-and-such to so-and-so.

For example, if we want to suggest to the player that he might give the carbuncle to the curator, we could add the following to the appropriate GiveTopic (previously defined):

```tads3
++ GiveTopic, SuggestedGiveTopic @carbuncle
  topicResponse
  {
   "{The curator/he} takes the carbuncle and examines it carefully, then declares,
   <q>Wunderbar! Ausgezeichnet! This is the famous purple carbuncle of King Solomon,
   nicht wahr? And you are giving it to the museum? How kind, how very kind!</q>
   Pausing just to wipe the tears of excitement and gratitude out of his eyes, he
   continues, <q>I shall enroll you on our roll of honoured benefactors <i>at once</i>!
   Please, please, do feel free to inspect the special treasures in our benefactors'
   exhibition room any time you please!</q>";
   carbuncle.moveInto(getActor);
  }
  name = 'the carbuncle'
;
```
