<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**
-->

# Reading Files

**WIP**

## Objective

* Understand what a file is
* Be able to open and close a file
* Be able to read and write from files

## Project {#file1-proj-spec}

Write a _line editor_.

Back in the day, before terminals were very capable and before we had
nice editors and IDEs like we do today, people used line editors. These
were bare-bones file editors that used simple commands to edit files.

For example:

```
$ python lineedit.py foo.txt
> l 1
1: This is some text that was already in the file.
> a 1
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

1. `l`ist the file starting from the given line.
2. `a`ppend multiple lines of text after the given line (until the user
   types `.` on its own line).
3. `l`ist the file from line 1.
4. `e`dit line 3.
5. `l`ist the file from line 1.
6. `d`elete line 2.
7. `l`ist the file from line 1.
8. `w`rite the file to disk.
9. `q`uit.

The commands are:

* `l`ist: list 10 lines (or up through the last line if there are fewer
  than 10 lines remaining) starting from the line the user specifies. If
  the user specifies a number less than 1, assume they entered 1.

* `a`ppend: append multiple lines after the line the user specified.
  Read lines one at a time, storing them in turn, until the user enters
  a sole period ("`.`") on a blank line.

* `d`elete: Works like `l`ist, except deletes the line.

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

## Reading Data a Line at a Time {#file1-line-at-a-time}

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

Problem-solving step: **Understanding the Problem**.

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


## Chapter Project

If you need to, [review the specification at the top of the
chapter](#file1-proj-spec).

This project is a bit bigger than the others, eh? I mean, writing an
entire editor is kinda biting off a lot, isn't it?

Sure! Yeah, it's a lot. But we can do it using the problem solving
framework just like always.

Something else a little different here is that I'm not going to include
line numbers in the listings. You'll have to work out the proper place
to put the code based on my descriptions and what makes sense. With
practice, it should get clearer how things piece together.

Let's start!

Problem-solving step: **Understanding the Problem**.

Review the spec from earlier if you have to, but the basic chunks of
this program are:

* Parse the command line to get the filename
* Read a file
* Write a file
* Read user commands as input
* List the file on the screen
* Append lines to the file
* Edit existing lines
* Delete lines

So first, make sure we know what all those do.

Then we'll attack.

Problem-solving step: **Devising a Plan**

We're going to do something a little different this time. We're going to
make an overarching plan, and then jump back and forth between Planning
and Carrying Out the subplans the larger plan is comprised of.

This is little more like how software dev actually works. You have a
general idea of where you're going, and you work out the details as you
get to them.

> This is a bit of a double-edged sword, and it takes practice and
> experience to get it right. You don't want to overplan, because you're
> undoubtedly going to have to change things and you don't want to waste
> your time. And you don't want to underplan, because then hidden
> gotchas might... get you later. You want to plan _just the right
> amount_. Whatever that is.
>
> In reality, devs consistently underplan. And they still make it work
> somehow, like _MAGIC_.
>
> And by "_MAGIC_", I mean tons of sweat, tears, and off-color language.

Being able to do this is a really, really important skill to practice.
This is where software development _really_ happens. The rest of coding
is just writing things down.

So let's do the rough overall, based on the outline, above in
Understanding The Problem.

* First we'll get the filename from the command line.
* Then we'll read the file.
* Then we'll loop to get input for whatever it is the user wants to do
  (append, list, edit, write, etc.)
* For whatever the user enters, we'll do that thing.
* When the user says `q` to quit, we'll quit.

That's a pretty loose plan. I mean, "We'll do that thing," isn't exactly
well-fleshed-out. But we know it's possible to do them, and we can work
on those individual command components one at a time (since none of them
are really dependent on one another).

Looks like some of those we can work on right away.

Problem-solving step: **Devising a Plan**

Let's start simple. Simplifying the problem is always a good way to get
bits and pieces done. Also, getting a minimum working piece going as
soon as possible can help direct our efforts and keep motivation up. Get
a core piece in place, and then keep adding on.

What's a simple version of the program?

Well, we could start by looking at the command line to see if there's a
filename there or not, and storing it if there is.

Remember the user has the option to run the program without specifying a
filename (since maybe they're creating a new file).

So we want to check the command line args in `sys.argv`. If the user
specified a filename, we'll store it. If they didn't, we'll store `None`
to indicate that case. If they specify more than one argument, we'll
print out a usage message.

Great! Let's go!

Problem-solving step: **Carrying Out the Plan**

``` {.py}
import sys

