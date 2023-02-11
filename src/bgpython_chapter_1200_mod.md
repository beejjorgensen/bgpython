<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**.
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**.
-->

# Importing Modules

## Objective

* Learn what a module is
* How to find modules to use
* How to import modules

## Chapter Project Specification {#mod-proj-spec}

Open a ZIP archive and print out a directory of the files that are in
there, their size in bytes, and the time they were last modified.

> If you're unfamiliar with the ZIP format, it's a way to take multiple
> files and compress them into a single file, called a _ZIP archive_.
> The _table of contents_ shows what files exist within the ZIP file.
> They can be recovered later by _extracting_ them, but we're not going
> to do that for this project.

An [flx[example ZIP file can be found in the examples
directory|example.zip]].

Output should be:

```
File Name                         Modified             Size
hello.txt                  2020-02-09 15:12:20            6
world.txt                  2020-02-09 15:12:24            7
```

(Spacing in the above example was changed to fit the margins---you don't
have to match spacing exactly.)

Keep this project in mind as we go through this chapter's material.

## What and Why of Modules

Problem-solving step: **Understanding the Problem**.

Modules are pieces of self-contained code that you can _import_ into
your code and use. Think of them as prefabricated building blocks that
you can put together in your project to accomplish tasks without needing
to write out the details yourself.

This is actually a really powerful concept that you have at your
disposal. Tons of code have already been written, and you can just use it!

Do you want to compute anything to do with date and time? Python has a
module for that.

Do you want to draw graphics on the screen? Python has a module for
that.

Do you want to generate animated GIFs from a sequence of stills?
There's a module for that.

Do you want to download an image from a URL and save it to disk? There
are modules for that.

