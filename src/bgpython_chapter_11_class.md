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
* How to test to see if an object has an attribute or not

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
* A list of movies that are showing at the theater (list)

The output should look similar to this, depending on your theater names
and movies:

```
McMenamin's Old St. Francis Theater is showing:
    Star Wars (scifi, 125 minutes)
    Shaun of the Dead (romzomcom, 100 minutes)
Tin Pan Theater is showing:
    Shaun of the Dead (romzomcom, 100 minutes)
    Citizen Kane (drama, 119 minutes)
Tower Theater is showing:
    Star Wars (scifi, 125 minutes)
    Shaun of the Dead (romzomcom, 100 minutes)
    Citizen Kane (drama, 119 minutes)
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

Problem-solving step: **Understanding the Problem**.

Objects have variables attached to them, and we call these
_attributes_^[Technically, even the methods are attributes, but we'll
get into the pedantic details another time.].

Attributes are qualities that an object possesses---what things it
_has_. For example, a starship would possess a name. In other words, a
starship would have a name attribute.

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


## More on Methods

Problem-solving step: **Understanding the Problem**.

Remember that methods are functions that are connected to the object.
Just like you could think of attributes as things the object _has_, you
can think of methods like things the object _does_.

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
    Person("Chris")
]

p = get_person_by_name(person_list, "Chris")

print(p)  # "Chris"

p = get_person_by_name(person_list, "Dave")

if p is None:
    print("Dave's not here.")
```

## Testing for Attributes

Sometimes at runtime you want to see if an object has an attribute or
not. Or maybe you have the attribute name as a string and you want to
get or set that attribute on an object.

Three built-in functions help make this happen:

* `hasattr()` tests to see if an attribute exists on an object.
* `getattr()` returns the value of an attribute, optionally returning a
  default value if the attribute doesn't exist.
* `setattr()` sets the value of an attribute, creating it if it doesn't
  exist.

This gives you more flexibility in writing your objects, because
then you can have _optional_ attributes on them.

Let's demo!

``` {.py}
class Foo:
    pass

f = Foo()
f.bar = 12

print(hasattr(f, "bar"))    # True
print(hasattr(f, "frotz"))  # False

print(getattr(f, "bar"))           # 12
print(getattr(f, "frotz", None))   # None, since attr frotz doesn't exist

setattr(f, "frotz", 99)  # Just like saying "f.frotz = 99"

print(f.frotz)  # 99
```

I wouldn't say that these functions get a lot of day-to-day use, but
they're a powerful thing to add to your toolkit.


## Chapter Project