# Parse the command line

if len(sys.argv) == 2:
    filename = sys.argv[1]

elif len(sys.argv) == 1:
    # We'll use this as a sentinel value later if we need to prompt for
    # a filename when writing the file.
    filename = None

else:
    print("usage: lineedit.py [filename]", file=sys.stderr)
    sys.exit(1)

# Let's just print it here to make sure it's working
print(filename)
```

That last line is only there temporarily. This lets us test things out.

```
$ python lineedit.py
None

$ python lineedit.py test
test

$ python lineedit.py test something
usage: lineedit.py [filename]
```

Perfect. What's next?

Problem-solving step: **Devising a Plan**

Looks like the next reasonable step is to read the file into memory so
that we can manipulate it later.

So a couple questions:

* How do we read a file?
* What do we store it in?

As for the first, hopefully you've been reading this chapter and know
about [how to open a file for reading and read individual lines from
it](#file1-line-at-a-time).

But how to keep all those lines?

Think about all the data structures we've talked about so far... lists,
dicts, objects... What is the file the most like?

Go ahead and give it some thought before I spoil it in the next couple
sentences.

You might argue that each line is like an object. And it is. It wouldn't
be wrong to have a class that represents a line. But somehow you still
need to store a list of lines.

Gah, what a giveaway!

Yeah, a list seems like a good idea. In a way, a text file is simply a
list of lines.

So let's read the file a line at a time, storing each into a list as we
go.

This seems like a self-contained piece of code, so I'm going to go ahead
and write a function that accepts a filename as an argument, and then
returns a list of all the lines in that file.

* Make an empty list
* Open the file
* For each line of the file, append it to the list
* Return the list

Problem-solving step: **Carrying Out the Plan**

``` {.py}
def read_file(filename):
    """Read a file from disk"""
    lines = []

    with open(filename) as f:
        for line in f:
            lines.append(line)

    return lines

if filename is not None:
    lines = read_file(filename)
else:
    lines = []

# Print it out just to make sure it works right
print(lines)
```

Now if we run that, and specify an input filename, it should print out a
list with all the lines in that file.

Of course, we need a sample input file. You can make one in VS
Code---just edit a new file called `lines.txt` and put whatever you want
in it. (About five lines is good for testing.) If you don't want to
bother, there's a file [flx[`lines.txt` in the examples
directory|lines.txt]].

Running it, we get our list, just like we wanted!

```
$ python lineedit.py lines.txt 
['This is line 1\n', 'This is line 2\n', 'This is line 3\n',
'This is line 4\n', 'This is line 5']

$ python lineedit.py
[]
```

Take a moment to digest what we did there: we made a _copy_ of the data
that was on disk and stored that copy in memory.

What's next in the big overall plan? Looks like it might be time for a
user input loop.

Problem-solving step: **Devising a Plan**

This is like so many other input loops we've done so far:

* Print a prompt
* Parse the input
* Run the command
* Stop looping when the user says to quit

Problem-solving step: **Carrying Out the Plan**

Your standard input loop. All it does is let you type `q`:

``` {.py}
# Main loop

done = False

while not done:
    command = input("> ").strip()

    if command[0] == 'q':
        done = True
```

If you hit `RETURN` it pukes right away because `command[0]` isn't a
thing if the string is empty.

A common thing to do here is just print another prompt if the user
enters a blank line. We can add this after the `input()` line to do
that:

``` {.py}
    # If the user entered a blank line, just give them another prompt
    if command == '':
        continue
```

And finally, let's add some output as an `else` to tell the user if they
input something we didn't recognize:

``` {.py}
    else:
        print("unknown command")
