<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**.
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**.
-->

# Reading Files

**WIP**

## Objective

* Understand what a file is
* Be able to open and close a file
* Be able to read and write from files

## Project

Write a _line editor_.

Back in the day, before terminals were very capable and before we had
nice editors and IDEs like we do today, people used line editors. These
were bare-bones file editors that used simple commands to edit files.

For example:

```
$ python lineedit.py foo.txt
> l
1: This is some text that was already in the file.
> a
This is some text that I'm appending to the file.
And some more.
.
> l 1
1: This is some text that was already in the file.
2: This is some text that I'm appending to the file.
3: And some more.
> e 3
And really some more.
> l 1
1: This is some text that was already in the file.
2: This is some text that I'm appending to the file.
3: And really some more.
> d 2
> l 1
1: This is some text that was already in the file.
2: And really some more.
> w
> q
```

In the example, everything following a `>` prompt is a line editor
command.

In order:

1. `l`ist the file starting from the current line (which defaults to 1).
2. `a`ppend some text on the end of the file (until the user types `.`
   on its own line).
3. `l`ist the file from line 1.
4. `e`dit line 3.
5. `l`ist the file from line 1.
6. `d`elete line 2.
7. `l`ist the file from line 1.
8. `w`rite the file (the name was specified on the command line).
9. `q`uit

The commands are:

* `l`ist: If the user specifies a line number, listing should start from
  that line. If the user specifies a second line number, the listing
  should end there. If the user doesn't specify a starting number,
  listing starts at the last line edited (or 1 if no line has been
  edited so far). If the user doesn't specify an ending number, the
  listing stops at the start plus 10 lines. In all cases, the listing
  ends at the end of the file, even if the user requests more.

* `a`ppend: If the user doesn't specify a line to append after,
  appending happens at the end of the file. If the user specifies line
  `0`, the lines are inserted at the top of the file. If the user
  specifies a line past the end of the file, the lines are appended to
  the end of the file.

* `d`elete: Works like `l`ist, except deletes the lines.

* `e`dit: Edits a single line, replacing it. If the line is out of
  range, an error message should be printed.

* `w`rite: Saves the file to disk. If the filename wasn't specified on
  the command line, the user must specify a filename after the `w`.

* `q`uit: exit the editor without saving the file.

From the user standpoint, lines are numbered starting from 1.

Keep this project in mind while you read through this chapter.


## What are Files, Anyway?

Problem-solving step: **Understanding the Problem**.

We're sort of used to them, already, right? I mean, you have MP3 files,
GIF files, or MPEG files...

> "So this guy comes up to me and he says, 'What do you do?'
>
> "'Well,' I says, 'I work on computers.'
>
> "An' he says, 'Wow---if you work on computers? Do you use files?'
>
> "An' I says, 'Do I use files? Why I use... ARJ files, GIF files, JPEG
> files, JAR files, RAR files, PNG files, DOC files, MPEG files, TXT
> files, PUB files, PY files, LOG files...
>
> "'An' I use files, files, files, files, files, files, files, files,
> files, files, files, files, files, files, files, files, files, files,
> files, files, files, files, files... files all the time!'---Take
> shots! 11!"
>
> ---With sincere apologies to _Jughead_ and _The Hockey Song_.

We're going to take a look at files from a high level, look at how to do
some basic operations on files, and we'll leave it there for now. Later
we'll revisit some more advanced techniques.

But what _is_ a file actually?

Let's start by saying a file is a collection of characters stored in a
particular order on your disk or SSD on your computer.

We've already seen a bunch of examples---our Python source files that
we've been saving this whole time! They're sequences of characters
stored in a specific order and saved on disk.

Now, files are actually far more general-purpose than that, but let's
start with this. We can always chase the rabbit further down the rabbit
hole later.

For this chapter, we're going to use a type of file commonly called a
_text file_. This is also just a sequence of characters, just like a
Python source file. But text files can be anything. Love letters, The
Gettysburg Address, the lyrics for the latest hit single by that one
band, the number $\pi$ computed to a million decimal places, or
whatever.

> Technically, Python source files are text files, as well, but they're
> a specific type. All Python source files are text files, but not all
> text files are Python source files.

As a human, you can identify the type of file by its _extension_. That
is, the part of the filename after the last period in the file.

For Python, we've been using `.py` (pronounced "dot-pie") as the
extension, identifying this file as a Python source file.

General text files use `.txt` ("dot-text") as an extension. And you can
make them with the same editor you've been using to write Python code.

Go ahead and open a new file, and call it `wargames.txt`. Enter some
text into it, like this:

> What he did was great! He designed his computer so that it could learn
> from its own mistakes. So, they'd be better the next time they played.
> The system actually learned how to learn. It could teach itself!

Now, the question is, how do you run a Python program that _reads_ this
file in, and stores or manipulates the data in memory?

## Reading Files, The Classic Way

Problem-solving step: **Understanding the Problem**.

In many programming languages, there are three steps to reading a file:

1. Open the file for reading.
2. Read data from the file.
3. Close the file.

This is super-duper common.

What does it mean to "open" and "close" the file?

Well, it's analogous to when you open the file in your editor, and then
close it.

