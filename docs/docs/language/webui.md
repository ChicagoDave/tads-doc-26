

# The Web UI


Starting in TADS 3.1, you can choose between the traditional TADS
user interface or the new Web UI.  In the traditional UI, the user
installs a TADS interpreter on her machine, and the interpreter
displays the user interface using the native features of the operating
system - opening a window on the Mac, for example, or writing to the
terminal window on Unix.  With the Web UI, the user interface isn't
part of the TADS interpreter at all, but instead runs in a standard
Web browser.  The game still runs in the TADS interpreter, but the
interpreter doesn't show any UI windows; instead, the game sends
everything to the Web browser for display, via a network connection.


The Web UI configuration offers several big new capabilities beyond
what's possible with the traditional TADS user interface:


- **Web-based play.**  You can set things up so that users can play
     your game directly in a browser, without installing your game or
     any TADS software on their machines.  Users simply point their
     browser to a URL, and the game runs in the browser window.  There's
     nothing for players to download or install - not even a plug-in, since
     the UI is built entirely on standard Web technologies that are native
     to all modern browsers (HTML, CSS, Javascript, and AJAX).  Your game
     and the TADS interpreter run on a separate Web server machine;
     the user only needs to know the URL to the server, which you can
     easily supply via a hyperlink on your own Web page.
- **Full support for Javascript, CSS, and HTML DOM.**  The
     traditional HTML TADS user interface uses an "extended subset"
     of the older HTML 3.2 standard, and has no support for
     CSS, Javascript, or HTML DOM access.  With the Web UI, you have
     access to all of those technologies, plus full standard HTML,
     because the UI runs in an actual browser.  HTML TADS is certainly
     more optimized for the traditional text game UI than a browser is,
     but the trade-off is that it's narrowly focused on that one type of
     UI.  Web browsers are much more flexible and powerful as UI platforms.
- **Multiuser gaming.**  A key TADS feature that makes the Web UI
     possible is a network server capability.  The network capability goes
     beyond just talking to the browser, though: it's really a full-featured
     networking layer that lets a game communicate with multiple clients,
     opening up numerous possibilities for collaborative and multi-user
     games.  Although the Adv3 library is only designed for a single player
     character, its new Web UI support does allow multiple people to
     connect to the same session and play the game collaboratively.


## Choosing between the regular UI and the Web UI


The Web UI is a whole separate output layer from the traditional
user interface, with its own set of functions.  This is good news and
bad news.


The good news is that the Web UI gives you vastly more control and
power than the traditional console UI offers.  For one thing, all of
the networking features are directly available - they're not hidden
inside the interpreter, but are readily accessible and controllable
from your program.  For another, you have direct access to all of the
browser-side coding: you can write your own HTML, CSS, Javascript, and
AJAX code to run in the browser, so you can customize virtually every
aspect of the user interface.  There's absolutely nothing about the
Web UI that's built into the interpreter; everything that's predefined
is simply part of the library, so it's readily accessible and
customizable.  Your game's UI can do anything that a Web site can do -
drag-and-drop, animation, dynamic pop-up lists, layered objects,
menus, and on and on.


The bad news is that **you must choose in advance** whether your
game will use the Web UI or the traditional UI.  If you stick to the
basic command-line user interface, the only difference is in compiler
options, so you can actually compile the same game both ways - so
you'd have a single set of source files, but you'd compile it twice,
once into a .t3 file for conventional play, and again into a separate
.t3 for Web play.  On the other hand, if you decide to take advantage
of the more advanced features of the conventional UI (such as sound
playback or the Banner API), or if you want to customize the
Javascript front end of the Web UI, your game will be tied to the UI
that you choose.


If you have an existing game that you created with a previous TADS
3 version, you can port it to the Web UI.  If you were careful to use
only Adv3 functions for input and output, rather than calling built-in
interpreter functions directly, porting your game to the Web UI should
be a simple matter of recompiling with the Web UI compiler settings.
If you made use of more advanced UI features, though, porting requires
somewhat more work:


- the banner API
- sound playback
- non-standard TADS HTML tags


### Creating a new Web UI game from scratch


The first step in creating a Web UI game is to set up your build
instructions (your project's .t3m file) to include the networking
functions and the Web UI version of the Adv3 library.


**If you're using Workbench on Windows:** Select the Create New
Project command.  The "wizard" dialog will ask you which type of user
interface to use; select the "Web UI" button.


Note that the UI option only appears if you use the Adv3 library -
that is, either the "Introductory" or "Advanced" template.  If you
choose a custom template, or the "Plain T3" (no library) option, the
UI option doesn't apply, so you'll have to follow the instructions
below for manual project creation.


**If you're creating your project file manually:** Follow the
standard procedure for creating a .t3m file for a regular Adv3 game.
Once you've set up the basic .t3m file, follow the instructions
[below](#manual_port) for changing a .t3m file from a
conventional game to the Web UI.


### Porting an existing game


To port an existing game based on the traditional console user
interface (including HTML TADS games), the first step is to switch to
the Web UI libraries.  This requires a few changes to your project's
.t3m file.


**Attention Workbench users on Windows:** It's possible to make
the necessary changes using Workbench, but the procedure is actually a
bit easier if you edit the .t3m file manually, so the explanation
below assumes you're going that route.  **Close Workbench** before
proceeding, and use a different editor, such as Notepad.  **Don't**
attempt to edit the .t3m file using Workbench or while it's open in
Workbench, since Workbench will overwrite any changes you make as long
as Workbench has it open.


<a name="manual_port"></a>
