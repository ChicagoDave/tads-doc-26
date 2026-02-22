# realTimeManager

*object* — defined in [events.t](../by-file/events.t.md) (line 870)


Real-Time Event Manager. This object manages all of the game's real-time events, which are events that occur according to elapsed real-world time.


**Superclass chain:** [BasicEventManager](basiceventmanager.md) > `object` > [InitObject](initobject.md) > [ModuleExecObject](moduleexecobject.md) > **realTimeManager**


## Properties


### `curEvent_`

Defined in events.t, line 1091

the event currently being executed


### `elapsedTimeAtSave`

Defined in events.t, line 1097

saved elapsed time - we use this to figure the virtual starting time when we restore a saved game


### `events_` *(overridden)*

Defined in events.t, line 1088

our event list


### `startingTime`

Defined in events.t, line 1042

The imaginary real-world time of the starting point of the game, treating the game as having been played from the start in one continous session. Whenever we restore a saved game, we project backwards from the current real-world time at restoration by the amount of continuous elapsed time in the saved game to find the point at which the game would have started if it had been played continuously in one session up to the restored point.


## Inherited Properties


*From [ModuleExecObject](moduleexecobject.md):* [`execAfterMe`](moduleexecobject.md#execAfterMe), [`execBeforeMe`](moduleexecobject.md#execBeforeMe), [`hasInitialized_`](moduleexecobject.md#hasInitialized_), [`isDoingExec_`](moduleexecobject.md#isDoingExec_), [`isExecuted_`](moduleexecobject.md#isExecuted_)


## Methods


### `execute` *(overridden)*

Defined in events.t, line 1050

Initialize at run-time startup. We want to set the zero point as the time when the player actually started playing the game (any time we spent in pre-initialization doesn't count on the real-time clock, since it's not part of the game per se).


### `execute` *(overridden)*

Defined in events.t, line 1108

Real-time manager: pre-save notification receiver. When we're about to save the game, we'll note the current elapsed game time, so that when we later restore the game, we can figure the virtual starting point that will give us the same effective elapsed time on the system real-time clock.


### `execute` *(overridden)*

Defined in events.t, line 1125

Real-time manager: post-restore notification receiver. Immediately after we restore a game, we'll tell the real-time manager to refigure the virtual starting point of the game based on the saved elapsed time.


### `executeEvents`

Defined in events.t, line 927

Run any real-time events that are ready to execute, then return the next event time. The return value has the same meaning as that of getNextEventTime().


### `getElapsedTime`

Defined in events.t, line 1000

Get the current game elapsed time. This is the number of milliseconds that has elapsed since the game was started, counting only the continuous execution time. When the game is saved, we save the elapsed time at that point; when the game is later restored, we project that saved time backwards from the current real-world time at restoration to get the real-world time where the game would have started if it had actually been played continuously in one session.


### `getNextEventTime`

Defined in events.t, line 889

Get the elapsed game time at which the next real-time event is scheduled. This returns a value which can be compared to that returned by getElapsedTime(): if this value is less than or equal to the value from getElapsedTime(), then the next event is reay for immediate execution; otherwise, the result of subtracting getElapsedTime() from our return value gives the number of milliseconds until the next event is schedulable.


### `restoreElapsedTime`

Defined in events.t, line 1077

Restore the elapsed time - this is called just after we restore a game. We'll project the saved elapsed time backwards to figure the imaginary starting time the game would have had if it had been played in one continuous session rather than being saved and restored.


### `saveElapsedTime`

Defined in events.t, line 1064

save the elapsed time so far - this is called just before we save a game so that we can pick up where we left off on the elapsed time clock when we restore the saved game


### `setElapsedTime(t)`

Defined in events.t, line 1016

Set the current game elapsed time. This can be used to freeze the real-time clock - a caller can note the elapsed game time at one point by calling getElapsedTime(), and then pass the same value to this routine to ensure that no real time can effectively pass between the two calls.


## Inherited Methods


*From [BasicEventManager](basiceventmanager.md):* [`addEvent`](basiceventmanager.md#addEvent), [`removeCurrentEvent`](basiceventmanager.md#removeCurrentEvent), [`removeEvent`](basiceventmanager.md#removeEvent), [`removeMatchingEvents`](basiceventmanager.md#removeMatchingEvents)


*From [ModuleExecObject](moduleexecobject.md):* [`_execute`](moduleexecobject.md#_execute), [`classExec`](moduleexecobject.md#classExec)
