# tadsgen.h


## Classes

- abs
- concat
- dataType
- firstObj
- getArg
- getFuncParams
- getTime
- makeList
- makeString
- max
- min
- nextObj
- rand
- randomize
- restartGame
- restoreGame
- rexGroup
- rexMatch
- rexReplace
- rexSearch
- rexSearchLast
- saveGame
- savepoint
- sgn
- sprintf
- toInteger
- toNumber
- toString
- undo


## Functions


### `abs(num)`

Defined in tadsgen.h, line 616

Get the absolute value of a number. The argument can be an integer or a BigNumber; the return value is the absolute value of the argument, and has the same type as the argument. (The absolute value of a positive number X (or zero) is X; the absolute value of a negative number X is -X.)


### `concat(...)`

Defined in tadsgen.h, line 640

Concatenate the arguments together into a single string. The arguments can be strings or any types that can be automatically converted to string for the regular "+" operator; non-strings are first converted to strings using the same rules that "+" uses when combining a string with a non-string. If there are no arguments, the result is an empty string.


### `dataType(val)`

Defined in tadsgen.h, line 24

Get the type of the given value. This returns a TypeXxx value.


### `firstObj(cls?, flags?)`

Defined in tadsgen.h, line 48

Get the first object in memory. If 'cls' is provided, we return the first object of the given class; otherwise we return the first object of any kind. 'flags' is an optional bitwise combination of ObjXxx values, specifying whether classes, instances, or both are desired. If this isn't specified, ObjAll is assumed. This is used in conjunction with nextObj() to iterate over all objects in memory, or all objects of a given class.


### `getArg(idx)`

Defined in tadsgen.h, line 30

Get the given parameter to the current function. 'idx' is 1 for the first argument in left-to-right order, 2 for the second, and so on.


### `getFuncParams(func)`

Defined in tadsgen.h, line 542

Get a description of the parameters to the given function. 'func' is a function pointer. This function returns a list: [minArgs, optionalArgs, isVarargs], where minArgs is the minimum number of arguments required by the function, optionalArgs is the additional number of arguments that can be optionally provided to the function, and isVarargs is true if the function takes any number of additional ("varying") arguments, nil if not.


### `getTime(timeType?)`

Defined in tadsgen.h, line 318

Get the current local time.


### `makeList(val, repeatCount?)`

Defined in tadsgen.h, line 607

Create a list by repeating the given value the given number of times. If the repeat count isn't specified, the default is 1; a repeat count less than zero throws an error. 'val' can be any value; it's simply repeated in each element of the list.


### `makeString(val, repeatCount?)`

Defined in tadsgen.h, line 531

Create a string by repeating the given value the given number of times. If the repeat count isn't specified, the default is 1; a repeat count less than zero throws an error. 'val' can be a string, in which case the string is simply repeated the given number of times; an integer, in which case the given Unicode character is repeated; or a list of integers, in which case the given Unicode characters are repeated, in the order of the list. The list format can be used to create a string from a list of Unicode characters that you've been manipulating as a character array, which is sometimes a more convenient or efficient way to do certain types of string handling than using the actual string type.


### `max(val1, ...)`

Defined in tadsgen.h, line 507

Get the maximum of the given arguments. The values must be comparable with the ordinary "<" and ">" operators. Note that because this is an ordinary function call, all of the arguments are evaluated (which means any side effects of these evaluations will be triggered).


### `min(val1, ...)`

Defined in tadsgen.h, line 516

Get the minimum of the given arguments. The values must be comparable with the ordinary "<" and ">" operators. Note that because this is an ordinary function call, all of the arguments are evaluated (which means any side effects of these evaluations will be triggered).


### `nextObj(obj, cls?, flags?)`

Defined in tadsgen.h, line 56

Get the next object in memory after the given object, optionally of the given class and optionally limiting to instances, classes, or both. This is used to continue an iteration started with firstObj().


### `rand(...)`

Defined in tadsgen.h, line 219

Select a random number or a random value. This uses the current random number algorithm as selected via randomize().


### `randomize(...)`

Defined in tadsgen.h, line 183

Random number generator (RNG) initialization. This selects and initializes the random number generator algorithm used by rand(). TADS provides several different RNG algorithms; each RNG has different properties, so some applications might have reasons to prefer a particular algorithm. For general purposes, any of them should produce good results.


### `restartGame`

Defined in tadsgen.h, line 498

Restart the program from the beginning. This resets all persistent objects to their initial state, as they were when the program was first started.


### `restoreGame(filename)`

Defined in tadsgen.h, line 491

Restore a previously saved state file. This loads the states of all persistent objects stored in the given file. The file must have been saved by the current version of the current running program; if not, an exception is thrown.


### `rexGroup(groupNum)`

Defined in tadsgen.h, line 364

