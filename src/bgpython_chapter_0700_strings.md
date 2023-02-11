<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Strings

## Objective

* Get a firm grip on what a string is
* Convert from other types to strings
* Concatenate strings
* Understand that strings are immutable
* Get individual characters with strings
* Slice a string
* for loop through a string
* Use basic string manipulation methods and functions
* Print strings using formatted output


## Chapter Project Specification {#strings-proj-spec}

Compute and print out a multiplication table. Allow the user to enter a
number between 1 and 19, inclusive, and then print out a times table up
to that value.

For example, if the user enters `4`, the output should be:

```
  1   2   3   4
  2   4   6   8
  3   6   9  12
  4   8  12  16
```

Be sure to leave enough room for the maximum number of digits you'll
need in the largest product.


## What is a String?

Problem-solving step: **Understanding the Problem**.

A string in Python is a sequence of characters (letters, punctuation,
numbers, foreign characters, etc.). You enclose it in either single
quotes (`'`) or double quotes (`"`), your choice, as long as they match
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
quotes in single-quoted strings by putting a backslash character in
front of them (`\`) <!-- ` fix syntax highlighting in vim -->. This is
called _escaping_ the character, which means "Hey, Python, treat this
like a literal quote mark---just print a quote mark out," as opposed to
"Hey, Python, this is the end of the string."

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

Problem-solving step: **Understanding the Problem**.

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

Problem-solving step: **Understanding the Problem**.

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

Problem-solving step: **Understanding the Problem**.

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

You often find the assignment-concatenation operator in use to add to
the end of a string:

``` {.py}
x = "B"   # start with "B"
x += "e"  # add an "e" to the end of the string
x += "e"  # add an "e" to the end of the string
x += "j"  # add a "j" to the end of the string
x += "!"  # add an "!" to the end of the string

print(x)   # Beej!
```


## Midterm Challenge

Use what we've learned so far to concatenate a string `"Hello"` with the
number `3490` (an integer, not a string).

Problem-solving step: **Devising a Plan**.

OK, so let's use `+` to concatenate the number onto the end of the
string.

Problem-solving step: **Carrying out the Plan**.

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

Problem-solving step: **Devising a Plan**.

Since we can't concatenate an `int` to a `str`, can we turn the `int`
into a `str`? Sure! New plan: convert the `int` to a `str` with the
`str()` function, and then concatenate it onto the first string with
`+`.

Problem-solving step: **Carrying out the Plan**.

``` {.py}
x = "Hello"
y = str(3490)
print(x + y)    # Hello3490
```

Success!

Problem-solving step: **Looking Back**.

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


## Getting Individual Characters From Strings

Problem-solving step: **Understanding the Problem**.

What if we want to extract a single character from a string?

We can do it, but we have to introduce new notation to allow it: `[` and
`]`, AKA _square brackets_.

Let's print out just the first two characters in a string:

``` {.py}
x = "Beej!"

print(x[0])  # Print character in position 0, "B"
print(x[1])  # Print character in position 1, "e"
print(x[4])  # Print character in position 4, "!"
```

When reading this code, `x[1]` would be read aloud as "`x` sub `1`", a
nod to classic mathematical notation $x_1$. The `1` in this case is
called the _index_ into the string.

**Really important:** index numbers start at `0`!!  The first character
in a string is sometimes referred to in speech as the _zeroth character_
and the second character is sometimes referred to as the _oneth
character_, and _twoth_, and _threeth_, and so on, in an attempt to
avoid ambiguity. Say "The character at index 3" if you want to be sure.

> _**Fun Indexing Fact**: every programming language in serious use
> today uses_ `0`-based indexing _(that is, indexes start at `0`). There
> are some useful mathematical implications for doing so, even if it's
> trickier to think about._

Do some experimentation here. Try getting characters past the end of the
string? What happens? (We'll learn to mitigate this later.)

What if you try a negative index? What do you think will happen? What
_does_ happen?

Turns out if you specify a negative index in Python, it gets the
character starting from the _end_ of the string!

``` {.py}
x = "Beej!"

print(x[-1])  # Print 1st from the end character: "!"
print(x[-4])  # Print 4th from the end character: "e"
print(x[-5])  # Print 5th from the end character: "B"
```

We're going to use these next when we talk about slices.


## Slices

Problem-solving step: **Understanding the Problem**.

A _slice_ is part of a string. You specify them by knowing the
_starting index_ and _ending index_ into a string, and separating them
by a colon `:`.


``` {.py}
x = "Beej!"
print(x[1:4])   # "eej"
```

The slice starts at the first index number and stops _just before_ the
second index number. (Remind you of anything? Yes---just like
`range()`!)

In this way, you can pull out any _substring_ from a string.

## Midterm Challenge

Problem-solving step: **Understanding the Problem**.

Write a program that will allow the user to input a string, then will
print out the entire string _except_ the first and last characters. You
can assume the string will be at least 3 characters long.

So if the user enters `Beej!`, we want to print out `eej`. If they enter
`Python`, we want to print out `ytho`.

Problem-solving step: **Devising a Plan**.

We need to:

1. Input a string.
2. Get a slice of the string not including the first and last
   characters.
3. Print the slice.

Steps 1 and 3 are pretty straightforward. But what about step 2?

Since we don't know how long the string will be (other than it's three
or more characters), we can't just get a slice from `1` to, say, `5`. We
have to get a slice from index `1` to the second-from-the-end character.

Fortunately, we know how to index to the second from the end: index
`-2`! But wait--there's a catch: slices only go up to, but not
including, the second index! So we need to end the slice at index `-1`
to cause it to not include the last character.

Problem-solving step: **Carrying out the Plan**.

``` {.py .numberLines}
x = input("Enter a string of at least 3 characters: ")
y = x[1:-1]  # all but the first and last
print(y)
```

Easy peasy!

Problem-solving step: **Looking Back**.

What could we have done better?

We didn't need the intermediate variable `y`. We could have simply:

``` {.py .numberLines}
x = input("Enter a string of at least 3 characters: ")
print(x[1:-1])  # all but the first and last
```

Also, we're not actually enforcing the user to enter at least 3 characters.
How would we do that? Remember how we used a `while` loop before to
verify input? We could do the same.

But how can we tell if a string is at least a certain length? There are
a couple of ways. Turns out, your slice will be an empty string (`""`) if
the length of the string is less than 3, and you could use that to
detect.

In a bit, we'll also discuss the `len()` function that will give you the
length of any string you pass in.


## Interlude: Mutable versus Immutable Types

Problem-solving step: **Understanding the Problem**. 

So far we've learned about three data types: integer, float, and string.
All of these share a common characteristic: they're all _immutable_.
(That is, you cannot change them. Note that you can always change the
thing a variable refers to---that is, you can assign the variable to
refer to something else---but you can't change the immutable thing,
itself.)

What this means is that _any time you do an operation on any of the
types, you get a new entity back_. Maybe the old one is kept, or maybe it
is forgotten depending on how your code works.

In short, there's no way to add something to the end of a string. You
can take a string and add something to it to make a completely new
string with the new stuff on the end, but it's a new string. The
original is never modified since it's immutable.

``` {.py}
x = "hello"
y = x + " world"

print(x)  # hello
print(y)  # hello world
```

See in that example how the value of `x` is unchanged? We couldn't
change it if we wanted to. Check this out:

``` {.py}
x = "hello"
print(x[2])  # print character 2, namely "l"

x[2] = "z"   # ERROR! Python won't allow you to change the string!
```

If you wanted to make a string where character number 2 is swapped out,
you'll have to slice it up and build it yourself.

``` {.py}
x = "hello"
y = x[:2] + "z" + x[3:]  # Make a new string

print(y)  # hezlo
```

Or you could use _regular expressions_^[We'll talk about regular
expressions, or _regexes_, later.] or some other string methods to
replace the letter... but remember that these methods produce a new
string---they have to since strings are immutable!

It's the same story with numbers, although this is behavior that you
might take for granted, it's so expected.

``` {.py}
x = 12
y = x + 2  # This creates a new number--it doesn't change 12

print(x)  # 12
print(y)  # 14
```

Like I said, so far all the types we've learned about are immutable.
But later, we'll talk about lists, dictionaries, and sets, which are the
three mutable types in Python.

So remember: any time you think you are "changing" a string, you're
actually making a completely new one. It's important to keep this model
in mind because it will prevent all kinds of bugs and misunderstandings
as we progress.


## `for`-loops with Strings

Problem-solving step: **Understanding the Problem**.

Remember how we used `for` with `range()` earlier to count up to a
certain number? Turns out `for` is far more capable than just doing
that. It's just full of surprises!

We can use a `for` loop on a string to process the characters
individually.

``` {.py}
s = "Hello!"

for c in s:
    print("character:", c)
```

If you run this, you'll see it prints each of the characters in turn:

```
character: H
character: e
character: l
character: l
character: o
character: !
```

You can use this if you ever need to traverse a string a character at a
time. Of course, if you only want to traverse _part_ of a string, you
can slice it first!

Another little tidbit here that might be useful is the `enumerate()`
function. This will return a series of _index-value pairs_. That is, it
returns both the index into the string _and_ the character at that
index.

``` {.py}
s = "Hello!"

for i, c in enumerate(s):
    print("character at index", i, "is:", c)
```

outputs:

```
character at index 0 is: H
character at index 1 is: e
character at index 2 is: l
character at index 3 is: l
character at index 4 is: o
character at index 5 is: !
```

That's useful if you need to know the index _and_ the character. More on
the `enumerate()` function later.


## String Functions and Methods

Problem-solving step: **Understanding the Problem**.

Python has a lot of built-in functions to help you manipulate and use
strings.

Here are a few of them:

|Function|Example|Description|
|:--------|:---------|:------------------------------------------------|
|`bool()` |`bool(s)` |Convert to Boolean value. The only string that converts to `False` is the empty string `""`. (This means that an empty string will count as `False` in an `if` condition.)|
|`float()`|`float(s)`|Convert to floating point value.|
|`input()`|`input(s)`|Print prompt `s`, then return string entered on keyboard.|
|`int()`  |`int(s)`  |Convert to integer point value.|
|`len()`  |`len(s)`  |Return the length of a string.|
|`print()`|`print(s)`|Print a string.|

Take note of the `len()` function---we'll use that to tell us how many
characters there are in a string.

But now I want to introduce a new term and style of coding that you'll
frequently encounter moving forward: _methods_.

Methods are functions that work on a specific _object_. We're getting
ahead of ourselves with this "method" and "object" talk, but for now
think of them as functions that work on a specific string.

But isn't that just like the functions we just saw?

Yes, you got me. But we use these differently! Yay! This will all make
more sense someday in the future, but bear with me for now.

Let's look at an example with the `.upper()` method. (Usually pronounced
"dot upper" or "upper method".)

