<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Functions

## Objective

* Understand what functions are and how they're useful
* Be able to use built-in functions
* Understand what function arguments are
* Be able to write your own functions
* Be able to write good functions
* Understand the difference between positional arguments and keyword arguments


## Chapter Project Specification {#func-proj-spec}

Allow the user to enter the locations of several starships in 3D space.

These should be entered as _x_,_y_,_z_ triplets when prompted. When the
user enters "done", stop entering ship locations.

```
Enter ship location x,y,z (or "done"): 10,20,30
Enter ship location x,y,z (or "done"): -17,16,50
Enter ship location x,y,z (or "done"): 0,13,30
Enter ship location x,y,z (or "done"): 5,20,-40
Enter ship location x,y,z (or "done"): done
```

Then print out a grid of the distances between them. The grid's top row
and left column should indicate the ship number (starting with 0).

Crossing a column with a row should give you the distance between the
ships.

Distances should be printed to 2 decimal places in fields of width 8.

We'll use a variant of the [flw[Pythagorean
Theorem|Pythagorean_theorem#Euclidean_distance]] to find the distance
between two 3D points.

$d=\sqrt{(x_0-x_1)^2+(y_0-y_1)^2+(z_0-z_1)^2}$

For each pair of 3D points, we take the difference in the X coordinates
squared, plus the difference in the Y coordinates squared plus the
difference in the Z coordinates squared, and then we take the square
root of that whole thing. And that's the distance between the two
points.

Example output (corresponding to the example input, above):

```
               0       1       2       3
       0    0.00   33.84   12.21   70.18
       1   33.84    0.00   26.42   92.74
       2   12.21   26.42    0.00   70.53
       3   70.18   92.74   70.53    0.00
```

So we can see ship #2 (along the top) is distance 26.42 from ship #1
(along the left). And notice the diagonal is all `0.00`, which makes
sense because every ship is zero distance from itself.

Keep this project in mind as we go through the chapter.

## What Are Functions?

You're about to seriously level up in programming by learning how to do
this, and it's not even that difficult. Functions are the key to getting
away from the toy programs we've been doing so far and doing _real_
programs.

So what are they?

Problem solving step: **Understanding the Problem**.

Functions are self-contained pieces of code that you can _call_ that do
a specific thing.

Does this sound at all familiar? Because we've been doing this the whole
time with the built-in `print()` function.

> Not to be confused with _statements_ like `for` and `if`. Know a
> function because it has parenthesis right after the name that you can
> use to pass _arguments_ to the function^[Purists will point out
> exceptions to this, like with `__add__()`, but let's skip that for
> now.].

The `print()` function has built-in functionality to print things on the
screen. Thankfully (really, really) we don't have to write that code
ourselves. We can just say:

``` {.py}
print(23 + 34)
```

and have `print()` do all the dirty work of getting us the answer
printed to the screen.

We've also used the `input()` function to get a string entered from the
keyboard.

``` {.py}
name = input("Enter your name: ")
```

This turns out to be a great way to simplify and organize code. Can you
imagine if you had to put all the code in to print out something on the
screen every time you wanted to print something? Much easier to _define_
the `print()` function once, and then use it over and over again by
calling it.

