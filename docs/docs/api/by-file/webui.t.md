# webui.t


## Classes

- [ClientEventRequest](../by-class/clienteventrequest.md)
- [ClientSession](../by-class/clientsession.md)
- [DownloadTempFile](../by-class/downloadtempfile.md)
- [WebCommandWin](../by-class/webcommandwin.md)
- [WebLayoutWindow](../by-class/weblayoutwindow.md)
- [WebResource](../by-class/webresource.md)
- [WebResourceGroup](../by-class/webresourcegroup.md)
- [WebResourceInit](../by-class/webresourceinit.md)
- [WebResourceResFile](../by-class/webresourceresfile.md)
- [WebStatusWin](../by-class/webstatuswin.md)
- [WebUIPrefs](../by-class/webuiprefs.md)
- [WebUIProfile](../by-class/webuiprofile.md)
- [WebWindow](../by-class/webwindow.md)


## Global Objects

- [coverArtResource](../by-class/coverartresource.md)
- [eventPage](../by-class/eventpage.md)
- [flushEventsPage](../by-class/flusheventspage.md)
- [guestConnectPage](../by-class/guestconnectpage.md)
- [inputDialogPage](../by-class/inputdialogpage.md)
- [inputEventPage](../by-class/inputeventpage.md)
- [inputFileCancel](../by-class/inputfilecancel.md)
- [inputFilePage](../by-class/inputfilepage.md)
- [inputLinePage](../by-class/inputlinepage.md)
- [mainWebGroup](../by-class/mainwebgroup.md)
- [morePromptDonePage](../by-class/morepromptdonepage.md)
- [setPrefsPage](../by-class/setprefspage.md)
- [setScreenNamePage](../by-class/setscreennamepage.md)
- [tempFileDownloadPage](../by-class/tempfiledownloadpage.md)
- [uiStatePage](../by-class/uistatepage.md)
- [uploadFilePage](../by-class/uploadfilepage.md)
- [webMainWin](../by-class/webmainwin.md)
- [webSession](../by-class/websession.md)
- [webuiResources](../by-class/webuiresources.md)
- generateRandomKey
- processNetRequests


## Functions


### `generateRandomKey`

Defined in webui.t, line 360

Generate a random key. This returns a 128-bit random number as a hex string. This is designed for ephemeral identifiers, such as session keys.


### `processNetRequests(doneFunc, timeout?)`

Defined in webui.t, line 1493

Process network requests. Continues until doneFunc() returns true, or a timeout or error occurs. If we return because doneFunc() returned true, we'll return nil. Otherwise, we'll return the NetEvent that terminated the wait.
