<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**
-->

# Exceptions

## Objective

* Learn about different ways of handling errors
* Understand what exceptions are
* Write programs that catch exceptions
* Throw your own exceptions

## Project {#exc-proj-spec}

Write a program called `head.py` that returns the first few lines of a
file. For example, if the user enters:

```
python head.py filename.txt 12
```

it should show the first 12 lines of `filename.txt`.

Take extra care to error-check all the input. Catch any exceptions that
might occur.

Spend some time thinking about this; what are _all_ the things that can
go wrong with _any_ user input?

If there is some kind of error condition, the program should print an
appropriate error message and exit.

## Errors in Programs

Problem-solving step: **Understanding the Problem**

Let's stop and think about this from a conceptual standpoint for just a
minute.

Normally, a program produces data in the way you've asked for it. Unless
something goes wrong. In which case, it produces "bad" data.

Now, computers don't really have much of sense of right and wrong, as
you've seen in the documentary _The Terminator_. So how can we
differentiate between good and bad data?

How can we tell that something's gone wrong?

## Classic Error Handling

Problem-solving step: **Understanding the Problem**

There's one way we've been using so far: the return value from a
function. If it's a particular _sentinel value_ that we're on the
lookout for, we can use that to determine success or failure.

For example, let's check out the `.find()` method on strings. This
returns the index in a string that a given substring can be found. For
example:

``` {.py}
s = 'Bears, beets, Battlestar Galactica'

x = s.find('beets')

print(x)  # 7, because that's the index 'beets' starts at in the string
```

The return value there of `7` is "good" data. We asked for a thing and
we got it. But what if something goes wrong?


``` {.py}
s = 'Bears, beets, Battlestar Galactica'

x = s.find('Dwight')

print(x)  # -1, because the substring isn't found
```

`-1` here is the sentinel value we're looking for to tell us if there's
an error.

We can make decisions on it. This is what I'd call "classic" error
handling. This is the way people used to handle errors when Stonehenge
was built. And, like Stonehenge, this method of handling errors is still
in use to this day. If it ain't broke, don't fix it.

OK, yes, I admit Stonehenge is broke. Allow me my analogy!

``` {.py}
s = 'Bears, beets, Battlestar Galactica'

x = s.find(substring)

if x == -1:
    print(f"Couldn't find {substring}")
else:
    print(f"Found {substring} at index {x}")
```

There! We successfully handled an error the classic way.

But now let's learn another way.

## Error Handling with Exceptions

Problem-solving step: **Understanding the Problem**

Exceptions are another way of indicating that something's gone wrong.

We've already seen some of these. For example, if we run code that does
this:

``` {.py}
int("Hello!")   # Convert Hello! to integer
```

Python's going to be upset. `"Hello!"` isn't a number it's ever heard
of. And when we run it, we get this message, and the program exits:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hello!'
```

That's an exception in action. We tried some code, and it _raised an
exception_ to tell us that what we were doing just wasn't going to work.

Exceptions are raised (also sometimes said to be _thrown_) for all
kinds of things in Python.

Try to open a nonexistent file for reading:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'keyser_soze.txt'
```

Try to divide a number by zero:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Those first condensed words on the last line of the exception you see
there? That's the name of the exception that occurred.

```
ValueError
FileNotFoundError
ZeroDivisionError
```

So, like using return values to indicate errors, exceptions also
indicate that an error occurred.

Now---how do we detect that and do something with it?

## Catching Exceptions

Problem-solving step: **Understanding the Problem**

Bear with me, because this code is a little different in how it gets
executed.

We're going to use two new statements in conjunction: `try` and `catch`.
Let's jump right in with an example that we can dissect:

``` {.py .numberLines}
try:
    x = input("Enter a number: ")

    x = int(x)   # Convert to integer

    print(x * 1000)

except ValueError:
    print(f'error converting "{x}" to integer')
```

