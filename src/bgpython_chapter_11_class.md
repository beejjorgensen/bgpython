<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**.
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**.
-->

# Classes and Objects

## Objective

* Learn what classes and objects are useful for
* Understand the relationship between classes and objects
* Be able to declare a class
* Be able to use that class to instantiate objects
* Understand that objects are reference types
* Understand the relationship between objects and `None`

## Chapter Project Specification {#class-proj-spec}

As you go through the chapter, remember this specification and think
about how we might use the new ideas in this chapter to implement it.
This can absolutely be implemented without using the material in this
chapter, but the goal is to implement it using the info

We want to store data for a number of theaters and the movies that are
being shown at those theaters.

Each movie has:

* A title (string)
* A duration (integer, minutes)
* A genre (string)

Each theater has:

* A name (string)
* A list of movies that are showing at the theater (list of movies)

The output should look similar to this, depending on your theater names
and movies:

```
McMenamin's Old St. Francis Theater is showing:
    Star Wars (scifi, 125 minutes)
    Shawn of the Dead (romzomcom, 100 minutes)
Tin Pan Theater is showing:
    Shawn of the Dead (romzomcom, 100 minutes)
    The World's Fastest Indian (drama, 127 minutes)
Tower Theater is showing:
    Star Wars (scifi, 125 minutes)
    Shawn of the Dead (romzomcom, 100 minutes)
    The World's Fastest Indian (drama, 127 minutes)
```

Note that multiple theaters might be showing the same movie title. Avoid
duplicating the movie data as much as possible. (Remember: Don't Repeat Yourself!)

Stretch goal: also store the per-theater show times for each movie at
that theater.

## What Problem Are We Even Trying To Solve?

Problem-solving step: **Understanding the Problem**.

Let's first learn about the problem we're trying to solve, and then
let's take a look at how classes and objects can help us solve it.

Okay, I said "problem", but it's actually multiple problems. Let's start
with the easier one.

Okay, I said "easier", but really they're the same.

_Get on with it!_

Let's pretend you have a game where you have a starship that has
multiple attributes. For example, it might have two attributes: XYZ
coordinates in 3-space (e.g. `[10, 20, 30]`), and a ship name (e.g.
`"USS Enterprise"`).

These two pieces of information are clearly related. They apply to one
single instance of a starship.

If we have multiple starships in the universe, they'll each have their
own names and coordinates.

So far so good?

Now... how do we store that data with what we know so far?

Well, we have lists, so let's try with those. We'll have three starships
with different names and different locations:

``` {.py}
ship_location = [
    [10, 20, 30],
    [-10, 20, -30],
    [10, -20, 30]
]

ship_name = [
    "MCRN Tachi",
    "Red Dwarf",
    "USCSS Nostromo"
]
```

And then we can access ship #1 like this:

``` {.py}
print(ship_name[1])
print(ship_location[1])
```

So we have two lists, one for name and one for location^[This technique
is called _parallel arrays_ or, in the case of Python, _parallel lists_.
It's not a popular technique today, having been made obsolete by the
very thing we're talking about in this chapter.].

It works, but it's a bummer to have to maintain two (or more) lists this
way. If we ever added a ship, we have to be sure we add all the
information to all the lists and make sure things don't get out of
order. It's easy to make a mistake and get the lists out of sync.

What would be nice is if we could bundle all the information about one
single ship into one single _object_ that held the information about
just that one ship. Other ships would be represented by other objects.
And then we'd have a list of those objects---just one list to maintain!


## What are Classes and Objects?

Problem-solving step: **Understanding the Problem**.

What we're starting to delve into here is the world of _Object-Oriented
Programming_. To discuss _everything_ about it would definitely be
information overload, so we're just going to start with the basics here,
and revisit some of the concepts later.

A bit of terminology here, following up on the starship example from
above.

First of all, we're going to _construct_ new starship _objects_ that
hold all the information about a single ship.

When the object is constructed, it is done based on a blueprint. We call
this blueprint a _class_.

So we're going to define a blueprint for a starship in a class, and then
we're going to build multiple, different starships based on that class.

Let's do this as simply as possible to start. It's not going to be a
common way of doing things, but it's a place to get your feet wet. We'll
fix it soon.

First of all, we'll define a new class. Remember, this is just the
blueprint for starships---it's not a starship itself.

Class names use [flw[camel case|Camel_case]] by convention. Let's define
that starship class!

``` {.py}
class StarShip:
    pass
```

...that's it? What's that `pass` in there?

Okay, you got me. I did say we were going to start simple (and not quite
_Right_), in my defense. What we have there is a class `StarShip`,
except it's like a blank blueprint. There's nothing in it.

The keyword `pass` means "do nothing" in Python. It's just there to
indicate to Python that there's no body inside this class.

> **Random Terminology Facts**: We also say a starship object is an
> _instance_ of the `StarShip` class.
>
> Constructing a new starship object is also referred to as
> _instantiating_ the object from the class. 

Let's go on to make a couple objects from the blueprint.

``` {.py}
class StarShip:
    pass

s0 = StarShip()
s1 = StarShip()
s2 = StarShip()
```

By putting parens after the class name, we're telling Python that we are
creating a new starship object from the `StarShip` class. In fact, we
made three of them, and saved a reference to each in `s0`, `s1`, and
`s2`. Of course, none of them have names or locations, but we'll remedy
that shortly.

If we print one, we get something like this:

``` {.py}
print(s1)  # <__main__.StarShip object at 0x7fa11828c8e0>
```

Not so pretty. But we'll make that better soon, as well.


## Making Different StarShips

Problem-solving step: **Understanding the Problem**.

In the previous example, all our starship objects were identical and
contained no information.

What we need is a way to pass that information in when the starships are
constructed.

We do this by defining a special function _inside_ the class.

> **Another Fun Terminology Fact**: functions declared inside classes
> are called _methods_.

This special function is always named `__init__()` (with the dunders)
and is called _the constructor_.

Let's add a constructor to our `StarShip` class that allows us to pass
in a ship name when the ship is constructed:

``` {.py}
class StarShip:
    def __init__(self, shipname):  # The constructor
        self.name = shipname

s0 = StarShip("MCRN Tachi")
s1 = StarShip("Red Dwarf")
s2 = StarShip("USCSS Nostromo")
```

Whoa, now... that's a lot of hard-to-read punctuation^[In fact, I think
the choice to use all those underscores in `__init__()` is one of the
few bad design choices in the language.] to sift through.

And there's that crazy `self` parameter to the function, whatever that
means!

Let's start with `self`^[A lot of other languages use the variable name
`this` instead of `self`.]. This is one of the hardest concepts to grok
about this chapter, so we'll spend some time on it.