```

OK! Now if we run it, we should be able to handle blank lines, unknown
commands, and `q` for quit.

```
$ python lineedit.py lines.txt 
> x
unknown command
>                       [ user hit RETURN a few times here ]
> 
>
> q
$
```

Not much of an editor so far, but Facebook wasn't built in a day. We're
just slowly getting the pieces in place.

What's a good piece to do next? Lots of options, because now we're to
the point of implementing the handlers for the various commands (besides
the one for quitting, which we just did).

Personally, if we have things that display data and things that modify
data, I prefer to do the ones that display the data first. They're less
likely to mess things up (since we're not modifying data), and if you
can't display the data correctly, your odds of modifying it correctly
are low, indeed.

So let's hit up that "list" command that will show us lines from the
file.

Problem-solving step: **Devising a Plan**

The list command takes a single argument representing the line number to
start listing from. And then it should list for 10 lines.

Since we have all the lines in a list already, this isn't too entirely
horrible. We just have to:

* Parse the starting position as entered by the user.
* If they entered a number less than 1, assume they meant 1.
* Start looping from that number, printing out 10 lines.
* If we hit the last line, stop printing.

Since we have all these different kinds of functionality, let's put them
in individual functions to keep the code well organized.

We'll make a `handle_list()` function that is called when the user asks
to list the file. It'll take a couple arguments: the arguments the user
typed after a command, as well as the list of lines we're going to
manipulate.

Problem-solving step: **Carrying Out the Plan**

Firstly, let's check and see if the user wants to list lines by checking
to see if the first letter of the command is `l`. If it is, then _it's
on_.

But there's an argument after the `l`, right? The user has to specify
which line to start listing from. And we have to get that into our
`handle_list()` function somehow.

So let's do two things. Let's parse those arguments, if any, out of the
overall command. We'll use `split()` to break the command apart on
spaces, and then we'll use a slice from `[1:]` (that is, from the second
element to the end) to get all the arguments.

The result will have any arguments following the command in a list, or
an empty list if there were no arguments.

And then we'll pass that to our handler function:

``` {.py}
    # Grab the arguments after the command
    args = command.split(" ")[1:]

    if command[0] == 'q':
        done = True

    # List lines
    elif command[0] == 'l':
        handle_list(args, lines)
```

And let's code up a _stub_^[A function stub is a callable function that
takes all the same arguments and, if necessary, returns a sensible
value. But it doesn't, in fact, do anything of use. It's a good way to
test that your overall call flow is working right. And it gives you a
nice, easy TODO spot to fill out.] of the function to handle it, just to
see if its working:

``` {.py}
def handle_list(args, lines):
    print(f'Handle list: {args}, {lines}')
```

Running, we get this:

```
$ python lineedit.py lines.txt
> l
Handle list: [], ['This is line 1\n', 'This is line 2\n',
'This is line 3\n', 'This is line 4\n', 'This is line 5\n']
> l 99
Handle list: ['99'], ['This is line 1\n', 'This is line 2\n',
'This is line 3\n', 'This is line 4\n', 'This is line 5\n']
```

So you can see that the lines are all coming in right. But, more
importantly, our _argument_ is coming in right.

In the first call, it prints out as `[]` empty.

But on the second, we see `['99']` which is the number we told it to
list.

We just have to extract that number somehow.

But before we do, we'd better test to see if the user entered an
argument at all. It's required for the list command, after all.

Then we'll use the start and end lines to print out everything in
between.

``` {.py}
def handle_list(args, lines):

    if len(args) == 1:
        # Compute start and end lines
        start = int(args[0])
        end = start + 10  # print 10 lines

    else:
        print("usage: l line_num")
        return

    # Print all the lines
    for i in range(start, end):
        # end="" to suppress newlines (since lines already have them)
        print(f'{i}: {lines[i]}', end="")
```

Now, if we run this, we see a problem:

```
$ python lineedit.py lines.txt
> l 1
1: This is line 2
2: This is line 3
3: This is line 4
4: This is line 5
Traceback (most recent call last):
  File "lineedit.py", line 71, in <module>
    handle_list(args, lines)
  File "lineedit.py", line 43, in handle_list
    print(f'{i}: {lines[i]}', end="")
