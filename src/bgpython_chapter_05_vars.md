<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell
-->

# Data and Processing Data

## Objective

* Understand what data is and how it is used
* Understand what variables are and how they are used
* Utilize variables to store information
* Do basic math
* Store input from the keyboard in variables
* Learn about integer versus string data types
* Print the value of variables on the screen
* Write a program that inputs two values and prints the sum

**For this chapter, we want to write a program that reads two numbers
from the keyboard and prints out the sum of the two numbers.**

## Data, Variables, and Math

Problem solving step: **Understand**

_Data_ is the general term we use to describe information stored in the
computer. In the case of programming, we're interested in values that we'll do
things with. Like add together. Or turn into a video game.

Really, data is information. Can you glean information from a symbol?
Then it's data. Sometimes it's a symbol like "8", or maybe a string of
symbols like "cat". 

Your goal as a software developer is to write programs that manipulate
data. You have to manipulate the input data in such a way that the
desired output is achieved. And you have to solve the problem of how to
do that.

In a program, data is commonly stored in what we call _variables_. If
you've taken any algebra, you are familiar with a letter that holds the
place of a value, such as the "slope-intercept" form of the equation of
a line:

> $y = mx + b$

or of a parabola:

> $y = x^2$

But beware! In programming code, variables don't behave like
mathematical equations. Similar, but different.

Enter the following code in a new program in your editor, save it, and
give it a run. (This is just like you did with the program in the
earlier chapter. You can name this one anything you'd like. If you need
inspiration, `vartest.py` seems good to me.)

``` {.py .numberLines}
a = 34    # Variable a is assigned value 34
print(a)
a = 90    # Variable a is now assigned value 90
print(a)
```

In Python, _variables hold values_^[More strictly speaking, values have
variable _names_ associated with them. But we're going to go with the
common _variables hold values_ model for now.]. We're saying on line 1 of
the code, above, "Store the value `34` in the variable `a`." Think of
`a` like a bucket that we can put something in, in this case the value
`34`.

Then Python moves to the next line of code and runs it, printing `34` to
the screen. And then on line 3 we put something different in that
bucket. We store `90` in `a`. The `34` is gone--this type of bucket only
holds one thing^[Later we'll learn that other types of buckets can hold
more than one thing.].

So the output will be:

```
34
90
```

> _We're using `a` and `b` for variable names, but they can be made up
> of any letter or group of letters, or digits, and can also include
> underscores (`_`). The only rule is they can't start with a digit!
>
> These are all valid variable names:
>
> `a`
> `b`
> `a1b2`
> `foo`
> `Bar`
> `FOOBAZ12`
> `Goats_Rock`

You can also do basic math on numeric variables. Add to the code above:

``` {.py .numberLines}
a = 34      # Variable a is assigned value 34
print(a)
a = 90      # Variable a is assigned value 90
print(a)

b = a + 40  # b is assigned a + 40 which is 90 + 40, or 130
print(a)    # Still 90! Nothing changed here
print(b)    # Prints "130"
```

On line 6, we introduced a new variable, `b`, and gave it the value of
"whatever `a`'s value is plus `40`".

> _What are all these `#` marks in the file? We call those_ hash _marks,
> and in the case of Python, they mean the rest of the line is a_
> comment _and will be ignored by the Python interpreter._

One last important point about variables: when you do an assignment like
we did, above, on line 6:

``` {.py}
b = a + 40  # b is assigned 130
```

When you do this, `b` stays at the value `130` even if `a` changes
later. The assignment happens once, when that line is executed, with the
value in `a` at that snapshot in time, and that's it.

Let's expand the example farther to demonstrate:

``` {.py .numberLines}
a = 34      # Variable a is assigned value 34
print(a)
a = 90      # Variable a is assigned value 90
print(a)

b = a + 40  # b is assigned a + 40 which is 90 + 40, or 130
print(a)    # Still 90! Nothing changed here
print(b)    # Prints "130"

a = 1000
print(b)    # Still 130!
```

Even though we had `b = a + 40` higher up in the code, `a` was `90` at
the time that code executed, and `b` is set to `130` until we assign
into it again. Changing `a` to `1000` did **not** magically change `b`
to `1040`.

> _**Fun Tax Fact**: The
> [fl[1040|https://en.wikipedia.org/wiki/Form_1040]] is nearly my
> least-favorite tax form._

For more math fun, you have the following operators at your disposal
(there are more, but this is enough to start):

|Function|Operator|
|:-:|:-:|
|Add|`+`|
|Subtract|`-`|
|Multiply|`*`|
|Divide|`/`|
|Integer Divide^[Integer division truncates the part of the number after the decimal point.]|`//`| |Modulo (remainder)|`%`|
|Exponent|`**`|

You can also use parentheses similar to how you do in algebra to force
part of an expression to evaluate first. [fl[Normal mathematical order
of operations rules
apply|https://en.wikipedia.org/wiki/Order_of_operations]].

``` {.py}
 8 + 4  / 2   #  8 + 4  / 2 ==  8 + 2 == 10
(8 + 4) / 2   # (8 + 4) / 2 == 12 / 2 == 6
```

And you thought all that algebra wouldn't be useful... _pshaw!_

## User Input

Problem solving step: **Understand**

We want to get input from the user and store it in a variable so that we
can do things with it.

Remember that our goal this chapter is to write a program that inputs
two values from the user on the keyboard and prints the sum of those
values.

Python comes with a built in _function_ that allows us to get user
input. It's called, uncoincidentally, `input()`.

But wait---what is a function?

A function is a chunk of code that does something for you when you
_call_ it (that is, when you ask it to). Functions accept _arguments_
that you can _pass in_ to cause the function to modify its behavior.
Additionally, functions _return_ a value that you can get back from the
function after it's done its work.

So here we have the `input()` function^[`input()` is what we call a
_built-in_ in Python. It comes with the language and we get to make use
of it. Later we'll learn to write our own functions from scratch!],
which reads from the keyboard when you call it. As an argument, you an
pass in a _prompt_ to show the user when they are ready to type
something in. And it returns whatever the user typed in.

What do we do with that return value? We can store it in a variable!
Let's try!

Here's another program, `inputtest.py`:

``` {.py .numberLines}
# Take whatever `input()` returns and store it in `value`:

value = input("Enter a value: ")
print("You entered", value)
```

We can run it like this:

```
$ python3 inputtest.py
Enter a value: 3490
You entered 3490
```

Check it out! We entered the value `3490`, stored it in the variable
`value`, and then printed it back out! We're getting there!

But you can also call it like this:

```
$ python3 inputtest.py
Enter a value: Goats rock!
You entered Goats rock!
```

Hmmm. That's not a number. But it worked anyway! So are we all good to
go?

Yes... and no. We're about to discover something very important about
data.

## Data Types

Problem solving step: **Understand**

We started with numbers, earlier. That was pretty straightforward. The
variable was assigned a value and then we could do math on it.

But then we saw in the previous section that `input()` was returning
whatever we typed in, including `Goats rock!` which is certainly not any
number I've ever heard of.

