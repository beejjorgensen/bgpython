<!--
# vim: ts=4:sw=4:nosi:et:tw=72:spell
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
commands you type on the _command line_ (i.e. where the cursor is).  The
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
> the original [fl[Bourne
> Shell|https://en.wikipedia.org/wiki/Bourne_shell]] from back in the
> day. Bash improves on it a bit.

TODO: Windows Terminal, Windows bash,
https://itsfoss.com/install-bash-on-windows/


### Windows WSL

TODO

### Windows

TODO

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

(Linux and Unix-like users can use their package manager to install VS
Code. Google for `ubuntu vscode install`, substituting the name of your
distro for `ubuntu`.)

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

As long as you can bring up a terminal and type on of the following and
get it to report version 3.6 or higher, you're set:

```
    python3 --version
    python --version
    py --version
```

If those aren't installed, or none of them report version 3.6 or higher,
then read on for an install. (Or google for instructions to upgrade.)


### Windows WSL (recommended)

TODO

### Windows native

TODO -- is there a way to streamline this with Windows WSL?

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

