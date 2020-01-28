# Appendix B: The REPL {repl}

## What is the REPL?

The REPL, pronounced _REP-əl_, is short for the _Read-Evaluate-Print
Loop_.

Great. I mean, truly, that's awesome.

But what does any of that mean?!

Check this out. If you run `python` on the command line (or whatever
your OS's variant is), you'll end up with a prompt that looks like this:

```
$ python
Python 3.8.0 (default, Oct 23 2019, 18:51:26) 
[GCC 9.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

And it just sits there, waiting for you to type something.

Actually, it's _reading_. The _Read_ part of REPL.

So type something and hit `RETURN`!

``` {.py}
>>> print("Hello, world!")
Hello, world!
```

What happened after you hit `RETURN` was that Python _Evaluated_ your
expression, and the _Printed_ the result. And then it printed another
`>>>` prompt, because it's doing this in a _Loop_! The REPL!

This is a method you could use to quickly test out Python commands to
see how they work. It's not commonly used for development, but it is
there if you find it convenient.

Any time you see the `>>>` prompt, it's waiting for another Python
command.

``` {.py}
>>> a = 20
>>> b = 30
>>> c = a + b
>>> print(c)
50
```

What about multi-line commands? Let's try printing numbers in a loop:

``` {.py}
>>> for i in range(5):
...
```

Wait! What's that `...` prompt? That means Python is waiting for more.
The fact that the previous line ended in a `:` indicates that a block is
to follow it. So Python is waiting for a properly-indented block. (Hit
`RETURN` on a blank line to exit the block. If you get stuck in `...`
mode, just keep hitting `RETURN` until you get back out to the `>>>`
prompt.)

``` {.py}
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
```

## Calculator

You can use the Python REPL as a quick and dirty calculator.

``` {.py}
>>> 50 + 20 * 10
250
>>> import math
>>> math.factorial(10)
3628800
>>> math.sqrt(2)
1.4142135623730951
```

## Getting Help

Python has a powerful built-in help system.

You can ask for help on any expression; help will be returned on the
type of that expression.

For example, if we ask for help on a variable of type string, we get
help on what we can do with that variable:

``` {.py}
>>> s = "Hello!"
>>> help(s)
```

This will output all kinds of stuff.

```
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
```

_Et cetera_. The `:` prompt at the bottom is the prompt for the _pager_.
You can hit `RETURN` to go to the next line, or `SPACE` to go to the
next page. Up and Down arrow keys also work. Type `q` to get out of the
pager and return to normal.

The first thing you might notice are a bunch of functions that have
double underscores around them, like this:

```
 |  __add__(self, value, /)
 |      Return self+value.
```

Those double underscores, AKA _dunderscores_ or just _dunders_, indicate
that this is an internal or special functions. As a beginner, you can
ignore them. As you get more advanced, you might want to see how to make
use of them.

So hit `SPACE` a bunch of times until you're past the dunders. After
that, you start getting to the documentation for the more common
functions, like this one:

```
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
```

We see there's a description there of what the method does, as well as
an important description of what each parameter to the function means.
But let's look at this line in particular:

```
 |      S.count(sub[, start[, end]]) -> int
```

That's not Python. It's documentation, and it has its own way of being
read.

Generally:

The `S.` refers to this string that we're operating on. For example, if
I say:

``` {.py}
"fee fie foe foo".count("fo")
```

the string `"fee fie foe foo"` is represented by `S` in the documentation.

The stuff after the `->` indicates the type of the return value. This
function returns an integer.

Now, what about that `start` and `end` stuff in the middle with the
square brackets?

In documentation, square brackets indicate _optional_ parameters to the
function. Notice in my example, above, I didn't pass `start` or `end`...
they're in square brackets, so they're optional.

Looking in more detail, you see the brackets are nested. This means you
can make the call with a `sub` and a `start`... and _then_ the `end`
becomes optional. There's no way to call it with just a `sub` and an
`end`, but no `start`. The optional `end` is optional if-and-only-if the
optional `start` had already been specified.

Finally, you can ask for help on a specific function or method:

``` {.py}
help("".count)  # Get help specifically on string.count method
```

## `dir()`---Quick and Dirty Help

The `dir()` built-in function is like `help()`, except extraordinarily
terse. It just returns a list of the methods on a particular thing.

For instance, we can get that list of methods and data attached to a
dictionary by asking for `dir({})` (or by passing any `dict` to
`dir()`).

``` {.py}
>>> dir({})
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
'__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values']
```

Not as good as `help()`, but it might get you the quick answer if you're
like, "What do I call to get the values out of a dictionary, again? Oh,
that's right. `values()`! Eureka!"

One place this is also useful is if you're using a poorly-documented
piece of software^[Which should serve as a not-so-gentle reminder that
you should document your code.]. Asking for `dir()` on an object can
give you insight on how to use it.

Though if you do this, beware that programmers change their undocumented
interfaces _all the time_ without telling people. There's a school of
thought that says if something's undocumented, you shouldn't use it at
all, lest it be silently changed or dropped some day in the distant
future. And that school has a point.


## Getting out of the REPL

Oh, sure, Beej, put this section at the end of the chapter. Well, I just
wanted to make sure you read the middle bit. `:)`

Since the REPL is reading from the keyboard as a "file", you should send
an EOF ([flw[End Of File|End-of-file]]) character to indicate that it
should be done.

On Mac and Linux and BSD and Ultrix and MINIX and SunOS and IRIX and
HP-UX and Solaris and GNU Hurd and Plan 9 From Bell Labs and any Unix
variant, EOF is indicated from the keyboard with `CTRL-d`.

On Windows and Windows and Windows and Windows and any Windows variant
and MS-DOS, EOF is indicated from the keyboard with `CTRL-z`. Followed
by `RETURN`.

Additionally, on any system, you can type `exit()` at the `>>>` prompt
and it'll quit out.
