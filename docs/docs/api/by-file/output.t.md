# output.t


## Classes

- [CaptureFilter](../by-class/capturefilter.md)
- [HtmlStyleTag](../by-class/htmlstyletag.md)
- [LogConsole](../by-class/logconsole.md)
- [MessageBuilder](../by-class/messagebuilder.md)
- [MonitorFilter](../by-class/monitorfilter.md)
- [OutputFilter](../by-class/outputfilter.md)
- [OutputStream](../by-class/outputstream.md)
- [OutputStreamWindow](../by-class/outputstreamwindow.md)
- [ParagraphManager](../by-class/paragraphmanager.md)
- [StringCaptureFilter](../by-class/stringcapturefilter.md)
- [StyleTag](../by-class/styletag.md)
- [SwitchableCaptureFilter](../by-class/switchablecapturefilter.md)


## Global Objects

- [announceObjStyleTag](../by-class/announceobjstyletag.md)
- [assumeStyleTag](../by-class/assumestyletag.md)
- [commandSequencer](../by-class/commandsequencer.md)
- [hyperlinkStyleTag](../by-class/hyperlinkstyletag.md)
- [inputlineStyleTag](../by-class/inputlinestyletag.md)
- [mainOutputStream](../by-class/mainoutputstream.md)
- [mainParagraphManager](../by-class/mainparagraphmanager.md)
- [notificationStyleTag](../by-class/notificationstyletag.md)
- [outputManager](../by-class/outputmanager.md)
- [parserStyleTag](../by-class/parserstyletag.md)
- [roomdescStyleTag](../by-class/roomdescstyletag.md)
- [roomnameStyleTag](../by-class/roomnamestyletag.md)
- [roomparaStyleTag](../by-class/roomparastyletag.md)
- [statusroomStyleTag](../by-class/statusroomstyletag.md)
- [statusscoreStyleTag](../by-class/statusscorestyletag.md)
- [styleTagFilter](../by-class/styletagfilter.md)
- say
- withQuotes


## Functions


### `say(val)`

Defined in output.t, line 21

The standard library output function. We set this up as the default display function (for double-quoted strings and for "<< >>" embeddings). Code can also call this directly to display items.


### `withQuotes(txt)`

Defined in output.t, line 32

Generate a string for showing quoted text. We simply enclose the text in a <Q>...</Q> tag sequence and return the result.
