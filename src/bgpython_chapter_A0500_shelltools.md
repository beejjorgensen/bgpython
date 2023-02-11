<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Accelerating Beyond IDLE

## Objectives

* Install a real IDE
* Learn about the _command line_.
* Get your terminal/shell up and running, and explain how it's used

## What with the What Now?

We've been using IDLE to edit code, and that's fine to get started. But
it's a little bit underpowered for getting to the next level when it
comes to programming.

In this section, we'll look at some tools that professional programmers
use to get the job done.

## The Terminal

Back in the day, people accessed mainframes through dedicated pieces of
hardware called _terminals_. These looked like old TV sets with
keyboards attached. Screens were typically monochrome, either white,
green, or amber colored, with pixely text.

Barely anyone has a real terminal anymore, but they have programs called
_terminal emulators_ that pretend to be terminals. In fact, real
terminals are so rare, and terminal emulators are so common, if you hear
someone say "terminal", they're certainly talking about a terminal
emulator.

So a terminal emulator is a program you run that gives you a text window
to interact with your computer.

You know how you point, click, and drag with the mouse to command your
computer to do things? We're going to do the same things, except we're
going type commands in to get them done, instead.

### The Shell

Sometimes you'll hear people talk about the "shell" and "terminal"
interchangeably.

Technically, though, the terminal is what you launch, and then the
terminal immediately launches another program, the _shell_, that you
interact with.

> The terminal is pretty dumb on its own. All it does it handle input
> from the keyboard and output to its "screen". It's the middleperson
> between you and the shell. The shell is the real brains of the outfit.

The shell is a program that takes your typed-in commands and executes
them, and tells you if something went wrong.

The most popular shell program on Unix-likes and Macs is the _Bourne
Again Shell_ (Bash)^[This is a bit of a pun around the original _Bourne
Shell_ from back in the day. Bash improves on it a bit.], although the
_Z-shell_ (Zsh) is growing in popularity. Bash is known by a `$` prompt
(sometimes prefixed with other information about which directory you're
in, or something similar). Zsh uses a `%` prompt.