Remember how the class is the blueprint, and the objects are made from
that blueprint?

And how after they're constructed, you get a reference back to that
newly-minted object? (These are the references we were storing in `s0`,
`s1`, and `s2`.)

Well, what about the object that's being constructed _right now_ inside
the `__init__()` method? It already exists, but isn't fully initialized
yet. But inside the constructor, we have a reference to that object that
is being built right now. And that reference is in `self`.

`self` means "the object that this method is operating on".

What's weird is that when we instantiated the starships, we only passed
one argument to `__init()__`.

``` {.py}
s0 = StarShip("MCRN Tachi")
```

When clearly `__init__()` has two parameters: `self` and `name`. What
gives?

``` {.py}
def __init__(self, shipname):  # The constructor
```

Doesn't the number of arguments need to match the number of parameters?

It does! But Python's doing something sneaky behind your back, here.
When a method has been called for a particular object, Python
automagically fills in the first parameter with the object that is being
operated on. We don't have to worry about it.

Python then takes the arguments we _did_ pass, and tacks them on after
that.

Let's take a look at that constructor again:

``` {.py}
class StarShip:
    def __init__(self, shipname):  # The constructor
        self.name = shipname

s0 = StarShip("MCRN Tachi")
```

This is a really common pattern, so let's make sure we understand what's
going on here. In particular, there's a weird dot after `self`. What
does that mean? But before we get there, let's look at `shipname`.

When we create our new starship `s0`, we pass in the name `"MCRN Tachi"`.
This calls the constructor `__init__()`.

Python automatically puts a reference to the object that's now being
constructed into `self`. And then it copies the string `"MCRN Tachi"` to
the `shipname` parameter of the function. So `shipname` is
`"MCRN Tachi"`.

And now we're to the guts of the thing. `self.name`? The saga continues!

## Attributes

Objects have variables attached to them, and we call these
_attributes_^[Technically, even the methods are attributes, but we'll
get into the pedantic details another time.].

Attributes are qualities that an object possesses. For example, a
starship would possess a name. In other words, a starship would have a
name attribute.

And we refer to these attribute by using the dot operator (`.`).

When we have a line like this:

``` {.py}
self.name = shipname
```

We're saying "change the `name` attribute on this starship object to be
the same as the `shipname` parameter that was passed into this method".

This is how we take the ship name that was passed in as an argument and
attach it to the newly-constructed object! We save a reference to the
name in an attribute on the object!

Note that I named `shipname` different than `ship` deliberately. (I did
this to show that they _could_ be different, but also to avoid confusion
when looking at the example.) But it's far more common to just name them
the same thing. This is OK since `self.name`, the attribute on `self`,
is different than `name`, the parameter.

Like so:

``` {.py}
class StarShip:
    def __init__(self, name):  # The constructor
        self.name = name
```

## Using Attributes

Problem-solving step: **Understanding the Problem**.

Now let's add one more thing to our starships: their location.

Instead of passing the location into the constructor, let's just
initialize it to location `[0,0,0]` right off the bat. Then we can
manually set it later.

``` {.py}
class StarShip:
    def __init__(self, name):  # The constructor
        self.name = name
        self.location = [0, 0, 0]   # <-- Add this
```

All ships will now start off at `[0,0,0]` because that's what the
blueprint says they'll do.

