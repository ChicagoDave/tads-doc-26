# TopicEntry Template

A TopicEntry can be defined with an optional score, followed by the match criteria (which can be either a single matching object, a list of  matching objects, or a regular expression pattern string), followed by the optional response text (which can be given either as a double-quoted string or as a list of single-quoted strings to use as an EventList).

```tads3
TopicEntry template
    +matchScore?
    @matchObj | [matchObj] | 'matchPattern'
    "topicResponse" | [eventList] ?;
```

A ShuffledEventList version of the above:

```tads3
TopicEntry template
    +matchScore?
    @matchObj | [matchObj] | 'matchPattern'
    [firstEvents] [eventList];
```

We can also include *both* the match object/list *and* pattern:

```tads3
TopicEntry template
   +matchScore?
    @matchObj | [matchObj]
    'matchPattern'
   "topicResponse" | [eventList] ?;
```

A ShuffledEventList version of the above

```tads3
TopicEntry template
    +matchScore?
    @matchObj | [matchObj] 'matchPattern'
    [firstEvents] [eventList];
```
