# OneOfIndexGen

*class* — defined in [_main.t](../by-file/_main.t.md) (line 1262)


<<one of>> index generator. The compiler generates an anonymous instance of this class for each <<one of>> list in string, setting the property 'numItems' to the number of items in the list, and 'listAttrs' property to a string giving the sequence type. The compiler generates a call to getNextIndex() within the string to get the next index value, which is an integer from 1 to numItems.


**Superclass chain:** `object` > **OneOfIndexGen**


## Properties


### `idx_`

Defined in _main.t, line 1468

current position in the list


### `listAttrs`

Defined in _main.t, line 1308

List attributes. This is a string with a comma-delimited list of tokens describing the treatment on the list for each fetch. The first call to getNextIndex() takes the first token off the list and generates an appropriate return value, possibly queuing up a list of future values. The next call to getNextIndex() reads from the queue. Once the queue is exhausted, the next call takes the second token off the attribute list and repeats the process. Once the attribute list is down to one token, we don't remove the token, but simply repeat it forever.


### `lst_`

Defined in _main.t, line 1465

generated list


### `numItems`

Defined in _main.t, line 1264

number of list items


## Methods


### `getNextIndex`

Defined in _main.t, line 1315

Get the next index value. Returns an integer from 1 to numItems. The algorithm for choosing the index depends on the list type, as defined by listAttrs.