"Opening" is asking the _operating system_^[The Operating System is like
Linux, Windows, MacOS, Unix, etc. It's a program that helps you, the
user, interface with the hardware on the system, like keyboards,
screens, and disks.] (OS) to give you access to the file. You can open
for reading, for writing, or for both.

For this section, we'll want to ask the OS to open the file for reading.

"Closing" the file is the opposite of opening. We're telling the OS that
we're done with the file. The OS does any cleanup it has to. You should
always close any files you open. (All files that you open will
automatically be closed when your program completes its run, but you
still should explicitly close them anyway^[It's a level of polish that
other devs will expect. If they see you're not thorough enough to close
any files you open, they'll wonder what else you've missed.].)

And "reading" is actually pulling the data from the file on disk into
strings in memory.

Problem-solving step: **Devising a Plan**

Let's write [flx[some code|fileread1.py]] to read our `wargames.txt`
file and print out the contents on the screen.

Our steps will be:

1. Open the file
2. Read the data
3. Close the file
4. Print the data

Problem-solving step: **Carrying Out the Plan**

``` {.py}
# Open the file
f = open("wargames.txt")

# Read all data from the file
data = f.read()

# Close the file
f.close()

# Print out the data we read earlier
print(data)
```

Some things to note:

* When we opened the file, we didn't specify read or write. In Python,
  it's "read" by default.
* Notice that we close the file before we print anything. We didn't
  _have_ to, but it demonstrates how we now have a _copy_ of the data in
  memory. We can still use it, even though we've closed the file.

Since we have a copy of the data, we can do all kinds of stuff to change
it.

If you modify the last two lines to be:

``` {.py}
# Print out the data we read earlier
print(data.upper())
```

we'll get the output in uppercase. (But the original file is still
lowercase, of course!) It's our copy of the data to do with as we
please!

## Opening Files with `with`

Now there is a more _canonical_^[Meaning, the One Right-_ish_ Way to do
something.] approach to reading files using the `with` statement in
Python.

Earlier, we read a file

``` {.py}
f = open("wargames.txt")
data = f.read()
f.close()
print(data)
```

The equivalent using the `with` statement looks like this:

``` {.py}
with open("wargames.txt") as f:
    data = f.read()
    print(data)
```

If you're looking closely, you'll notice that the `f.close()` is
missing. That's because when you use `with` to open the file, that gets
handled automatically for you! Not only that, but even if some error
occurs, the file will be properly closed.

Although the pattern of open-read-close is really common in other
languages, and Python supports it, the preferred way of doing things is
with the fantastic `with` statement.

## Reading Data a Line at a Time

Check this out: in our previous examples, we read the entire file into
memory at once. That's what the `.read()` method does.

For small files, that's no problem.

But what if you have a file that's 200 GB of data? You (probably, as of
this writing in 2020) don't have that much memory. How can you deal with
big files like this?

The answer is to read them a little bit at a time.

With text files like this, a common thing to do is to read them a _line_
at a time. Then you process that line, and then move on to the next one.
This way you only need to have a single line from the file in memory at
once, instead of the whole 200 GB worth.

Let's use the `with` statement to open a file, and then read a line at a
time.

``` {.py}
line_num = 1
with open("wargames.txt") as f:
    for line in f:
        print(f'{line_num}: {line}')
        line_num += 1
```

And we get this output:

```
1: What he did was great! He designed his computer so that it could learn

2: from its own mistakes. So, they'd be better the next time they played.

3: The system actually learned how to learn. It could teach itself!
 
```

Pretty neat, eh? We just get to use a `for` loop on the opened file to
read one line at a time.

But wait! Why is there an extra newline being printed out? What are
those blank lines between the lines?

This is a common beginner mistake. The reason is that there is a newline
at the end of every line of the file already (because that's where the
line breaks are). And, in addition, `print()` adds its own newline! So
we get both of them printed.

The easiest workaround is to use the `end` keyword argument on
`print()` to stop it from adding a newline of its own:

``` {.py}
print(f'{line_num}: {line}', end='')
```

Another option is to use `.rstrip()` on the string to strip newlines
from the end.

``` {.py}
line = line.rstrip('\r\n')
```

That'll strip carriage returns or newlines from the right side of the
string. We have to specify both since some OSes use different characters
to represent the end of the line, somewhat irksomely.

An even-more-portable way to write this is to first:

``` {.py}
import os
```

then

``` {.py}
line = line.rstrip(os.linesep)
```

and Python will automatically use the proper end-of-line character no
matter what system you're running the program on.

## Writing files

So far we've been dealing with getting data out of files, but now let's
talk about creating new file and writing data to them.

This is a how programs permanently save data that they need to use
later. If you don't save the data to disk, then it all vanishes once the
program exits.

The process is similar to reading, except when we open the file, we need
to specify that we want to _write_. (If we don't tell `open()`
otherwise, it assumes we're opening for reading.)

> **WARNING**: if you open an existing file for writing, the contents of
> that file are instantly lost!

Let's open a file and write some data to it using the `write()` method.

``` {.py}
with open("newfile.txt", "w") as f:
    f.write("Hello, world!\n")
```

There we go! If you run this, then have a look, you'll see a file called
`newfile.txt` that has the magic words in it.

Now you have the power to save data to disk and read it back again!

