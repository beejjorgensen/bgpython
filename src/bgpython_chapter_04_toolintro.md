<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# How do I write a program?

## Objectives

* Move around the directory hierarchy using the shell
* Edit some source code in an editor
* Run that program from the command line

## The Problem That Needs Solving

Let's use our problem-solving framework!

1. **Understand**: We want to write a program that prints a neat little
   message to the screen.

   In the process, we want to get used to using the command line and our
   code editor.

2. **Make a plan**

   1. Open a terminal
   2. Make a directory and change to it
   3. Open a new file in your code editor
   4. Write code and save it to that file
   5. Run your program from the command line

3. **Code it up**: This is where we execute on our plan. We'll do that
   in the following sections.

4. **Postmortem**: We'll do this, below, as well. In future chapters,
   we'll leave these last two off the number list and just do them in
   subsequent sections.

Let's go!

## Start with the Terminal

We're going to do this old-school. Later on, if you find procedures you
like more, you can use those. But programmers have been using the
command line for over 10,000 years, and it has staying power for a
reason.

Launch a terminal and bring up a bash shell. You can use another shell
if you want, but I'll be talking bash here.

At the `$` prompt, type the following commands, one per line:

```
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

```
$ ls -la
total 0
drwxr-xr-x    2 beej  staff    64 Nov 18 23:14 .
drwxr-xr-x+ 123 beej  staff  3936 Nov 18 23:14 ..
```

This is showing you all the files you have. Namely there are two of
them: `.` and `..`. These mean "this directory" and "parent directory",
respectively. (You know how folders can be inside other folders? The
outer folder is called the "parent" folder, which is what the parent
dierctory is. If you want to get back to your home directory from here,
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

```
code hello.py
```

or to launch Vim to do the same thing:

```
vim hello.py
```

> _If you get in Vim and have no idea how to get out, hit the `ESC` key
> and then type `:q!` and hit `RETURN`---this will exit without saving.
> If you want to save and exit, hit `ESC` then type `ZZ` in caps. I'm
> not going to talk about Vim any longer and will stick to VS Code._

In any case, one you get your editor of choice launched, you should be
faced with a largely-blank window and a cursor.

This is your canvas! This is where the magic happens!

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

```
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

Then type this to run it (if `python3` doesn't work, try `python` or
`py` depending on your system):

```
python3 hello.py
```

and hit `RETURN`! _[Angelic Chorus!]_

```
$ python3 hello.py
Hello, world!
My name's Beej and this is (possibly) my first program!
```

You just wrote some instructions and the computer carried it out!

Next up: write a Quake III clone!

Okay, so maybe there might be a small number of _in between_ things that
I skimmed over, but, as Obi-Wan Kenobi once said, "You've taken your
first step into a larger world."

## Exercises

1. Make another program called `dijkstra.py` that prints out your three
   favorite [fl[Edsger Dijkstra
   quotes|https://en.wikiquote.org/wiki/Edsger_W._Dijkstra]].

## Summary

* Move around the directory hierarchy using the shell
* Edit some source code in an editor
* Run that program from the command line