IndexError: list index out of range
```

So clearly things have gone awry. There's that huge error message that's
dominating the accident scene and it's hard to notice anything else
other than the lines of the file being printed at the top.

At least nothing went wrong before that error, right?

...Or _did_ it?

Notice anything weird about those first printed lines? Sure, the numbers
start at `1`, but the first line says `This is line 2`! That sets off
some alarm bells. (Especially since when you opened the file in your
real editor, you see the first line says `This is line 1`.)

Problem-solving step: **Understanding the Problem**.

We have two problems.

1. That `list index out of range` error
2. Our [flw[_off-by-one error_|Off-by-one_error]] that's causing our
   lines to be off by one.

Yes, off-by-one errors are famous enough to have their own Wikipedia
page.

As the name suggests, our computations are one off. But why? How?

This is a really common disagreement between humans and computers. We
humans like to have our lists start at index "1", and computers like
them to start at index "0". It's the age old battle. Even the Romans
started with "I", but that was mainly because Roman numerals didn't have
a character for zero until 725 AD---latecomers!

And in this case, we have a human entering numbers that start indexing
at "1". And we print them out for the human to see starting with index
"1"...

But in Python, the lines are in a list starting from index "0"!

Problem-solving step: **Devising a Plan**

We need to do some math.

* When we want to go from a human (1-based) index to a computer
  (0-based) index, we _subtract_ one from the number. 1 becomes 0.
* When we want to go from a computer (0-based) index to a human
  (1-based) index, we _add_ one from the number. 0 becomes 1.

Since we're using `start` and `end` to index the list, I feel a bit
better having them 0-based because the list is 0-based.

There's a general rule of thumb at play here:

* When a user enters a 1-based number, convert it to 0-based as soon as
  you can for internal use in the program.
* When you have to display a 1-based number, keep it 0-based for as long
  as you can, and only convert it at the last second when you output it.

Keeping these conversions to a minimum and doing them only on input and
output can save you a lot of headaches.

What **not** to do: don't just jump in and start adding `+1`s and `-1`s
all over the place and hoping for the best. That way lies madness,
assuredly. Stop, understand, and plan. And then carry it out.

Problem-solving step: **Carrying Out the Plan**

I'm going to write a little helper function here to convert from 0-based
to 1-based since I think we're going to be using this all over the
place. And it helps clarify the code a bit; instead of having a bunch of
`+1`s and `-1`s all over, you have a function name that has some meaning
to future readers.

``` {.py}
def one_to_zero(n):
    """Convert a number from a 1-based index to a 0-based index."""
    return n - 1
```

And now we can make use of that. Let's make `start` 0-based and try it
out.

``` {.py}
        start = one_to_zero(int(args[0]))
```

Now running it gives:

```
$ python lineedit.py lines.txt
> l 1 
0: This is line 1
1: This is line 2
2: This is line 3
3: This is line 4
4: This is line 5
Traceback (most recent call last):
  File "lineedit.py", line 76, in <module>
    handle_list(args, lines)
  File "lineedit.py", line 48, in handle_list
    print(f'{i}: {lines[i]}', end="")
IndexError: list index out of range
```

Same pukey error, but let's look at the lines before then. The good news
is we're getting all the lines printed. The bad news is that line number
on the left is in computer 0-based land, and we need it in human 1-based
land. Let's add another helper function:

``` {.py}
def zero_to_one(n):
    """Convert a number from a 0-based index to a 1-based index."""
    return n + 1
```

And then let's call that in our print output line:

``` {.py}
        print(f'{zero_to_one(i)}: {lines[i]}', end="")
```

Now a run gives:

```
$ python lineedit.py lines.txt
> l 1
1: This is line 1
2: This is line 2
3: This is line 3
4: This is line 4
5: This is line 5
Traceback (most recent call last):
  File "lineedit.py", line 80, in <module>
    handle_list(args, lines)
  File "lineedit.py", line 52, in handle_list
    print(f'{zero_to_one(i)}: {lines[i]}', end="")
IndexError: list index out of range
```

Bam! That's what we want. All lines printed with correct line numbers.

Now, what about that error? It's telling us the list index is out of
range, which isn't too surprising since it's going off the end of the
file.

Before our `for`-loop, let's just add some code that makes sure the
`start` and `end` are sane. (Remember we've decided that they are
0-based indexes.)

``` {.py}
    # Make sure start isn't before the beginning of the list
    if start < 0:
        start = 0

    # Make sure end isn't past the end of the list
    if end > len(lines):
        end = len(lines)
