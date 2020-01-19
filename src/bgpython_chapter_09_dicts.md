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

Let's store some genealogical^[This is all about family trees. Did you
know I'm related to Queen Elizabeth II (by marriage)? I'm her mother’s
sister’s husband’s father’s father’s sister’s daughter’s husband’s
wife’s (_drama!_) sister’s husband’s father’s brother’s son’s son’s
daughter’s son’s daughter’s son. For realsies! I'm willing to bet that
you're related to Queen Elizabeth II, as well. That makes us cousins!]
data!

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

(Ok, I hear you saying, "Wait, your mom and dad were both Jorgensens?
That's suspicious. I mean, I'm not saying, but I'm just saying." Hold
your tongue! I can assure you they're not related^[Except via Queen
Elizabeth II, like the rest of us.].)

We want to write an app that will allow you to print out the birthdays
of the parents of any given person.

Example:

```
Enter a name (or q to quit): Beej Jorgensen
Parents:
    Mom Jorgensen (1970)
    Dad Jorgensen (1965)
```

So we'll need some way to store that, and some way to look through the
data to get information about other people who are referenced.

Yes, we could use lists of people and just search through, but there's a
less clunky way we might go about doing this.

This chapter is all about how we might store such data.


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
average, it takes the same amount of time to get a value out of a
dictionary, _regardless of how many items are in the dictionary_^[Time
complexity enthusiasts will recognize this as $O(1)$, or _constant_
time.].

Keep this fact in mind going forward. We'll get into more complex
problems that can make use of this feature to keep your programs running
quickly. _Vroom!_

## Does this `dict` have this key?

Problem solving step: **Understanding the Problem**.

If you have a dictionary, it's nice to be able to check to see if a key
even exists.

The secret to doing this is the `in` statement that will return a
Boolean indicating if a key is in a dict.

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

There is also a way to get an item out of a dictionary using the
`.get()` method. This method returns a default value of `None`^[If you
haven't seen it before or need a refresher, this is a value that
represents "no value". It's a placeholder (what we call a _sentinel
value_) to indicate a no-value condition.] if the key doesn't exist.

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

Remember how you could iterate over all the elements in a list with
`for`? Well, we can do the same thing with dictionaries. Except in this
case, we'll be looping over the _keys_ in the dictionary, not the
values.

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

Note that in the latest version of Python, the keys come out in the same
order they've been added to the dictionary.

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

And now we have this, where the keys have been sorted alphabetically^[Or
what we call _lexicographically sorted_. It's like alphabetical, but on
steroids so that it can handle letters, numbers, punctuation and so on,
all of which are all numbers deep down.].

```
key a has value 30
key b has value 20
key c has value 10
```

Also, similar to how lists work, you can use the `.items()` method to
get all keys and values out at the same time in a `for` loop, like this:

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

You have a number of tools in your toolkit for working with dicts in
Python:

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

You can create a dictionary from any iterable that you can go over in a
`for` loop. This is a pretty powerful way of creating a dictionary if
you have the data in another, iterable, form, like a list or an input
stream of something.

Let's go through a list and store the list value as the key, and the
list value times 10 as the value in the dictionary. And let's ignore the
number 20 in the list, just for fun.

``` {.py}
a = [10, 20, 30]
d = { x: x*10 for x in l if x != 20 }

print(d)  # {10: 100, 30: 300}
```

If you have a list of key/value pairs, you can read those into a
dictionary pretty easily, too.

``` {.py}
a = [["alice", 20], ["beej", 30], ["chris", 40]]
d = { k: v for k, v in a }

print(d) # {'alice': 20, 'beej': 30, 'chris': 40}
```

## Dictionaries of Dictionaries

Problem solving step: **Understanding the Problem**.

Here's the deal: the value that you store for a given key can be
_anything_!

Well, not like a whale, or Mars, but any data type. So you can store
strings, ints, floats, lists, or even other dictionaries as the value
for the dictionary key!

Check out this _nested declaration_, and check out how we drill down
through the dictionary layers to get to the data:

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

Nesting dictionaries like this can be a really powerful method of
storing data.

## Dictionaries are reference types

Problem solving step: **Understanding the Problem**.

