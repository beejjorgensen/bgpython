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

**WIP**

## Objective

* Learn what a module is
* How to find modules to use
* How to import modules
* Splitting projects: Importing your own files

## Chapter Project Specification {#mod-proj-spec}

TODO

## What and Why of Modules

Problem-solving step: **Understanding the Problem**.

Modules are pieces of self-contained code that you can _import_ into
your code and use. Think of them like prefabricated building blocks that
you can put together in your project to accomplish tasks without needing
to write out the details yourself.

This is actually a really powerful concept that you have at your
disposal. Tons of code has already been written, and you can just use it!

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
unless you're dying ot curiosity over a particular module.

Are there are [fl[_zillions_ of third-party modules|https://pypi.org/]]
you can use, as well.

You can import as many modules as you want into an individual project.

## Using a Module

Problem-solving step: **Understanding the Problem**.

You declare your intent to us a module with the `import` keyword. We're
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
Fortunately the `sys` module had everything we needed right there.

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

But _how_ do you get those extra command line arguments?

Our good friendly `sys` module can help us again here.

The variable `sys.argv` is a list that contains the program name
followed by all the command line arguments.

Run this program with a variety of command line arguments and see what
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
Beej---how am I supposed to figure all that out? Was November 12, 1955 a
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
`prmonth()` method on the class that you can use to to print a calendar
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
previous section how to get command line arguments into a list.

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

Running it again, we get the same error, but before that we see some
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
user specified 1-12, or print an error otherwise. Something like this:

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

The `time` modules has a function called `ctime()` that prints the time
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

Is that a function that the programmer defined, or is it something that
we `from import`ed from somewhere? By putting the name of the module
first, it helps mitigate that ambiguity:

``` {.py}
print(time.ctime())
```

So in general, I don't use `import from` unless it makes the code
decidedly more readable to do so.

Remember: readable code is high-value code!

## Importing Your Own Files

### .pyc