```

And then you can run the `for`-loop after that with impunity!

```
$ python lineedit.py lines.txt
> l 1
1: This is line 1
2: This is line 2
3: This is line 3
4: This is line 4
5: This is line 5
> l 3
3: This is line 3
4: This is line 4
5: This is line 5
> 
```

Perfection! That's the list functionality complete!

Things only tend to get easier from here on out. The first part of the
implementation is the worst, but now we just have variants on a theme:

1. Check for the proper command on input
2. Pass the args to a handler function for that command
3. Build out the handler function
4. Repeat

What's the next simplest thing to work on? How about "delete a line"?

Problem-solving step: **Understanding the Problem**.

So we want to delete a single line. This is as easy as removing an
element from the list containing all the lines.

We just need to know the element number to remove.

Of course, the user enters it after the `d` command, so we can grab it
from there.

But remember: what the user enters is 1-based! We have to convert it to
0-based before we use the number to delete a line... otherwise we'll
delete the wrong line.

Problem-solving step: **Devising a Plan**

So we should be able to:

* Add a handler to the main input loop
* In the delete handler, get the line to delete
* Convert it to 0-based
* Delete that line from the list of lines

A little digging in the help reveals that the `pop()` method removes an
element from a list at a given index:

``` {.py}
pop(self, index=-1, /)

    Remove and return item at index (default last).
```

Problem-solving step: **Carrying Out the Plan**

To our main input loop, let's go ahead and add a call to the handler if
the user requests a deletion:

``` {.py}
    # Delete a line
    elif command[0] == 'd':
        handle_delete(args, lines)
```

And now let's write the delete handler. This is going to be similar to
the line listing handler at first: we have to get the line number the
user entered, and convert it to 0-based.

And then make sure it's in range.

And then delete that line with the `pop()` method.

``` {.py}
def handle_delete(args, lines):
    """Delete a line in the file."""

    if len(args) == 1:
        # Get the line number to delete
        line_num = one_to_zero(int(args[0]))

    else:
        print("usage: d line_num]")
        return

    # Make sure we're in range
    if line_num < 0 or line_num >= len(lines):
        print("no such line")
        return

    # Delete the line
    lines.pop(line_num)
```

And that's all there is to it. Let's try it:

```
> l 1
1: This is line 1
2: This is line 2
3: This is line 3
4: This is line 4
5: This is line 5
> d 3
> l 1
1: This is line 1
2: This is line 2
3: This is line 4
4: This is line 5
> d 0
no such line
> d 5
no such line
```

Looks good!

What's next easiest? Probably the "edit" functionality.

Problem-solving step: **Understanding the Problem**

When we edit a single line, we want to replace the element in the lines
list completely with a new element that we input from the keyboard.

The only line is thrown away.

For this, the user enters `e` for "edit", followed by a line number.

Problem-solving step: **Devising a Plan**

Let's do the same as with delete, except that instead of using `pop()`
to remove a line, we'll just use `input()` to get another one, and store
it directly in the list.

Problem-solving step: **Carrying Out the Plan**

Firstly, let's add that command handler to the main loop:

``` {.py}
    # Edit a line
    elif command[0] == 'e':
        handle_edit(args, lines)
```

Secondly, let's implement the edit handler. Same code and rationale
until the last line:

``` {.py}
def handle_edit(args, lines):
    """Edit a line in the file."""

    if len(args) == 1:
        # Get the line number to edit
        line_num = one_to_zero(int(args[0]))
    else:
        print("usage: e line_num")
        return

    # Make sure we're in range
    if line_num < 0 or line_num >= len(lines):
        print("no such line")
        return

    # Edit the line
    lines[line_num] = input()
```

Notice how we just replace the named line in the list with whatever line
is returned by `input()`.

Let's try it!

```
> l 1
1: This is line 1
2: This is line 2
3: This is line 3
4: This is line 4
5: This is line 5
> e 2
NEW LINE 2!
> l 1
1: This is line 1
2: NEW LINE 2!3: This is line 3
4: This is line 4
5: This is line 5
> 
```

Wait a second! Lines 2 and 3 are all bunched up after I edited it! That
can't be right.

Problem-solving step: **Understanding the Problem**

This all ties back to the newlines we keep at the end of lines in the
list.

Remember that we're storing each line with the newline attached to the
end.

_But `input()` strips the newline off!_ Not what we were after.

Problem-solving step: **Devising a Plan**

So we have to add the newline to the end of the, er, new line that we
just entered. We'll just tack it on with the `+` string concatenation
operator.

Problem-solving step: **Carrying Out the Plan**

Modify the last line of the `handle_edit()` function to add the newline:

``` {.py}
    # Edit the line, adding a newline to the end (since input() strips
    # it off).
    lines[line_num] = input()# + '\n'
