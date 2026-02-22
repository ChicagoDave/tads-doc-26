# DownloadTempFile

*class* — defined in [webui.t](../by-file/webui.t.md) (line 3369)


Downloadable temporary file descriptor. We create this object when the program calls inputFile() to ask for a writable file. This lets the caller create and write a temporary file on the server side; when the caller is done with the file, we'll offer the file for download to the client through the UI.


**Superclass chain:** `object` > **DownloadTempFile**


## Properties


### `isReady`

Defined in webui.t, line 3415

is the file ready for download?


### `isWebTempFile`

Defined in webui.t, line 3418

this is a web temp file


### `mimeType`

Defined in webui.t, line 3409

MIME type


### `resName`

Defined in webui.t, line 3405

root resource name, and full resource path


### `resPath`

Defined in webui.t, line 3406


### `tempFileName`

Defined in webui.t, line 3402

TemporaryFile object for the local temp file


### `timeCreated`

Defined in webui.t, line 3412

creation timestamp, as a system tick count value


## Methods


### `closeFile`

Defined in webui.t, line 3392


### `construct(res, mimeType)`

Defined in webui.t, line 3370


### `getFilename`

Defined in webui.t, line 3391

File spec interface. This allows the DownloadTempFile to be used as though it were a filename string.
