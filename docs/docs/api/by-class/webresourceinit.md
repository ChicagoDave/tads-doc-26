# WebResourceInit

*class* — defined in [webui.t](../by-file/webui.t.md) (line 1145)


Session initializer resource. This is a mix-in class designed to be used for a special resource that initializes the session. Mix this with a WebResource class to set up the initializer. When you connect to the client via connectWebUI(), point the client to this resource.


**Superclass chain:** `object` > **WebResourceInitGlobal objects:** [webMainWin](webmainwin.md)


## Properties


### `server`

Defined in webui.t, line 1219

the HTPTServer for communicating with the client


## Methods


### `connectUI(srv)`

Defined in webui.t, line 1152

Connect to the client. The program should call this after creating its HTTPServer object, which you pass here as 'srv'. This establishes the client UI connection, generating the path to the start page.


### `processRequest(req, query)`

Defined in webui.t, line 1165

Process the request. This sets up the program and client session keys as cookies.