``` {.py}
a = "Beej!"
b = a.upper()
print(b)       # BEEJ!

print(a)       # Beej! -- unchanged since .upper() returns a new string
```

The upper method converts a string to uppercase.

Now, conversationally, I said "converts to", but remember that strings are
_immutable_, so it really doesn't change the string in `a` at all. It
makes a new uppercase version of the string and returns it, and we refer
that to the new string by `b`.

As for methods, there are a whole bunch of them attached to strings. So
you can take any string, add a dot (`.`), and then put the method name
to operate on that string. They work just like regular functions, except
have this different notation.

> _**Fun Objected-Oriented Programming Fact**: all this talk about
> methods and objects has its roots in a_ programming paradigm _called_
> Object-Oriented Programming _(OOP). A programming paradigm is a way of
> modeling problems so that you can solve them. So far, we've been
> using the_ imperative _programming paradigm, which means we think of a
> problem as a sequence of steps and conditions. But with OOP, you think
> of a problem as a collection of objects that you can do things with._
>
> _Python is "multiparadigm", which means it can do OOP or imperative
> as we see fit. We'll use a mix of them from now on, and we'll cover
> OOP in more detail in its own chapter._

Here are some common string methods:

|Method|Description|
|:--------------|:----------------------------------------|
|`.split()`     | Split a string into a `list`^[More on lists in upcoming chapters.] on the given string.
|`.strip()`     | Strip whitespace^[Spaces, tabs, and newlines.] from both ends of the string.
|`.upper()`     | Convert string to all uppercase.
|`.lower()`     | Convert string to all lowercase.
|`.replace()`   | Replace all occurrences of one word with another in the string.
|`.find()`      | Find the index of the substring in the string, or `-1` if it's not found.
|`.count()`     | Count the number of occurrences of the substring.
|`.startswith()`| Return `True` if the string starts with the given string.
|`.endswith()`  | Return `True` if the string ends with the given string.
|`.capitalize()`| Capitalize the first letter of each word in the string.

