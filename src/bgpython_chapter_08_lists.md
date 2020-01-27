<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Lists

## Objective

* Understand whats lists are
* Understand references versus values
* Access individual elements and slices in a list
* Iterate over lists with `for`
* Use common lists built-in functions
* Construct new empty lists of repeating fixed values
* Construct new lists with list comprehensions
* Construct and use lists of lists (2D lists)


## Chapter Project Specification {lists-proj-spec}

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

Problem solving step: **Understanding the Problem**.

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

Keeping with the "things you can also do with strings" theme, you can
also slice an array, just like a string.

``` {.py}

a = [1, 2, 3, 4, 5]

b = a[1:-1]   # Slice all but the first and last elements

print(b)  # [2, 3, 4]
```

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


## Reference Versus Value---Fight! {ref-val}

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

It's like `y` got a _copy_ of `x`, so subsequent changes to `y` did
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
have certain characteristics:

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

What if you _want_ a copy of a list, and not just a copy of the
reference? You can force a list copy a number of ways, but these are
three common ones:

``` {.py}
b = a.copy()  # Copy with .copy() method
b = list(a)   # Copy with the list() function
b = a[:]      # Copy by slicing the entire list
```

Even if you don't have it quite down yet, don't worry. We'll hit this
topic a few more times as we progress.


## `for` and Lists---Powerful Stuff

Problem solving step: **Understanding the Problem**.

Remember our good friend the `for` loop? We used it with `range` to loop
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

Problem solving step: **Understanding the Problem**.

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

Problem solving step: **Understanding the Problem**.

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

Problem solving step: **Devising a Plan**.

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

Problem solving step: **Carrying out the Plan**.

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

Problem solving step: **Looking Back**.

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


## Built-in Functions for Lists

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

Problem solving step: **Understanding the Problem**.

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
the addition ourselves---we want the code to compute it for us.

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

Problem solving step: **Carrying out the Plan**.

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

Problem solving step: **Looking Back**.

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

## Building New Lists, Repeating and Empty

Problem solving step: **Understanding the Problem**.

We've already seen how to initialize a list with a few elements in it:

``` {.py}
a = [11, 55, 33, 99]
```

You can multiply a list by a constant value to get a new list repeated
that many times.

What?

Easier demonstrated:

``` {.py}
a = [11, 99]
b = a * 3

print(b) # [11, 99, 11, 99, 11, 99]
```

It just repeats the list that many times into a new list.

A very common use of this is to create a new list of a certain number of
elements, initialize to zero:

``` {.py}
a = [0] * 10
print(a)   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
```

While we're on about esoteric list declarations, you can declare a list
of no elements like so"

``` {.py}
a = []
```

presumably to compute values for later.

## List Comprehensions {list-comprehensions}

Problem solving step: **Understanding the Problem**.

This is a really neat language feature of Python. It allows you to
construct a new list from an old one, modifying and filtering elements
as you go.

Before going into the syntax, we'll write something using what we know
so far with `for` and `if` and see how that looks. Then we'll compare it
to a list comprehension version.

I'm going to write some code that takes a list and produces a new list
from it, not including all the odd numbers, and replacing the even
numbers with the even number times 4.

``` {.py}
a = [1, 2, 3, 4, 5, 6]
new_list = []

for v in a:
    if v % 2 == 0:  # if v is even
        new_list.append(v * 4)

print(new_list)   # [8, 16, 24]
```

Study that until you're sure you have it down.

Now, here's that same program as a list comprehension:

``` {.py}
a = [1, 2, 3, 4, 5, 6]
new_list = [v * 4 for v in a if v % 2 == 0]

print(new_list)   # [8, 16, 24]
```

Well, it's certainly more concise!

But it's also, I'm suspecting you're finding, a lot harder to read.
Yeah.

It's _always_ like this when you try to pick up a new piece of weird
syntax you've never seen before. At first, it's all weird, but the more
you study it, the more used to it you get.

What I _don't_ want is for you to look at it and think, "It's
unreadable! Forget it!"

All you have to do is take it a step at a time.

What do we have in that line?

``` {.py}
#          result    loop        filter
#          |----| |--------| |-----------|
new_list = [v * 4 for v in a if v % 2 == 0]
```

It's split into three parts.

The "result": this is what values will be included in the output list.
The variable named here is the one in the "loop" clause.

The "loop": assigns elements from the list into a variable, repeatedly.

