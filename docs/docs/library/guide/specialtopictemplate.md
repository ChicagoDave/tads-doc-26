# SpecialTopic Template

A [SpecialTopic](specialtopic.md) takes a keyword list or a regular expression instead of  the regular match criteria. It also takes a suggestion name string and the normal response text. There's no need for a score in a special topic, since these are unique.

```tads3
SpecialTopic template
   'name'
   [keywordList] | 'matchPat'
   "topicResponse" | [eventList] ?;
```

A ShuffledEventList version of the above:

```tads3
SpecialTopic template
   'name'
   [keywordList] | 'matchPat'
   [firstEvents]
   [eventList];
```