Here are some examples:

``` {.py}
s = "hello, goats! "

s.split(",") # [ "hello", "goats! " ]
s.strip()    # "hello, goats!"
s.upper()    # "HELLO, GOATS! "
s.lower()    # "hello, goats! "

s.find("goats")          # 8 (index of "goats" in the string)
s.count("goats")         # 1
s.startswith("Goats")    # False
s.endswith("goats! ")    # True
s.capitalize()           # "Hello, goats! "

s.replace("goats", "world")  # "hello, world! "

```

You can also chain them together and they evaluate in turn, left to
right:

``` {.py}
s = "   another EXAMPLE!    "

s.strip().lower().capitalize()  # "Another example!"
```

There are a whole lot of [fl[string
methods|https://docs.python.org/3/library/stdtypes.html#string-methods]]
you can use, more than we're going to talk about here. But go peruse
them just so you have an idea of what you have at your disposal.


## Formatted Output with F-Strings

Problem-solving step: **Understanding the Problem**.

So far we've just been using `print()` like so:

``` {.py}
x = 10
print("x is", 10)
```

which works, but doesn't offer as much control over the output.

Let's take a look at something called _F-strings_ which are new in
Python 3.6. ("Formatting strings".)

These offer us a really powerful method of formatting output. So
powerful we'll only be scratching the surface here.

The gist is that we can make a new string where we inject the value of
variables (or expressions) into a string at a specific spot.

Simple example:

``` {.py}
x = 10
print(f"x is {x}")  # x is 10
```

Notice a couple of things:

1. There's an `f` in front of the quotes. This signifies that this is an
   F-string, as opposed to a regular string.
2. We inject the expression to evaluate inside _curly braces_^[Also
   called _squirrely braces_.] `{` and `}`. 

Python automagically evaluates that expression and puts the result into
the F-string at that point.

Here's another:

``` {.py}
x = 10
print(f"x plus 10 is {x + 10}")   # x plus 10 is 20
```

But that's not all!

We can also put a field width in there which controls how big the "cell"
is in which the number is printed.

Compare this:

``` {.py}
print(f"a number: {1000}")
print(f"a number: {50}")
print(f"a number: {250}")
```

which outputs:

```
a number: 1000
a number: 50
a number: 250
```

to this:

``` {.py}
print(f"another number: {1000:4}")
print(f"another number: {50:4}")
print(f"another number: {250:4}")
```

which outputs:

```
another number: 1000
another number:   50
another number:  250
```

The `:4` says to output the expression in a 4-space-wide field. This
gives us a great way to make columns align on subsequent rows, like if
you were printing out a spreadsheet.

Another thing it can do is specify a number of decimal places to print
out floating-point numbers.

``` {.py}
x = 3.1415926
print(f"Pi is {x:.2f}")  # Pi is 3.14
```

That format string says "print `x` as a floating-point number, with
`2` decimal places".

F-strings are _really_ powerful when it comes to controlling your
output. We'll explore more as we go.

### `.format()` Method

There is yet-another method of printing formatted strings that are
really similar to F-strings: using `.format()`:

``` {.py}
x = 3.1415926
print("Pi is {:.2f}".format(x))  # Pi is 3.14
```

This form has fallen out of favor due to the popularity of F-strings.

### `%` printf Operator

If you go back even farther in time, you might find instances of `%`
being used as the _printf operator_ to format output. An example:

``` {.py}
x = 3.1415926
print("Pi is %.2f" % x)  # Pi is 3.14
```

It's even _farther_ out of favor. F-strings are the new thing.

> _**Fun Computing History Fact**: `printf()` is a function in the C
> programming language that was considered_ so awesome _that the
> creators of Python decided to immortalize it with the `%` operator
> that does the same thing. And even now, the_ format specifiers _used
> in F-strings to describe the type of data being printed match those
> from the C language. Not bad for a language invented in the 1970s,
> eh?_

Note that the printf `%` operator is the same as the arithmetic modulo
(remainder) operator `%`. Python looks at the arguments to the operator
and does the right thing. If the left argument is a string, it's printf.
If it's a number, it's modulo.

## Chapter Project

It's time to do that project... way back from the beginning of the
chapter! Remember? If not, [jump back to the top and
refresh](#strings-proj-spec).

We're going to print a times table. This will use knowledge from this
chapter, as well as from previous chapters. Use any means you know to
solve the problem.

Problem-solving step: **Understanding the Problem**.

Let's take another look at the sample output when the user enters `4`:

```
  1   2   3   4
  2   4   6   8
  3   6   9  12
  4   8  12  16
```

(If you're rusty on your multiplication tables, what you do to multiply
$3\times4$ is to look up `3` along the top edge, then look up `4` along the
left edge, and then look in the table where they cross. There you'll
find `12`, the answer.)

How can do we attack this? Let's look at a couple of things.

First, look for patterns. See any?

I'll wait while you look.

There are several in there.

* The diagonals read 1, then 2 2, then 3 4 3, then 4 6 6 4... it's
  symmetric.
* The first row is 1 2 3 4, and the second is 2 4 6 8, and the third is
  3 6 9 12. The first skips by 1, the second by 2, the third by 3.
* Columns do the same as rows in terms of numbers skipped.

Can we use any of those to our advantage? Maybe...!

Second, let's try to simplify the problem.

What if the problem were to print:

```
  1   2   3   4
```

and that's all. How would you solve that?

What if it were to print only this:

```
  3   6   9  12
```

How would you solve that?

> _**Fun Realism Fact**: There are a _lot_ of ways to program this. As I
> write this, at least four are immediately coming to mind. Remember:
> **coding is creative** and there're almost always many ways to get the
> same result. Be creative! It's your sandbox to mess around in! You
> can't break the computer._

Problem just some simple `for` loops, right? We could do this with three
`for` loops:

```
  1   2   3   4
  2   4   6   8
  3   6   9  12
```

Something like this (pseudocode):

``` {.py}
for i in range(1, 5, 1): print(...)
for i in range(2, 10, 2): print(...)
for i in range(3, 15, 3): print(...)
```

But of course, we don't just want to print rows three times... the end
result is going to have the number of rows that the user input. We need
to loop to make it happen. A loop of loops! A _nested loop_!

Problem-solving step: **Devising a Plan**.

Before we jump into this, I'd like you to take the time to think about
this. Set a timer and work on it for 3 minutes.

Do it.

Timer. Do it. You will gain valuable experience points for the attempt.

I'll be back in 3 minutes.

_[Elevator music---do it now!]_

Okay, I'm back. What did you come up with?

I'll go over one solution here, but if you came up with one and it's
different, don't worry! There are no wrong answers here. There are only
answers that you, personally, like better or worse than others. Part of
being skilled in the art is that you can get better at making these
assessments as you progress.

One possible plan for this is to have an _inner_ loop (the _nested_
loop) that prints a complete row out. In other words, it's printing out
all the columns in the row. And then outside of that, we have the
_outer_ loop that is responsible for printing out a bunch of rows.

And then inside there, we have to compute what values to print for each
row, based on which row we're on.

First, we have to get user input. Let's do that, and validate that it's
between 1 and 19 similar to the last project.

```
while input isn't between 1 and 19:
    ask the user for input
```

After that, we'll print the table:

```
outer loop over rows:
    inner loop over columns:
        print value for column
```

Of course, printing the value for the column is the tricky bit.

Remember when we did our sample with three hardcoded loops, above?

``` {.py}
for i in range(1, 5, 1): print(...)
for i in range(2, 10, 2): print(...)
for i in range(3, 15, 3): print(...)
```

See any patterns in there? 1 2 3 is a pretty easy one. But what about
that 5 10 15? Clearly, it's multiples of 5, but where does "5" come from?

In that example, we were printing rows and columns from 1 to 4. (That
is, the user inputs the number 4.) And 5 is one more than 4. That's _a_
pattern. Is it the right one? Let's try!

If we take the first 3 numbers in the ranges (that is, 1 2 3), and
multiply by 4+1, we end up with 5 10 15, just like we want.

So there's a formula in there for that middle number in the range.
Assuming the user enters `x` as the value, then the middle number for
any `range()` call would be:

``` {.py}
row_number * (x + 1)
```

and the first and last numbers in the range would simply be the row
number!

The last thing we need to do is make sure we have the times table all
formatted correctly so that the columns line up. The biggest number
we'll print is `361` ($19\times19$) so we'll need a space between
columns and three spaces for the number. We can use an F-string with a
field width of `4` to make this happen.

Problem-solving step: **Carrying out the Plan**.

Let's start by entering a number and make sure this works:

``` {.py .numberLines}
valid_input = False

while not valid_input:
    x = input("Enter a number between 1 and 19: ")
    x = int(x)

    if x >= 1 and x <= 19:
        valid_input = True
 
```

We just loop until we get valid input, just like in the last project.

Now for the times' table part. We want to go from `1` to the number
entered, so we'll start at `1` and go to `x + 1`.

And then we'll compute the max number for each row, just like we
planned, above. And we'll print the value!

One gotcha is that we want to print a bunch of things on the same line
and `print()` goes to the next line by default. We'll use our friend
`end=""` in the `print()` call to keep it on the same line, and then add
another empty `print()` after the loop to go to the next line.;

(Continuation of the code above!)

``` {.py .numberLines startFrom="10"}
for row in range(1, x + 1):
    for product in range(row, row * (x + 1), row):
        print(f"{product:4}", end="")
    print()
```

Let's try it!

```
Enter a number between 1 and 19: 6
   1   2   3   4   5   6
   2   4   6   8  10  12
   3   6   9  12  15  18
   4   8  12  16  20  24
   5  10  15  20  25  30
   6  12  18  24  30  36
```

Woot!

Did you have another solution that worked? There are plenty others!

Problem-solving step: **Looking Back**.

What are the corner cases that you should test? (Look for the `if`
statements, and test on either side of those. `0` and `1` and `19` and
`20`.)

If you didn't come up with a different solution, try to do so now. What
if you used `while` loops instead of `for` loops?

([flx[Solution|multtable.py]].)

## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

A lot of these can use `for` loops in the solution! Use any knowledge
you have to solve these, not only what you learned in this chapter.

**Always** use the [four problem-solving steps](#problem-solving) to
solve these problems: understand the problem, devise a plan, carry it
out, look back to see what you could have done better.


1. Given the following varibles:

   ``` {.py}
   x = 3490
   y = 3.14159
   ```

   write code that prints out the following:

   ``` {.py}
   x is    3490.00
   y is       3.14
   x + y = 3493.14
   ```

   ([flx[Solution|ex_fstring.py]].)

2. Write code to count the number of occurrences `goat` in this string:

   ``` {.py}
   s = "How many goats could a goat goat goat if a goat could goat"
   ```

   ([flx[Solution|ex_goatcount.py]].)

3. Using this string, create a copy of it where all the vowels are
   uppercase and all the consonants are lowercase.

   ``` {.py}
   s = "The quick brown fox jumps over the lazy dogs."
   ```

   Hint: _think like a human_. If you had a physical set of blocks with
   letters on them in front of you, what would be the process and steps
   for building a new string with the required changes?

   ([flx[Solution|ex_uppervowel.py]].)

4. Allow the user to input a string, and also a number. Print out the
   character at that index number in the string. Don't allow the user to
   enter a number that's out of range.

   (After you solve this, check out the [flx[solution|ex_charat.py]] for
   a twist on checking for valid input.)

5. Allow the user to input a string, and also two numbers. Print out the
   slice from those index numbers in the string. Don't allow the user to
   enter numbers that are out of range.

   (In the [flx[solution|ex_sliceat.py]], there's duplicated code to
   enter two numbers. Later, when we get to _functions_, we'll learn how
   to remove this duplicated code.)

6. Makeup two more exercises and code them up.


## Summary

In this chapter, we did _all kinds_ of crazy things with strings.

* Conversions from other types
* How to concatenate strings with `+`
* How to get characters and slices out of a string
* How `for` loops process strings
* Learned a bunch of string methods and functions
* Formatted output with F-strings

Coming up, we're going to learn even more built-in data types that we
can use. After that, we'll talk about functions, and then you'll be
dangerously close to being able to write _real programs_!