The "filter" (optional): only elements for which the condition is true
will be included in the output.

If we wanted to include only the _odd_ numbers times 4, we could have
done this:

``` {.py}
#          result    loop        filter
#          |----| |--------| |-----------|
new_list = [v * 4 for v in a if v % 2 == 1]
```

Or the odd numbers divided by 3:

``` {.py}
#          result    loop        filter
#          |----| |--------| |-----------|
new_list = [v / 3 for v in a if v % 2 == 1]
```

Leaving the filter off makes the list unconditionally. For example, all
the numbers in the list times 4:

``` {.py}
#          result    loop
#          |----| |--------|
new_list = [v * 4 for v in a]
```

When should I use them?

Any time you're making a new list from an existing one and you want to
optionally change or filter elements from the original list, list
comprehensions are a great tool to us.

## Lists of Lists

Problem solving step: **Understanding the Problem**.

You can have lists of just about anything in Python. Lists of numbers,
lists of strings, lists of lists...

That's right, folks. Lists containing other lists. How does that work?

Here's one example where we'll make a bunch of lists, and then put them
in another list.

``` {.py}
x = [1, 2, 3]
y = [4, 5, 6]
z = [x, y]
```

Remember that _lists are reference types_. So we have a list `x` and
`y`, and both of these are _referred to_ in list `z`.

In that example, how could we access elements of the lists-in-list?

We're going to use square bracket notation again, but even more-so.

``` {.py}
x = [1, 2, 3]
y = [4, 5, 6]
z = [x, y]

print(z[0]) # z[0] refers to x, so this prints [1, 2, 3]
print(z[1]) # z[1] refers to y, so this prints [4. 5. 6]
```

So far so good?

Here's the thing to notice: since `z[0]` and `z[1]` are lists, you can
access the elements within those lists by using square bracket notation
_again_.

Let's try to get the number `6` out of that second list.

``` {.py}
print(z[1][2]) # prints 6
```

Take apart that line of code. What's happening there?

First Python evaluates the first square brackets it comes to. It knows
`z` is a list, and so it evaluates `z[1]` to get the list `[4, 5, 6]`.
Then it takes that list and evaluates it with `[2]`, getting the `6` out
of it.

Another way to think of it would be to imagine using parentheses:

``` {.py}
(z[1])[2] # first evaluate z[1], then evaluate [2] on the result

z[1][2]   # this is equivalent to the previous line
```

