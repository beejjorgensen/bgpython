<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Strings

## Objective

* Get a firm grip on what a string is
* Convert from other types to strings
* Understand that strings are immutable
* Get individual characters with strings
* Slice a string
* Use basic string manipulation methods
* Print strings using formatted output

## Chapter Project Specification {#strings-proj-spec}

Multiplication tables, nicely formatted


## What is a String?

Problem solving step: **Understand**.

A string in Python is a sequence of characters (letters, punctuation,
numbers, foreign characters, etc.). You enclose it in either single
quotes (`'`) or double quotes (`"`), you choice, as long as they match
on either side.

Here are some strings:

``` {.py}
"Hello!"
"This is test #37"
"3490"                 # string of digits
"         "            # string of spaces
""                     # empty string, 0 characters
"Beej's String"        # string with an apostrophe
'Beej says, "hi!"'     # string with double quotes in it
```

You can also embed double quotes in double-quoted strings (or single
quotes in single quoted strings by putting a backslash character in
front of them (`\\`). This is called _escaping_ the character, which
means "Hey, Python, treat this like a literal quote mark---just print a
quote mark out," as opposed to "Hey, Python, this is the end of the
string."

``` {.py}
'Beej\'s string'        # Equivalent to the example, above
"Beej says, \"hi!\""
```

Strings are commonly used when:

* Printing out characters on the screen
* Reading from the keyboard with `input()`
* Reading/writing data from/to files (called _File I/O_, short for _File
  Input/Output_).
* Network I/O

## Creating Strings

Problem solving step: **Understand**.

Strings are generally created one of two ways:

* by declaring a _string constant_
* getting a string back from a function

The former we've already seen. Here's another example of a string
constant:

``` {.py}
x = "This is a constant string!"
```

But we've also already seen functions that produce strings:

``` {.py}
y = input("Enter a string: ")
```

`input()` returns a string that gets stored in `y`.

But wait---there's clearly a constant string there, as well! The prompt
`"Enter a string:"` is a string! Strings everywhere!

Later we'll learn about file and network I/O and how they're used with
strings and other data types. But for now, we'll stick to some basics.


## Converting Other Types To Strings and Vice Versa

Problem solving step: **Understand**.

We've already mentioned this in a previous chapter, but it's worth
covering again as a review.

You can convert a lot of other types to strings with the `str()`
function. We'll see how to make use of this later.

Examples:

``` {.py}
x = str(3490)    # "3490"
y = str(3.14159) # "3.14159"
z = str("Hi!")   # "Hi!" (does nothing, since "Hi!" was already a string!)
```

Likewise, you can convert from strings to other types, like `int` and
`float` with those respective functions:

``` {.py}
x = int("3490")         # Integer 3490
y = float("3.14159")    # Float 3.14159
```

In this way, if you have a string with a number in it, you can convert
it to a numeric value so that you can perform math on it.


## String Concatenation with `+`

Problem solving step: **Understand**.

You're used to using `+` to add two numbers, but did you know you could
also "add" strings? It doesn't do it arithmetically, but it will glue
the strings together, a process known as _concatenation_
(cən-CA-tən-ay-shun---"cat" in the middle pronounced like the animal.)
You can _concatenate_ two strings.

``` {.py}
x = "Hello, "
y = "world!"
z = x + y      # z becomes "Hello, world!"
```

This is how you build smaller strings together into larger ones.


## Midterm Challange

Use what we've learned so far to concatenate a string `"Hello"` with the
number `3490` (an integer, not a string).

Problem solving step: **Make a Plan**.

Ok, so let's use `+` to concatenate the number onto the end of the
string.

Problem solving step: **Code it up**.

``` {.py}
x = "Hello"
y = 3490
print(x + y)
```

But running it, we get this output:

```
Traceback (most recent call last):
  File "foo.py", line 3, in <module>
    print(x + y)
TypeError: can only concatenate str (not "int") to str
```

Let's take a close look at that. It's telling us that on line 3 of
`foo.py`, where we have `print(x + y)` we're getting this error:

```
TypeError: can only concatenate str (not "int") to str
```

`y` is an `int`, but `x` is a `str`. This error is telling us that we
can't concatenate an `int` onto a `str`. What to do now?

Problem solving step: **Make a Plan**.

Since we can't concatenate an `int` to a `str`, can we turn the `int`
into a `str`? Sure! New plan: convert the `int` to a `str` with the
`str()` function, and then concatenate it onto the first string with
`+`.

Problem solving step: **Code it up**.

``` {.py}
x = "Hello"
y = str(3490)
print(x + y)    # Hello3490
```

Success!

Problem solving step: **Postmortem**.

Any other ways to solve this? We could have done the `str()` call later:

``` {.py}
x = "Hello"
y = 3490
print(x + str(y))    # Hello3490
```

and that would have worked just as well.

Also ponder a related problem: what if you had a string `"3490"` and you
wanted to arithmetically add `1000` to it, and then produce a final
string of `"4490"`? What kinds of conversions and operations would you
have to do?


## Immutability of Strings

Problem solving step: **Understand**.

If some data is _mutable_, it means you can modify it. If it's
_immutable_, it means you cannot.

We've seen numbers are mutable:

``` {.py}
x = 3490
x += 1000
print(x)  # we changed `x` to 4490, `x` is mutable
```

but, get this: _strings are immutable_. You cannot change them. The only
thing you can do is to make a new string.

``` {.py}
x = "Hello, "
y = "world!"
z = x + y      # z is a completely new string; x and y are unchanged
```

So remember: any time you think you are "changing" a string, you're
actually making a completely new one. It's important to keep this model
in mind because it will prevent all kinds of bugs and misunderstandings
as we progress.
