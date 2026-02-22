# StyleTag

*class* — defined in [output.t](../by-file/output.t.md) (line 765)


Style tag. This defines an HTML-like tag that can be used in output text to display an author-customizable substitution string.


**Superclass chain:** `object` > **StyleTagSubclasses:** [HtmlStyleTag](htmlstyletag.md)


**Global objects:** [announceObjStyleTag](announceobjstyletag.md), [assumeStyleTag](assumestyletag.md), [notificationStyleTag](notificationstyletag.md), [parserStyleTag](parserstyletag.md), [roomdescStyleTag](roomdescstyletag.md), [roomnameStyleTag](roomnamestyletag.md), [roomparaStyleTag](roomparastyletag.md), [tipStyleTag](tipstyletag.md)


## Properties


### `closeText`

Defined in output.t, line 780

Closing text - this is substituted for each instance of the tag with a '/' prefix (<./xxx>). Note that non-container tags don't have closing text at all.


### `openText`

Defined in output.t, line 773

opening text - this is substituted for each instance of the tag without a '/' prefix


### `tagName`

Defined in output.t, line 767

name of the tag - the tag appears in source text in <.xxx> notation
