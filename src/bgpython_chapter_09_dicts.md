<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Dictionaries

## Objective

* Understand whats dictionaries are
* Initialize a dictionary
* Access individual elements in a dictionary
* Check to see if a key is in a dictionary
* Iterate over dictionaries with `for`
* Use common dictionaries built-in functions
* Construct new dictionaries with dictionary comprehensions
* Build Dictionaries of Dictionaries
* Understand that Dictionaries are Reference Types

## Chapter Project Specification {dicts-proj-spec}

Let's store some genealogical^[This is all about family trees. Did you know I'm
related to Queen Elizabeth II (by marriage)? I'm her mother’s sister’s husband’s
father’s father’s sister’s daughter’s husband’s wife’s (_drama!_) sister’s
husband’s father’s brother’s son’s son’s daughter’s son’s daughter’s son. For
realsies! I'm willing to bet that you're related to Queen Elizabeth II, as
well. That makes us cousins!] data!

We'll have a number of data records associated with each person:

```
Beej Jorgensen:
    Born: 1990 [yes, I'm 29, is my story I'm sticking to]
    Mother: Mom Jorgensen
    Father: Dad Jorgensen
    Siblings: [Brother Jorgensen, Sister Jorgensen, Little Sister Jorgensen]

Mom Jorgensen:
    Born: 1970
    Mother: Grandma Jorgensen
    Father: Grandpa Jorgensen
    Siblings: [Auntie Jorgensen]

Dad Jorgensen:
    Born: 1965
    Mother: Granny Jorgensen
    Father: Grandad Jorgensen
    Siblings: [Uncle Jorgensen]
```

(Ok, I hear you saying, "Wait, your mom and dad were both Jorgensens? That's
suspicious. I mean, I'm not saying, but I'm just saying." Hold your tongue! I
can assure you they're not related^[Except via Queen Elizabeth II, like the rest
of us.].)

We want to write an app that will allow you to print out the birthdays of the
parents of any given person.

Example:

```
Enter a name: Beej Jorgensen
Parents:
    Mom Jorgensen (1970)
    Dad Jorgensen (1965)
```

So we'll need some way to store that, and some way to look through the data to
get information about other people who are referenced.

## What are Dictionaries?

Problem solving step: **Understanding the Problem**.

Remember how with lists, we could key an index number into the list and
get a value out, and how we could use that same index number to store
something in that "slot"?

Was really convenient for storing collections of information that you
could index by number, right?

Well, what if you wanted to refer to a slot with something that _wasn't_
a number? What if you wanted to use, say, a string, like so?

``` {.py}
x = [1, 2, 3]

x["beej"] = 3490  # Not going to work with a list
```

That makes Python unhappy because `"beej"` isn't an integer. And with
lists, it wants integers.

But we can get around that limitation with _dictionaries_, or _dicts_
for short.

Declaring a dictionary is a little bit different, but here's a simple
example to start:

``` {.py}
d = {}  # Squirrely braces, not square brackets!

d["beej"] = 3490

print(d["beej"])  # 3490
```

So very similar in usage, though the initial declaration of the variable
is different than a list.

With dicts, the value in the square brackets is called the _key_, and
the value stored there is the _value_.

``` {.py}
#   key        value
#    |           |
#  --+--      ---+---
d["goats"] = "awesome"
```

You use the key to lookup a value in the dictionary, or to set a value
in the dictionary.

The key can be any immutable type (e.g. integers, floats, strings). The
value can be any type.

## Initializing a Dictionary

Problem solving step: **Understanding the Problem**.

As we saw above, you can initialize an empty dictionary like so:

``` {.py}
d = {}
```

But you can also pre-initialize the dictionary with a number of keys and
values:

``` {.py}
d = {
    "name": "Beej",
    "age": 29,  # ish
    "favorite OS": "windows",
    "no really, favorite OS": "linux"
}
```

That's the equivalent of setting them by hand, albeit less verbose:

``` {.py}
d = {}
d["name"] = "Beej"
d["age"] = 29  # ish
# etc.
```

