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
* Dictionaries of Dictionaries

## Chapter Project Specification {dicts-proj-spec}

TODO


## What are Dictionaries?

Problem solving step: **Understand**.

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

Problem solving step: **Understand**.

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

Problem solving step: **Understand**.

Like lists, dicts are really fast at looking up information. In fact, on
average, it takes the same amount of time to get a value out of a dictionary,
_regardless of how many items are in the dictionary_^[Time complexity
enthusiasts will recognize this as $O(1)$, or _constant_ time.].

Keep this fact in mind going forward. We'll get into more complex problems that
can make use of this feature to keep your programs running quickly. _Vroom!_

## Does this `dict` have this key?

Problem solving step: **Understand**.

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

Problem solving step: **Understand**.

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

Problem solving step: **Understand**.

You have a number of tools in your toolkit for working with dicts in Python:

|Method|Description|
|----------|-------------------------------------------------------------------|
|.clear()|Empty a dictionary, removing all keys/values|
|.copy()|Return a copy of a dictionary|
|.get(key)|Get a value from a dictionary, with a default if it doesn't exist|
|.items()|Return a list-ish of the `(key,value)` pairs in the dictionary|
|.keys()|Return a list-ish of the keys in the dictionary|
|.values()|Return a list-ish of the values in the dictionary|
|.pop(key)||Return the value for the given key, and remove it from the dictionary|
|.popitem()|Pop and return the most-recently-added `(key,value)` pair|


