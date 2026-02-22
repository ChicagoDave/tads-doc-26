# List

*class* — defined in [systype.h](../by-file/systype.h.md) (line 394)


The native list type


**Superclass chain:** [Collection](collection.md) > [Object](object.md) > **List**


## Methods


### `append(val)`

Defined in systype.h, line 499

append an element - this works almost exactly like the concatation operator ('+'), but if the argument is a list, this simply adds the list as a new element, rather than adding each element of the list as a separate element


### `appendUnique(lst)`

Defined in systype.h, line 491

append the elements of the list 'lst' to the elements of this list, then remove repeated elements in the result; returns a new list with the unique elements of the combination of the two lists


### `car`

Defined in systype.h, line 430

car/cdr - head/tail of list


### `cdr`

Defined in systype.h, line 431


### `countOf(val)`

Defined in systype.h, line 478

count the number of elements with the given value


### `countWhich(cond)`

Defined in systype.h, line 481

count the number of elements for which the callback returns true


### `forEach(func)`

Defined in systype.h, line 448

Invoke the callback func(val) on each element, in order from first to last. No return value.


### `forEachAssoc(func)`

Defined in systype.h, line 557

Invoke the callback func(index, val) on each element, in order from first to last. No return value.


### `getUnique`

Defined in systype.h, line 484

get a new list consisting of the unique elements of this list


### `indexOf(val)`

Defined in systype.h, line 427

get the index of the first match for the given value


### `indexWhich(cond)`

Defined in systype.h, line 442

Find the first element for which the given condition is true, and return the index of the element. Applies the callback function (which encodes the condition to evaluate) to each element in turn, starting with the first. For each element, if the callback returns nil, proceeds to the next element; otherwise, stops and returns the index of the element. If the callback never returns true for any element, we'll return nil.


### `insertAt(startingIndex, val, ...)`

Defined in systype.h, line 535

Insert one or more elements at the given index. If the index is 1, the elements will be inserted before the first existing element. If the index is one higher than the number of elements, the elements will be inserted after all existing elements.


### `intersect(other)`

Defined in systype.h, line 424

intersect with another list


### `lastIndexOf(val)`

Defined in systype.h, line 458

find the last element with the given value, and return its index


### `lastIndexWhich(cond)`

Defined in systype.h, line 469

Find the last element for which the condition is true, and return the index of the element. Applies the callback to each element in turn, starting with the last element and working backwards. For each element, if the callback returns nil, proceeds to the previous element; otherwise, stops and returns the index of the element. If the callback never returns true for any element, we'll return nil.


### `lastValWhich(cond)`

Defined in systype.h, line 475

Find the last element for which the condition is true, and return the value of the element


### `length`

Defined in systype.h, line 418

get the number of elements in the list


### `mapAll(func)`

Defined in systype.h, line 415

Apply the callback function to each element of this list, and return a new list consisting of the results. Effectively maps the list to a new list using the given function. Suppose the original list is


### `prepend(val)`

Defined in systype.h, line 522

Prepend an element - this inserts the value before the first existing element.


### `removeElementAt(index)`

Defined in systype.h, line 542

Delete the element at the given index, reducing the length of the list by one element. Returns a new list with the given element removed.


### `removeRange(startingIndex, endingIndex)`

Defined in systype.h, line 551

Delete the range of elements starting at startingIndex and ending at endingIndex. The elements at the ends of the range are included in the deletion. If startingIndex == endingIndex, only one element is removed. Returns a new list with the given element range removed.


### `sort(descending, ?, comparisonFunction, ?)`

Defined in systype.h, line 516

Sort the list, returning a new list. If the 'descending' flag is provided and is not nil, we'll sort the list in descending order rather than ascending order.


### `sublist(start, len, ?)`

Defined in systype.h, line 421

extract a sublist


### `subset(func)`

Defined in systype.h, line 401

Select a subset of the list: returns a new list consisting only of the elements for which the callback function 'func' returns true.


### `valToSymbol` *(overridden)*

Defined in reflect.t, line 323


### `valWhich(cond)`

Defined in systype.h, line 455

Find the first element for which the given condition is true, and return the value of the element. Returns nil if no item satisfies the condition.


## Inherited Methods


*From [Collection](collection.md):* [`createIterator`](collection.md#createIterator), [`createLiveIterator`](collection.md#createLiveIterator)


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType)