(While Python doesn't mind if you use parentheses like this, programmers
don't do it since it makes the code look messy.)

But what does this buy us? Lists of lists are exciting and all. (Right?)
What are they useful for?

Having a list of lists literally adds a second dimension to the data you
can represent. With a single list, you can represent one "row" of data.
With a list of lists, you can represent multiple rows or a _grid_ of
data.

What are some places in computing a grid or multiple rows of data are
used?

Spreadsheets! What else? See if any other ideas come to mind.

For declaring lists of lists, it's really common to just declare them
all at once, and not use intermediate variable to represent the
sublists.

For example, the previous list we were using, above, could be declared
more simply like so:

``` {.py}
z = [
    [1, 2, 3],
    [4, 5, 6]
]
```

or, if it looks better and your style guide allows it, you can put it on
one line:

``` {.py}
z = [ [1, 2, 3], [4, 5, 6] ]

print(z[0][1])  # Prints 2
```

Now let's see if we can put it all together for this chapter's project!


## Chapter Project Implementation

This is the big one. This project is going to draw on multiple things
we've learned so far and put them all together into a working solution.

That makes this project more difficult that the previous ones. We're
going to break down the problem and decide what tools we know that we
can bring to bear to solve it.

And this is what being a software developer is all about.

I'm not expecting the answer to be obvious. It's rare you'll see a
problem that has an obvious solution, even as a seasoned developer. But
we do have our problem solving framework to break down the problem into
workable parts. So let's do it!

Problem solving step: **Understanding the Problem**.

We want to do several things with this project:

* Print a map on the screen
* Get user input
* Use the input to move a player indicator around the map
* Make sure the player doesn't move through walls
* Keep repeating until the player quits

What's missing from [the spec](#lists-proj-spec) that we need to know?

Remember your compass directions?

```
    N
    |
W --+-- E
    |
    S
```

Now's the time to get the answers to questions clarified. Much easier to
do it now than after you've coded up the wrong thing!

What if the user provides invalid input? What happens then is missing
from the spec. For that, let's print an error message:

```
Unknown command: {x}
```

Where `x` is whatever the user entered.

What if the player tries to move through a wall? Let's use this error
message:

```
You can't go that way.
```

Anything else missing from the spec?

Problem solving step: **Make A Plan**.

We're going to make use of two important techniques as we make this
plan: _simplify the problem_ and _breaking down subproblems_.

Simplifying the problem means to take our eventual goal and remove
requirements to make it easier to code. Sure, eventually we'll have to
add those requirements back in, but simplifying the problem makes the
initial coding easier.

What are examples of things we can simplify about this project? Here are
some ideas:

* Don't bother putting the `@` on the map where the player is
* Allow the player to move through walls
* Keep repeating forever, ignoring `q`
* Don't validate user input

Again, we'll have to add this eventually, but removing them temporarily
makes it much easier to reach an initial version.

The other technique, breaking down subproblems, is a variant of what
we've been doing already.

Let's start with high-level pseudocode, and then break it down where
required.

```
while not quit:
    print map and player indicator
    get input
    make sure input is valid
    make sure we're not moving through walls
```

How do we know that breaking down subproblems will be useful with this
pseudocode? The first clue is that some of the steps are substantial,
e.g. "print map and player indicator" immediately brings to mind the
question, "How the heck can we do that?"

If any steps are too complex or are unclear, it means you have to break
them down farther. Let's do that for all the unclear sections:

```
while not quit:
    print map and player indicator
    for each row of the map:
        for each column of the map:
            if this is where the player is:
                print @
            else:
                print the map character

    get input
    make sure input is valid

    if input invalid:
        print error message

    elif input is "q":
        quit

    else:
        figure out the new row and column of the player

    if the map at the new player position is "#":
        print "You can't go that way."
    else:
        set the current position to the new position
```

That's significantly better. It'll be a lot easier to translate to
Python.

Now... how are we going to store the data we need for this project? And
what data do we need, anyway?

* The map representation
* The player's current position, row and column

How are we going to store the map? In the spec, it's displayed as text,
like so:

```
#####################
#...#...............#
#...#..........#....#
#...#..........#....#
#...#..........#....#
#...#..........#....#
#..............#....#
#..............#....#
#####################
```

where `#` is a wall and `.` is empty floor (that we can move through).

We could store all that as a single string... but that might make our
lives a little more difficult since we have to put an `@` in where
the player is located.

And, because of that, we're planning to print the map out a character at
at a time so we can decide if we're going to draw an `@` or the map
character.

What would be a more sensible way to store the map rather than a single
big string?

Ponder that for a second.

Spoiler alert!

How about a list of strings? One string would be one row of the map.
Then we could go through the single row a character at a time and decide
what to print. (Remember we can use array bracket notation on a string
to get single characters out!)

Look at all the techniques we're using!

* Variables to store player's current row and column on the map
* A list of strings to store the map
* Iterating through a list with `for`
* Iterating through strings for `for`
* Nested `for` loops
* `if` conditions to decide what to do with user input
* `if` conditions to determine if we can move that direction
* Booleans and a `while` loop to run the game until the user quits

Holy moly! That's a lot of stuff. But that's what we do as software
developers: we take all we know and figure out how to put it together
into the solution.

And it's rarely an obvious one. We all have to work hard to come up with
the answers.

Problem solving step: **Carrying out the Plan**.

Before we start this phase, I want you to notice how much time we've
spend on the Understand and Plan phases without writing any code at all.
It's very tempting, especially for junior devs, to want to jump into the
code without spending sufficient time on Understanding and Planning.
Unfortunately, this practice causes one to waste productivity
unnecessarily.

You're not done understanding the problem until you have no more
questions about.

You're not done making a plan until you know how to convert every step
of the plan to code.

If you spend enough time understanding an planning, coding almost
becomes an afterthought.

And here we are. Let's take our pseudocode and convert it into Python.

Coming back to _simplify the problem_, let's start off by just storing
and printing the map. No player, no input, no loop. Let's just get that
working.

First of all, we need to store the map data, so let's do that:

``` {.py .numberLines}
# The map

map_data = [
    "#####################",
    "#...#...............#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#..............#....#",
    "#..............#....#",
    "#####################"
]
```

We've split the map list onto multiple lines to make it easier to read.

Now we need to print it out. In our pseudocode, we used a nested `for`
loop with `if` conditions.


``` {.py .numberLines}
# The map

map_data = [
    "#####################",
    "#...#...............#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#..............#....#",
    "#..............#....#",
    "#####################"
]

# Print map and player indicator

for row in map_data:  # for each row
    for map_character in row:  # for each col
        print(map_character, end="")
    print()
```

There are a couple things to note there, so make sure to digest the
code. We're going through each row, and for each row, we're going
through each column and printing the character.

We want the characters to all print on the same line for a given row, so
we use the `end=""` trick to keep Python from going to the next line.

And at the end of each row we have an empty `print()` to get the cursor
down to the next line for starting to print the next row.

And when we run that, we get the map printed out!

But we don't have the player position stored anywhere, and we're not
showing it on the screen. Let's add that next.

``` {.py .numberLines}
# The map

map_data = [
    "#####################",
    "#...#...............#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#..............#....#",
    "#..............#....#",
    "#####################"
]

# Player position

player_row = 4          # <-- add player position
player_column = 9

# Print map and player indicator

# Use enumerate() to get the row and column indexes for the if:
for row_index, row in enumerate(map_data):  # for each row
    for col_index, map_character in enumerate(row):  # for each col
        if row_index == player_row and col_index == player_column:
            print("@", end="")  # end="" no newline
        else:
            print(map_character, end="")
    print()
 
```

So there we've added a couple variables to store where the player is,
and then in the map printing loop we check to see if this location is
where the player is. If it is, print an `@`, otherwise print the map
character.

For the next small thing to add, let's get user input and quit if the
user enters "`q`". Otherwise, we'll print the map again in a loop.

``` {.py .numberLines}
# The map

map_data = [
    "#####################",
    "#...#...............#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#..............#....#",
    "#..............#....#",
    "#####################"
]

# Player position

player_row = 4
player_column = 9

quit = False

while not quit:

    # Print map and player indicator

    for row_index, row in enumerate(map_data):  # for each row
        for col_index, map_character in enumerate(row):  # for each col
            if row_index == player_row and col_index == player_column:
                print("@", end="")  # end="" no newline
            else:
                print(map_character, end="")
        print()

    # Get input

    command = input("Enter a move (n,s,w,e,q): ")
 
    if command == "q":
        quit = True
        continue  # jump right back to the top of the while
    else:
        print(f'Unknown command {command}')
```

Getting there!

Something new to note! There's a `continue` statement on line 40. This
causes program execution to jump back to the top of the `while` loop,
ignoring the rest of the loop body. It means, "Don't do anything else in
this block---just short circuit back to the `while` condition. (Which
tests to false immediately and exits the loop.)

So now we have the player position being printed, and we have the user
inputting a command. However, we still need to handle the directional
commands and actually move the player around.

Our plan is to compute the new position for the player based on the
current position and the user input. For example, if the user goes north
(up) on the screen, the player's column stays the same, but the row
number decreases by 1.


``` {.py .numberLines}
# The map

map_data = [
    "#####################",
    "#...#...............#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#...#..........#....#",
    "#..............#....#",
    "#..............#....#",
    "#####################"
]

# Player position

player_row = 4
player_column = 9

quit = False

while not quit:

    # Print map and player indicator

    for row_index, row in enumerate(map_data):  # for each row
        for col_index, map_character in enumerate(row):  # for each col
            if row_index == player_row and col_index == player_column:
                print("@", end="")  # end="" no newline
            else:
                print(map_character, end="")
        print()

    # Get input

    command = input("Enter a move (n,s,w,e,q): ")
 
    # Figure out the new row and column of the player
    # Make sure input is valid
    if command == "n":
        new_row = player_row - 1
        new_column = player_column
    elif command == "s":
        new_row = player_row + 1
        new_column = player_column
    elif command == "w":
        new_row = player_row
        new_column = player_column - 1
    elif command == "e":
        new_row = player_row
        new_column = player_column + 1
    elif command == "q":
        quit = True
        continue  # jump right back to the top of the while
    else:
        print(f'Unknown command {command}')

    # Set the current position to the new position
    player_row = new_row
    player_column = new_column
```

That's working great, but we can still walk through the walls. Let's
change those last few lines of the program to verify that the new
position is an empty room before we move the player in there. (Note the
line numbers!)

``` {.py .numberLines startFrom="58"}
    if map_data[new_row][new_column] != ".":
        print("You can't move that way!")
    else:
        # Set the current position to the new position
        player_row = new_row
        player_column = new_column
```

Woo! You've written your very own [flw[Roguelike|Roguelike]] game!

Problem solving step: **Looking Back**.

For next steps, consider adding some of the following:

* Treasures
* Monsters
* Stats
* Weapons
* Whatever you desire! It's your game!

Just back to "Understand the Problem" and implement some of those
things.

Also, the game looks neater if you clear the screen before printing the
map, but unfortunately there's no easy way to do this in a
cross-platform manner^[Well, not at this point in our learning,
anyway.]. But there is a hacky thing we can do.

If your terminal obeys [flw[ANSI escape codes|ANSI_escape_code]], which
is likely, we can send special sequences of characters to it to clear
the screen then home the cursor (move it to the top left).

The magical incantation looks like this:

``` {.py}
print("\x1b[2J\x1b[H", end="")  # Clear the screen
```

Go ahead and tuck that up above where you start printing the map and
you'll see the effect. If your terminal doesn't support ANSI sequences,
you'll just see some weird characters.
[fl[Bogus|https://www.youtube.com/watch?v=q3fx6TugN7g]].

If you really want to get into character graphics, there's a library you
should try: [fl[curses|https://docs.python.org/3/howto/curses.html]]. It
allows you to clear the screen, position the cursor, get input without
echoing it to the screen or waiting for `RETURN`, output in color, and
more.

Although we have enough knowledge to add monsters and treasure and so
on, it will be easier to do so once we learn about dictionaries and
objects in future chapters. We have more tools at our disposal!

## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

Use any knowledge you have to solve these, not only what you learned in
this chapter.

1. The following code prints out `99`:

   ``` {.py .numberLines}
   a = [1, 2, 3]
   b = a

   b[0] = 99

   print a[0]
   ```

   How can we change only line 2 so that `b` is a copy of `a`, causing
   the program to print out `1` instead?

   ([flx[Solution|ex_refval.py]].)

2. Write a loop that prints out the total sum of the following list:

   ``` {.py}
   [14, 31, 44, 46, 54, 59, 45, 55, 21, 11, 8, 34, 66, 41]
   ```

   The sum is 529.

   ([flx[Solution|ex_listsum.py]].)

3. Take the following list:

   ``` {.py}
   [11, 22, 33]
   ```

   and write one line of Python that changes the list to:

   ``` {.py}
   [11, 22, 33, 99]
   ```

   Then write another line that changes _that_ list to:

   ``` {.py}
   [11, 33, 99]
   ```

   Then, finally, write another line that changes the list to:

   ``` {.py}
   [11, 33, 88, 99]
   ```

   This exercise should manipulate the same list, not create new lists.

   ([flx[Solution|ex_listchange.py]].)

4. Create the following list in under 20 characters of Python code:

   ``` {.py}
   [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
   ```

   ([flx[Solution|ex_replist.py]].)

5. Using a list comprehension, make a new list from the following that
   only includes numbers that are multiples of 5:

   ``` {.py}
   [14, 31, 44, 46, 54, 59, 45, 55, 21, 11, 8, 34, 66, 41]
   ```

   ([flx[Solution|ex_listcompx5.py]].)

6. Using a list comprehension, make a new list from the following that
   only includes all-uppercase versions of all words that begin with a
   consonant.

   ``` {.py}
   ["alice", "beej", "chris", "dave", "eve", "frank"]
   ```

   Sample output:

   ```
   ['BEEJ', 'CHRIS', 'DAVE', 'FRANK'] 
   ```

   ([flx[Solution|ex_listcompcap.py]].)

7. Write a program that generates a list of lists (2D list) containing a
   multiplication table up to $12\times12$.

   You should be able to print the result of, say, $7\times5$ like so:

   ``` {.py}
   print(multtable[7][5])  # prints 35
   ```

   ([flx[Solution|ex_listmult.py]].)


## Summary

Look at all the stuff we've covered this chapter!

* A brand new data structure to hold lists of information
* Understanding _reference_ versus _value_ assignments
* How to access and change items in a list
* How to modify and copy the list
* How to create new lists of repeating values
* List comprehensions! Wow!
* Lists of lists!

Lists are a powerful tool to add to our arsenal. We're going to make
heavy use of them as our programs get more complex.
