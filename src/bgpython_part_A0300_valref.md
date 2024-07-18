# Appendix C: Assignment Behavior {#assignment-behavior}

In this book, we've talked about how Python variables work, but let's
dig into it a little more here.

When we have data of some kind, like a number or a list or a string,
that's stored in memory. And we can assign it to a variable name so that
we can have a way to refer to it.

That variable name is a reference to the data.

So if everything's a reference, that must mean that if we do this,
there's only one string, right? Just two names for the same string?

``` {.py}
s = "Beej!"
t = s
```

Yes! That's exactly what that means. `s` and `t` both refer to the same
string in memory. That means if you changed the string, both `s` and `t`
would show the changes because they're both two names for the same
string.

_But you can't change the string! It's immutable!_

It's the same with numbers:

``` {.py}
x = -3490
y = x
```

Both `x` and `y` refer to the same number in memory. If you changed the
number, both `x` and `y` would show the change.

_But you can't change the number! It's immutable!_

Let's try a list:

``` {.py}
c = [1, 2, 3]
d = c
```

Just like with strings and numbers, both variables `c` and `d` refer to
the same thing in memory. But the difference is that the list _is_
mutable! We _can_ change it, and we'd see the change in `c` and `d`.

``` {.py}
c = [1, 2, 3]
d = c

c[1] = 99
print(d[1])   # 99
```

Of course, you can reassign a variable to point at anything else at any time.

## How This Relates To Functions

All this adds up to Python's call-by-sharing evaluation strategy.

When you call a function, all the arguments passed to the function are
assigned into the parameters in the parameter list.

That assignment, even though it doesn't use the `=` assignment operator,
behaves in the same way, nonetheless.

In the following example, both `x` and `a` refer to the same object...
right up to the moment we reassign `x` on line 4. At that point, `x`
refers to a different list, but `a` still refers to the original.

``` {.py .numberLines}
def foo(x):
    x[1] = 99  # x still refers to the same list as a

    x = [4, 5, 6]  # x refers to a different list than a, now

a = [1, 2, 3]
foo(a)
```

## Is Any of This True?

Yes, believe it!

We can verify it in the [REPL](#repl) with the built-in `id()` function
and the `is` operator.

The `id()` function will give us the location in memory where a thing
(like a string or number) that a variable refers to is stored. If two
variables return the same ID, they must be pointing to the same thing in
memory.

Let's try in the REPL:

``` {.py}
>>> s = "Beej!"
>>> t = s
>>> id(s)
140156808252976
>>> id(t)
140156808252976
```

The exact number doesn't matter (it will vary), but what matters is that
they're identical. Both `s` and `t` refer to the entity in memory at
that location, namely the string `"Beej!"`.

You could compare those numbers to determine if both variables point to
the same thing:

``` {.py}
>>> id(s) == id(t)
True
```

but there's a shorthand for that with the `is` operator:

``` {.py}
>>> s is t
True
```

Note that it's typically only want you assign from one variable to
another that they refer to the same thing. If you assign to them
independently, they typically won't:

``` {.py}
>>> s = "Beej!"
>>> t = "Beej!"
>>> s is t
False
```

In the above example, there are two strings in memory with value
`"Beej!"`.

I recognize that I said "typically" a bunch up there, and that should
rightfully raise a bunch of "Beej is hand-waving" red flags.

The actual details get a bit more gritty, but if you want to stop with
what we've said up there, you're good.

"No, keep going down the rabbit hole!"

Okay then!

## Python Compiler Optimizations

If you take this example from the REPL, above:

``` {.py}
>>> s = "Beej!"
>>> t = "Beej!"
>>> s is t
False
```

and you put it in a python program, like `test.py`:

``` {.py}
s = "Beej!"
t = "Beej!"
print(s is t)
```

and run it from the command line, you'd think you'd get `False`, just
like in the REPL. Wrong!

``` {.default}
$ python test.py
True
```

What gives? Why is it `False` in the first case and `True` in the
second? Well, in the latter case, the Python interpreter is getting a
little clever. Before it even runs your code, it analyzes it. It sees
that you have two `"Beej!"` strings in there, so it just makes them the
same one to save you memory. Since strings are immutable, you can't tell
the difference.

## Internment

In that same example, above:

``` {.py}
>>> s = "Beej!"
>>> t = "Beej!"
>>> s is t
False
```

what if we use a different string, like "Alice"?

``` {.py}
>>> s = "Alice"
>>> t = "Alice"
>>> s is t
True
```

`True`?? What's up with that? Why does Alice get special treatment?

Or look at this:

``` {.py}
>>> x = 257
>>> y = 257
>>> x is y
False
```

which is fine---but then check this out, with 256 instead of 257:

``` {.py}
>>> x = 256
>>> y = 256
>>> x is y
True
```

`True`, again?

We're getting into a deep language feature of Python called
_internment_. Basically Python makes sure to only have one copy in
memory of certain, specific values of data.

For these values, all variables will refer to the same item in memory.

They are:

* Integers between -5 and 256 inclusive.
* Strings that contain only letters, numbers, or underscores.
* The `None` object.
* The `True` and `False` objects.

This is why `"Beej!"` isn't interned (because it contains punctuation),
and why `"Alice"` _is_ interned.

You can intern your own strings with `sys.intern()` for dictionary
lookup optimization, but that's something 99.99999% of the Python
programming populace will never bother doing.
