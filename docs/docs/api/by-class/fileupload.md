# FileUpload

*class* — defined in [tadsnet.t](../by-file/tadsnet.t.md) (line 292)


A FileUpload represents a file uploaded by a network client via a protocol server, such as an HTTPServer.


**Superclass chain:** `object` > **FileUpload**


## Properties


### `contentType`

Defined in tadsnet.t, line 335

The content type. This a string giving the MIME type specified by the client with the upload. This is the full content-type string, including any attributes, such "charset" for a text type. This can be nil if the client doesn't specify a content-type at all.


### `file`

Defined in tadsnet.t, line 318

The file data.


### `filename`

Defined in tadsnet.t, line 352

The client-side filename, if specified. This is a string giving the name of the file on the client machine. This generally has no particular meaning to the server, since we can't infer anything about the directory structure or naming conventions on an arbitrary client. However, this might be useful for reference, such as showing information about the upload in a user interface. It's sometimes also marginally useful to know the suffix (extension) for making further guesses about the content type - although as with the content-type, you can't rely upon this, but can only use it as a suggestion from the client.


## Methods


### `construct(file, contentType, filename)`

Defined in tadsnet.t, line 293