Remember how we were talking about [references versus values](#ref-val)
with lists? Turns out that dicts are the same.

When you make a copy of a dictionary, it's copying the _reference_ to
the same dictionary, not making a new one.

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

That first way is preferred because it's easier to read, and easy to
read code is _Happy Code_™.

## The Chapter Project

Pop back up top and [refresh on the spec](#dicts-proj-spec) if you need
to. Let's break it down!

Problem solving step: **Understanding the Problem**.

The goal of the project is to, for a given person, print out their
parents' names as well as their year of birth.

Pretty straightforward, but the devil's in the details!

Problem solving step: **Devising a Plan**.

If we look at a sample record, we can see that a dict lends itself quite
well to the data, with keys `born`, `mother`, `siblings`, etc.

```
Beej Jorgensen:
    Born: 1990 [yes, I'm 29, is my story I'm sticking to]
    Mother: Mom Jorgensen
    Father: Dad Jorgensen
    Siblings: [Brother Jorgensen, Sister Jorgensen, Little Sister Jorgensen]
```

Not only that, but we can store all of _those_ dicts in another
container dict which uses the person's name as the key!

``` {.py}
tree = { # Outer dict holds records for all the people
    "Beej Jorgensen: {  # Inner dict holds details for each person
        "born": 1990,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": [
            "Brother Jorgensen",
            "Sister Jorgensen",
            "Little Sister Jorgensen"
        ]
    }
}
```

So that looks like a reasonable approach to storing data. We can just
add the other people to the dictionary at that outermost layer.

Not only that, but we now have part of the problem solved. If the user
enters "Beej Jorgensen", all we have to do is look that directly up in
the outer dict, and then we can print out my parents' names!

Of course, we're still missing out on printing their birth years, but
let's tackle the smaller problem first, and _then_ figure out how to
extract that missing data.

We'll come back to the "Understanding the Problem" step in a while to
revisit that.

Problem solving step: **Carrying out the Plan**

We'll start with a simple tree of just a single person. Let's keep it as
simple as possible, and then go from there.

``` {.py .numberLines}
tree = {
    "Beej Jorgensen": {
        "born": 1990,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": [
            "Brother Jorgensen", 
            "Sister Jorgensen",
            "Little Sister Jorgensen"
        ]
    }
}
 
```

And now let's add some code to get the person's name, or quit if they
enter "`q`":

``` {.py .numberLines startFrom=14}
done = False

while not done:
    name = input("Enter a name (or q to quit): ")

    if name == "q":
        done = True
        continue  # Jump back to the top of the loop
 
```

And, finally, let's print out the person's name and their parents' names:

``` {.py .numberLines startFrom=23}
    record = tree[name]  # Look up the record in the outer dict

    mother_name = record["mother"]  # Extract parent names from inner dict
    father_name = record["father"]

    print("Parents:")
    print(f'    {mother_name}')
    print(f'    {father_name}')
```

Giving this a run, we get some good output!

```
$ python3 familytree.py
Enter a name (or q to quit): Beej Jorgensen
Parents:
    Mom Jorgensen
    Dad Jorgensen
Enter a name (or q to quit): q
```
    
We're still missing the parents' birth years, but, like I said, we'll
tackle that later.

What happens if we run it with an unknown name? Remember that when
you're testing your code, you should think like a villian and enter the
most unexpected things you can.

Let's try it with someone it doesn't know.

```
$ python3 familytree.py
Enter a name (or q to quit): Arch Stanton
Traceback (most recent call last):
  File "familytree.py", line 23, in <module>
    record = tree[name]  # Look up the record in the outer dict
KeyError: 'Arch Stanton'
```

Well, that's ugly. It would be much nicer to print out some kind of
error message.

What does the spec say we should do?

...nothing! It says nothing about this case! That's not useful! The spec
is missing information!

True, it is.

Turns out, this is a really common thing when programming. Your boss
asks you to implement a thing, but doesn't fully define what that thing
is. It's not that your boss is bad at this; it's just that writing down
the exact spec and not leaving anything out is _hard_.

I promise you that if I asked you to write out the rules to
Tic-Tac-Toe^[That's Noughts and Crosses, to some of you.], I'd find
something you left out. ("You never said my 'X' could only take up one
grid square!")

The right thing to do at this point is go back to the creator of the
specification and ask exactly what should happen in this case.

Problem solving step: **Understanding the Problem** (again)

"Hey, specification writer! What do we do if the person doesn't exist in
the data?"

Answer: print out an error message like this:

```
No record for "Arch Stanton"
```

All right!

Problem solving step: **Devising a Plan** (again)

We're using this code to get a person's record:

``` {.py}
record = tree[name]  # Look up the record in the outer dict
```

but as we see, that throws an exception if `name` isn't a valid key in
the dict.

How can we handle that? There are a couple ways. One of them involves
_catching_ the exception, but we'll talk more about that in a later
chapter.

Something we can do that we discussed earlier in this chapter is to use
the `.get()` method on the dict. This will return the record, or `None`
if the key doesn't exist in the dict. Then we can test for that and
print out some error messages.

Problem solving step: **Carrying out the Plan** (again)

``` {.py .numberLines startFrom=23}
    record = tree.get(name)  # Look up the record in the outer dict

    if record is None:  # Use "is" when comparing against "None"
        print(f'No record for "{name}"')
        continue

    mother_name = record["mother"]  # Extract parent names from inner dict
    father_name = record["father"]

    print("Parents:")
    print(f'    {mother_name}')
    print(f'    {father_name}')
```

Now we're getting pretty close. But we still are missing one big piece:
the birth years of the parents.

Getting their names was cake: it was right there in the record for the
person we're looking up. But their birth years aren't in there.

How do we get them?

Problem solving step: **Devising a Plan** (again)

We have the names for the parents. That's it.

How do we go from a name to a birth year?

Looks like "Beej Jorgensen" has a birth year listed in his record...

We should add records for "Mom Jorgensen" and "Dad Jorgensen" and then
they can have their own birth years.

But the question still remains: how can we go from the user-entered
"Beej Jorgensen" to the birth years for his parents?

What we're doing here is trying to tie one piece of data ("Beej
Jorgensen") to other pieces of data (1965 and 1970, his parents' birth
years.)

This is _super_ common in programming. "How do I get from x to y?" We
need to find the path.

So let's see... we have Beej Jorgensen there, with his parents' names
listed.

That's a start. But given his parents' names, how do you get his
parents' birthdays?

Yes! You just take their names and look them up in the dictionary!

Except we haven't added them yet. Let's do that now. (Note that program
line numbers, below, are reset at this point.)

``` {.py .numberLines}
tree = {
    "Beej Jorgensen": {
        "born": 1990,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": [
            "Brother Jorgensen", 
            "Sister Jorgensen",
            "Little Sister Jorgensen"
        ]
    },
    "Mom Jorgensen": {
        "born": 1970,
        "mother": "Grandma Jorgensen",
        "father": "Grandpa Jorgensen",
        "siblings": ["Auntie Jorgensen"]
    },
    "Dad Jorgensen": {
        "born": 1965,
        "mother": "Granny Jorgensen",
        "father": "Grandad Jorgensen",
        "siblings": ["Uncle Jorgensen"]
    }
}
 
```

And then the main loop logic (unchanged from before):

``` {.py .numberLines startFrom=26}
done = False

while not done:
    name = input("Enter a name (or q to quit): ")

    if name == "q":
        done = True
        continue  # Jump back to the top of the loop
 
    record = tree.get(name)  # Look up the record in the outer dict

    if record is None:  # Use "is" when comparing against "None"
        print(f'No record for "{name}"')
        continue

    mother_name = record["mother"]  # Extract parent names from inner dict
    father_name = record["father"]
 
```

Except now, when we print out the parents, we have to look up the
mother's and father's record.

``` {.py .numberLines startFrom=44}
    # Get the parent records
    mother_record = tree.get(mother_name)
    father_record = tree.get(father_name)

    # Get the birth year of the mother; note if missing
    if mother_record is not None:
        mother_born_date = mother_record["born"]
    else:
        mother_born_date = "missing record"

    # Get the birth year of the father; note if missing
    if father_record is not None:
        father_born_date = father_record["born"]
    else:
        father_born_date = "missing record"

    print("Parents:")
    print(f'    {mother_name} ({mother_born_date})')
    print(f'    {father_name} ({father_born_date})')
```

That's it!

Problem-solving step: **Looking Back**

What could we do better? What are the shortcomings of this app?

Look at the dictionary structure we used to store the data. How could
that be better? Think of all the cases that exist in family trees. Sure,
we covered the common case, but what about kids who were adopted? How do
we model that? Divorces? Second marriages? It turns out that modelling a
family tree is far more complex that you might originally anticipate.

What if two people have the same name? In a real family tree, it's
entirely likely there could be multiple Tom Jones^[It's not unusual.] in
the family tree. But since we're using the name as the key in the dict,
and keys have to be unique, we're in trouble. Ergo, the name can't be
the key---something unique must be.

One option there is to use a
[fl[UUID|https://en.wikipedia.org/wiki/Universally_unique_identifier]]
as the key, and map that UUID to names somehow. Maybe you have _another_
dict that, for a given name, stores a list of UUIDs that represent
people who have that name. Then we could ask the user, "Did you mean the
Beej Jorgensen who was born in 1971, 1982, 1997, or 2003?" if there were
multiple Beej Jorgensens.

Lots of options for improvement, here!

## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

Use any knowledge you have to solve these, not only what you learned in
this chapter.

