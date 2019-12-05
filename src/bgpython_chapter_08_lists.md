<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Lists

## Objective

* Understand whats lists are
* Understand references versus values
* Access individual elements in a list
* Iterate over lists with `for`
* Use common lists built-in functions
* Construct new empty lists of fixed value
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

Problem solving step: **Understand**.

Remember how regular variables hold one thing? Well, _lists_ are
variables that can hold a lot of things.

> _**Fun Lists Fact**: Most other languages have a different name for
> lists: they call them "arrays". Same thing._

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

Do you remember that strings had a cool trick where you could use a
negative index to refer to characters from the end of the string? We can
do the same thing with lists!

``` {.py}
print(x[-1])  # prints 9, the element at the end of the list
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

And with strings, since they're immutable, we end up with the same
situation, more or less.

``` {.py}
x = "Hello"
y = x

print(x)   # prints Hello
print(y)   # prints Hello

y = "world!"

print(x)   # prints Hello
print(y)   # prints world!
```

What we have in this case is what we'll call _value types_. They
have certain charactistics:

* When you assign from a value type variable to another variable, a
  _copy_ of that value gets made.

Value types include (memorize this!):

* Integers
* Floating point numbers
* Strings^[Effectively, since they're immutable. Again with the
  hand-waving here.]

Notably absent from the list are _lists_. Lists are a _reference type_.

Reference types also have certain characteristics:

* When you assign a reference type variable to another variable, both
  variables _refer to the same thing_.

Or, another way, when you assign with a value type, another one of those
comes into existence.

But when you assign with a reference type, there still is only one of
those things. It just has two variables that refer to it. It has two
names.

Still confusing? Let's have an example with a list:

``` {.py}
x = [11, 88, 33, 99]

# At this point, there's one list in memory. Just those 4 numbers.

y = x  # Reference type assignment!

# At this point, there is still only the one list. Both `x` and `y`
# are names for that one list. They both refer to the same list.

# And so:

y[1] = 3490  
print(x[1])  # `x` (yes, `x`!) prints 3490
```

In that example, how can assigning to `y[1]` change the value in `x[1]`?
But that very question is the wrong way of thinking about it. The right
way: since the list is a reference type, both `x` and `y` point to the
_exact same list_ after the assignment. It's not a copy of the list.
It's _the_ list.

After the assignment, it doesn't matter if we refer to the list with `x`
or `y`. They're both names for the same list.

Reference types include the following (some of which we haven't talked
about yet):

* Lists
* Dictionaries
* Objects^[Technically, lists and dictionaries _are_ objects, so we're
  being a bit redundant.]

In summary, there are two categories of data types to keep track of:
value types (like integers and floats and strings), and reference types
(list lists, dictionaries, and objects).

On assignment:

* Value types are copied
* Reference types just refer to the same underlying object

Another way to think of this that might (or might not) help: all
assignments make a copy of a thing. But with value types, that thing
that is copied is the object (the value) itself. With reference types,
the thing that is copied is a _reference to the object_.

A reference is like a street address written on a Post-It note. It's
not the house itself, but it is a reference to it. Now, you can copy
that Post-It note to another, but they still both refer to the same
house. (And certainly the house itself hasn't been copied!)

Even if you don't have it quite down yet, don't worry. We'll hit this
topic a few more times as we progress.


## `for` and Lists---Powerful Stuff

Problem solving step: **Understand**.

Remeber our good friend the `for` loop? We used it with `range` to loop
a number of times, and we used it with strings to loop over each
character in the string.

We can also use it with lists^[Technically we can use it to iterate over
anything that's _iterable_, which is quite a number of things.] to do
things with each list element in order!

Here's a simple example that prints all the elements in a list:

``` {.py}
x = [11, 55, 33, 99]

for i in x:
    print(f"element is: {i}")
```

and this will output:

```
element is: 11
element is: 55
element is: 33
element is: 99
```

But wait, there's more!

Recall from above that you can get the element out of a list if you
know its index, for example, `x[2]`.

Let's put those together in another way to use `for` and lists. This
example does the same thing as the one above, just in a different way:

``` {.py}
x = [11, 55, 33, 99]

for i in range(4):
    print(f"element is: {x[i]}")
```

Although that's not idiomatic Python^[Idiomatic means "the standard,
accepted way of doing a thing in a language".] (the first example is
better), it demonstrates how to use a variable _as the index_. We refer
to `x[i]` inside the loop, and then have `i` change to loop over every
element's index.

It's irking me that we have that hard-coded `4` in the `range()`. It
only works for lists of length `4`. Let's see if we can fix it.

Sneak preview: you can get the number of elements in a list with
`len()`.

Let's make the `range()` go up to "the length of the list" instead of to
`4`:

``` {.py}
x = [11, 55, 33, 99]

for i in range(len(x)):             # <---
    print(f"element is: {x[i]}")
