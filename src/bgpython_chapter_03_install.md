<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# What software will I need?

## Objectives

* Install a code editor, and explain what it's for
* Get your terminal/shell up and running, and explain how it's used
* Install Python, and explain what it does

## What are all these things?

Writing code strays away from the GUI that you might be used to. It's
definitely possible to use a GUI to do everything (almost... maybe) but
devs use a couple other tools to keep their speed up.

One of these _is_ a GUI: the _code editor_. This is where you write the
instructions (code) that the computer will run.

The other is the _terminal_. This is a window that allows you to type
computer commands in a program called a _shell_. The shell executes the
commands you type on the _command line_ (i.e. where the cursor is). The
commands aren't Python, but are shell-specific commands.

Developers use these tools to write code. A typical cycle is:

1. Edit code in your editor
2. Run the code from the command line
3. Check output, prepare to debug
4. Repeat!

> _**Note!** Technology changes quickly---this book might already be out
> of date. If you get stuck, Google around for more modern answers.

## Terminal/Shell

The most popular shell program on Unix-likes and Macs is the _bash
shell_. It's known by a `$` prompt (sometimes prefixed with other
information about which directory you're in, or something similar).

When you bring up a terminal window on a Mac or Unix-like or Windows
WSL, it's a bash shell you'll find running in it.

> Bash _stands for_ Bourne Again SHell _which is a bit of a pun around
> the original [flw[Bourne Shell|Bourne_shell]] from back in the day.
> Bash improves on it a bit.

Now Bash isn't the only shell, by any means. But it is the only one I'll
be talking about for Mac, Linux, and WSL.

### Windows

For Windows, there are plenty of options, some of which you have
installed already.

