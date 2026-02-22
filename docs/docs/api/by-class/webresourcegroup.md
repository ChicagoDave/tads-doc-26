# WebResourceGroup

*class* — defined in [webui.t](../by-file/webui.t.md) (line 1228)


A WebResourceGroup is a container for WebResource objects. When a server receives a request, it looks in its group list to find the resource object that will handle the request.


**Superclass chain:** `object` > **WebResourceGroupGlobal objects:** [mainWebGroup](mainwebgroup.md)


## Properties


### `all`

Defined in webui.t, line 1305

class property: list of all WebResourceGroup objects


### `contents`

Defined in webui.t, line 1267

the WebResource objects in the group


### `priority`

Defined in webui.t, line 1254

The priority of the group, relative to other groups. If the same server matches multiple groups, this allows you to designate which group has precedence. A higher value means higher priority.


### `server`

Defined in webui.t, line 1264

The HTTPServer object or objects this group is associated with. The general event processor uses this to route a request to the appropriate resource group, by finding the group that's associated with the server that received the request.


## Methods


### `isGroupFor(req)`

Defined in webui.t, line 1234

Should this group handle the given request? By default, we say yes if the server that received the request is associated with this group via the group's 'server' property.


### `processRequest(req)`

Defined in webui.t, line 1274

Process a request. This looks for the highest priority matching resource in the group, then hands the request to that resource for processing.
