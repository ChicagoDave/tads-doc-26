# tadsiox.h


## Classes

- enableSystemMenuCommand
- showPopupMenu


## Functions


### `enableSystemMenuCommand(id, stat)`

Defined in tadsiox.h, line 106

Enable/disable a system menu command. Some interpreters offer a set of common system-level game commands via menus, toolbars, or similar UI widgets, depending on local conventions - commands such as SAVE, RESTORE, UNDO, and QUIT that most games offer.


### `showPopupMenu(x, y, txt)`

Defined in tadsiox.h, line 61

Show a popup menu. This opens a temporary window, drawn in a style consistent with the local conventions for popup menus. The new window is shown in the foreground, in front of the active game window. 'txt' gives HTML text that's used for the contents of the new window.