* **CMD**: classic shell with origins way back in the MS-DOS days.
* **PowerShell**: a new, more powerful shell.
* **Bash via Git**: the famous [fl[Git|https://git-scm.com/]] software
  package has a bash shell called, appropriately, "gitbash".
* **Bash via WSL**: if you install WSL (below), it uses bash, as well.

Unless you're going with one of the bash options, you should use
PowerShell because it's newer, better, and maintained.

Almost all of the bash commands we use in this guide also work in
PowerShell and CMD.

Hitting the Windows key and running `cmd` will bring up the CMD prompt.
(Type `exit` to get out.)

Hitting the Windows key and running `PowerShell` will bring up the
PowerShell prompt. (Type `exit` to get out.)

### Windows gitbash (optional)

[fl[Git|https://git-scm.com/downloads]] is a _source code control
system_. And it's great. Tons of people use it. You should install it.

When you install it, it installs a bash shell called gitbash that you
can use.

### Windows Shell App (optional)

If you have Windows 10, there's a great new app for running multiple
shells at once in tabs: Terminal. You don't _need_ this, but it allows
you to run different terminal types in different tabs, if you want to do
that.

1. Update Windows 10 to the latest version
2. Drop into the Microsoft store and grab Terminal.

When you run it, there will be options to bring up different kinds of
shells. This works with CMD, PowerShell, and any WSL shells (if you
install WSL), and gitbash shells (if you install git).

If you install gitbash, you'll want to add it to the settings for
Terminal. (If you don't do this, you'll only be able to launch gitbash
from outside the Terminal app, which isn't the end of the world.)

This is a rather unfriendly editing of a [flw[JSON|JSON]] file
(which might be easier after you install VS Code).

If you do it, carefully add this block to the JSON config before the
other blocks in the obvious section:

``` {.json}
{
    "guid": "{8cbf8e47-b0bd-4956-8c76-ae5d6250fe67}",
    "icon" : "ms-appx:///ProfileIcons/{0caa0dad-35be-5f56-a8ff-afceeeaa6101}.png",
    "name" : "Git Bash",
    "commandline" : "\"%PROGRAMFILES%\\git\\usr\\bin\\bash.exe\" -i -l",
    "cursorShape" : "filledBox",
    "startingDirectory" : "%USERPROFILE%"
},
```

I know that if you're a beginner, this looks like voodoo. Trust your
instincts. Where does it _look_ like this block needs to go? What
patterns do you see in the config file?

(Note the `cursorShape`---you can add that line to the other shells,
too, if you prefer it.)

### Windows WSL (optional)

**Windows 10 or later required!**

The Windows Subsystem for Linux is a really awesome piece of kit. It
unobtrusively puts a little Linux install on your Windows machine. And
then you can use the Linux command line.

To install:

1. Update Windows to the latest version.
2. [fl[Follow the WSL setup
   instructions|https://docs.microsoft.com/en-us/windows/wsl/install-win10]]
3. Head to the Microsoft Store and grab Ubuntu (not the LTS version).
4. Once installed, run Ubuntu and you'll see a bash prompt.
5. Make a new username and password when prompted. This is for WSL and
   is completely separate from your Windows username and password.
   Though you can make them the same if you want---easier to remember
   that way.
6. Upgrade Ubuntu by running these two commands:
   ```
   sudo apt-get update
   sudo apt-get upgrade 
   ```
7. At this point, you should be able to run Python:
   ```
   python3 --version
   ```
8. Type `exit` and then run the shell again to finalize the install.

When running VS Code, you can just run it from the bash prompt:

```
code
```

You can also open a file Explorer window with:

```
iexplore.exe .
```

(Yes, that's a period after a space at the end.)

### Mac

Macs come with a terminal built in. Run the `Terminal` app and you'll be
presented with a bash shell prompt.

### Linux/Unix-likes

All Unix-likes come with a variety of terminals and shells. Google for
your distribution.

## Code editor

Simple code editors just allow you to edit files. More complex ones are
more full-featured and are sometimes called _Integrated Development
Environments_, or _IDE_ for short.

I recommend Visual Studio Code (VS Code), an IDE.

(Okay, I'm lying. I recommend Vim, an editor! But it has a steep
learning curve (worth it) and [fl[you might need a
tutorial|https://www.openvim.com/]].)

Visit the [fl[Visual Studio Code|https://code.visualstudio.com/]]
website for downloads.

### Windows VS Code

When you install:

* Make sure "Add Path" is checked
* Check "Register Code as an editor for supported file types"
* Recommended: Check "Add 'Open with Code' option"

When you launch code in PowerShell or gitbash or WSL for the first time
with

```
code
```

click the icon on the left bar of VS Code to manage extensions.

* Install Python extension
* Install Pylint extension

If running WSL, or you might run WSL:

* Install Remote WSL extension

### Mac

Just install it. No special instructions.

### Linux and other Unix-likes

Linux and Unix-like users can use their package manager to install VS
Code. Google for `ubuntu vscode install`, substituting the name of your
distro for `ubuntu`.

If you already have a code editor you prefer using (Vim, Emacs, Sublime,
Atom, PyCharm, etc.) feel free to use that, no problem!

## Python itself!

### A note on Python2 versus Python3

Back in the day, Python version 2.x was king. Everything was written
using it. But it had a few shortcomings that couldn't be addressed
without major surgery. This surgery resulted in what we call _breaking
changes_ to the language. That is, old programs written for Python2
would be broken when trying to run them on Python3. They had to be
updated.

After only 37,600 years^[I always exaggerate.], the old Python2 code was
dragged kicking and screaming into the glorious future of Python3 and
now Python3 is finally the go-to version for all Python developers.

Not to say there's not tons of Python2 code out there, because there is,
but everything we'll be doing here will be in Python 3.6 and later.
(Google for `python2 vs python3` for more information on the differences
if you happen to cruelly find yourself in a Python2 environment.

### Checking to see if you already have Python installed

There are a number of different ways on different platforms.

As long as you can bring up a terminal and type on of the following on
your terminal and get it to report version 3.6 or higher, you're set:

```
python3 --version
python --version
py --version
```

If those aren't installed, or none of them report version 3.6 or higher,
then read on for an install. (Or google for instructions to upgrade.)


### Windows native

There are two ways to do this:

* Install from the Microsoft Store
* Install from the official website

I can't see any disadvantage to installing it from the store. Just
remember to install Python 3 (not Python 2).

If you install it from the [fl[official
website|https://www.python.org/downloads/]], you need to remember to
check the "Add to PATH" box during the install procedure!

Once this is installed, you should be able to bring up PowerShell and
run

```
py --version
```

and see that it's in place.

### Windows WSL

If you've followed the instructions for installing WSL, above, you
should just be able to go to WSL bash and run

```
python3 --version
```

straightaway.

### Mac

There are a few third-party package managers for command line tools for
the Mac, including [fl[Homebrew|https://brew.sh/]] and
[fl[MacPorts|https://www.macports.org/]]. We're only going to cover
Homebrew here.

Visit the Homebrew home page, and install it.

Then run this in the bash shell:

```
brew install python
```

After that, `python3 --version` should work.

You can also install Python straight from the official website, but lots
of people on the web recommend using brew to manage it instead.

### Linux/Unix-likes

The Linux community tends to be pretty supportive of people looking to
install things. Google for something like `ubuntu install python3`,
replacing `ubuntu` with the name of your distribution.

## Summary

* The code editor is where you'll be typing your programs.
* The terminal is where you'll be running your programs and doing
  various other file machinations.
* Python is a program that will run your Python programs!

