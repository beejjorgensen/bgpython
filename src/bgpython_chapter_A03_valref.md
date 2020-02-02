# Appendix C: Value versus Reference, for Realsies {#valref}

## The Big Lie

In the book, I talk about reference versus value types. We've said:

* When you make an assignment with a value type, a _copy_ of the item
  gets made. After that, there are two items.
* When you make an assignment with a reference type, you get another
  reference to the same entity. After that, there is still only one
  entity, but with two references to it.
* Numbers and strings are examples of value types.
* Lists, dictionaries, and objects are examples of reference types.

For example, with a value assignment:

``` {.py}
x = 5
y = x  # y is a copy of x

y = y + 1

print(x)  # still prints 5, since y was a copy
print(y)  # 6
```

But with a reference type assignment:

``` {.py}
x = [1, 2, 3]
y = x   # x and y refer to the same list!

y.append(4)

print(x)  # [1, 2, 3, 4], since x and y point to the same list
print(y)  # [1, 2, 3, 4], y is just another name for the same list
```

The reason I talk about Python variables in these terms is because:

1. It's a mental model that works.
2. A lot of other languages actually work this way.
3. And if they don't work this way, the mental model probably still
   works for them, anyway.

But the way Python does variables under the hood is a little bit
different.

## Taking The Red Pill

The truth is this: _all variables are reference types in Python_.

Whaaaaaaa... `:mind-blown:`

The real different is all about this: is the type of the data _mutable_
or _immutable_. Let's explore this a bit.

If a data type is mutable, you can change it after it has been
created. If immutable, you can't.

Now, by "change it", I want to be clear that this refers to changing the
value of a specific piece of data. It does _not_ refer to changing
something that a variable name refers to. You can always change what a
variable refers to, even if it referred to something immutable before.

_It's not the variables that are mutable or immutable; it's the data
they refer to that is mutable or immutable._

Here are the mutable types:

* Lists
* Dictionaries
* Sets
* Objects from classes that you've created

Here is the list of immutable types:

* Everything else: integers, floats, strings, tuples, etc.

A string is one of the easiest immutable types to consider. If you look
through the documentation for strings, you'll see there's no way to
change one.

Let's try:

``` {.py}
s = "Beej!"

s[2] = "X"  # Try to change the second "e" to an "X"
```

This throws the error:

```
TypeError: 'str' object does not support item assignment
```

It's immutable. You can't change it. You can only build new ones:

``` {.py}
s = "Beej!"

t = s[:2] + "X" + s[3:]  # Make another string with pieces of the old one

print(s)  # "Beej!"
print(t)  # "BeXj!"
```

But remember that it's the string itself that is immutable, not the name
`s`. (Again, variables are neither mutable nor immutable; it's the data
they refer to that is or isn't.)

So we could have written this:

``` {.py}
s = "Beej!"

s = s[:2] + "X" + s[3:]  # Make another string with pieces of the old one

print(s)  # "BeXj!"
```

In that case, we're just changing what `s` points to. It used to point
to the string `"Beej!"`, but we made another string `"BeXj!"` and
set `s` to point to that, instead^[What happens to the old string
`"Beej!"` if no variables refer to it any longer? It get _garbage
collected_, which means Python detects that the string will no longer be
used, it frees up the memory, and the string is gone forever. Until
you make another one just like it.].

Let's contrast to a list, which is a mutable type:

``` {.py}
x = [1, 2, 3]

x[1] = 99  # No error this time!

print(x)  # [1, 99, 3]
```

Got it?

Now, how does mutability fit in with the whole "everything is a
reference" idea? Let's explore that now.

## Back to Reference Versus Value

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


## No, Keep Going Down the Rabbit Hole!

Okay, first things first.

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

```
$ python test.py
True
```

What gives? Well, in the latter case, the Python interpreter is getting
a little clever. Before it even runs your code, it analyzes it. It sees
that you have two `"Beej!"` strings in there, so it just makes them the
same one to save you memory. Since strings are immutable, you can't tell
the difference.

And second things second.

In that same example:

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

`True`?? What's up with that?

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

This is why `"Beej!"` isn't interned (because it contains punctuation),
and why `"Alice"` _is_ interned.

You can intern your own strings with `sys.intern()` for dictionary
lookup optimization, but that's something 99.99999% of the Python
programming populace will never bother doing.