There are [fl[_tons_ of modules built-in to
Python_|https://docs.python.org/3/library/index.html]]. Give the list a
skim so you know what's there, but you don't need to drill down at all
unless you're dying of curiosity over a particular module.

Are there are [fl[_zillions_ of third-party modules|https://pypi.org/]]
you can use, as well.

You can import as many modules as you want into an individual project.

## Using a Module

Problem-solving step: **Understanding the Problem**.

You declare your intent to use a module with the `import` keyword. We're
going to do an example with the built-in [fl[`sys`
module|https://docs.python.org/3/library/sys.html]], which contains all
kinds of useful information about the system.

Let's see what platform Python thinks we're running.

But first, some syntax.

When using a function or variable inside a module, you use the dot
operator to get the variable, similar to how you get attributes from
objects. In fact, very similar. When you `import` a module, Python gives
you an object by that name with functions and data attached to it as
attributes.

Step one is to `import` the module. Then you can access the members of
that module.

For example, if we:

``` {.py}
import sys
```

we'll end up with an object called `sys` with attributes that you can
access!

Problem-solving step: **Devising a Plan**

Digging through the documentation for the `sys` module, we find there's
something called `sys.platform` that looks really promising.

Let's print it!

Problem-solving step: **Carrying Out the Plan**

``` {.py}
import sys    # Gets us access to all the sys goodies

print(sys.platform)
```

What does it output for you?

For me, on Linux or Windows WSL, it prints "`linux`". On Windows, it
prints "`win32`".

Notice there was nothing we had to do ourselves to make this
determination. (Which is good, because it would be a pain to write!)
Fortunately, the `sys` module had everything we needed right there.

## Command Line Arguments

Problem-solving step: **Understanding the Problem**.

I've been hiding something.

In terms of how you run Python programs from the command line.

It turns out you can add things _after_ the Python program name.

Say what?

Let's say you have a program called `foo.py`. You can run it like this,
of course:

```
python foo.py
```

You can also run it like this:

```
python foo.py something another antelopes
```

Those extra words after the program name are called _command line
arguments_.

But _why_ would you do this?

So you can control the behavior of the program from the command line!
When you run it, it's nice to be able to influence behavior this way
instead of having to call `input()` with prompts and everything else.

But _how_ do you get those extra command-line arguments?

Our good friend `sys` module can help us again here.

The variable `sys.argv` is a list that contains the program name
followed by all the command line arguments.

Run this program with a variety of command-line arguments and see what
it outputs:

``` {.py}
import sys

print(sys.argv)
```

Example output:

```
$ python foo.py
['foo.py']
```
```
$ python foo.py aa bb cc
['foo.py', 'aa', 'bb', 'cc']
```

So at runtime, we can look in `sys.argv` and make decisions about what
we want to do!

Let's put it to use in the next section.

## Printing Calendars

Print a calendar for any month and year!

Problem-solving step: **Understanding the Problem**.

Your first thought should have been something like, "Holy cow,
Beej---how am I supposed to figure all that out? Was November 12, 1955, a
Friday or a Saturday? I don't know!"

Luckily, we don't have to know! There's a module, `calendar`, that we
can use to do all the dirty work for us.

If you pop to [fl[the
instructions|https://docs.python.org/3/library/calendar.html]], you'll
see pages and pages of material. It's intimidatingly impenetrable.

Reading docs is one of the things you'll get better at with practice. At
first, it's a bit of a slog, but you'll improve.

First of all, start skimming down and looking for anything that has to
do with text calendars. If it doesn't seem to have anything to do with
that, keep skimming.

I'll wait. Go for it.

Spoilers coming! Really go scan them and find it yourself! Practice
makes perfect!

Problem-solving step: **Devising a Plan**

OK---so hopefully you got about halfway down the page and found the
`TextCalendar` class. It says:

> This class can be used to generate plain text calendars.

That sounds promising. In fact, just below that, it mentions there's a
`prmonth()` method on the class that you can use to print a calendar
for a given month and year.

Perfect!

Problem-solving step: **Carrying Out the Plan**

We can code it up like this:

``` {.py}
import calendar

tc = calendar.TextCalendar()   # Make a new TextCalendar object

tc.prmonth(1970, 1)  # Print January 1970
```

and this will present us with a nice text calendar that looks like this:

```
    January 1970
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
```

Problem-solving step: **Looking Back**.

We found what we wanted halfway down the documentation, so we're good
right?

Well, it might be worth skimming the rest of the documentation just to
see what else the calendar module can do.

And, in fact, if we look down farther, the docs say:

> For simple text calendars this module provides the following
> functions.

And one of those functions is `prmonth()`. We can just call it directly
without making an intermediate object!

``` {.py}
import calendar

calendar.prmonth(1970, 1)
```

gets us the same output as before---and it's simpler!

Problem-solving step: **Understanding the Problem**.

Let's mod this. Right now, it's hardcoded to print out a January, 1970
calendar. Let's change it so that you could run it from the command line
and pass in the arguments you need, like this:

```
python cal.py 1970 1
```

or

```
python cal.py 1955 11
```

to print out the January, 1970 or November, 1955 calendars, respectively.

That makes it more flexible---we get all kinds of new behavior without
changing the code. Much more usable.

Problem-solving step: **Devising a Plan**

We saw in this section how to print a calendar, and we saw in the
previous section how to get command-line arguments into a list.

Let's get the year and month from `sys.argv` and pass them into
`calendar.prmonth()`.

Problem-solving step: **Carrying Out the Plan**

Let's do exactly that:

``` {.py}
import sys
import calendar

year = sys.argv[1]
month = sys.argv[2]

calendar.prmonth(year, month)
```

When we run it with:

```
python cal.py 1970 1
```

though, something bad happens:

```
Traceback (most recent call last):
  File "cal.py", line 7, in <module>
    calendar.prmonth(year, month)
  File "/usr/lib/python3.8/calendar.py", line 350, in prmonth
    print(self.formatmonth(theyear, themonth, w, l), end='')
  File "/usr/lib/python3.8/calendar.py", line 358, in formatmonth
    s = self.formatmonthname(theyear, themonth, 7 * (w + 1) - 1)
  File "/usr/lib/python3.8/calendar.py", line 341, in formatmonthname
    s = month_name[themonth]
  File "/usr/lib/python3.8/calendar.py", line 59, in __getitem__
    funcs = self._months[i]
TypeError: list indices must be integers or slices, not str
```

Yikes!

Let's take this error apart and see if we can tell what's up. It's not
really being that forthcoming, is it?

Start at the top. It tells you what file the error is in on the first
line: `cal.py` on line 7. And it shows us the line below that... it's
where we're calling `calendar.prmonth()`.

But that looks fine, right?

Going farther down, it's showing us the _call stack_, that is, the path
of function calls that culminated in the error. And those are in the
`calendar.py` file, which is the `calendar` module.

We didn't even write that code! How dare there be an error in it!

Well, it's not an error---it's the module telling us, in a roundabout
way, we're not using it right.

Finally, at the bottom, we see the error itself: `TypeError`. And the
description:

```
TypeError: list indices must be integers or slices, not str
```

We don't have any lists in our code, so what's it even talking about
lists for? Well, who knows how the stuff is implemented in the library,
but scan that error message and see if there's anything in there that
hints toward what we have to do.

It says "must be integers or slices, not str". Hmmm.

When we called it with

``` {.py}
calendar.prmonth(1970, 1)
```

it was fine, but now it's not? Wait---when we called it that way, we
passed integers in... but now we're passing in `sys.argv[1]`. Is that an
integer?

There's a built-in function called `type()` we can use. Let's add this
code:

``` {.py}
import sys
import calendar

year = sys.argv[1]
month = sys.argv[2]

print(type(year))    # <-- Add this
print(type(month))   # <-- Add this

calendar.prmonth(year, month)
```

Running it again, we get the same error, but before that, we see some
output:

```
<class 'str'>
<class 'str'>
```

That's telling us `sys.argv[1]` and `sys.argv[2]` are strings! And we
were passing ints before. Let's convert those to ints before we pass
them in. The error message did say we needed ints, not strings.

``` {.py}
import sys
import calendar

year = int(sys.argv[1])
month = int(sys.argv[2])

calendar.prmonth(year, month)
```

And now when we run it:

```
$ python cal.py 2038 1
    January 2038
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

Whee!

Problem-solving step: **Looking Back**.

Not too shabby. What else can we make better?

It's time to think like a villain. What can you do to this program as a
user to break it?

How about passing in a negative year? (Hey, that works!)

What about a negative month?

That crashes with a big ugly stack trace.

We could fix that by checking the values of `month` and making sure the
user-specified 1-12, or print an error otherwise. Something like this:

``` {.py}
if month < 1 or month > 12:
    print("Month must be 1-12!")
    sys.exit()  # call this to stop running the program here!
```

What if the user specifies a year, but no month? Another crash.

We could check the length of `sys.argv` and make sure it was the right
value (namely 3, since it includes the name of the program along with
the year and month). If it wasn't, we could print an error message and
exit.

Here's the complete code with error checking:

``` {.py}
import sys
import calendar

if len(sys.argv) != 3:
    print("usage: cal.py year month")
    sys.exit()  # stop running

year = int(sys.argv[1])
month = int(sys.argv[2])

if month < 1 or month > 12:
    print("Month must be 1-12!")
    sys.exit()  # stop running

calendar.prmonth(year, month)   
```

Ship it!

## Importing Specific Attributes

There's an alternate syntax for `import` that you can use to bring
attributes from a module directly into the global namespace.

What do I mean by that?

Well, the upshot is that if you're tired of typing the module name
followed by a dot to access a particular function or piece of data, you
can bring that in to use directly, instead.

Let's do an example.

The `time` modules have a function called `ctime()` that prints the time
out in a classic format.

``` {.py}
import time

print(time.ctime())  # "Sun Feb  9 13:37:00 2020"
```

But if you're going to call it repeatedly, it might make the code look
worse to have "`time.`" all over the place.

We can do this, instead:

``` {.py}
# Bring in ctime() explicitly:

from time import ctime

print(ctime())  # Look, ma! No "time."!
```

If a module has multiple things you want to import, you can bring them
in with a comma list:

``` {.py}
# import all three!

from time import ctime, localtime, monotonic
```

Or, if you're feeling bold, you can import it all!

``` {.py}
from time import *
```

But I generally recommend against that. It takes time for Python to do
it, and if you only need a few things, pick them explicitly.

Furthermore, a lot of devs rely on the module name being a visual cue
that we're talking about a function in a module, here. If we come across
some code that says:

``` {.py}
print(ctime())
```

Is that a function that the programmer-defined, or is it something that
we `from import`ed from somewhere? By putting the name of the module
first, it helps mitigate that ambiguity:

``` {.py}
print(time.ctime())
```

So in general, I don't use `import from` unless it makes the code
decidedly more readable to do so.

Remember: readable code is high-value code!

## Learning All The Modules

If you check out [fl[the list of
modules|https://docs.python.org/3/library/index.html]] you get with
Python, it looks pretty intimidating. I mean, there's a _lot_ there.

How do you deal with it?

This is one of the toughest parts of learning a new language: learning
the _standard library_ (the bundled modules) that comes with it. Each
language has its own way of doing things, and those ways are legion.

Step one: give up now. You're not going to memorize all this.

The best thing to do is skim it at the level of the contents. Just try to
remember that there exists a module for dealing with times. And a module
for dealing with calendars. And for dealing with network communication.
And so on.

Don't worry about the details. You can always look them up later. But if
you don't know that there even _is_ a module that handles reading and
writing of [flw[CSV|Comma-separated_values]] files, then you won't know
to look it up when you need it.

All devs, even experienced ones, look things up. All the time.

## Chapter Project

If you need to, [review the specification at the top of the
chapter](#mod-proj-spec).

You might be thinking, "This is kind of a big jump, don't you think,
Beej? I mean, we haven't even talked about how to open a file, and here
you want me to somehow gaze magically inside a ZIP file and extract the
contents?"

Well... yes. By "magically", though, I mean something in particular. As
you might have guessed, there's a [fl[module for opening ZIP
files|https://docs.python.org/3/library/zipfile.html]]. We can import
this and make it do the heavy lifting for us!

Easy, right?

Well, not so fast. If you follow the link to the docs, above, you'll
find pages and pages and pages of material with no clear indication of
where to start. (Bring up that URL now, because we're about to go
through it.)

It's nice that the module is there for us to use, but we have to sift
through all this to use it?

Pretty much.

There is a shortcut that you can take. You can Google for "python print
zip archive example", and you'll get some hits. This can be super
powerful, and we do this kind of thing _all the time_ in development,
but for this project try _not_ doing this.

Let's just look at the docs and try to make sense of them, because this
is a skill in itself, and is worth practicing.


Problem-solving step: **Understanding the Problem**.

This one's pretty straightforward. We have a ZIP file from the examples,
and we want to print out the files that are compressed within it.

In fact, this can be done in three lines of Python. Just... what three
lines?

We just have to plan it out.


Problem-solving step: **Devising a Plan**

Here's where we start digging. Start skimming the docs, and take note of
anything that sounds remotely like what you want to do. Ignore anything
you don't understand. We want to get information about the contents of
the ZIP file.

Keep your eyes peeled for example code.

Let's skim!

I want you to come up with a list of functions or data in the docs that
sound promising. As we learned earlier in this chapter, it can pay to
skim the entire document so you don't miss anything.

Go for it.

I'll wait.

I'm about to share my list of candidates, now, so run get yours to see
how it compares.

Spoiler alert!

Here are things that I thought sounded like they might get me my table
of contents for the ZIP file.

Here are the first few I found. As I go, I'm keeping track in my head
about which one sounds the most promising:

``` {.py}
ZipInfo            # Class containing info about a ZIP file member
ZipFile.getinfo()  # Return a ZipInfo object for a file member
ZipFile.infolist() # Return ZipInfo objects for all file members
ZipFile.namelist() # Return list of file members by name
```

Let's keep looking.

``` {.py}
ZipFile.open()     # Access member of the archive
ZipFile.printdir() # Print a table of contents to sys.stdout (!!!!)
```

Now _that_ sounds promising.

> `sys.stdout` is a _file stream_ that represents what we call _standard
> output_. For now, when you hear `stdout` or _standard output_, replace
> it with "the screen".

So `printdir()` prints the table of contents to the screen, which sounds
exactly like what we're after.

But let's keep looking, just to be sure.

``` {.py}
ZipFile.read()     # Read bytes from a member of the archive
ZipFile.filename   # Name of the ZIP file

ZipInfo.filename   # Name of an archive member
ZipInfo.date_time  # Modification time of an archive member
ZipInfo.file_size  # File size of an archive member
```

And that's the end of my skim. How did it compare with your list?

Now... Those last three look interesting. If we could get the `ZipInfo`
object for each item in the archive, we could use those attributes to
print out our directory listing.

But that sounds like it's just going to get us what the `printdir()`
function would do, and `printdir()` looks easier to use.

Maybe we're wrong, but let's pursue `printdir()`, and if it doesn't pan
out, we can go to Plan B and try the `ZipInfo` fields.

So... How do we use it? Let's read the docs again.

> ``` {.py}
> ZipFile.printdir()
> ```
> 
> Print a table of contents for the archive to `sys.stdout`.

So we need a `ZipFile` object that represents the ZIP file
`example.zip`.

That is, we know the ZIP is named `example.zip`, and we need to go from
that to a `ZipFile` object. Once we have the `ZipFile` object for
`example.zip`, we can call `printdir()`.

OK. So how do we do that? Time to get back to skimming docs! How do I
create a `ZipFile` object?

Skim now!

We saw earlier this was the class:

``` {.py}
zipfile.ZipFile
```

And a bit farther down, we have:

> ``` {.py}
> class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED,
>                      allowZip64=True, compresslevel=None, *,
>                      strict_timestamps=True)
> ```
> Open a ZIP file, where `file` can be a path to a file (a string), a
> file-like object or a path-like object.

Recognize that? It's a _constructor_!! That's what we want! We want to
construct a `ZipFile` object from the string `example.zip`, and that's
exactly what this does for us.

Continuing down, I'm not seeing anything else that helps us make a
`ZipFile` object, so let's pursue this plan.

1. Import the ZIP file functionality.
2. Create a `ZipFile` object from `example.zip`.
3. Print the table of contents with `printdir()` on that `ZipFile`
   object.

Let's go!

Problem-solving step: **Carrying Out the Plan**

``` {.py .numberLines}
import zipfile
 
```

Check.

Okay---now we need to do something with that `ZipFile` constructor.
Recall that since it's in the `zipfile` module, we have to refer to it
as `zipfile.ZipFile` when we use it.

But, man, the docs are thick for the constructor. What is all that
stuff?

Remember that any keyword argument with something after an equal sign is
optional. We don't have to pass arguments for `mode`, `compression`, or
any of those.

What we _do_ have to pass in in the `file`, which is the filename to
read. Let's do that, and we'll save the newly-constructed object in the
variable `zf`:

``` {.py .numberLines startFrom="3"}
# Important: make sure example.zip is in the same directory
# as this program!

zf = zipfile.ZipFile('example.zip')
 
```

Great!

And now that we have that object, let's print its directory:

``` {.py .numberLines startFrom="8"}
zf.printdir()
```

And that gives us this output:

```
File Name                         Modified             Size
hello.txt                  2020-02-09 15:12:20            6
world.txt                  2020-02-09 15:12:24            7
```

Yes!

Problem-solving step: **Looking Back**.

What else can we do with this to improve it?

One easy thing to do would be to use `sys.argv` to get the name of the
archive to print out the listing for.

Another thing that you might have noticed in the docs is there is all
kinds of additional info about members of the archive. In addition to
name, time, and size, there's also comments, compression type,
compressed size, [flw[CRC|Cyclic_redundancy_check]], and other things to
print.

By adding up all the uncompressed sizes, the compressed sizes, and then
dividing one by the other, you can get the _compression ratio_---how
much smaller the files got by putting them in the archive.

([flx[Solution|zipdir.py]], [flx[example zipfile|example.zip]].)


## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

Use any knowledge you have to solve these, not only what you learned in
this chapter.

**Always** use the [four problem-solving steps](#problem-solving) to
solve these problems: understand the problem, devise a plan, carry it
out, look back to see what you could have done better.


1. Every process running on your system is represented by a numeric
   _process ID_. When you run a program, it gets a unique process ID
   (PID) that exists until the process exits.

   Write a program to print out its current process ID. Check out the
   [fl[docs for the `os`
   module|https://docs.python.org/3/library/os.html]] for hints. You
   might want to search that page for anything to do with "current
   process ID"... `:)`

   Don't forget to import the module!

   When you run it, run it multiple times to see that the PID changes
   from run to run.

   ([flx[Solution|ex_printpid.py]].)

2. Write a program to generate random UUIDs. A UUID (pronounced
   "YOU-id") is a random string of letters and digits that looks like
   this:

   ```
   54c3bfab-fd9f-4f4a-96db-8f9fccff88cd
   ```

   (Well, yours will be different because it's very, very, _very_
   unlikely that you'll ever generate the same random one twice.)

   It's short for _Universally Unique ID_. That means it's unique in the
   universe, forever. Very, _very_ probably.

   Using the [fl[UUID
   module|https://docs.python.org/3/library/uuid.html]], generate a
   random UUID.

   Actually, generate several. Have the user enter a number on the
   command line. Generate that many UUIDs.

   For example:

   ```
   $ python ex_uuidgen.py 5
   8a8128fb-941a-4a2f-8982-75273d7c0048
   5fd7d64e-8491-4b61-82b0-f9438e7195dc
   4012f3ed-f6d7-40b5-9031-961ee06a30ad
   86c71566-014f-4e36-a55b-b18d677624b2
   2c1e5b3f-f0de-4186-80c5-767628c437b3
   ```

   Eagle-eyed readers might notice that the 13th digit is always `4`.
   That's because there are different types of UUIDs, and this digit
   indicates the type. (This case it's type 4, meaning random. Except
   for the 4.)

   You might also have noticed that, in addition to the numerals, only
   the letters "a" through "f" make an appearance. Surprise! UUIDs,
   except for the hyphens, are actually numbers! They're written in a
   base-16 numbering system called _hexadecimal_. More on that in
   another chapter.

   UUIDs are good any time you want to create an ID that you can be
   confident isn't already used by anyone, anywhere.

   You might wonder how you can be sure? I mean, there's a chance
   someone else will choose that number, right?

   Yes, there is a chance. It's:

   1 in 21,267,647,932,558,653,966,460,912,964,485,513,216.

   For comparison, the odds of winning the Mega Millions lottery jackpot
   are:

   1 in 258,900,000.

   So unless you're worried about winning the lottery jackpot
   82,146,187,456,773,479,978,605,303,068 times, you shouldn't be
   worried about someone choosing a duplicate UUID.

   And I wouldn't say I'm _worried_ I'd win the lottery that many times.
   More like _disappointed_. 

   ([flx[Solution|ex_uuidgen.py]].)

3. You're given the following string in Python---go ahead and paste it
   into a new source file:

   ``` {.py}
   matrix = """The Matrix is everywhere. It is all around us. Even
   now, in this very room. You can see it when you look out your window,
   or when you turn on your television. You can feel it when you go to
   work, when you go to church, when you pay your taxes."""
   ```

   That's a big multi-line string.

   I want you to print it out, but reformat it so that it's only 40
   columns wide, maximum:

   ```
   The Matrix is everywhere. It is all
   around us. Even now, in this very room.
   You can see it when you look out your
   window, or when you turn on your
   television. You can feel it when you go
   to work, when you go to church, when you
   pay your taxes.
   ```

   There's a handy module called
   [fl[`textwrap`|https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper]]
   that has some functionality that you can use to make your life
   easier.
   
   ([flx[Solution|ex_wrap.py]].)

4. Print a random integer between 0 and 1000, inclusive.

   It should print a different number every run, for example:

   ```
   $ python ex_rand1000.py 
   601
   $ python ex_rand1000.py 
   374
   $ python ex_rand1000.py 
   824
   ```

   See the [fl[`random`
   module|https://docs.python.org/3/library/random.html]] for help.

   ([flx[Solution|ex_rand1000.py]].)


5. Print out the current date in the form:

   ```
   Mon Feb 10
   ```

   See the [fl[`time`
   module|https://docs.python.org/3/library/time.html]] for help.

   In case it happens to come up, _locale_ refers to the human language
   spoken in the physical location where the program is running, e.g.
   English or French or Chinese or Esperanto, etc.

   ([flx[Solution|ex_curdate.py]].)


6. Write a program called `zipextract.py` that extracts files from a ZIP
   archive.

   The command line should accept the name of the ZIP file as the first
   argument, and, optionally, the name of the file in the archive to
   extract.

   If the second argument is left off, extract all the files.

   To extract all files:

   ```
   python zipextract.py example.zip
   ```

   To extract a specific file, run:

   ```
   python zipextract.py example.zip hello.txt
   ```

   ([flx[Solution|ex_zipextract.py]].)


## Summary

Modules make the world go around... a lot more easily than it would have
if you had to write all that stuff yourself.

In this chapter, we learned what modules were and how to find them in
the official Python docs.

Also, we learned how to import entire modules and individual components
from within modules.

Later we'll learn to write and import our own modules.