What's happening there? Look at the big blocks first. We have a `try`
block and an `except` block.

Think of the `try` block as the code you want to execute in your shiny
dreamworld where your user enters correct information every time.

Like the user enters `3490`, and it converts to integer just fine, and
then you print out `3490000`.

Perfect.

But what if the user enters `beans` instead of a number? `int()` is
going to freak out and raise a `ValueException`, just like we saw
earlier.

_Here's the magic_. If that happens, execution of the `try` block will
stop immediately, and Python will transfer control to the matching
`except` block, if it exists.

So for example, here's a successful run:

```
Enter a number: 3490
3490000
```

and here's a run where an exception is thrown:

```
Enter a number: beans
error converting "beans" to integer
```

See how it transferred control right into the `except` block?

That's how we handle exceptions!

## Catching Multiple Exceptions

Problem-solving step: **Understanding the Problem**

What if your `try` block throws multiple exceptions?

Turns out you can catch multiple exceptions just by having multiple
`except` clauses.

Let's try a program that divides a number by another:

```
x, y = input('Enter two numbers separated by a space: ').split()

x = int(x)
y = int(y)

print(f'{x} / {y} == {x / y}')
```

What are the exceptions that can be thrown?

Good question. Although there is a [fl[list of built-in
exceptions|https://docs.python.org/3/library/exceptions.html]], it's not
immediately obvious which one gets raised when.

The easy thing to do is try it in the [REPL](#repl). But try what?

_Think like a villain._ What are the things that can go wrong? What
kinds of bad input can you pass this program?

Give it some thought. I count four things that can go wrong with bad
user input. Can you see them?

Well, we're taking input, running it through `.split()`, and then
assigning the results into two variables. So the `split()` better
return a list of length `2`, or something bad is going to happen.

I'm going to put that line of code into the REPL and see what it says if
I enter something that's not two numbers separated by a space.

``` {.py}
>>> x, y = input("Enter 2 numbers: ").split()
Enter 2 numbers: 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 2, got 1)
```

Check it out! I entered a single number, and it raised `ValueError`
exception (with a message saying there weren't enough values).

Let's try too many values:

``` {.py}
>>> x, y = input("Enter 2 numbers: ").split()
Enter 2 numbers: 1 2 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

`ValueError` again! That means we can do something like this to catch
it:

``` {.py}
try:
    x, y = input('Enter two numbers separated by a space: ').split()

    x = int(x)
    y = int(y)

    print(f'{x} / {y} == {x / y}')

except ValueError:
    print("That's not two numbers separated by a space!")
```

And that will catch it. Here's a run:

```
Enter two numbers separated by a space: 1 2 3
That's not two numbers separated by a space!
```

Whee!

What's the next place we can mess things up?

Well, we're converting to `int()`... what does that function do if we
pass in something awful, like the word `manfrengensenton`?

Again in the REPL:

``` {.py}
>>> int("manfrengensenton")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'manfrengensenton'
```

Hey, it's `ValueError` again! Conveniently, we're already catching that
with an appropriate error message. Totally handled.

That takes care of three of the four cases I saw where we could get
exceptions. What's the fourth?

_Mathematics hat on_. Do you see it?

That's right, we're doing a division in there... and you can't divide by
zero. What happens when we do?

We already saw, above, that we get a `ZeroDivisionError`. So let's add
that to the end of our code:

``` {.py}
try:
    x, y = input('Enter two numbers separated by a space: ').split()

    x = int(x)
    y = int(y)

    print(f'{x} / {y} == {x / y}')

except ValueError:
    print("That's not two numbers separated by a space!")

except ZeroDivisionError:
    print("Can't divide by zero!")
```

So as you can see, you can handle as many different types of exceptions
as you want in their own `except` clauses after the `try`.

## Catching Multiple Exceptions II

If you want to handle multiple exceptions with the same handler code,
you can make a list of them:

```
except (FileNotFoundError, PermissionError):
    print("File not found or insufficient permissions")
```

This isn't as frequently used, since often you want to take a different
course of action for different exceptions.

## Getting More Exception Information {#exc-more-info}

Each exception is actually an instance of a class. And the class name is
the name you use in your `except` clauses.

Because it's an instance, it has some additional information attached to
it we can grab, but first we have to bind it (assign it) to a variable
name. We can do that with the `as` statement.

``` {.py}
try:
    1 / 0
except ZeroDivisionError as e:  # e is a reference to the exception
    print(e)
    print(repr(e))   # Print its representation
```

results in:

```
division by zero
ZeroDivisionError('division by zero')
```

That could be useful for getting more detailed information. In our
example in the previous chapter, we catch `ValueError`, but we saw three
different circumstances that could lead to it. We could use this
technique to give the user more detailed information about the nature of
the exception, should we choose.

All exceptions have an attribute called `args` that is a list of the
arguments that are passed to the exception when it was created. The
first of these is often a human-readable error message.

For instance, this code:

``` {.py}
try:
    1 / 0
except Exception as e:
    print(e.args[0])
```

prints the helpful message:

```
division by zero
```

Furthermore, any exception that is based on `IOError` includes the
string attribute `strerror` that contains a human-readable error message
corresponding to the error. You can find the list of exceptions that are
derived from `IOError` in the [fl[exceptions
documentation|https://docs.python.org/3/library/exceptions.html]].

## Catching All Exceptions

A `catch` statement that doesn't specify a particular exception will
catch _all_ previously uncaught exceptions.

For this reason, a blank `catch` should definitely be last, after all
the other catches. Python will stop at the first `catch` that matches,
even if it's a "catch all".

When you're in any `catch`, you can look at the results from the
built-in function `sys.exc_info()`. This function returns a tuple (think
"list" for now, if you're not familiar with tuples) with three pieces of
information: the type of the exception, a reference to the exception
itself, and a traceback^[A traceback, also known as a _stack trace_, is
a list of all the function calls that have taken place to get to this
point. It's really useful information for debugging.]

Let's mod our division program to catch all exceptions and print out the
exception info:

``` {.py}
import sys

try:
    x, y = input('Enter two numbers separated by a space: ').split()

    x = int(x)
    y = int(y)

    print(f'{x} / {y} == {x / y}')

except:
    print(sys.exc_info())
```

Here are some sample runs:

```
Enter two numbers separated by a space: 1
(<class 'ValueError'>, ValueError('not enough values to unpack (expected
2, got 1)'), <traceback object at 0x7f7899794f80>)
```

```
Enter two numbers separated by a space: a b
(<class 'ValueError'>, ValueError("invalid literal for int() with base
10: 'a'"), <traceback object at 0x7f6d0c9732c0>)
```

```
Enter two numbers separated by a space: 1 0 (<class
'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback
object at 0x7fe2ea373040>)
```

This isn't as common, to catch and examine exceptions in this way. But
it is another tool in your toolbox.

Be careful with catch-alls. They might hide exceptions that you weren't
expecting and should have let through. They're rare in practice.


## Finally `finally`

Problem-solving step: **Understanding the Problem**

There's a greater structure to be found here. We've already talked about
`try` and `catch`, but there's a way to add code that runs after the
`try` no matter what, regardless of whether or not an exception
occurred.

It's the `finally` clause, and it comes after the `except` clause(s).

Again, this block of code will run no matter what.

``` {.py}
try:
    print(1/1)
except ZeroDivisionError:
    print("Divide by zero!")
finally:
    print("All done!")
```

The above code will print:

```
1
All done!
```

If we modified that first line to `print(1/0)`, we'd get a divide by
zero exception, and the output would be:

```
Divide by zero!
All done!
```

In all cases, the `finally` block will run.

You can use this block to execute finalization or cleanup code, if you
need to.

`try`-`except` is really common. `finally` is less so, but not entirely
uncommon.


## What Else? `else`!

Problem-solving step: **Understanding the Problem**

Just when you thought `try`-`except`-`finally` was all she wrote, turns
out we can add an `else` in there for `try`-`except`-`else`-`finally`.

It's entirely possible that you won't ever see this, but I wanted to
quickly touch on it here. Just give it a glance:

``` {.py}
try:
    print("This is what we're trying to do")
    print("and where exceptions might occur.")

except:
    print("Caught an exception!")

else:
    print("This only runs if there was no exception.")

finally:
    print("This runs no matter what.")
```

Using `else` can give you more control over the flow of your program
when exceptions occur.

## Exception Objects

Problem-solving step: **Understanding the Problem**

At this point, we've covered catching exceptions, and this is all you
need to know 99% of the time you're using Python.

But that doesn't mean we should stop there. Part of being a good dev is
having a good mental model of _how_ these things work, not just to
memorize some patterns to use. Having deeper understanding will serve
you well.

So let's talk about how exceptions in Python are represented by objects.

We've already [hinted at this, above](#exc-more-info), where we talk
about getting more information from exceptions.

We found there is a class named `ZeroDivisionError` and another named
`ValueError`. Indeed, we can just make new ones of these if we want:

``` {.py}
e = ValueError()   # Construct a new ValueError object
```

There's a [fl[whole list of exceptions that are ready to
use|https://docs.python.org/3/library/exceptions.html]], but if none of
those seem to fit, you can just make a new `Exception` with some
information passed to it:

``` {.py}
e = Exception('Something went horribly awry')
```

Lastly, you can make your own new exception classes if you'd like. You
don't have to---you can use `Exception` or any of the other preexisting
ones.

But if you do make your own, the only catch is that these **must**
_inherit_ from the `Exception` base class.

Whooooaa, there, Beej. What are you even talking about?

Okay, you got me. I stepped into some Object-Oriented Programming
terminology, there. Now, we'll talk about what that all means in a later
chapter, but for now, take my word that you need to declare your new
exception, you have to use similar syntax to this:

``` {.py}
class MyAwesomeException(Exception):  # <-- Note "(Exception)"
    pass
```

This is telling Python, "I'm making a new class called
`MyAwesomeException`, but, here's the thing, `MyAwesomeException` _is_
an `Exception`."

Also, if you have a constructor, make sure you do this:

``` {.py}
class MyAwesomeException(Exception):  # <-- Note "(Exception)"

    def __init__(self, *args):        # <-- Get all positional args
        print("In my constructor")
        print("Doing whatever it is I have to do here")

        # The following line makes sure the constructor for the underlying
        # Exception object gets called with the arguments specified:

        super().__init__(*args)       # <-- Add this
```

Because `MyAwesomeException` is an `Exception`, suddenly we have two
constructors: one for `Exception` and one for `MyAwesomeException`.

The one in `MyAwesomeException` _overrides_ the one in `Exception`. In
order to make sure both are called, we add that `super()` line in there.

Don't worry about the details of how it works for now. We'll cover that
in detail in another chapter.

One final note: if you ever `catch Exception:` in your code, make sure
that `catch` is **after** all the more specific exceptions, like
`ValueException`. Python will use the first one it finds that matches,
and `Exception` matches most everything.

But in the meantime, we can construct exceptions. But so what? What can
we do with them?

## Raising Exceptions

Problem-solving step: **Understanding the Problem**

Let's say you've written some code and you want to use exceptions to
notify the caller when some error condition has occurred.

The process is going to be:

1. Construct a new exception of some kind.
2. Raise it with the `raise` statement.

Often these happen in the same line.

As an example, let's write a function that reads a number between 0 and
9 from the keyboard. If the number read is out of range, let's raise a
new `ValueError` with the message `"out of range"` as the argument.

``` {.py}
def getnum():
    n = input("Enter a number 0-9: ")

    n = int(n)   # Convert to int

    if n < 0 or n > 9:
        # If out of range, raise a ValueError:
        raise ValueError("out of range")

    return n
```

And then add some code to call it and catch any exceptions:

``` {.py}
try:
    n = getnum()
    print(f'{n} * 15 == {n * 15}')

except ValueError as v:
    print(f'Exception: {v}')
```

If we give it a run with a valid value:

```
Enter a number 0-9: 4
4 * 15 == 60
```

But if we specify something out of range, we get:

```
Enter a number 0-9: -1
Exception: out of range
```

What if we enter the letter `a`? That'll bomb out on the call to
`int()`... but it'll do it with a `ValueError`, like we saw earlier in
the chapter.

And, hey! Coincidentally, we're already catching `ValueError` in our
code, above.

Let's try it:

```
Enter a number 0-9: a
Exception: invalid literal for int() with base 10: 'a'
```

Caught it! Note that the error message is different than the "out of
range" exception, so we can differentiate.

So, hey! We now know how to:

* Catch exceptions
* Create new exceptions
* Raise exceptions

That's not bad so far!

## Re-raising Exceptions

Sometimes you might be interested in seeing that an exception occurred,
but don't want to stop it. You want it to continue to propagate so that
the caller can also see it.

We can do this pretty simply with a lone `raise` inside the `catch`.

The following function notes a `ValueError` if it occurs, but then
re-raises it so that it can get caught by the `try` block in the main
code:

``` {.py}
def makeint(x):
    try:
        return int(x)

    except ValueError:
        print("Hey, I saw an exception!")
        print("But I'll let someone else handle it.")

        raise    # Re-raise the exception

try:
    x = makeint("beej")

except ValueError as v:
    print(f'Exception: {v}')
```

This outputs:

```
Hey, I saw an exception!
But I'll let someone else handle it.
Exception: invalid literal for int() with base 10: 'beej'
```

## Project Implementation

Go ahead and [review the project specification from the beginning of the
chapter](#exc-proj-spec) if you have to.

Problem-solving step: **Understanding the Problem**

The big challenge here is how to we provide complete error checking of
all user inputs to make sure everything is sensible?

What are all the things that could go wrong?

Go ahead and make a list on your own, and then you can compare it to the
list I have, below.

Spoilers ahead!

Here's what I can think of happening:

* User doesn't enter the correct number of command line arguments.
* User enters a non-number for the second command line argument.
* User enters a filename that doesn't exist.
* User enters a non-positive number.
* The file isn't a regular file (e.g. it's a directory or other special
  file).
* The user doesn't have permission to read the file.
* User enters a number that's larger than the number of lines in the
  file.

Some of these you can handle with simple `if` statements. Others we'll
have to catch with exceptions.

That last one, about what happens when you enter a number larger than
the number of lines in the file, is a great question. The spec doesn't
say. So we should ask the creator of the spec for clarification.

"Hey, Beej! The spec doesn't say what to do if the number of lines
specified is greater than the number of lines in the file. What do we do
in that case?"

Let's do this: we'll stop outputting lines at either the number of lines
the user specifies, or the end of the file, whichever comes first. No
message to the user is required in either case.

Ok, let's plan!

Problem-solving step: **Devising a Plan**

Looking at the spec, the program can be broken down into a number of
parts.

* Read user input
* Open the file for reading
* Read the number of lines up to what the user specified (or EOF)

For each of those parts, we'll have to do input validation and tell the
user if anything went wrong.

Problem-solving step: **Carrying Out the Plan**

Some of this stuff we've seen before, so we'll skim over it a bit.

First, let's get the user input from the command line, check that the
right number of arguments was passed, and check the input to make sure
it's sensible.

``` {.py .numberLines}
import sys

if len(sys.argv) != 3:
    print("usage: head.py filename count")
    sys.exit(1)

filename = sys.argv[1]
total_count = int(sys.argv[2])

if total_count < 1:
    print("head.py: count must be a positive integer")
    sys.exit(2)
```

That's partway there, but we're missing an error case. Do you see it?

What if the user enters "`bananas`" for the count? If we try to run it
to see what happens, sure enough, we get an exception.

```
Traceback (most recent call last):
  File "foo.py", line 8, in <module>
    total_count = int(sys.argv[2])
ValueError: invalid literal for int() with base 10: 'bananas'
```

It's the `ValueError` exception that we've seen before. Let's modify our
code to catch that exception and handle it.

``` {.py .numberLines}
import sys

if len(sys.argv) != 3:
    print("usage: head.py filename count")
    sys.exit(1)

filename = sys.argv[1]

try:
    total_count = int(sys.argv[2])
except ValueError:
    print("head.py: count must be a positive integer")
    sys.exit(2)

if total_count < 1:
    print("head.py: count must be a positive integer")
    sys.exit(2)
```

There! That fixes it. And that code works, but...

Notice anything messy about it? That's right---we sure are repeating
ourselves a lot. Let's refactor and see if we can get rid of those
duplicate lines.

One option would be to set a flag in either case to `True` if there was
an error, and then print the message and exit. That would work, and
wouldn't be a bad solution at all.

But we can be a bit more clever and actually make the exception handler
do all the work for us by simply raising a `ValueError` exception if the
`total_count` is less than one. Then we'll get a `ValueError` in both
cases, and we can handle it in one place.

``` {.py .numberLines startFrom="9"}
try:
    total_count = int(sys.argv[2])

    if total_count < 1:
        raise ValueError()

except ValueError:
    print("head.py: count must be a positive integer")
    sys.exit(2)
```

Check that out. If `int()` raises the exception, we catch it. And if we
raise the exception ourselves, we also catch it. Plus all the logic for
testing the input value for correctness is all in the same `try` block,
nicely.

OK! We have the code getting correct input. Let's go on to the next step
and print lines from the file.

We can start by simplifying the problem to just print all the lines and
not worrying about the count for now.

Let's take our code from before for printing out a file:

``` {.py .numberLines startFrom="19"}
with open(filename) as f:
    for line in f:
        print(line, end="")
```

If we run the program, passing in an existing file, we see all the lines
of that file printed out.

But what if we pass in the name of a non-existent file?

Let's try it!

```
$ python head.py nosuchfile.txt 5
Traceback (most recent call last):
  File "foo.py", line 19, in <module>
    with open(filename) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'nosuchfile.txt'
```

Bammo! Another exception! This time it's `FileNotFoundError`.

Let's try it on a directory:

```
$ python head.py / 5
Traceback (most recent call last):
  File "foo.py", line 19, in <module>
    with open(filename) as f:
IsADirectoryError: [Errno 21] Is a directory: '/'
```

An `IsADirectoryError` exception!

Let's try it on a file we don't have permission to read:

```
$ python head.py noperm.txt 5
Traceback (most recent call last):
  File "foo.py", line 19, in <module>
    with open(filename) as f:
PermissionError: [Errno 13] Permission denied: 'noperm.txt'
```

Yet another exception: `PermissionError`.

One option we have here is to specifically catch all these exceptions:

``` {.py .numberLines startFrom="19"}
try:
    with open(filename) as f:
        for line in f:
            print(line, end="")

except (FileNotFoundError, IsADirectoryError, PermissionError):
    print(f'head.py: error reading file {filename}')
```

And that works.

But I have a bit of insider knowledge that we can use. All of those
exceptions are derived from `IOError`. 
We can see that in the [fl[list of built-in
exceptions|https://docs.python.org/3/library/exceptions.html]].

You can see, there are a lot of exceptions that are `IOError`s. Instead
of catching them individually, an option is to just catch `IOError` and
print out an appropriate error message. This has the benefit of catching
_all_ those errors that `file()` might raise. It also has the drawback
of not being able to easily differentiate between them. So how can we
print an appropriate error for each one?

Luckily, `IOError` has a handy attribute in it called `strerror` that
gives a nice human-readable error message that describes what went
wrong. We could print that.

So let's just catch the `IOError` exception and print its error message
out.

``` {.py .numberLines startFrom="19"}
try:
    with open(filename) as f:
        for line in f:
            print(line, end="")

except IOError as e:
    print(f'head.py: {filename} {e.strerror}')
```

And when we run it, we get some nice error message for whatever error
case we get:

```
$ python head.py noperm.txt 5
head.py: noperm.txt Permission denied

$ python head.py / 5
head.py: / Is a directory

$ python head.py nofile.txt 5
head.py: nofile.txt No such file or directory
```

Pretty neat!

What's left? Oh yeah---we have to actually implement the functionality
to only show the first however-many lines of the file.

There are a couple approaches to this.

One, we could use a while loop and test for the end of the file _or_
reaching the required count, whichever comes first.

That would be fine. But a more straightforward option might be to just
bail on the loop when the counter gets high enough. The `break`
statement can be used to bail out of a loop partway through.

``` {.py .numberLines startFrom="19"}
line_count = 0  # Number of lines we've read so far

try:
    with open(filename) as f:
        for line in f:

            line_count += 1

            if line_count > total_count:
                break

            print(line, end="")

except IOError as e:
    print(f'head.py: {filename} {e.strerror}')
```

As you see, we're keeping track of the number of lines read so far, and
if that exceeds our magic target number, we just break straight out of
the loop and we're done.

And it works!

```
$ python head.py rocks.txt 3
marble
coal
granite
```

Super-robust against bad input and errors. This is what we call
_defensive coding_, when you prepare for the worst and handle those
cases without crashing. It's a good strategy because not only does it
make your program more capable of handling errors, but it also makes you
stop and consider what the errors are that might occur in the first
place. And, as we've said, hours of debugging can save you minutes of
planning.

([flx[Solution|head.py]].)

## Exercises

1. When we run this code, it prints out "Exception" instead of "Division
   by Zero". Why? What can we do, without deleting any code, to get it
   to print "Division by zero"?

   ``` {.py}
   try:
       x = 3490 / 0
   except Exception:
       print("Exception")
   except ZeroDivisionError:
       print("Division by Zero")
   ```

   ([flx[Solution|ex_catchorder.py]].)

2. Write a function that takes a list of numbers, and two integers as
   index values. The function should return the sum of the two numbers
   in the list at the two given indexes.

   Catch the specific exception that is raised if the list indexes are
   out of range. Print an appropriate error.

   Hint: to see which exception is raised if the list indexes are out of
   range, run the code _without_ a `try`-`except` block and see what it
   prints when it bombs. Then add a `try`-`except` for that exception.

   ([flx[Solution|ex_listadd2.py]].)

3. Write a function that accepts a list of three numbers and returns the
   sum. If the list does not contain three numbers, raise a
   `InvalidListSize` exception. (Note that this exception doesn't
   exist---you'll have to write it.)

   Also write an exception handler that catches the exception if it is
   thrown.

   ([flx[Solution|ex_listadd.py]].)

## Summary

New big concept in this chapter with exceptions. It's a technique we
haven't used before to catch errors, but is a powerful one to add to
your skillset.

We compared and contrasted error handling via return values with error
handling with exceptions, wrote programs that could catch exceptions and
handle them, and also wrote programs that generates our own, new
exceptions.

Additionally, we learned how flow control works around exception
handling, with the `else` and `finally` clauses.

Any time you learn a new basic way of doing something, it's difficult to
wrap your head around at first. But enough practice with it, and I
guarantee after a while it will become second nature.