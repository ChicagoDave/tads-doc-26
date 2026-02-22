# mainWebGroup

*object* — defined in [webui.t](../by-file/webui.t.md) (line 1313)


The default web resource group. This is the default container for WebResource objects.


**Superclass chain:** [WebResourceGroup](webresourcegroup.md) > `object` > **mainWebGroup**


## Properties


### `priority` *(overridden)*

Defined in webui.t, line 1316


## Inherited Properties


*From [WebResourceGroup](webresourcegroup.md):* [`all`](webresourcegroup.md#all), [`contents`](webresourcegroup.md#contents), [`server`](webresourcegroup.md#server)


## Methods


### `execute`

Defined in webui.t, line 1325

At startup, put each WebResource object into the contents list for its group.


### `isGroupFor(req)` *(overridden)*

Defined in webui.t, line 1315

the default group matches any server, but with low priority


## Inherited Methods


*From [WebResourceGroup](webresourcegroup.md):* [`processRequest`](webresourcegroup.md#processRequest)
