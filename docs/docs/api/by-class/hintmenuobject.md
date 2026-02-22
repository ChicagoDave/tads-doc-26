# HintMenuObject

*class* — defined in [hintsys.t](../by-file/hintsys.t.md) (line 31)


A basic hint menu object. This is an abstract base class that encapsulates some behavior common to different hint menu classes.


**Superclass chain:** `object` > **HintMenuObjectSubclasses:** [Goal](goal.md), [HintLongTopicItem](hintlongtopicitem.md), [HintMenu](hintmenu.md), [TopHintMenu](tophintmenu.md)


## Properties


### `topicOrder`

Defined in hintsys.t, line 41

The topic order. When we're about to show a list of open topics, we'll sort the list in ascending order of this property, then in ascending order of title. By default, we set this order value to 1000; if individual goals don't override this, then they'll simply be sorted lexically by topic name. This can be used if there's some basis other than alphabetical order for sorting the list.


## Methods


### `compareForTopicSort(other)`

Defined in hintsys.t, line 52

Compare this goal to another, for the purposes of sorting a list of topics. Returns a positive number if this goal sorts after the other one, a negative number if this goal sorts before the other one, 0 if the relative order is arbitrary.
