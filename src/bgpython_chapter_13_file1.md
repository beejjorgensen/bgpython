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

TODO

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

## TODO

* with
* reading a line at a time
* writing