```

And now that works for lists of any length---much better!


## `for` and `enumerate()`

Problem solving step: **Understand**.

In the examples above, we used `for` with the elements in the list
themselves, and also with `range()` over the indexes of the elements in
the list.

What if you want to do both at the same time? That is, you want the
elements _and_ you want the indexes?

A function that's worthy of mention is `enumerate()`. It will iterate
through each element in the list, returning the element and its index.
You can get them both at the same time!

``` {.py}
x = [11, 55, 33, 99]

for i, v in enumerate(x):
    print(f"The element at index {i} has value {v}")
```

This results in:

```
The element at index 0 has value 11
The element at index 1 has value 55
The element at index 2 has value 33
The element at index 3 has value 99
```

## Midterm: Doubling The Values

Problem solving step: **Understand**.

Let's write some code that takes a list and goes through all the
elements in that list. If an element is _even_, we should multiply the
value by `2`. If it's odd, we should do nothing with it.

For example, if the input list is:

``` {.py}
[1, 2, 3, 4, 5, 6]
```

after processing and doubling all the even values, it will be:

``` {.py}
[1, 4, 3, 8, 5, 12]
```

Problem solving step: **Make a Plan**.

We know we need to iterate over the list, so that sounds like a job for
a `for`-loop. And we need to test if a number is even or odd, which
sounds like a job for a `if` statement.

> How can we tell if a number is odd?
> 
> There's a very common way to do this. Divide by `2` and take the
> remainder. If the remainder is `1`, it's odd. If it's `0`, it's even.
>
> Do you remember how to take the remainder in Python? With the _modulo_
> operator: `%`.
>
> ``` {.py}
> x = 12
>
> if x % 2 == 0:
>   print("x is even!")
> else:
>   print("x is odd!")
> ```

So our plan is shaping up like this:

```
for each element in the list:
    if that element is even:
        double the value and store it at the same place in the list
```

Then maybe print it out at the end, just for fun.

Problem solving step: **Code It Up**.

Here's each line of the plan's pseudocode [flx[converted to
Python|listdouble.py]]:

``` {.py .numberLines}
x = [1, 2, 3, 4, 5, 6]

# for each element in the list

for i, v in enumerate(x):

    # if that element is even

    if v % 2 == 0: # check if v is even

        # double the value and store it at the same place in the list
        x[i] = v * 2

print(x)  # Print it out, just for fun
```

And the output:

```
[1, 4, 3, 8, 5, 12]
```

_Voila!_ There it is!

Problem solving step: **Postmortem**.

Anything you could make better about this?

Instead of using `enumerate()`, you could have used
`for`-`range()`-`len()` like we did in an earlier example. Would you
have felt that produced cleaner code?

(Remember: _coding is creative_. There are a lot of solutions. It's up
to you as a dev to make informed decisions about which methods you like
more than others!)

One interesting thing to note is that on line 14, we just printed the
entire list in one go. You can do that! `print()` prints out the string
version of whatever you pass in. More on that in the future.


## Build-in Functions for Lists

There are a number of very useful built-in functions and
methods^[Remember that a method is a function that you call on a
particular object with the dot (`.`) operator.] that you can use with
lists. Some we've already seen.

In the following table, the variable `a` represents a list.

|Function|Description|
|:---------------|:---------------------------------------------------|
|`len(a)`        |Return the number of elements in the list|
|`enumerate(a)`  |Iterate over index/value pairs in the list|
|`a.append(x)`   |Append variable `x` to the end of the list|
|`a.clear()`     |Clear all elements from the list|
|`a.copy()`      |Make a copy of the list|
|`a.count(v)`    |Count the number of occurrences of `v` in the list|
|`a.extend(b)`   |Add elements of list `b` to end of list `a`|
|`a.index(v)`    |Return the first index of `v` in list `a`|
|`a.insert(i,v)` |Insert `v` in list `a` before index `i`|
|`a.pop()`       |Remove and return the last element in `a`|
|`a.pop(i)`      |Remove and return the element at index `i` in `a`|
|`a.reverse()`   |Reverse the elements in the list|
|`a.sort()`      |Sort the list|

Let's just fire up the editor and start messing around with these to see
how they work.

Here's a program called [flx[`listops.py`|listops.py]] that does just
that. You should also experiment with variations of these to get a feel
for them:

``` {.py .numberLines}
a = [5, 2, 8, 4, 7, 4, 0, 9]

print(len(a))   # 8, the number of elements in the list

a.append(100)

print(a)  # [5, 2, 8, 4, 7, 4, 0, 9, 100]

print(a.count(4))  # 2, the number of 4s in the list

print(a.index(4))  # 3, the index of the first 4 in the list

v = a.pop()  # Remove the 100 from the end of the list

print(v)   # 100
print(a)   # [5, 2, 8, 4, 7, 4, 0, 9]

a.reverse()   # Reverse the list

print(a)   # [9, 0, 4, 7, 4, 8, 2, 5]

a.insert(2, 999)  # insert 999 before index 2

print(a)   # [9, 0, 999, 4, 7, 4, 8, 2, 5]

b = [1, 2, 3]

a.extend(b)  # Add contents of b to end of a

print(a)   # [9, 0, 999, 4, 7, 4, 8, 2, 5, 1, 2, 3]

