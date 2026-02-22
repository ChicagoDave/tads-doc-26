# Date

*class* — defined in [date.h](../by-file/date.h.md) (line 134)


The Date intrinsic class stores a date-and-time value representing a particular point in time, and provides methods and operators for date arithmetic, formatting, and parsing.


**Superclass chain:** [Object](object.md) > **Date**


## Methods


### `addInterval(interval)`

Defined in date.h, line 280

Add an interval to this date, returning a new date object. The interval is given as a list of integers: [years, months, days, hours, minutes, seconds]. The 'seconds' value can be a BigNumber with a fractional part (but anything smaller than milliseconds is discarded). Elements can be omitted from the end of the list; for example, [0, 2] adds two months. An element can be negative: [-1] subtracts one year.


### `compareTo(date)`

Defined in date.h, line 204

Compare to another Date object; returns an integer less than zero if this Date is before the other Date, zero if they refer to the same date, greater than zero if this Date is after the other Date. The same comparisons can be done with the ordinary comparison operators (<, >, <=, >=, ==, !=), but this is convenient for sorting callbacks since it lets you get the greater/equal/less result in one shot.


### `findWeekday(weekday, which, tz?)`

Defined in date.h, line 292

Find a given day of the week relative to this date, in its local time zone. 'weekday' is the target weekday to find, as an integer: 1 for Sunday, 2 for Monday, ..., 7 for Saturday. 'which' is an integer specifying which relative day to find: 1 means to find the next occurrence of the given weekday on or after this date, 2 means the second occurrence on or after this date, and so on. -1 means the first occurrence on or before this date; -2 is the second occurrence on or before this date; etc.


### `formatDate(format, tz?)`

Defined in date.h, line 188

Format the date/time value as a Gregorian calendar date, using the given format template string. Returns a string with the formatted date/time. The date/time is displayed in the given time zone (or the system's local time zone if 'tz' isn't specified).


### `formatJulianDate(format, tz?)`

Defined in date.h, line 194

Format the date/time value as a Julian calendar date, using the given format template string.


### `getClockTime(tz?)`

Defined in date.h, line 269

Get the wall clock time represented by this Date object, in terms of local time in the given time zone (or the system's local time zone is 'tz' isn't specified). Returns a list of integers: [hour, minute, second, ms]. The hour is on a 24-hour clock, with 0 hours representing midnight and 23 representing 11 PM. The 'ms' value is a value from 0 to 999 giving the milliseconds portion of the time.


### `getDate(tz?)`

Defined in date.h, line 214

Get the Gregorian calendar date represented by this Date object, in terms of local time in the given time zone (or the system's local time zone if 'tz' isn't specified). Returns a list consisting of [year, month, day, weekday], each value represented as an integer. The weekday is 1 for Sunday, 2 for Monday, etc. For example, June 21, 2012 (a Thursday) is represented as [2012,6,21,5].


### `getISOWeekDate(tz?)`

Defined in date.h, line 259

Get the ISO 8601 week date. This returns a list with three elements, [year, week, day], where 'year' is the ISO year number containing the date, 'week' is the week number (1 to 53), and 'day' is the day of the week (1-7, Monday to Sunday, per the ISO 8601 conventions). The year on the ISO week calendar can differ from the year on the Gregorian calendar for dates during the first and last week of a year on Gregorian calendar, because year boundaries on the ISO calendar always occur on week boundaries. For example, Jan 1, 2005 has the ISO week date 2004-W53-6 - it's part of 2004 on the ISO week calendar because weeks can't be split across years, so the entire week belongs to 2004 on the ISO calendar. This can work in both directions: Dec 31, 2007 has the ISO week date 2008-W01-1.


### `getJulianDate(tz?)`

Defined in date.h, line 243

Get the Julian calendar date for this Date object, in terms of the local time in the given time zone (or the system's local time zone if 'tz' isn't specified). Returns a list consisting of [year, month, day, weekday]. (The weekday on the Julian calendar is always the same as the weekday on the Gregorian calendar for a given Date value.)


### `getJulianDay`

Defined in date.h, line 233

Get the Julian day number. This is the number of days since January 1, 4713 BCE on the (proleptic) Julian calendar, at noon UTC. This is an important figure in astronomy. It's also often useful as a common currency for converting between arbitrary calendars: you might not be able to find a published formula for converting between calendar X and calendar Y, but you can almost always find a formula for converting between any given calendar and the Julian day system.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