```

And done with that one!

What's the next easiest thing to code up? Well, looks like there's only
one more editing command: "append".

Problem-solving step: **Understanding the Problem**

This one's a little different. It looks like we go ahead and read the
line to append just like with any other command. But then we go into a
weird mode where we repeatedly enter lines until the user enters a
single period on a line by itself.

And each of those lines are appended in turn.

If the user says to append after line 0, the lines should be inserted at
the top of the file.

Problem-solving step: **Devising a Plan**

So let's go ahead and do the usual command line parsing to see which
line we want to insert after.

And then let's loop until the user enters a single period.

Inside the loop we'll read a line and append it into the list in the
right place.

Looking at the documentation, there is an `append()` method for lists,
but it only appends onto the end of the list.

We want ours to be able to do that, but also to be able to put those
lines in the middle, or at the top.

Let's keep looking down the documentation.

There's `insert()` to put an object _before_ an index. This seems to
work for the beginning and the middle, but what about appending to the
end? Do we have to use the `append()` method in that special case?

The docs aren't entirely clear on the matter. Let's bring up the
[REPL](#repl) and try some tests.

I'll make a list and then try to `insert()` values in various places.

First, let's try inserting before element 0, which should insert at the
beginning:

``` {.py}
>>> a = [11, 22, 33]
>>> a.insert(0, 99)
>>> a
[99, 11, 22, 33]
```

Great! The 99 went in first, just like I wanted.

Let's insert another number before index 2:

``` {.py}
>>> a.insert(2, 999)
>>> a
[99, 11, 999, 22, 33]
```

That worked, too.

Now, the list only has up to element index 4... but let's go out on a
limb and try inserting before index 5 (which doesn't exist) and see if
that appends on the end:

``` {.py}
>>> a.insert(5, 9999)
>>> a
[99, 11, 999, 22, 33, 9999]
```

Yes! It worked! We don't have to special case a call to `append()`.

It is a little weird, but if you put _any_ index past the last one in
for append, it'll put the value at the end of the list.

If we make a small list and try to insert the value 3490 at index 99, it
just puts it at the end:

``` {.py}
>>> a = [1, 2, 3]
>>> a.insert(99, 3490)
>>> a
[1, 2, 3, 3490]
```

This kind of experimentation to see what works and what doesn't is
really common, and is a great way to explore and learn how the system
works.

Ok, so we:

* Get the line number to append after. Remember that we want this to be
  zero-based, so we'll subtract 1 from whatever they enter. If they
  enter "2", that means that we want to insert _after_ index 1.
* But since the `insert()` method inserts _before_ a line, not after,
  we'd better add one to the line index so that we append after that
  line.
* Then we loop until the user enters a period, inputting a line and
  inserting it into the list in the right place.

Now, you might wonder why bother subtracting one just so we could add
one right after?

And you're right---it does nothing. We don't have to do that.

But there's an argument to be made that it's clearer to a future reader
of the code. We clearly subtract one to get to a 0-based indexing method
as soon as possible. And we add one to get `insert()` to insert after a
line instead of before it. Two different reasons to do the arithmetic,
clearly spelled out. If we were to just leave them both off, that
information wouldn't be obvious to the next developer reading the code.

Problem-solving step: **Carrying Out the Plan**

First, let's do our standard parsing of the command argument:

``` {.py}
def handle_append(args, lines):
    """Append a line in the file."""

    if len(args) == 1:
        # Get the line number to append at. +1 because we want to line_num
        # adding lines one _after_ the specified line.
        line_num = one_to_zero(int(args[0]))

    else:
        print("usage: a line_num")
        return
```

Then, continuing down the function, do our adding one:

``` {.py}
    # +1 because we want to line_num adding lines one _after_ the
    # specified line.
    line_num += 1
