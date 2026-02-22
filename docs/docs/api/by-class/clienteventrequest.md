# ClientEventRequest

*class* — defined in [webui.t](../by-file/webui.t.md) (line 768)


Client event request. Each client session object keeps a queue of pending event requests, representing incoming "GET /webui/getEvent" requests that have yet to be answered.


**Superclass chain:** `object` > **ClientEventRequest**


## Properties


### `req`

Defined in webui.t, line 776

the underlying HTTPRequest object


### `reqTimeout`

Defined in webui.t, line 784

The system time (ms ticks) when the request times out. If we don't have an actual event to send in response by this time, the housekeeper will generate a no-op reply just to let the client know that we're still here.


## Methods


### `construct(req)`

Defined in webui.t, line 769
