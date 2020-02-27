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

**WIP**

## Objective

* Learn about different ways of handling errors
* Understand what exceptions are
* Write programs that catch exceptions
* Throw your own exceptions

## Project {#exc-proj-spec}

TODO

## Errors in Programs

Problem-solving step: **Understanding the Problem**

Let's stop and think about this from a conceptual standpoint for just a
minute.

Normally, a program produces data in the way you've asked for it. Unless
something goes wrong. In which case, it produces "bad" data.

Now, computers don't really have much of sense of right and wrong. So
how can we differentiate between good and bad data?

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


## Exceptions

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

Those first condensed words on the third line of the exception you see
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

