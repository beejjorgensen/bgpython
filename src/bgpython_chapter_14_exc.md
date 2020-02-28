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


## Exceptions

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


## Getting More Exception Information

* Learn about different ways of handling errors


## Catching All Exceptions