In case you've forgotten, [review the chapter project specification at
the beginning of this chapter](#class-chap-proj).

Problem-solving step: **Understanding the Problem**.

Looks like we need to store information about a number of theaters, as
well as information about a number of movies.

And a movie might be showing in multiple theaters simultaneously.

Problem-solving step: **Devising a Plan**

There are a lot of ways to store this data. But since this chapter is
all about classes and objects, how about we use those?

Looks like we should have a `Theater` class to handle information about
each theater.

And a `Movie` class to handle information about each movie.

And a theater can be showing several movies, so we can give it an
attribute that is a list of movies that is currently showing there.

We'll also keep a list of all the theaters and a list of all the movies,
as well.

Problem-solving step: **Carrying Out the Plan**

Here's a theater class. We pass a name to the constructor, but
initialize the movies to an empty list. We can fill them in later.

``` {.py .numberLines}
class Theater:
    """Holds all the information about a specific theater."""
    def __init__(self, name):
        self.name = name
        self.movies = []
 
```

and a movie class:


``` {.py .numberLines startFrom="7"}
class Movie:
    """Holds all the information about a specific movie."""
    def __init__(self, name, duration, genre):
        self.name = name
        self.duration = duration
        self.genre = genre
 
```

So far so good.

Now we need to instantiate a bunch of movies so that we can add them to
the theaters' `.movie` lists.

There are a couple things we could do.

We could use one variable per movie, but that's a bit unwieldy. Let's
use some kind of collection, like a list! We'll make one for all the
movies and all the theaters. Go ahead and add your favorites.

``` {.py .numberLines startFrom="14"}
movies = [
    Movie("Star Wars", 125, "scifi"),
    Movie("Shaun of the Dead", 100, "romzomcom"),
    Movie("Citizen Kane", 119, "drama")
]

theaters = [
    Theater("McMenamin's Old St. Francis Theater"),
    Theater("Tin Pan Theater"),
    Theater("Tower Theater")
]
 
```

Take a look in there to see what we've done. Notice that `movies` is a
list, and inside the list, while we're initializing it, we're
constructing new `Movie` objects.

And we do the same thing with `theaters`. It's a list of
newly-constructed `Theater` objects.

Nextly, we need to associate those movies with the theaters that are
showing them.

Remember that each `Theater` object has a list of movies in its
`.movies` attribute. So we need to append the movies to that list.

This next bit is a little cryptic, so make sure

``` {.py .numberLines startFrom="26"}
# McMenamin's is showing Star Wars and Shaun of the Dead
theaters[0].movies.append(movies[0])
theaters[0].movies.append(movies[1])
 
```

What's that saying?

Well, take it a bit at a time, each line from left to right.

What's `theaters[0]`?

If we look in our `theaters` list, we see that's McMenamin's. 

And then we get its movie list with `theaters[0].movies`.

Its movies list is a list, so we can use the `.append()` list method to
add a movie to it. But which movie to append?

We append `movies[0]`... and if we look in our `movies` list, we see
that's _Star Wars_.

So `theater[0]` is McMenamin's, and `movies[0]` is _Star Wars_.

That means the first line, above, is saying, "Append 'Star Wars' to
McMenamin's list of currently-showing movies."

And the line below that is saying, "Append 'Shaun of the Dead' to
McMenamin's list of currently-showing movies."

Let's do some more. What do each of these lines do?

``` {.py .numberLines startFrom="30"}
# Tin Pan is showing Shaun of the Dead and Fastest Indian
theaters[1].movies.append(movies[1])
theaters[1].movies.append(movies[2])

# Tower is showing all three
theaters[2].movies.append(movies[0])
theaters[2].movies.append(movies[1])
theaters[2].movies.append(movies[2])
 
```

What we've done here, effectively, is linked up all the movie objects
with their respective theaters.

Notice how movies are listed in multiple theaters. For example
`movies[0]` (_Star Wars_) is in `theaters[0]` (McMenamin's) **and** also
in `theaters[2]` (Tower).

Does that mean there are two copies of the _Star Wars_ `Movie` object?
Since it's in two theaters?

Think carefully!

No, there's just one! The one we created back on line 15! Since it's an
object, making a "copy" through assignment (or with `.append()`) just
makes another reference to the same object. There's only one, but it's
referred two by two `Theater` objects. And also referred to by the
`movies` list. So many references to the same object for good memory
savings.

Now we want to print out all the theaters and their showtimes. I'm going
to make a helper function here to print a single theater's data. We'll
pass in a reference to a theater object, print its name, and then print
the data for all the movies in its `.movies` list.

``` {.py .numberLines startFrom="39"}
def print_theater(theater):
    """Print all the information about a theater."""

    print(f'{theater.name} is showing:')

    for m in theater.movies:
        print(f'    {m.name} ({m.genre}, {m.duration} minutes)')
 
```

And lastly, all we have to do is call `print_theater()` for all the
theaters in our `theaters` list:

``` {.py .numberLines startFrom="47"}
# Main code
for t in theaters:
    print_theater(t)
```

There we have it! ([flx[Solution|moviesign.py]].)

Problem-solving step: **Looking Back**.

Check out how we looked at the problem description (which basically said
"theaters show movies, and a movie might be shown at multiple theaters")
and mapped that into two classes to hold the information per theater and
per movie.

Notice how the classes keep all the information for a theater or movie
in a self-contained single object. Nice and clean, plus it's easy to
pass around a reference to an object if another function wants to use
it.

What are some shortcomings?

Those lines where we add the movies to theaters are pretty hard to read.
And they refer to things like `movies[0]` instead of referring to them
by name.

It might be convenient to have some kind of helper function that could
look up the movie object by name, similar to this:

``` {.py}
def find_movie_by_name(movies, name):
    for m in movies:
        if m.name == name:
            return m

    return None   # Didn't find it
```

and use that to clean up the code a bit. And something similar for
theaters. (Of course, the more movies you have, the longer it takes to
find one. A dictionary might be a faster data structure to use here.)

But this approach doesn't handle the case where there are two movies or
theaters of the same name. So another workaround would have to be found
there---maybe a unique identifier number for each theater and movie that
we'd key off instead?

Now... what about that stretch goal to add movie times to all this?

Problem-solving step: **Understanding the Problem**.

This one might not seem tricky at first, but it comes to get you with
the details.

You might think, no problem, we'll just add times to the `Movie` class,
right?

Yes, but... Different theaters are all showing the same movie. But at
different times.

If you think about it, the times a movie is showing is more data
attached to the _theater_, and not really data attached to the the
_movie_. It would make no sense for Disney to say, "Coming this Winter:
Star Wars Episode 47, at 8 pm and 10 pm!" They don't know when theaters
are going to show the movie!

Okay, then, let's attach the times to the `Theater` class.

But this presents us with another problem. How do we associate a set of
times with a particular `Movie` object? We need a way in code to show
that they're linked so that we can print them out together.

Problem-solving step: **Devising a Plan**

We can do this with a new class---call it `MovieTime`---that contains
both a reference to a movie _and_ a list of times that movie is showing.
And then we can add instances of this new class to the `Theater`
objects.

In this way, if we have a reference to a `Theater`, we can look up its
list of `MovieTime` objects, and then for each of those, look up the
`Movie` object reference contained within and print it out along with
the times.

We're shimming a new class in the middle with _both_ the movie and the
showtimes. This is how we can bundle that together.

Problem-solving step: **Carrying Out the Plan**

Let's add that new class that holds both a reference to a movie as well
as the times it's showing:

``` {.py}
class MovieTime:
    """Holds a movie and the times it is playing"""
    def __init__(self, movie, times):
        self.movie = movie
        self.times = times
```

Then we need to modify the `Theater` class to have a list of `MovieTime`
objects instead of `Movie` objects.

``` {.py}
class Theater:
    """Holds all the information about a specific theater."""
    def __init__(self, name):
        self.name = name
        self.movietimes = []   # <-- Now this is MovieTime objects
```

And now when we construct our lists of theater information, we need to
add new `MovieTime` objects to the list in the theater. The `MovieTime`
objects contain references to the movie being shown, as well as a list
of show times.

``` {.py}
# McMenamin's is showing Star Wars and Shaun of the Dead
theaters[0].movietimes.append(MovieTime(movies[0], ["7pm", "9pm", "10pm"]))
theaters[0].movietimes.append(MovieTime(movies[1], ["5pm", "8pm"]))

# Tin Pan is showing Shaun of the Dead and Fastest Indian
theaters[1].movietimes.append(MovieTime(movies[1], ["2pm", "5pm"]))
theaters[1].movietimes.append(MovieTime(movies[2], ["6pm", "8pm", "10pm"]))

# Tower is showing all three
theaters[2].movietimes.append(MovieTime(movies[0], ["3pm"]))
theaters[2].movietimes.append(MovieTime(movies[1], ["5pm", "7pm"]))
theaters[2].movietimes.append(MovieTime(movies[2], ["6pm", "7pm", "8pm"]))
```

Lastly, when we print it out, we need to extract the movie and the show
times from the `MovieTime` object so we can print them:

``` {.py}
def print_theater(theater):
    """Print all the information about a theater."""

    print(f'{theater.name} is showing:')

    for mt in theater.movietimes:
        m = mt.movie
        t = " ".join(mt.times) # Make string of times separated by spaces
        print(f'    {m.name} ({m.genre}, {m.duration} minutes): {t}')
```

And that's that!

Output now looks like this:

```
McMenamin's Old St. Francis Theater is showing:
    Star Wars (scifi, 125 minutes): 7pm 9pm 10pm
    Shaun of the Dead (romzomcom, 100 minutes): 5pm 8pm
Tin Pan Theater is showing:
    Shaun of the Dead (romzomcom, 100 minutes): 2pm 5pm
    Citizen Kane (drama, 119 minutes): 6pm 8pm 10pm
Tower Theater is showing:
    Star Wars (scifi, 125 minutes): 3pm
    Shaun of the Dead (romzomcom, 100 minutes): 5pm 7pm
    Citizen Kane (drama, 119 minutes): 6pm 7pm 8pm
```

([flx[Solution|moviesign2.py]].)

Problem-solving step: **Looking Back**.

Aside from the improvements noted in the last "Looking Back", we might
be able to fix this one up a bit with respect to how it handles times.

Right now, we're storing the times in strings, but it would be better to
store them as [fl[`datetime` objects from the Python standard
library|https://docs.python.org/3/library/datetime.html]].

This would enable us to do date math with the show times, e.g. to tell
the user how many minutes until the next showing.

## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

Use any knowledge you have to solve these, not only what you learned in
this chapter.

1. Write a class that describes a car. What are the attributes the class
   would have? What methods? (There's no one right answer here---thing
   freely.)

   ([flx[Potential Solution|ex_car.py]].)

2. Write a class called `SubwayCar` that represents a single train car
   on a subway train. What attributes would it have? What methods?

   Add a `name` attribute to the class so you can name the cars.

   Add a `next` attribute to the class that points to the next
   `SubwayCar` in the train. This should refer to the next `SubwayCar`
   instance, or to `None` if it's the last car.

   Have a variable, `head`, that points at the first subway car.

   This way you can "hook together" a train, like this (pseudocode):

   ``` {.py}
   head = SubwayCar("Engine")
   car1 = SubwayCar("Passenger car 1")
   car2 = SubwayCar("Passenger car 2")
   car3 = SubwayCar("Passenger car 3")

   head.next = car1
   car1.next = car2
   car2.next = car3
   car3.next = None   # End of the train
   ```

   Now have a variable, `location`, that is your current location in the
   train. Start it at the `head`:

   ``` {.py}
   location = head
   ```

   Then write a loop to "walk" the `location` variable down the train
   (by following the `next` pointers), printing out the name of each car
   as it goes, until it reaches the end.

   This famous data structure is actually called a _linked list_. But I
   disguised it as a subway train so as to be less intimidating.

   ([flx[Solution|ex_subway.py]].)

3. Make a `Room` class that has a `name` attribute.

   Also give it `n_to`, `s_to`, `w_to`, and `e_to` attributes. These
   will refer to the room that are north, south, west, and east of a
   particular room. `None` in one of these attributes means there's no
   exit that direction.

   For example, two rooms that are hooked up west to east (and vice
   versa) could be constructed like this:

   ``` {.py}
   room0 = Room("Cobble Crawl")
   room1 = Room("Debris Room")

   room0.e_to = room1  # east from Cobble Crawl to Debris Room
   room1.w_to = room0  # west from Debris Room to Cobble Crawl
   ```

   Make 5-6 rooms and hook them up in various directions.

   Now have a variable, `location`, that is the current player location
   in the world. Start it pointing to the starting room, e.g.:

   ``` {.py}
   location = room0
   ```

   Next, get player input of either `n`, `s`, `w`, or `e`, and change
   location to the room in the specified direction.

   If there's no room there, print the string `"You can't go that
   way."`.

   If the user enters `q`, quit the game.

   ([flx[Solution|ex_adv2.py]].)


## Summary

All kinds of goodies in this chapter! We dipped our toes in the magical
world of classes and objects, which is the beginning of learning
the world-famous Object-Oriented Programming (OOP).

We saw how we could concisely bundle data and functionality into a
single convenient class, and the make objects from the class, using the
class as a blueprint.

And, importantly, we learned that multiple variables can refer to the
same object---that objects are _not_ copied when you make an assignment.

Finally, we touched on the idea that `None` could be used to indicate
"absence of an object".

Though objects and classes form the basis for OOP, we really haven't
touched on what that means yet. But that's a story for another chapter.