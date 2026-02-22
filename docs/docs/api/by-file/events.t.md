# events.t


## Classes

- [BasicEvent](../by-class/basicevent.md)
- [BasicEventManager](../by-class/basiceventmanager.md)
- [Daemon](../by-class/daemon.md)
- [Event](../by-class/event.md)
- [EventAction](../by-class/eventaction.md)
- [Fuse](../by-class/fuse.md)
- [OneTimePromptDaemon](../by-class/onetimepromptdaemon.md)
- [PromptDaemon](../by-class/promptdaemon.md)
- [RealTimeDaemon](../by-class/realtimedaemon.md)
- [RealTimeEvent](../by-class/realtimeevent.md)
- [RealTimeFuse](../by-class/realtimefuse.md)
- [RealTimeSenseDaemon](../by-class/realtimesensedaemon.md)
- [RealTimeSenseFuse](../by-class/realtimesensefuse.md)
- [Schedulable](../by-class/schedulable.md)
- [SenseDaemon](../by-class/sensedaemon.md)
- [SenseFuse](../by-class/sensefuse.md)


## Global Objects

- [eventManager](../by-class/eventmanager.md)
- [realTimeManager](../by-class/realtimemanager.md)
- runScheduler


## Functions


### `runScheduler`

Defined in events.t, line 26

Run the main scheduling loop. This continues until we encounter an end-of-file error reading from the console, or a QuitException is thrown to terminate the game.