Get the given regular expression group. This can be called after a successful rexMatch() or rexSearch() call to retrieve information on the substring that matched the given "group" within the regular expression. A group is a parenthesized sub-pattern within the regular expression; groups are numbered left to right by the open parenthesis, starting at group 1. If there is no such group in the last regular expression searched or matched, or the group wasn't part of the match (for example, because it was part of an alternation that wasn't matched), the return value is nil. If the group is valid and was part of the match, the return value is a list: [index, length, string], where index is the character index within the matched or searched string of the start of the group match, length is the character length of the group match, and string is the text of the group match.


### `rexMatch(pat, str, index?)`

Defined in tadsgen.h, line 332

Match a string to a regular expression pattern. 'pat' can be either a string giving the regular expression, or can be a RexPattern object. 'str' is the string to match, and 'index' is the starting character index (the first character is at index 1) at which to start matching. Returns the length in characters of the match, or nil if the string doesn't match the pattern. (Note that a return value of zero doesn't indicate failure - rather, it indicates a successful match of the pattern to zero characters. This is possible for a pattern with a zero-or-more closure, such as 'x*' or 'x?'.)


### `rexReplace(pat, str, replacement, flags?, index?, limit?)`

Defined in tadsgen.h, line 444

Search for the given regular expression pattern (which can be given as a regular expression string or as a RexPattern object) within the given string, and replace one or more occurrences of the pattern with the given replacement text.


### `rexSearch(pat, str, index?)`

Defined in tadsgen.h, line 346

Search the given string for the given regular expression pattern. 'pat' is a string giving the regular expression to find, or a RexPattern object. 'str' is the string to search, and 'index' is the optional starting index (the first character is at index 1; negative indices are from the end of the string, so -1 is the last character, -2 is the second to last, and so on). If a match to the pattern isn't found, returns nil. If a match is found, the return value is a list: [index, length, string], where index is the starting character index of the match, length is the length in characters of the match, and string is the text of the match.


### `rexSearchLast(pat, str, index?)`

Defined in tadsgen.h, line 680

Search backwards in the given string for the given regular expression pattern. 'pat' is a string giving the regular expression to find, or a RexPattern object. 'str' is the string to search, and 'index' is the optional starting index (the first character is at index 1; negative indices are from the end of the string, so -1 is the last character, -2 is the second to last, and so on; 0 means the position just after the last character of the string). If 'index' is omitted, the default is to search the entire string from the end, which is equivalent to passing 0 or str.length()+1 for 'index'.


### `saveGame(filename, metatab?)`

Defined in tadsgen.h, line 483

Save the current system state into the given file. This uses the VM's internal state-save mechanism to store the current state of all persistent objects in the given file. Any existing file is overwritten.


### `savepoint`

Defined in tadsgen.h, line 450

Create an UNDO savepoint. This adds a marker to the VM's internal UNDO log, establishing a point in time for a future UNDO operation.


### `sgn(num)`

Defined in tadsgen.h, line 623

Get the sign of a number. The argument can be an integer or a BigNumber. The return value is an integer: 1 if the argument is positive, 0 if the argument is zero, -1 if the argument is negative.


### `sprintf(format, ...)`

Defined in tadsgen.h, line 599

Format values into a string. This is similar to the traditional C language "printf" family of functions: it takes a "format string" containing a mix of plain text and substitution parameters, and a set of values to plug in to the substitution parameters, and returns a new string containing the formatted result.


### `toInteger(val, radix?)`

Defined in tadsgen.h, line 285

Convert the given value to an integer.


### `toNumber(val, radix?)`

Defined in tadsgen.h, line 571

Convert the given value to a number. This is similar to toInteger(), but can parse strings containing floating point numbers and whole numbers too large for ordinary integers.


### `toString(val, radix?, isSigned?)`

Defined in tadsgen.h, line 259

Convert the given value to a string representation. 'val' can be an integer, in which case it's converted to a string representation in the numeric base given by 'radix' (which can be any value from 2 to 36), or base 10 (decimal) if 'radix' is omitted; nil or true, in which case the string 'nil' or 'true' is returned; a string, which is returned unchanged; or a BigNumber, in which case the number is converted to a string representation in the given radix; a list or vector, in which case the individual elements are converted recursively, then the results concatenated together into a string with commas separating elements; or any of the built-in object types with default string conversions (ByteArray, StringBuffer, FileName, Date, TimeZone, FileName, etc).


### `undo`

Defined in tadsgen.h, line 465

UNDO to the most recent savepoint. This uses the VM's internal UNDO log to undo all changes to persistent objects, up to the most recent savepoint. Returns true if the operation succeeded, nil if not. A nil return means that there's no further UNDO information recorded, which could be because the program has already undone everything back to the start of the session, or because the UNDO log was truncated due to memory size such that no savepoints are recorded. (The system automatically limits the UNDO log's total memory consumption, according to local system parameters. This function requires at least one savepoint to be present, because otherwise it could create an inconsistent state.)
