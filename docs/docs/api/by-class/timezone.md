# TimeZone

*class* — defined in [date.h](../by-file/date.h.md) (line 508)


TimeZone intrinsic class. A TimeZone object represents a location entry in the IANA zoneinfo database. It contains information on the location's wall clock time settings relative to universal time (UTC), allowing translations between local wall clock time and UTC. The object stores the current clock settings in the location, the current ongoing rules for future switches between standard and daylight time (if applicable in the zone), and a full history of the past changes to the location's time settings, including standard/daylight time changes, redefinitions of the time zone, and changes in the location from one time zone to another. (For example, some US cities that lie near zone borders have switched their time zones at various points in their history.) The historical information for most zones goes back to the original establishment of standard time zones, typically in the late 19th century, and for dates before that, the history usually includes the Local Mean Time settings for the location. The history information allows the accurate reconstruction of the local time representation for virtually any date and time in the past, present, or future.


**Superclass chain:** [Object](object.md) > **TimeZone**


## Methods


### `getHistory(date?)`

Defined in date.h, line 566

Get the history item that applies to a given date, or the entire enumerated history of clock changes in this timezone.


### `getLocation`

Defined in date.h, line 628

Get the zone's location. This returns a list: [country, lat, lon, comment], where 'country' is a string with the country code (a two-letter ISO 3166 code) for the country that contains the zone's main city, 'lat' is a string giving the latitude in the format +ddmm (degrees and minutes) or +ddmmss (and seconds), 'lon' is the longitude as a string in the format +dddmm or +dddmmss, and 'comment' is a string with any comment text from the zoneinfo database.


### `getNames`

Defined in date.h, line 520

Get the name or names for this timezone. This returns a list of strings with the timezone's names, as defined in the IANA zoneinfo database. The zoneinfo database names zones by location, usually using a combination of a continent major city, as in 'America/New_York'. Some zones have multiple aliases as a matter of convenience, such as when there are several major cities in a region that share the same timezone rules. When a zone has aliases, the primary name is listed first, followed by the aliases.


### `getRules`

Defined in date.h, line 616

Get the ongoing rules that are in effect after the last enumerated history item. This returns a list of the rules for future changes to the zone; each rule fires once annually, and encodes the day of year when the rule fires, and the new clock settings in effect after the rule fires. Virtually all zones that use ongoing rules have exactly two: one for the annual change to daylight savings time in the spring, and one for the return to standard time in the fall. Each rule's firing date is specified in an abstract format designed to handle the variety of regional daylight savings schemes: "last Sunday in March", "second Sunday in November", "January 15", etc.


## Inherited Methods


*From [Object](object.md):* [`getPropList`](object.md#getPropList), [`getPropParams`](object.md#getPropParams), [`getSuperclassList`](object.md#getSuperclassList), [`isClass`](object.md#isClass), [`isTransient`](object.md#isTransient), [`ofKind`](object.md#ofKind), [`propDefined`](object.md#propDefined), [`propInherited`](object.md#propInherited), [`propType`](object.md#propType), [`valToSymbol`](object.md#valToSymbol)
