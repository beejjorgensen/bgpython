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


## Chapter Project Specification {dicts-proj-spec}

TODO

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
[fl[DRY
principle|https://en.wikipedia.org/wiki/Don%27t_repeat_yourself]]
(_Don't Repeat Yourself_). If you can remove as much repetitive code as
you can and move it to a function, that makes your code easier to read
and maintain. DRY code is happy code.

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
|`bin()`|Return a string representing the number in binarys.|
|`chr()`|Return a character for the Unicode (and ASCII) value passed in.|
|`dir()`|Return a list of methods on this object.|
|`enumerate()`|Return an iterator over a list of (index, value) pairs.| |`filter()`|Repeatedly run a function on items of a list filtering some out.|
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
> ---Excerpt from Monty Python's Argument Clinic sketch

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
> ---A good friend of mine trolling a reporter at [fl[DEFCON
> 2|https://www.defcon.org/html/defcon-2/defcon-2.html]].

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

### Line 1: defining the function

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

### Line 2: Compute the result

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

### Line 4: Return the result

A function can optionally return a value. You know how arguments are a
way to pass data _into_ a function? The return value is a way to pass
data back _out_ of the function to the caller.

Back where the function is called, you can think of the function call as
_having_ the return value. Then you can do things like assign it into a
variable.

### Line 6: Capture the returned result in a variable

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


 If the function operates on
> an object with a dot `.` before the function name, we call that
> function a _method_.
