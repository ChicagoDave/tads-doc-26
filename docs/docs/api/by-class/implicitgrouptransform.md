# implicitGroupTransform

*object* — defined in [report.t](../by-file/report.t.md) (line 1435)


Transcript Transform: group implicit announcements. We'll find any runs of consecutive implicit command announcements, and group each run into a single announcement listing all of the implied actions. For example, we'll turn this:


**Superclass chain:** [TranscriptTransform](transcripttransform.md) > `object` > **implicitGroupTransform**


## Methods


### `applyTransform(trans, vec)` *(overridden)*

Defined in report.t, line 1436


### `canGroupWith(a, b)`

Defined in report.t, line 1745

Can we group the second item with the first? Returns true if the second item is also an implicit action announcement, or it's a default object announcement whose parent action is the first item's action.


### `processDefaultAnnouncements(vec)`

Defined in report.t, line 1683

Process default object announcements in a grouped message vector.


### `unstackRecursiveGroup(groupVec, vec, idx)`

Defined in report.t, line 1621

"Unstack" a recursive group of nested announcements. Adds the recursive group to the output group vector in chronological order, and returns the index of the next item after the recursive group.
