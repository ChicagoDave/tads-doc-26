

# TemporaryFile


A TemporaryFile object represents the name of a temporary file in
the local file system.  Since it represents a filename, you can use
a TemporaryFile object in place of a filename string when calling
the "open" methods of the [File](file.md) object.


A temporary file is a file that only exists for as long as the
program is running.  This is useful for things like storing data too
large to fit conveniently in memory, or data that you don't need to
access frequently but wish to keep around for reference purposes.


A temporary file is mostly the same as an ordinary file, but has a
few special properties:


- A temporary file is automatically deleted when the program
     exits.  (That's the reason it's called "temporary".)
- The file's name is assigned by the system, not by your program
     or by the user.  When you create a TemporaryFile object, the system
     automatically assigns the object a unique name that doesn't refer
     to any existing file on the system.
- The file's directory location is determined by the system, not
     by your program or by the user.  Most operating systems have special
     directories designated to store temporary files.  This lets the
     system delete old temporary files from time to time in case the
     programs that create them fail to clean them up themselves.
- Temporary files bypass the file safety settings, so you can
     use temporary files even when the safety level prohibits other
     access to the file system.


To use the TemporaryFile class, you should #include the system
header file `file.h` in your source files.


TemporaryFile objects are always transient.  This means that
they're not saved or restored as part of saved game files.  Saving a
TemporaryFile would be meaningless because it represents a filename
that's only valid for as long as the program is running; restoring
such a name from a saved session wouldn't be usable anyway, since
the name only applied to that previous session.


## Creation


To create a TemporaryFile object, use the `new` operator:


```tads3
local temp = new TemporaryFile();
```


There are no arguments.  The system automatically assigns the new
object a unique filename in the local file system directory designated
by the operating system for temporary files.  For example, on Linux
systems, this will usually be the /tmp directory.


## Accessing temporary files


Creating a TemporaryFile object **doesn't** actually create a
file on disk.  It merely assigns a unique name that you can use to
create a file.  To create the file itself, you can use any of the
"open" methods of the [File](file.md) object, passing the
TemporaryFile in place of the filename:


```tads3
local f = File.openTextFile(temp, FileAccessWrite, 'ascii');
```


After you open a temporary file, you can use it just like an
ordinary file.


You can also pass a TemporaryFile object in place of a filename string
to the following built-in functions:


- [logConsoleCreate()](../functions/tadsio.md#logConsoleCreate) (create
     a log file console)
- [setLogFile()](../functions/tadsio.md#setLogFile) (set a transcript
     or command log file)
- [setScriptFile()](../functions/tadsio.md#setScriptFile) (read commands
     from a command transcript)
- [restoreGame()](../functions/tadsgen.md#restoreGame) (restore the game
     state from a file)
- [saveGame()](../functions/tadsgen.md#saveGame) (save the game state
     to a file)


## Methods


<a name="deleteFile"></a>

`deleteFile()`


Explicitly deletes the local file corresponding to the TemporaryFile
object.  There's no error if the local file doesn't exist or if it
exists but can't be deleted.


The purpose of this method is to explicitly release the temporary
file early.  The system automatically deletes the underlying file
system file, either when the garbage collector deletes the
TemporaryFile object, or when the program exits, whichever is earlier.
This method lets you delete the underlying file even earlier, if you
know that you won't have any further use for it.  This is never
necessary, since the automatic deletion will eventually do the same
thing anyway.  However, if you make heavy use of temporary files in a
program that you expect to run for a long time continuously, it might
help reduce your total disk usage if you use this method to delete
temporary files immediately when you're done with them, rather than
waiting for the garbage collector to get around to it.


This method has no arguments and no return value.


<a name="getFilename"></a>