We have an important principle in computer programming called the
[flw[DRY principle|Don%27t_repeat_yourself]] (_Don't Repeat Yourself_).
If you can remove as much repetitive code as you can and move it to a
function, that makes your code easier to read and maintain. DRY code is
happy code.

Not only can we use functions to make DRY code, we can also use them to
organize our code into logical sections, even if a function is called
only one time.

It is clearer to have your functionality in discrete sections that you
call in sequence rather than just having a single huge block of code
that does everything

## Using Built-In Functions

Problem solving step: **Understanding the Problem**.

Python has a _lot_ of built-in functions that you can use. It's not
necessary to memorize the usage in detail (you can always look up the
details), but it's a good idea to skim their descriptions just so you
can recall that they exist.

We've already used `print()` and `input()` quite a bit, but there are
plenty more. [fl[Look them up
online|https://docs.python.org/3/library/functions.html]].

Here are some common ones, though this is not an exhaustive list:

|Built-in Function|Description|
|-|-|
|`abs()`|Return the absolute value of a number.|
|`bin()`|Return a string representing the number in binary.|
|`chr()`|Return a character for the Unicode (and ASCII) value passed in.|
|`dir()`|Return a list of methods on this object.|
|`enumerate()`|Return an iterator over a list of (index, value) pairs.|
|`filter()`|Repeatedly run a function on items of a list filtering some out.|
|`float()`|Convert a number or string to a floating point value.|
|`help()`|Get help on a data type.|
|`hex()`|Return the hexadecimal representation of a number.|
|`input()`|Get input from the keyboard and return that string.|
|`int()`|Convert a floating point or string to an integer value.|
|`isinstance()`|Return true if an object is an instance of a class.|
|`len()`|Return the length of an iterable, like a list or string.|
|`map()`|Run a function on every value in an iterable, returning the results.|
|`max()`|Return the maximum of the arguments or of an iterable.|
|`min()`|Return the minimum of the arguments or of an iterable.|
|`ord()`|Return the Unicode value (code point) for a given character.|
|`pow()`|Return a base value raised to an exponent.|
|`print()`|Print to the console.|
|`range()`|Return an iterator that runs over a range of values.|
|`reversed()`|Return an iterator over a reversed version of the argument.|
|`round()`|Round a number to the nearest whole number.|
|`sorted()`|Return a sorted version of an iterable.|
|`str()`|Convert a value to a string.|
|`sum()`|Return the sum of all arguments and/or of an iterable.|
|`super()`|Get access to an object's superclass.|
|`zip()`|Merge parallel lists into a dictionary.|

These are all available for use at any time in your program.

## Arguments

> "Oh look, this isn't an argument."
>
> "Yes it is."
> 
> "No it isn't. It's just contradiction."
>
> "No it isn't."
>
> ---_Excerpt from Monty Python's Argument Clinic sketch_

Problem solving step: **Understanding the Problem**.

When you call a function, the things you put in the parentheses are
called the _arguments_ to the function. Arguments are separated by commas.

``` {.py}
print(2)        # 1 argument
print(2, 3)     # 2 arguments
print(2, 3, 4)  # 3 arguments
print()         # 0 arguments
```

The arguments are the way you can pass data _into_ a function to have it
operate on that data to produce a result.

We refer to them by number, as well. "Pass the number of goats in as the
second argument to the function."

Functions often take a specific number of arguments. But, like we see
above with `print()`, they can take variable numbers of arguments, too.

## Writing Your Own Functions

> "What do you like most about hacking?"
>
> "The power."
>
> ---_A good friend of mine trolling a reporter at [fl[DEFCON
> 2|https://www.defcon.org/html/defcon-2/defcon-2.html]]_

The power. This is where we fly. Writing your own functions. This is
where we get to DRY our code, organize it better, and make it more
readable overall.

Problem solving step: **Understanding the Problem**.

All programmers use their own functions heavily, and to great effect.

Let's say we want to write a program that adds 13 to a number, and then
divides the resultant sum by 7.

No problem. We got this. Let's do it with 30.

``` {.py}
print((30 + 13) / 7)
```

Great! Oh, and we also need it for 8, 19, 21, 37, 402, 516, 1024, and
3490.

OK. Still no problem.

``` {.py}
print((30 + 13) / 7)
print((8 + 13) / 7)
print((19 + 13) / 7)
print((21 + 13) / 7)
print((37 + 13) / 7)
print((402 + 13) / 7)
print((516 + 13) / 7)
print((1024 + 13) / 7)
print((3490 + 13) / 7)
```

Great! Oh, did I say "divide by 7"? I'm sorry, that should be "multiply
by 7".

And here we get a taste of why DRY code is good code. Since the spec
changed^[This happens all the time in development.], we have to go back
and modify all those lines of code to make them right.

If only we hadn't repeated ourself, we might have been able to only
change it in one place. This would also be better because we wouldn't be
taking the risk of missing a place we should have changed the code.

But how to do it?

With... _FUNCTIONS_! Let's write a function to do that math and return
the result. Then we can just call it over and over, like this:

``` {.py}
print(do_the_math(30))
print(do_the_math(8))
print(do_the_math(19))
print(do_the_math(21))
print(do_the_math(37))
print(do_the_math(402))
print(do_the_math(516))
print(do_the_math(1024))
print(do_the_math(3490))
```

Sure, we're repeating the function name `do_the_math()`, but we're not
repeating the actual mathematical expression, itself, which is what
matters.

But how do we define the function `do_the_math()`?

We use the `def` statement, like this:

``` {.py .numberLines}
def do_the_math(x):
    result = (x + 13) * 7

    return result

answer = do_the_math(30)
print(answer)
```

The indented stuff after the `def` is called the _function body_. That's
where all the work gets done.

There's a lot of stuff to unpack here, so let's take it nice and slow.

### Line 1: defining the function {.unlisted .unnumbered}

When we say `def do_the_math`, we're telling Python, "Hey, I'm making a
brand new function from scratch called `do_the_math`.

The part in the parentheses describes what _arguments_ can be passed to
this function. In this case, we can pass a single argument to our
function. It will be represented inside the function by the variable
`x`.

When we call the function on line 6, `x` will be initialized with a
_copy_ of the argument. So in this example, `x` will be assigned `30`,
because that's the argument we passed to the function for that call.

Variables inside the parentheses have a special name. They are called
_parameters_.

Remember: _you pass in arguments that get copied into parameters_.

A parameter is a special type of _local variable_. We'll get into their
story on line 2.

### Line 2: Compute the result {.unlisted .unnumbered}

You can see on line 2 that we take the parameter `x` and feed it into
the equation our boss tasked us with. (They told us to change it to
multiply by 7, remember?)

And then Python does that math and stores that into the variable
`result`.

Now that variable `result` is special. It's what we call a _local
variable_. Because it's used inside the function, it's only visible
inside the function. Once the function returns (more on that below), the
valued in the local variables vanish forever.

You can name the local variables anything you want, even if you've used
that same name in another function! Each local variable is isolated from
the rest of the world, and only exists within its own function.

And as I mentioned above, the parameters are also local variables. They
just have the added property that they are assigned the values of the
arguments automatically.

### Line 4: Return the result {.unlisted .unnumbered}

A function can optionally return a value. You know how arguments are a
way to pass data _into_ a function? The return value is a way to pass
data back _out_ of the function to the caller.

Back where the function is called, you can think of the function call as
_having_ the return value. Then you can do things like assign it into a
variable.

### Line 6: Capture the returned result in a variable {.unlisted .unnumbered}

We call our function, and we take the _return value_ from that function
and assign it into the variable `answer`. Then we can do things with it,
like print it out on line 7.

Problem solving step: **Looking Back**.

In the function as written, above, we use a lot of variables to help
demonstrate a number of concepts and ideas surrounding functions.

But in reality, a dev would probably simplify the above code to:

``` {.py .numberLines}
def do_the_math(x):
    return (x + 13) * 7

print(do_the_math(30))
```

Compare the two until you are convinced they are equivalent.


## Multiple Return Values

Problem solving step: **Understanding the Problem**.

You can always return a list or a dict or anything from a function, but
you can also return two values and assign them to different variables.

``` {.py}
# Function that returns the argument times 10, and divided by 10

def timesdiv10(x):
    return x * 10, x / 10

a, b = timesdiv10(100)

print(a, b)   # 1000 10
```

Or you can assign the result to a single variable. The result will be a
_tuple_, which is a read-only list that you can access with square
bracket notation:

``` {.py}
a = timesdiv10(100)

print(a[0], a[1])   # 1000 10
```

Magic!


## What Makes a Good Function

Problem solving step: **Understanding the Problem**.

The biggest rule is "do one thing and do it well".

It's more of a guideline than a rule, because you're the boss when it
comes to programming.

But it's a great guideline that should be followed when you can.

The biggest things you'll use functions for are:

* Mathematical equations
* Anything that happens repeatedly
* Breaking up code into smaller, self-contained sections

Let's talk about that last item more, since it's less obvious.

Very frequently---almost always---you'll start with a series of steps
you need to perform to solve the problem, like this:

``` {.py}
# While we still have data to process
    # Process the data
    # Output the data
```

And then you go in and fill in all the code for processing the data and
outputting the data.

But that could make for a bulky, hard-to-read `while` loop. It might be
better to code it up like this:

``` {.py}
while d in data:
    d = process(d)
    output(d)
```

and the write the functions `process()` and `output()` to operate on the
data that is passed into them.

This makes the logic of the loop _really_ easy to read. And being
easy-to-read is _king_ (or _queen_, if you prefer).

If you find you have some large amounts of code that are getting
deeply-nested, it might be time to break them out into functions, even
if you only call those functions from that single place.

Knowing _when_ to break up code into functions is more of an art than a
science. If you start feeling like your code is remotely unwieldy,
consider what it might look like split into different functions. If you
like it more, do it!

## Positional Arguments versus Keyword Arguments

Problem solving step: **Understanding the Problem**.

We'll talk more about this in detail later, but function arguments can
be split into these two broad classes in Python: _positional_ and
_keyword_.

Positional arguments are the arguments that have to occur at certain
positions in a function call.

For instance, if we want to compute $14^{12}$, we need to pass those two
arguments in a specific order to the `math.pow()` function, which
expects the base to be first and the exponent to be second:

``` {.py}
math.pow(14, 12)   # 56693912375296.0
```

If you put the 12 first, you get a different answer. These are
positional arguments.

But for some functions, after the positional arguments, you can specify
additional keyword arguments. These are arguments that are identified by
a certain name.

For example, normally `print()` puts a newline at the end of the string.
But you can override this behavior with the `end` keyword argument by
telling `print()` to put nothing (an empty string) at the end of the line:

``` {.py}
# Together, prints "Beej" on a single line

print("Be", end="")
print("ej")
```

Notice how we had to identify the keyword argument by name.

For now, it's enough to know that these exist and how to call them.
Later on, we'll talk about how to write our own.


## The Chapter Project

Problem solving step: **Understanding the Problem**

It's that time! If you need a refresher, [pop back up to the top and
check out the spec](#func-proj-spec).

So we want to do a couple things:

1. Read in a list of starship positions.
2. Print out a grid of distances between each ship.

The positions are entered as X,Y,Z coordinates (until the user enters
"done").

The distances are computed with the distance formula variation of the
Pythagorean Theorem.

A grid of distances is printed. There should be ship numbers along the
axes.

Problem solving step: **Devising a Plan**

We already have a bit of a plan, don't we? We listed it right up there.

1. Read in a list of starship positions.
2. Print out a grid of distances between each ship.

Don't look now, but these would make a great couple of functions. Sure,
we _could_ stick them all in one big main routine, but it's way more
logical and easier to read if we make them their own functions.

We could have one function read the list of positions and return it.

And we could take that returned list and pass it into another function
to print the grid.

``` {.py}
locations = get_ship_locations()
print_grid(locations)
```

We're taking a _top down_ approach, here. Starting with the big pieces
of logic and then implementing them as we go down.

In fact, let's simplify the problem, and just start like this:

``` {.py}
locations = get_ship_locations()
print(locations)
#print_grid(locations)
```

That way we can just do one bit and make sure it's working.

> **Fun Motto Fact**: Get something working as quickly as possible, no
> matter how much a piece of the project it is.

Problem solving step: **Understanding the Problem**

For getting the ship locations, looks like we want to have the user
enter an X,Y,Z coordinate. Then we want to split that into a list of
numbers. And we need to make sure they are int type---remember that
`input()` returns a string, so we'll have to convert them to int.

And we repeat that until the user enters "done".

Problem solving step: **Devising a Plan**

Looping until the user enters "done" is a solved problem. We've done
that a few times now. Just make a variable for the `while()` condition,
and then set it when the user enters "done".

Otherwise we have to split the string up into a list of 3 numbers,
splitting on the comma. Remember how to do that?

Yes, that's right (or no, not right, if you don't remember), it's the
`split()` string method. Example:

``` {.py}
"1,2,3".split(',')  # produces list ["1","2","3"]
```

But that's not enough. Like we noted, we need to convert that list from
a list of strings to a list of numbers. Remember how to convert a string
to a number? Yes, with the built-in `int()` function!

``` {.py}
int("2") == 2  # True!
```

So we can loop through our list of strings and convert them to ints.

And then we'll have a list of 3 ints, representing the X,Y,Z coordinates
of a single ship. Of course, the user is going to enter any number of
ships, and we'll have to keep all those lists of coordinates
somewhere... where?

It's almost like we'll need a list for all those lists. A list of lists!
Why not? We made some of those in the lists chapter, right?

So we add the new X,Y,Z list to the end of a master list that holds all
the coordinates.

Then we can return that master list to be used later when we print the
grid.

Let's code!

Wait---you're right---we haven't finished the _entire_ plan for the
whole project. True. But that's okay. We completed enough devising of a
plan to do the first part of the project.

And this is one of the beautiful things about functions. We've split the
problem up so nicely that we can implement different parts of it
_completely independently_! In fact, if you have a programming pal, you
could get them to write the `print_grid()` function at the same time you
were writing the `get_ship_locations()` function!

Problem solving step: **Carrying Out the Plan**

Let's get coding!

``` {.py}
def get_ship_locations():
    """
    Ask the user to enter a number of X,Y,Z ships coordinates.
    Returns a list of all the coordinates.
    """

    done = False     # True when the user asks to be done
    locations = []   # Master list of all ship positions

    while not done:
        xyz = input('Enter ship location x,y,z (or "done"): ')

        if xyz == "done":
            done = True
        else:
            # Get a list of the x,y,z coordinates
            xyz_list = xyz.split(',')

            # Convert to integers
            for i, v in enumerate(xyz_list):
                xyz_list[i] = int(v)

            # Build the master list
            locations.append(xyz_list)

    return locations

locations = get_ship_locations()
print(locations)
#print_grid(locations)
```

If we give that a run, we see something like this:

```
Enter ship location x,y,z (or "done"): 1,2,3
Enter ship location x,y,z (or "done"): 4,5,6
Enter ship location x,y,z (or "done"): done
[[1, 2, 3], [4, 5, 6]]
```

There's our list of lists holding the ships' coordinates! It's ready to
feed into the `print_grid()` function. But first we'd better think about
that for a bit.

One more thing: if you were looking closely, you saw the big multiline
string at the beginning of the function describing what the function
does. This is called a _doc string_ and it's a comment that gives
overall information about the function. Automatic documentation
generators can extract these and build documentation for you, just like
you can get with the `help()` function in the [REPL](#repl).

Problem solving step: **Understanding the Problem**

All righty. What do we need to do for this second part of printing out
the grid of distances between the ships?

There are sort of three big pieces here.

* We need to print out a grid.
* We need the first row and first column to list out ship numbers so we
  can cross-reference.
* We need to actually compute the distance and print that.

Problem solving step: **Devising a Plan**

Let's simplify a bit first. Instead of worrying about computing the
distance, let's just concentrate on the grid. We'll just put the bogus
number of `99.99` in for all the inter-ship distances.

> **Protip**: When putting in bogus data, make sure it's _obviously_
> bogus so that obviously people obviously know they must obviously
> replace this with real data before the product ships.

And to simplify even further, let's forget about the ship numbers in the
first row and first column. We can add those in later. Remember: it's
good to identify the minimum independent piece you can implement next
and test that it's working.

We know how many ships we have---it's the length of the master list of
ship coordinates.

If we have _n_ ships, we'll need and _n_ by _n_ grid to be displayed to
show all the distances between all of them. But how? Think back to the
loops chapter...

You can do it with a _nested loop_. The outer one goes for _n_ rows, and
the inner one goes for _n_ columns.

For printing the number with 2 decimal places in a field of width 8, you
can use a f-string with some special formatting specifiers, for example:

``` {.py}
distance = 99.99
print(f'{distance:8.2f})   # prints "   99.99"
```

All righty! Let's print some stuff!

``` {.py}
def print_grid(locations):
    """Print a grid of ship-to-ship distances."""

    num_ships = len(locations)
    
    for i in range(num_ships):
        for j in range(num_ships):
            dist = 99.99
            print(f'{dist:8.2f}', end="")
        print()

locations = get_ship_locations()
print_grid(locations)
```

Running that gives:

```
Enter ship location x,y,z (or "done"): 1,2,3
Enter ship location x,y,z (or "done"): 4,5,6
Enter ship location x,y,z (or "done"): 7,8,9
Enter ship location x,y,z (or "done"): done
   99.99   99.99   99.99
   99.99   99.99   99.99
   99.99   99.99   99.99
```

Hey, a nice 3x3 grid for our 3 ships!

Next, let's put the ship row number just to the left of each row. Just
editing the `for`-loop here:

``` {.py}
    for i in range(num_ships):
        print(f'{i:8}', end="")   # <-- add this
        for j in range(num_ships):
            dist = 99.99
            print(f'{dist:8.2f}', end="")
        print()
```

We printed it in field width 8 just for consistency with the distance
numbers. Output is now:

```
       0   99.99   99.99   99.99
       1   99.99   99.99   99.99
       2   99.99   99.99   99.99
```

Which is good! Now we just need a row on the top. How about another loop
before everything else to print out that row?

``` {.py}
    # Add this loop:
    for i in range(num_ships):
        print(f'{i:8}', end="")
    print()

    for i in range(num_ships):
        print(f'{i:8}', end="")
        for j in range(num_ships):
            dist = 99.99
            print(f'{dist:8.2f}', end="")
        print()
```

And we get this:

```
       0       1       2
       0   99.99   99.99   99.99
       1   99.99   99.99   99.99
       2   99.99   99.99   99.99
```

Er, well, that's _almost_ right. The top row is shifted one column left.
We need to stick 8 blank spaces in before it to scooch it over. So let's
just do it, using string multiplication to make us 8 spaces:

``` {.py}
    print(" " * 8, end="")   # <-- Add this

    for i in range(num_ships):
        print(f'{i:8}', end="")
    print()
```

And now we have this:

```
               0       1       2
       0   99.99   99.99   99.99
       1   99.99   99.99   99.99
       2   99.99   99.99   99.99
```

which is looking _right on_. Except that all the distances are listed as
`99.99`. Let's get that out of there and replace it with the real
distance between the ships.

## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

Use any knowledge you have to solve these, not only what you learned in
this chapter.

1. Write a function that accepts the mass of two planets and the
   distance between them (for a total of 3 arguments) and returns the
   force between them.

   Use Newton's Universal Law of Gravitation to calculate the force $F$:

   $F=G\cfrac{m_1 m_2}{r^2}$

   In mathematical notation, to variables next to each other like $m_1
   m_2$, above, indicate multiplication.

   And for $r^2$, a simple equivalent is $r\times{r}$.

   So we can convert that whole equation to:

   ``` {.py}
   F = G * (m1 * m2) / (r * r)
   ```

   where `m1` is the mass of one planet, `m2` is the mass of the other
   planet, and `r` is the distance between them.

   So far so good.

   But what's `G`? It's the _gravitational constant_:

   $G=6.67430\times10^{-11}$ 

   That's written in scientific notation, but we can do the same thing
   in Python:

   ``` {.py}
   G = 6.67430e-11
   ```

   That should be enough to go on. Write the function and call it with a
   variety of different values. Here are some sample values so you can
   see if your code is working:

   |m1|m2|r|result|
   |-:|-:|-:|-:|
   |`10`|`20`|`30`|`1.48317e-11`|
   |`10`|`40`|`30`|`2.96635e-11`|
   |`100`|`5`|`10`|`3.33714e-10`|

   ([flx[Solution|ex_grav.py]].)

2. Write a program to input numbers repeatedly until the user types
   "done". Keep track of all the numbers in a list.

   Print out the maximum value the user entered using built-in
   functions.

   ([flx[Solution|ex_max.py]].)

3. Write a function that takes an integer between 0 and 9 as an
   argument. It should return a string that corresponds to the English
   word for that number. For example, if the argument is `3`, the
   function should return `"three"`.

   ([flx[Solution|ex_ennum.py]].)

4.

## Summary

Functions are a super-important part of programming and a highly
valuable 
* Understand what functions are and how they're useful
* Be able to use built-in functions
* Understand what function arguments are
* Be able to write your own functions
* Be able to write good functions
* Understand the difference between positional arguments and keyword arguments
