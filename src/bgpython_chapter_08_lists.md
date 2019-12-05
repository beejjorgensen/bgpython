<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Lists

## Objective

* Understand whats lists are
* Understand references versus values
* Access individual elements in a list
* Use common lists built-in functions
* Iterate over lists with `for`
* Construct new empty lists
* Construct new lists with list comprehensions
* Construct and use lists of lists (2D lists)


## Chapter Project Specification

Game time!

Allow the user to navigate a maze by entering directions to move (`n`,
`s`, `w`, or `e`). They can also enter `q` to quit.

The maze should look like this, with `.` representing a space the player
can move into, and `#` representing a wall. An `@` symbol indicates the
player's current position.

Every move, the map should be displayed:

```
#####################
#...#...............#
#...#..........#....#
#...#..........#....#
#...#..........#....#
#...#..@.......#....#
#..............#....#
#..............#....#
#####################

Enter a move (n,s,w,e,q):
```

Keep this project in mind as you read through the chapter.

## What Are Lists?

Remember how regular variables hold one thing? Well, _lists_ are
variables that can hold a lot of things.

> _**Fun Lists Fact**: Most other languages have a different name for
> lists: they call them _arrays_. Same thing._

But wait---if a list can hold a lot of things, how do we differentiate?
How do I tell Python that I want the second thing in the list? Or the
fifth thing?

Luckily it's easy enough; we just have to specify the _index_ into the
list that hold the thing we want.

Think of it like a row of postboxes, numbered starting from `0`, then
`1`, then `2`, and going on up to however many postboxes we have. Each
postbox can hold a thing, and you can refer to it by giving the postbox
number.

Let's take a look at a simple example:

``` {.py}
x = [10, 3, 7, 9]
```

There's a list. We know it's a list because of the square brackets
around it. It's a list of four integers.

Let's print out the zeroth element in the list. We do this by using
square brackets after the list variable name, and giving the index
inside those brackets. Does this look familiar? It's the same syntax we
used to get individual characters out of strings!

``` {.py}
print(x[0])  # prints 10
```

and the element at index 2:

``` {.py}
print(x[2])  # prints 7
```

Remember that indexes start at zero, again, just like with strings.

You can also _set_ individual elements, leaving the rest of the list
unchanged:

``` {.py}
x[1] = 99

print(x[1])  # now prints 99
```

This brings us to a stark difference between lists and strings: _lists
are mutable_. You can change individual elements inside the list
without creating a new list! Remember with strings, you couldn't change
them---you could only make new ones.

It's such a key difference, we're going to talk about it in detail now,
and then again later. This is a big source of confusion among new
developers.


## Reference Versus Value---Fight!

Not really a fight. They're best friends! They wouldn't do that.

Let's go back to regular old variables that hold numbers:

``` {.py}
x = 20
y = x

print(x)   # prints 20
print(y)   # prints 20

y = 99

print(x)   # prints 20
print(y)   # prints 99
```

Take a look at that code. We say that `y` is assigned the value in `x`,
so they both become `20`.

But when we change `y` to `99`, `x` remains unchanged.

It's like `y` got a _copy_ of `x`, so subsequence changes to `y` did
_not_ affect `x`^[The under-the-hood details of how Python handles
assignments like this are rather more complex, and I'm really being
hand-wavy here. But, that said, you can still use this mental model
about making copies and have it work perfectly well.].

