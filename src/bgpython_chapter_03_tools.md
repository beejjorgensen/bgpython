<!--
# vim: ts=4:sw=4:nosi:et:tw=72
-->

# What software will I need?

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

I recommend Visual Studio Code (VS Code).

(Okay, I'm lying. I recommend Vim! But it has a steep learning curve
(worth it) and [fl[you might need a
tutorial|https://www.openvim.com/]].)

Visit the [fl[Visual Studio Code|https://code.visualstudio.com/]]
website for downloads.

(Linux and Unix-like users can use their package manager to install VS
Code. Google for `ubuntu vscode install`, substituting the name of your
distro for `ubuntu`.)

If you already have a code editor you prefer using (Vim, Emacs, Sublime,
Atom, PyCharm, etc.) feel free to use that, no problem!

## Python itself!

This is enough of a challenge that we'll do it in the next chapter.