```

Then, continuing again, let's put in our loop to read lines until the
user enters a period, and insert them into the correct location in the
list.

``` {.py}
    done = False

    # We're going to loop until the user enters a single `.` on a line
    while not done:

        # Read a line of input
        line = input()

        # Check if we're done
        if line == '.':
            done = True
            continue  # Jump back to the `while`

        # Otherwise, insert the line, adding a newline to the end (since
        # input() strips it off).
        lines.insert(line_num, line + '\n')

        # And now on to the next line
        line_num += 1
```

All right, let's test it. Let's insert lines at the beginning:

```
> l 1
1: This is line 1
2: This is line 2
3: This is line 3
4: This is line 4
5: This is line 5
> a 0
NEW line 1
NEW line 2
.
> l 1
1: NEW line 1
2: NEW line 2
3: This is line 1
4: This is line 2
5: This is line 3
6: This is line 4
7: This is line 5
```

Works!

Let's insert lines in the middle:

```
> a 4 
NEW line in the middle
.
> l 1
1: NEW line 1
2: NEW line 2
3: This is line 1
4: This is line 2
5: NEW line in the middle
6: This is line 3
7: This is line 4
8: This is line 5
```

Works!

Let's insert some lines at the end:

```
> a 8
NEW end line 1
NEW end line 2
.
> l 1
1: NEW line 1
2: NEW line 2
3: This is line 1
4: This is line 2
5: NEW line in the middle
6: This is line 3
7: This is line 4
8: This is line 5
9: NEW end line 1
10: NEW end line 2
```

Also works! _Woot!_

Although it's not automated, this is good _test coverage_. We looked
at the common case (insert in the middle), but we also looked at the
_edge cases_ (insert at the beginning and end) just to make sure those
worked properly. When testing, always think about which cases _aren't_
common and test those explicitly.

Now there's but one thing remaining: saving the file to disk with the
"w" (write) command.

Problem-solving step: **Understanding the Problem**

We already wrote some code back in the day to read a file a line at a
time and store the results in a list.

This time, we want to do the opposite. Go through our list and write the
file a line at a time until we're done.

Problem-solving step: **Devising a Plan**

Compared to the append command, this is cake.

* Open the file for writing
* Loop through all the lines
* Write each line to the file

Also:

* Hook up the "w" command in the main input loop.

And:

* Parse the argument from the "w" command to get the filename

Since "write a bunch of lines to disk" is a good self-contained
operation, I plan to write function that does just that and nothing
more. I'll write a different function to get called when a write is
requested which will make sure the args are correct and so on. Keep it
modular!

Problem-solving step: **Carrying Out the Plan**

First, let's add a function to write the file to disk. As arguments,
it'll take the list of lines to write and a filename to write it to.

When we open the file, we'll pass the `"w"` argument to it to indicate
that we're writing this file.

Note that as soon as you open a file for writing, it erases that file if
it exists. But this should be OK in this case since we're about to write
it again.

And since every line already has a newline at the end, we don't have to
add one when we write it to disk.

``` {.py}
def write_file(lines, filename):
    """Write a file to disk"""
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
```

Now let's write the handler for the command. This will check if the arg
was specified and print an error if not. And then write the file.

``` {.py}
def handle_write(args, lines):
    """Handle the write command"""

    if len(args) == 1:
        filename = args[0]
    else:
        print("usage: w filename")
        return

    write_file(lines, filename)
```

Lastly, we need to add a handler to the main command loop so that when
we type "w", it saves the file:

``` {.py}
    # Write (save) the file
    elif command[0] == 'w':
        handle_write(args, lines, filename)