If you come from a web background, you might have come across
[fl[JSON|https://en.wikipedia.org/wiki/JSON]]-format data. The Python
dictionary is very similar in format, though not exactly the same.

## Speed Demon

Problem solving step: **Understanding the Problem**.

Like lists, dicts are really fast at looking up information. In fact, on
average, it takes the same amount of time to get a value out of a dictionary,
_regardless of how many items are in the dictionary_^[Time complexity
enthusiasts will recognize this as $O(1)$, or _constant_ time.].

Keep this fact in mind going forward. We'll get into more complex problems that
can make use of this feature to keep your programs running quickly. _Vroom!_

## Does this `dict` have this key?

Problem solving step: **Understanding the Problem**.

If you have a dictionary, it's nice to be able to check to see if a key even
exists.

The secret to doing this is the `in` statement that will return a Boolean
indicating if a key is in a dict.

``` {.py}
d = {
    "a": 10,
    "b": 20
}

if "a" in d:
    print(f'key a\'s value is: {d["a"]}')

if "x" not in d:
    print('There is no key "x" in "d"')
```

There is also a way to get an item out of a dictionary using the `.get()`
method. This method returns a default value of `None`^[If you haven't seen it
before or need a refresher, this is a value that represents "no value". It's a
placeholder (what we call a _sentinel value_) to indicate a no-value condition.]
if the key doesn't exist.

``` {.py}
val = d.get("x")

if val is None:  # Note: use "is", not "==" with "None"!
    print("Key x does not exist")
else:
    print(f"Value of key x is {d[x]}")
```

You can also detect a non-existent key with `try`/`catch`. But that's a story
for another time.

## Iterating over Dictionaries

Problem solving step: **Understanding the Problem**.

Remember how you could iterate over all the elements in a list with `for`? Well,
we can do the same thing with dictionaries. Except in this case, we'll be
looping over the _keys_ in the dictionary, not the values.

Let's try it!

``` {.py}
d = {
    "c": 10,
    "b": 20,
    "a": 30
}

for k in d:
    print(f"key {k} has value {d[k]}")
```

This gives us the output:

```
key c has value 10
key b has value 20
key a has value 30
```

Note that in the latest version of Python, the keys come out in the same order
they've been added to the dictionary.

If you want them in another order, there are options:

``` {.py}
d = {
    "c": 10,
    "b": 20,
    "a": 30
}

for k in sorted(d):  # <--- Add the call to sorted()
    print(f"key {k} has value {d[k]}")
```

And now we have this, where the keys have been sorted alphabetically^[Or what we
call _lexicographically sorted_. It's like alphabetical, but on steroids so that
it can handle letters, numbers, punctuation and so on, all of which are all
numbers deep down.].

```
key a has value 30
key b has value 20
key c has value 10
```

Also, similar to how lists work, you can use the `.items()` method to get
all keys and values out at the same time in a `for` loop, like this:

``` {.py}
d = {
    "c": 10,
    "b": 20,
    "a": 30
}

for k, v in d.items():
    print(f"key {k} has value {v}")
```

## Common Built-in Dictionary Functionality

Problem solving step: **Understanding the Problem**.

You have a number of tools in your toolkit for working with dicts in Python:

|Method|Description|
|----------|----------------------------------|
|`.clear()`|Empty a dictionary, removing all keys/values|
|`.copy()`|Return a copy of a dictionary|
|`.get(key)`|Get a value from a dictionary, with a default if it doesn't exist|
|`.items()`|Return a list-ish of the `(key,value)` pairs in the dictionary|
|`.keys()`|Return a list-ish of the keys in the dictionary|
|`.values()`|Return a list-ish of the values in the dictionary|
|`.pop(key)`|Return the value for the given key, and remove it from the dictionary|
|`.popitem()`|Pop and return the most-recently-added `(key,value)` pair|

We already saw a use of `.get()`, earlier, but it can also be modified
to return a default value if the key doesn't exist in the dictionary.

``` {.py}
d = {
    "c": 10,
    "b": 20,
    "a": 30
}

v = d.get("x", -99)  # Return -99 if key doesn't exist

print(v)  # Prints -99, since key `x` doesn't exist
```

We've already seen a use of `.items()`, above. If you want to see just
all the keys or values, you can get an iterable back with the `.keys()`
and `.values()`:

``` {.py}
d = {
    "c": 10,
    "b": 20,
    "a": 30
}

for k in d.keys():
    print(k)   # Prints "c", "b", "a"

for v in d.values():
    print(v)   # Prints 10, 20, 30
```

## Dictionary Comprehensions

Problem solving step: **Understanding the Problem**.

Remember [list comprehensions](#list-comprehensions)? If you don't, pop
over there for a quick refresher, because this is the same thing except
for dictionaries.

You can create a dictionary from any iterable that you can go over in a `for`
loop. This is a pretty powerful way of creating a dictionary if you have the
data in another, iterable, form, like a list or an input stream of something.

Let's go through a list and store the list value as the key, and the list value
times 10 as the value in the dictionary. And let's ignore the number 20 in the
list, just for fun.

``` {.py}
a = [10, 20, 30]
d = { x: x*10 for x in l if x != 20 }

print(d)  # {10: 100, 30: 300}
```

If you have a list of key/value pairs, you can read those into a dictionary
pretty easily, too.

``` {.py}
a = [["alice", 20], ["beej", 30], ["chris", 40]]
d = { k: v for k, v in a }

print(d) # {'alice': 20, 'beej': 30, 'chris': 40}
```

## Dictionaries of Dictionaries

Problem solving step: **Understanding the Problem**.

Here's the deal: the value that you store for a given key can be _anything_!

Well, not like a whale, or Mars, but any data type. So you can store strings,
ints, floats, lists, or even other dictionaries as the value for the dictionary
key!

Check out this _nested declaration_, and check out how we drill down through the
dictionary layers to get to the data:

``` {.py}
d = {
    "a": {
        "b": "Mars! Ha!"
    }
}

print(d)           # {'a': {'b': 'Mars! Ha!'}}
print(d["a"])      # {'b': 'Mars! Ha!'}
print(d["a"]["b"]) # Mars! Ha!
```

Nesting dictionaries like this can be a really powerful method of storing data.

## Dictionaries are reference types

Problem solving step: **Understanding the Problem**.

Remember how we were talking about [references versus values](#ref-val) with
lists? Turns out that dicts are the same.

When you make a copy of a dictionary, it's copying the _reference_ to the same
dictionary, not making a new one.

``` {.py}
d = { "beej": 3490 }

e = d  # both e and d refer to the same dict!

e["beej"] = 3491  # modify it

print(d["beej"])  # 3491
```

If you want to make a copy of a dictionary use one of the following:

``` {.py}
d = { "beej": 3490 }

e = d.copy() # make a copy, the preferred way
e = dict(d)  # make a copy
```

That first way is preferred because it's easier to read, and easy to read code
is _Happy Code_™.

## The Chapter Project

Pop back up top and [refresh on the spec](#dicts-proj-spec) if you need to.
Let's break it down!

Problem solving step: **Understanding the Problem**.