a.sort()   # Sort all elements

print(a)   # [0, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 999]

a.clear()  # Remove all elements

print(a)   # [], an empty list of length 0
```

In addition to those functions, the `+` operator will take two lists and
concatenate them together into a third list:

``` {.py}
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b  # c refers to a new list [1, 2, 3, 4, 5, 6]

# lists a and b are unchanged
```

Look at the amount of control we have over lists now! Not only can you
read and write values at specific list indexes, but you can add to the
end, insert stuff in the middle, remove from the end, or from anywhere
within the list.

You are _All Powerful!_

Okay, maybe not, but at least you can do a thing or two with lists.


## What Good Are They?

"So I can become some kind of list ninja. What good does that do me?"

When it comes to anything in programming, it's often helpful to try to
think of physical, actual-real-life examples. What are some of the lists
you have in real life? You can use Python lists to store those.

Shopping lists, bowling scores, favorite rocks, employee names, numbers,
etc., etc.

``` {.py}
shopping_list = [
    "spam",
    "eggs",
    "bacon",
    "sausage",
    "spam",
    "spam"
]
```

Sometimes we know those lists up front, and other times we compute them
as we go.


## Midterm Challenge

Problem solving step: **Understand**.

More math! _[Groan!]_ Let's compute the Fibonacci Sequence! _[Yay!]_

The Fibonacci Sequence is a famous mathematical sequence (a progression
of related numbers) that runs like this:

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...$

Before I give it away, study it a bit---can you see the pattern?

Lots of times, the job of a dev is to find patterns in data so that you
can write code that generates them.

Spoiler alert!

Each number is the sum of the previous two numbers.

$0+1=1$, $1+1=2$, $1+2=3$, etc.

But what about the first two numbers in the sequence

Those are given to be $0$ and $1$, no questions asked. This way you
always have at least two previous numbers to get the next one.

What we want to do is write a program that builds and prints a list
containing the first 100 Fibonacci numbers. We don't want to do any of
the addtion ourselves---we want the code to compute it for us.

Problem solving step: **Make A Plan**.

We're going to need a list to hold all the numbers.

We have the first two numbers ($0$ and $1$), so we can put those in the
list.

Then we have to look at the previous two numbers from the end, add them
together, and then append the sum to the end of the list.

And we have to do that 98 more times to get 100 numbers.

Doing something 98 times seems like a `for`-`range()` loop to me.

We can append with the `.append()` method.

We can get the last and previous-to-last elements in the list with
negative list indexes.

```
initialize the list with [0, 1]

for 98 times:
    compute the sum of the previous two numbers
    append sum to the list

print the list
```

Time to code it up!

Problem solving step: **Code It Up**.

[flx[`fiblist.py`|fiblist.py]]:

``` {.py .numberLines}
# initialize the list with [0, 1]
fib = [0, 1]

# for 98 times
for _ in range(98):

    # compute the sum of the previous two numbers
    s = fib[-1] + fib[-2]

    # append sum to the list
    fib.append(s)

# print the list
print(fib)
```

And you'll get some output that looks vaguely like this (I've rewrapped
the output here---yours might not be so pretty):

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296,
433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976,
7778742049, 12586269025, 20365011074, 32951280099, 53316291173,
86267571272, 139583862445, 225851433717, 365435296162, 591286729879,
956722026041, 1548008755920, 2504730781961, 4052739537881,
6557470319842, 10610209857723, 17167680177565, 27777890035288,
44945570212853, 72723460248141, 117669030460994, 190392490709135,
308061521170129, 498454011879264, 806515533049393, 1304969544928657,
2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464,
14472334024676221, 23416728348467685, 37889062373143906,
61305790721611591, 99194853094755497, 160500643816367088,
259695496911122585, 420196140727489673, 679891637638612258,
1100087778366101931, 1779979416004714189, 2880067194370816120,
4660046610375530309, 7540113804746346429, 12200160415121876738,
19740274219868223167, 31940434634990099905, 51680708854858323072,
83621143489848422977, 135301852344706746049, 218922995834555169026]
```

Problem solving step: **Postmortem**.

Notice how the list grows bigger and bigger each step of the loop. If
we were to print out the list every iteration of the loop, we'd see
something like this:

```
[0, 1]
[0, 1, 1]
[0, 1, 1, 2]
[0, 1, 1, 2, 3]
[0, 1, 1, 2, 3, 5]
[0, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8, 13]
```

and so on. We're constructing the list as we go, building it from the
previous elements^[We're using a technique here generally called
_bottom-up dynamic programming_. But that's a story for another time.
Probably involving Fibonacci again.].

Another thing I did in the `for` loop was use `_` as the looping
variable name. That's a perfectly legitimate variable name^[Names can
be made up of letters, digits, and underscores, as long as they don't
start with a digit.].

By convention, `_` is used as a name when you don't intend to use it
elsewhere.

You _must_ have a variable named in your `for` loop---no option not to.
But using `_` for that name indicates to programmers that you are just
using the loop to count, and you don't actuall care what the count is.


