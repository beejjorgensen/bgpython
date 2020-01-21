<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Functions

## Objective

* Understand what functions are and how they're useful
* Be able to use built-in functions
* Be able to write your own functions
* Be able to write good functions
* Understand the difference between positional arguments and keyword arguments


## Chapter Project Specification {dicts-proj-spec}

TODO

## What Are Functions?

You're about to seriously level up in programming by learning how to do
this, and it's not even that difficult. Functions are the key to getting
away from the toy programs we've been doing so far and doing _real_
programs.

So what are they?

Problem solving step: **Understanding the Problem**.

Functions are self-contained pieces of code that you can _call_ that do
a specific thing.

Does this sound at all familiar? Because we've been doing this the whole
time with the built-in `print()` function.

> Not to be confused with _statements_ like `for` and `if`. Know a
> function because it has parenthesis right after the name that you can
> use to pass _arguments_ to the function^[Purists will point out
> exceptions to this, like with `__add__()`, but let's skip that for
> now.].

The `print()` function has built-in functionality to print things on the
screen. Thankfully (really, really) we don't have to write that code
ourselves. We can just say:

``` {.py}
print(23 + 34)
```

and have `print()` do all the dirty work of getting us the answer
printed to the screen.

This turns out to be a great way to simplify and organize code. Can you
imagine if you had to put all the code in to print out something on the
screen every time you wanted to print something? Much easier to _define_
the `print()` function once, and then use it over and over again by
calling it.

We have an important principle in computer programming called the DRY
principle (_Don't Repeat Yourself_). If you can remove as much
repetitive code as you can and move it to a function, that makes your
code easier to read and maintain. DRY code is happy code.

Not only can we use functions to make DRY code, we can also use them to
organize our code into logical sections, even if a function is called
only one time.

It is clearer to have your functionality in discrete sections that you
call in sequence rather than just having a single huge block of code
that does everything


## Using Built-In Functions

Problem solving step: **Understanding the Problem**.

Python has a _lot_ of built-in functions that you can use. It's not
necessary to memorize the usage in detail (you can always look up the
details), but it's a good idea to skim their descriptions just so you
can recall that they exist.

We've already used `print()` and `input()` quite a bit, but there are
plenty more. [fl[Look them up
online|https://docs.python.org/3/library/functions.html]].

Here are some common ones, though this is not an exhaustive list:

|Built-in Function|Description|
|-|-|
|`abs()`|Return the absolute value of a number.|
|`bin()`|Return a string representing the number in binarys.|
|`chr()`|Return a character for the Unicode (and ASCII) value passed in.|
|`dir()`|Return a list of methods on this object.|
|`enumerate()`|Return an iterator over a list of (index, value) pairs.| |`filter()`|Repeatedly run a function on items of a list filtering some out.|
|`float()`|Convert a number or string to a floating point value.|
|`help()`|Get help on a data type.|
|`hex()`|Return the hexadecimal representation of a number.|
|`input()`|Get input from the keyboard and return that string.|
|`int()`|Convert a floating point or string to an integer value.|
|`isinstance()`|Return true if an object is an instance of a class.|
|`len()`|Return the length of an iterable, like a list or string.|
|`map()`|Run a function on every value in an iterable, returning the results.|
|`max()`|Return the maximum of the arguments or of an iterable.|
|`min()`|Return the minimum of the arguments or of an iterable.|
|`ord()`|Return the Unicode value (code point) for a given character.|
|`pow()`|Return a base value raised to an exponent.|
|`print()`|Print to the console.|
|`range()`|Return an iterator that runs over a range of values.|
|`reversed()`|Return an iterator over a reversed version of the argument.|
|`round()`|Round a number to the nearest whole number.|
|`sorted()`|Return a sorted version of an iterable.|
|`str()`|Convert a value to a string.|
|`sum()`|Return the sum of all arguments and/or of an iterable.|
|`super()`|Get access to an object's superclass.|
|`zip()`|Merge parallel lists into a dictionary.|


 If the function operates on
> an object with a dot `.` before the function name, we call that
> function a _method_.