And we can print it! We'll access the values in those attributes by
using the dot operator on `s0`!

``` {.py}
s0 = StarShip("MCRN Tachi")

print(s0.name)       # MCRN Tachi
print(s0.location)   # [0, 0, 0]
```

But wait! There's more! That's not all!

You can also _set_ values!

``` {.py}
print(s0.name)   # MCRN Tachi

s0.name = "Rocinante"

print(s0.name)   # Rocinante
```

And we could modify the location of the ship this way, as well:

```
s0.location[1] = 99

print(s0.location)  # [0, 99, 0]
```

_This is important!_ Even though we're changing the values for the
attributes of `s0`, the attributes of the other objects (like `s1` and
`s2`) remain unchanged! (Until we explicitly change them.)

We've successfully bundled all the information about a single ship into
this single object. Nice and consolidated.


## More Methods

Problem-solving step: **Understanding the Problem**.

Let's add another method to set the ship location.

``` {.py .numberLines}
class StarShip:
    def __init__(self, name):  # The constructor
        self.name = name
        self.location = [0, 0, 0]   # <-- Add this

    def set_location(self, x, y, z):
        """Set a ship's location to x,y,z"""

        self.location[0] = x
        self.location[1] = y
        self.location[2] = z

s0 = StarShip("MCRN Tachi")

print(s0.location)  # [0, 0, 0]

s0.set_location(10, 20, 30)

print(s0.location)  # [10, 20, 30]
```

On line 6, we define our new method, `set_location()`. Importantly,
notice the first parameter is `self`, which will be initialized to
represent the object we're setting the location of. (That is, when we
call `s0.set_location()`, `self` will be set to refer to `s0` inside
`set_location()`.)

> **Fun Debugging Fact**: If you get an error about incorrect number of
> arguments to your method, make sure you have `self` as the first
> parameter!

Then on line 17, when we call `set_location()` on `s0`, `self` gets set
to `s0`, and `x`, `y`, and `z` get set to `10`, `20`, and `30`,
respectively.

Then we use `x`, `y`, `z`, and `self` inside the method to change the
values in this ship's location.

This way, when we print it out on line 19, we see the new values there.

Attributes!

## Pretty Printing

Right now when we print one of our starship objects, Python prints
something like this on the screen:

```
<__main__.StarShip object at 0x7fa11828c8e0>
```

Not particularly useful. Let's _override_ that functionality and have it
print something nicer.

Go ahead and add this method to the `StarShip` class:

``` {.py}
    def __str__(self):
        """Return string representation of this object."""
        return f'{self.name}: {self.location}'
```

The `__str__()` method returns a string to use any time an object is
printed.

Now if we build three new ships and print them all:

``` {.py}
s0 = StarShip("Rocinante")
s1 = StarShip("Red Dwarf")
s2 = StarShip("USCSS Nostromo")

s0.set_location(10, 20, 30)
s1.set_location(40, 50, 60)
s2.set_location(70, 80, 90)

print(s0)
print(s1)
print(s2)
```

We get some nice output, like this:

```
Rocinante: [10, 20, 30]
Red Dwarf: [40, 50, 60]
USCSS Nostromo: [70, 80, 90]
```

Perfect!

## Objects are Mutable Reference Types

When you assign one object to another, you don't get a second object.
You get another reference to the first object. Just like happens with
lists and dictionaries.

Or, another way, doing an assignment with an object does _not_ result in
a new object. Both variables are names for the same object. ([Check out
Appendix C for details](#valref).)

``` {.py}
class Forest:
    pass

x = Forest()  # Construct a new object
y = x

x.antelopes = 4

print(y.antelopes)  # 4, since y and x refer to the same object
```

This means you can pass objects to functions as arguments, and the
function can change the values in the object's attributes.

``` {.py}
def set_antelopes_to_10(o):
    o.antelopes = 10

class Forest:
    pass

x = Forest()
x.antelopes = 4

set_antelopes_to_10(x)

print(x.antelopes)  # 10!
```

## Objects and `None`

We've already seen that variables can point to the value `None` to
indicate nothing.

This gets commonly used with objects to indicate some "not found" or
error condition.

For example, let's have a list of objects and a function to search them
by name. The function should return the object that has a `name`
attribute that matches the `name` parameter to the function.

But a question should naturally arise! What if there is no object by
that name in the list? What should the function return? `None` is a
prime candidate here.

``` {.py .numberLines}
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

def get_person_by_name(person_list, name):
    """Return a person object with this name, or None if not found"""
    for p in person_list:
        if p.name == name: 
            # If we found them, return the object
            return p

    # If we got here, we didn't find anyone by that name
    return None

person_list = [
    Person("Annie"),
    Person("Beej"),
    Person("Chris"),
    Person("Dave")   # "Dave's not here"
]

p = get_person_by_name(person_list, "Chris")

print(p)  # "Chris"

p = get_person_by_name(person_list, "Rolo Tomassi")

print(p)  # None
```