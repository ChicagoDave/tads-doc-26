# DefaultConsultTopic

DefaultConsultTopic : [DefaultTopic](defaulttopics-overview.md)

If the player tries to consult our History Book about something for which we've defined no response, we need an appropriate message to be displayed. We use a DefaultConsultTopic for this purpose (just as we use other [DefaultTopic](defaulttopics-overview.md) types in conversation).

An appropriate DefaultConsultTopic is not hard to define. Since a book is an inanimate object, we don't need to vary its behaviour, and something simple like the following should suffice:

```tads3
+ DefaultConsultTopic
  "The book doesn't seem to have anything useful to say on that subject. "
;
```

If you wanted to make this a bit more sophisticated by suggesting to the player the topics that are available to be listed in the book, you could add a name property to each ConsultTopic you want suggested (e.g. name = 'Benedict' or name='the museum') and then expand the DefaultConsultTopic thus:

```tads3
+ DefaultConsultTopic
  "The book doesn't seem to have anything useful to say on that subject,
   but a quick look in the index suggests that you could consult it
   about <<suggestionList>>. "
   suggestionList()
   {
     local lst = [];
     foreach(local cur in location.consultTopics)
      if(cur.name != nil)
        lst += cur.name;
     stringLister.showSimpleList(lst);
   }
;
```

There are both advantages and disadvantages to this approach. On the one hand the player is not left to guess which topics the book implements; on the other, the message is a bit directive and may make consulting the book feel like working through the list of topics suggested.

A less directive approach, which may provide the best compromise, could be to provide the book with an index topic and drop a broad hint in the DefaultConsultTopic that there is an index to be consulted:

```tads3
+ ConsultTopic @tIndex
  "A quick look in the index suggests that you could consult it
   about <<suggestionList>>. "
  suggestionList()
   {
     local lst = [];
     foreach(local cur in location.consultTopics)
      if(cur.name != nil)
        lst += cur.name;
     stringLister.showSimpleList(lst);
   }
;
+ DefaultConsultTopic
  "So far as you can tell from the index, the book doesn't seem to
   have anything useful to say on that subject. "
;
tIndex : Topic 'index/contents';
```

If you had several books in your game that you wanted to provide with an index you could avoid repetitive coding by defining an IndexTopic class:

```tads3
class IndexTopic : ConsultTopic
  suggestionList()
   {
     local lst = [];
     foreach(local cur in location.consultTopics)
      if(cur.name != nil)
        lst += cur.name;
     stringLister.showSimpleList(lst);
   }
;
```

Note that the IndexTopic only responds to commands like LOOK UP INDEX IN BOOK. If you want it to respond to commands like X INDEX, LOOK INDEX and CONSULT INDEX you'll need to add a physical index object to the book to handle such commands, for example:

```tads3
+ Component 'index' 'index'
    dobjFor(Examine) remapTo(ConsultAbout, location, tIndex)
    dobjFor(LookIn) remapTo(ConsultAbout, location, tIndex)
    dobjFor(Consult) remapTo(ConsultAbout, location, tIndex)
;
```
