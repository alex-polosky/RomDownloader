==============
||  README  ||
==============
ROM Downloader
v 2.0.0
~ Hondros - alexpolosky@gmail.com

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
1. What is this?
2. Usage
 2a. Menu Layout
 2b. Example
 2c. Gui Version
3. Needs Done
4. Change Log
5. Copyright
6. FAQ
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
1. What is this?

In a nutshell, ROM Downloader is exactly what is in the name:
a rom downloader. It searches a website that I found to have
quality roms (http://romhustler.net), returns a list of roms
you searched for, and then downloads it for you. It can also
catalog the roms on the website
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
2. Usage

Using this program is simple enough. To navigate the menus,
just enter the number for the selection and press 'Enter' to
advance through the menus. When you come to the actual
search, just type in what you're looking for. Note, however,
that it will only search in the catagory for the first
letter of your search query. For example, if you want to 
find 'Super Mario World', you must type 'S' or more. 'Mario'
will not find it

---------------
2a. Menu Layout

1) Search for roms
  1) Input System
    --
  2) Choose System
    1 - x) System
      1) Search for game
        Enter...
      2) Save catalog of games
        Enter...
      3) Download all games [EXPERIMENTAL]
        --
      4) Back
    x) Back
  3) Back
2) Catalog games
  1 - x) System
    Enter...
  x) Back
3) Copyright
  --
4) Help
  --
5) Quit
  ==
-----------
2b. Example

In this example, we will be downloading 
"Super Mario World" for the "Super Nintendo"
1. Run Application
2. Enter '1' for 'Search for roms'
3. Enter '2' for 'Choose System'
4. Enter '34' for 'Super Nintendo'
5. Enter '1' for 'Search for game'
6. Type 'Super Mario World'
7. Enter '1' for 'Super Mario World'
8. Wait for download
See the following:
==============================================================
|Downloading Super Mario World for the Snes		     |
|Note, depending on the size of the game, it may take a while|
|Please be patient					     |
|							     |
|There are 1 parts for this game			     |
|							     |
|Working on 1 of 1					     |
|http://romhustler.net/rom/snes/1504/super-mario-world       |
==============================================================
9. After finishing, open the .7z with WinRar or 7Zip and 
unextract the roms from the archive

----------------
2c. GUI Version

Usage of this program is even simpler.
Start the program, ignore the catalog and browse buttons,
select your system, replace "Game" with the rom you want
to download, and press Search. A list of all the roms
that are found will appear, click on the one you want, and
press "Download". If it is a 1 part download, you will find
a .7z. If it is a multi-part, you'll find several .rar's.
I included 7-zip to unzip the .7z, however, you will have
to get WinRar or something else to unzip the .rar yourself.
Inside these archives you will find your roms.

PLEASE WAIT WHILE THE DOWNLOAD IS IN PROGRESS
IF THE WINDOW FREEZES, IT IS NORMAL

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
3. Needs Done

Console Version:
- Add functionality for inputting a system instead of 
  entering a number from the list [Needs to use common names]
- Add a command line option for the program in format:
  "application system gamename [destination]"
- After download, back to main menu

GUI Version:
- Add cataloging of systems
- Add a status bar >.<
- Add a browse feature to change where it downloads to

Both:
- Auto-Extract .7z for single part roms and .rar for parted
  roms [This is tough]
- Add a search all systems
- If cataloged system file found, use that as a search
  instead of searching the site
- Allow buffer size change

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
4. Change Log

v 1.0.0
-------
- Released the initial program

v 2.0.0
- Added a GUI version
- 

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
5. Copyright [Sort of, I'm no lawyer]

The site 'Rom Hustler' (http://romhustler.net)
has no affliation with me as a programmer, or in general
I do not believe that the owner of this website enjoys
this program, nor do I believe that he supports piracy


I do not accept any penalties that may arise as of you
using this program to download roms that you may or may
not have. It might be illegal, I am not completely sure
Use this program at your own risk.

I grant anyone using this program the ability to
redistribute this program or it's source code, so long
as it is distributed in full

C 2010

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

6. FAQ

None as of yet