There are multitudes of shells, but we'll just assuming you're going to
use Bash or Zsh (with a hat-tip to Windows's built-in shells), and
they're compatible enough for our purposes.

### Windows Terminals and Shells

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

### Windows gitbash

[fl[Git|https://git-scm.com/downloads]] is a _source code control
system_. And it's great. Tons of people use it. You should install it.

When you install it, it installs a bash shell called gitbash that you
can use.

### Windows WSL

The Windows Subsystem for Linux is an awesome piece of kit. It
unobtrusively puts a little Linux install on your Windows machine. And
then you can use the Linux command line.

To install [fl[Follow the WSL setup
instructions|https://learn.microsoft.com/en-us/windows/wsl/install]]

There's a recommendation in there to also [install Windows
Terminal](https://learn.microsoft.com/en-us/windows/terminal/install),
an alternate terminal to the existing ones. It's a good choice.

After installing, update the system:

``` {.default}
sudo apt update
sudo apt -y upgrade
```

and Python should be there; running this should get you the version
number:

``` {.default}
python3 --version
```

You can open a File Explorer window with:

``` {.default}
iexplore.exe .
```

(Yes, that's a period after a space at the end.)

### Mac

Macs come with a terminal built-in. Run the `Terminal` app and you'll be
presented with a bash shell prompt.

### Linux/Unix-likes

All Unix-likes come with a variety of terminals and shells. Google for
your distribution.

## Installing an IDE

There are a lot of IDEs out there, but a good free one is VS Code.

Visit the [fl[Visual Studio Code|https://code.visualstudio.com/]]
website for downloads.

Let's get it installed!

### Windows VS Code

When you install:

* Make sure "Add Path" is checked
* Check "Register Code as an editor for supported file types"
* Recommended: Check "Add 'Open with Code' option"

If you're using WSL, first run VS Code from _outside_ WSL, and install
the "Remote WSL" extension. Then you should be able to run it from
inside WSL.

### Mac

Just install it. No special instructions.

### Linux and other Unix-likes

Linux and Unix-like users can use their package manager to install VS
Code. Google for `ubuntu vscode install`, substituting the name of your
distro for `ubuntu`.

If you already have a code editor you prefer using (Vim, Emacs, Sublime,
Atom, PyCharm, etc.) feel free to use that, no problem!

## Running VS Code

In the shell of your choice, if all has gone well, you should be able to
type:

``` {.default}
code
```

and have it launch VS Code.

Once launched, click the icon on the left bar of VS Code to manage
extensions.

* Install Python extension
* Install Pylint extension

## Using a Barebones Editor and Terminal

Not all development environments are integrated. Some programmers use
standalone editors and debuggers to get the work done.

A typical cycle is:

1. Edit code in your editor
2. Run the code from the command line
3. Check the output, prepare to debug
4. Repeat!

### Start with the Terminal

We're going to do this old-school. Programmers have been using the
command line for over 10,000 years, and it has staying power for a
reason.

Launch a terminal and bring up a shell. You can use another shell if you
want, but I'll be talking bash/zsh here.

At the prompt, type the following commands, one per line:

``` {.default}
cd
mkdir bgpython
cd bgpython
ls -la
```

These commands do four amazing things:

1. `cd` means _change directory_. (A directory is the same as a folder.)
   On a line by itself, it means "change to my _home directory_".

2. `mkdir` means _make directory_. We're creating a new folder called
   `bgpython`.

3. `cd bgpython` to change into that directory.

4. `ls -la` to get a long directory listing (i.e. all the files in that
   folder.)

At this point you should see something like this:

``` {.default}
$ ls -la
total 0
drwxr-xr-x    2 beej  staff    64 Nov 18 23:14 .
drwxr-xr-x+ 123 beej  staff  3936 Nov 18 23:14 ..
```

This is showing you all the files you have. Namely, there are two of
them: `.` and `..`. These mean "this directory" and "parent directory",
respectively. (You know how folders can be inside other folders? The
outer folder is called the "parent" folder, which is what the parent
directory is. If you want to get back to your home directory from here,
you can type `cd ..`.)

> _You should think of the shell as "being" in a certain directory at
> any particular time. You can `cd` into directories, or `cd ..` back
> into the parent, or `cd` to get to your home directory from anywhere.
> It's like the folder you have open that has focus in a GUI._

(The remaining information on each line tells you the permissions on the
file, who owns it, how big it is, when it was modified, and so on. We
can worry about that later.)

Other than those there are no other files. We'll soon fix that! Let's
add a Python program and run it!

## Launching your code editor

Usually launching an editor to edit a file is as simple as typing the
editor name directly followed by the filename on the command line.

For example, to launch VS Code to edit the file `hello.py`:

``` {.default}
code hello.py
```

But wait--isn't VS Code a full-fledged IDE? Yes, it is. Another popular
editor is Vim:

``` {.default}
vim hello.py
```

But in any case, you're in the editor and ready to type code.

This is your canvas! This is where the magic happens!

> If you get in Vim and have no idea how to get out, hit the `ESC` key
> and then type `:q!` and hit `RETURN`---this will exit without saving.
> If you want to save and exit, hit `ESC` then type `ZZ` in caps.
>
> Vim is a complex editor that is hard to learn. But after you learn it,
> I maintain it's the fastest editor on the planet. I'm using it to type
> this very sentence right now.
>
> To learn it, I recommend OpenVim's [interactive Vim
> tutorial](https://www.openvim.com/) and this reference of [Vim
> commands from beginner to
> expert](https://thevaluable.dev/vim-commands-beginner/).

Type [flx[the following|hello.py]] into your editor (the line numbers,
below, are for reference only and shouldn't be typed in):

``` {.py .numberLines}
print("Hello, world!")
print("My name's Beej and this is (possibly) my first program!")
```

Pull down `File`→`Save` to save the file.


## Running the Program!

Pop back into your terminal window and type `ls -la` to get a directory
listing:

``` {.default}
$ ls -la
total 8
drwxr-xr-x    3 beej  staff    96 Nov 18 23:27 .
drwxr-xr-x+ 123 beej  staff  3936 Nov 18 23:14 ..
-rw-r--r--    1 beej  staff    87 Nov 18 23:27 hello.py
```

There it is! `hello.py` clocking in at 87 bytes (characters, roughly) in
size.

Let's run this puppy. Remember how the program is just a recipe for
doing a thing---what do you think our `hello.py` program does? Guess!

Then type this to run it (if `python` doesn't work, try `python3` or
`py` depending on your system):

``` {.default}
python hello.py
```

and hit `RETURN`! _[Angelic Chorus!]_

``` {.default}
$ python hello.py
Hello, world!
My name's Beej and this is (possibly) my first program!
```

You just wrote some instructions and the computer carried it out!

Next up: write a Quake III clone!

Okay, so maybe there might be a small number of _in between_ things that
I skimmed over, but, as Obi-Wan Kenobi once said, "You've taken your
first step into a larger world."

## Exercises

Remember to use the [four problem-solving steps](#problem-solving) to
solve these problems: understand the problem, devise a plan, carry it
out, look back to see what you could have done better.

1. Make another program called `dijkstra.py` that prints out your three
   favorite [fl[Edsger Dijkstra
   quotes|https://en.wikiquote.org/wiki/Edsger_W._Dijkstra]].

## Summary

* Move around the directory hierarchy using the shell
* Edit some source code in an editor
* Run that program from the command line