```

And that's that!

Problem-solving step: **Looking Back**

There are a lot of things we can do to improve the code here.

* Add the option for the delete command to specify and ending as well as
  a starting line to erase a block of lines at once.

* Make it so that if the user specifies a filename on the command line
  and does _not_ specify one after the write command, it writes to the
  same file specified on the command line.

* Add an insert command that works like append, except it puts the new
  material _before_ the line specified. How can you do this with a
  minimal addition of code? After all, append and insert are _very_
  similar.

What's crazy is that you can use this to write Python programs. Let's do
one!

```
$ python lineedit.py
> a 0
print("Hello, world!")
print("I wrote this with my own editor!")
.
> l 1
1: print("Hello, world!")
2: print("I wrote this with my own editor!")
> w my_hello.py
> q
$ python3 my_hello.py 
Hello, world!
I wrote this with my own editor!
$ 
```

Well, you can probably tell that's not quite as easy as using VS Code
(or any other editor, for that matter). But, believe it or not, line
editors were _the_ way to enter programs for a long time.

Be thankful for standing on the shoulders of giants!

([flx[Solution|lineedit.py]].)


## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

Use any knowledge you have to solve these, not only what you learned in
this chapter.

1. You've been misbehaving in class and the teacher sentences you to
   write 500 lines as punishment. Shrewdly, you ask if you can type the
   lines, and the teacher agrees^[True story. This was back when I was
   in the 7th grade and computers were a bit of a novelty. We had a
   daisywheel printer at home which was fairly indistinguishable from a
   typewriter. In real life, though, I didn't write a program to
   generate the lines. I told dad about the task, and he rolled his eyes
   and showed me how to copy and paste in WordStar.].

   The program should accept command line arguments of the filename to
   output to and the number of lines. All command line arguments after
   that are the punishment line itself that should be repeated that many
   times in the output file.

   For example:

   ```
   python writelines.py outfile.txt 500 I will not talk in class.
   ```

   would generate a file `outfile.txt` with the line
   
   ```
   I will not talk in class.
   ```

   repeated 500 times.

   **WARNING**: Apostrophes and quotes (and other punctuation) often
   have special meaning to the shell. Avoid any characters other than
   periods or you might get strange results. If weird things happen, hit
   `CTRL-c` to get out of it.

   ([flx[Solution|ex_writelines.py]].)


2. Write a program to read comma-separated values (CSV) files.

   A CSV file is one that has a bunch of values separated by commas, one
   record per row.

   Here's [flx[the file we want to read|games.csv]]. Look through it and
   see how all the information for a particular record is in each row:

   ``` {.csv}
   Title,Release Year,Studio,Publisher
   Minecraft,2011,Mojang,Microsoft Studios
   M.U.L.E.,1983,Ozark Softscape,Activision
   X-Men The Official Game,2006,Z-AXIS,Activision
   Populous,1989,Bullfrog Productions,Electronic Arts
   DOOM,1993,id Software,id Software
   Lemmings,1991,DMA Design,Psygnosis
   ```

   Your goal is to read the file and store each record in an object.
   (Make a class that defines the same fields you have in the CSV file
   to instantiate the objects from.)

   Then print out the data, like so:

   ```
   M.U.L.E.                  1983   Ozark Softscape        Activision            
   Populous                  1989   Bullfrog Productions   Electronic Arts       
   Lemmings                  1991   DMA Design             Psygnosis             
   DOOM                      1993   id Software            id Software           
   X-Men The Official Game   2006   Z-AXIS                 Activision            
   Minecraft                 2011   Mojang                 Microsoft Studios
   ```

   The printout, above, is shown in sorted-by-year order. That's a
   stretch goal if you want to take it on. (Hint: check out the `key`
   keyword argument to the `.sort()` method. Also, the solution code
   talks about it in detail.)

   Also, incidentally, [flw[M.U.L.E.|M.U.L.E.]] is one of the greatest
   games ever written. Despite it being over 25 years old, _PC World_
   magazine rated it the 5th-greatest game of all time in 2009. If you
   haven't played it, grab an Atari 800 emulator, four gamepads, and
   four friends, and have some fun. (Or play solo against the computer.)

   > Now, a quick word of warning: this exercise assumes you're going to
   > implement the logic for parsing this file yourself. But in real
   > life, in Python, you'd never do this. Python has built-in
   > functionality to parse CSV files, and it's far more robust and
   > correct than what we're doing here. We're just reinventing the
   > wheel in this case as a programming exercise.

   Notice that the first line of the CSV file is a _header_. It
   describes what the columns are, but isn't actual data. You'll have to
   skip this line when you're reading the file. (Hint: call the `next()`
   function on the file iterator returned by `open()` to get the next
   line one time at the beginning.)

   ([flx[Solution|ex_simplecsv.py]].)

* Modify your multiplication table generator to save the table to disk
* Write a program to count the number of words in a file
* Write a program that sorts each line of a file in alphabetical order
