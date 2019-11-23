<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell
-->

# Data and Processing Data

## Objective

* Understand what data is and how it is used
* Understand what variables are and how they are used
* Utilize variables to store information
* Print the value of variables on the screen
* Do basic math
* Store input from the keyboard in variables
* Learn about integer versus string data types
* Convert between data types
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
x = 34      # Variable x is assigned value 34
print(x)
x = 90      # Variable x is assigned value 90
print(x)
```

In Python, _variables hold values_^[More strictly speaking, values have
variable _names_ associated with them. But we're going to go with the
common _variables hold values_ model for now.]. We're saying on line 1 of
the code, above, "Store the value `34` in the variable `x`." Think of
`x` like a bucket that we can put something in, in this case the value
`34`.

Then Python moves to the next line of code and runs it, printing `34` to
the screen. And then on line 3 we put something different in that
bucket. We store `90` in `x`. The `34` is gone--this type of bucket only
holds one thing^[Later we'll learn that other types of buckets can hold
more than one thing.].

So the output will be:

```
34
90
```

> _We're using `x` and `y` for variable names, but they can be made up
> of any letter or group of letters, or digits, and can also include
> underscores (`_`). The only rule is they can't start with a digit!
>
> These are all valid variable names (and, of course, you can make up
> any name you want!):
>
> `x`
> `y`
> `a1b2`
> `foo`
> `Bar`
> `FOOBAZ12`
> `Goats_Rock`

You can also do basic math on numeric variables. Add to the code above:

``` {.py .numberLines}
x = 34      # Variable x is assigned value 34
print(x)
x = 90      # Variable x is assigned value 90
print(x)

y = x + 40  # y is assigned x + 40 which is 90 + 40, or 130
print(x)    # Still 90! Nothing changed here
print(y)    # Prints "130"
```

On line 6, we introduced a new variable, `y`, and gave it the value of
"whatever `x`'s value is plus `40`".

> _What are all these `#` marks in the file? We call those_ hash _marks,
> and in the case of Python, they mean the rest of the line is a_
> comment _and will be ignored by the Python interpreter._

One last important point about variables: when you do an assignment like
we did, above, on line 6:

``` {.py}
y = x + 40  # y is assigned 130
```

When you do this, `y` stays at the value `130` even if `x` changes
later. The assignment happens once, when that line is executed, with the
value in `x` at that snapshot in time, and that's it.

Let's expand the example farther to demonstrate:

``` {.py .numberLines}
x = 34      # Variable x is assigned value 34
print(x)
x = 90      # Variable x is assigned value 90
print(x)

y = x + 40  # y is assigned x + 40 which is 90 + 40, or 130
print(x)    # Still 90! Nothing changed here
print(y)    # Prints "130"

x = 1000
print(y)    # Still 130!
```

Even though we had `y = x + 40` higher up in the code, `x` was `90` at
the time that code executed, and `y` is set to `130` until we assign
into it again. Changing `x` to `1000` did **not** magically change `y`
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

And, no, it's not a number, indeed. It's a sequence of characters, which
we call a _string_.

Wait... there's another type of data besides numbers? Yes! Lots of types
of data! We call them _data types_.

Python associates a _type_ with every variable. This means it keeps
track of whether a variable holds an integer, a _floating point_^[This
is the way most computers represent numbers with a decimal point in
them, such as $3.14159265358979$. When you see "floating point" or
"float", think "number with a decimal point in it" as opposed to
"integer".] number, or a string of characters.

Here are some examples and their associated types. When you store one of
these values in a variable, the variable remembers the type of data
stored within it.

|Example Data|Type in English|Type name in Python|
|:-|:-|:-|
|`2`|Integer|`int`|
|`3490`|Integer|`int`|
|`-45`|Integer|`int`|
|`0`|Integer|`int`|
|`3.14159`|Floating Point|`float`|
|`-13.8`|Floating Point|`float`|
|`0.0`|Floating Point|`float`|
|`"Hello!"`|String|`str`|
|`"3490"`|String|`str`|
|`""`|String (empty)|`str`|

In the examples, above, strings are declared using double quotes (`"`),
but they can also be done with single quotes, as long as the quotes
match on both ends:

``` {.py}
"Hello!"  # is the same as 'Hello!'
'Hello!'  # is the same as "Hello!"
```

Okay, that's all fine. But is `input()` returning a string or a number?
We saw both happen when we tried it out, right?

Actually, turns out, `input()` **always** returns a string. Period. Even
if that's a string of numbers. Note that these things are **not** the
same:

``` {.py}
3490     # int
"3490"   # string
```

Sure, they look kinda the same, but they aren't the same _because they
have different types_. You can do arithmetic on an `int`, but not on a
string.

Well, that's just great. The task for this chapter is to get two numbers
from the keyboard and add them together, but the `input()` function only
returns strings, and we can't add strings together!

How can we solve this problem?

## Converting Between Data Types

Problem solving steps: **Understand**

If we can't add strings mathematically, can we convert the string
`"3490"` into the integer `3490` and then do math on that?

Yes!

In fact, we can convert back and forth between all kinds of data types!
Watch us convert a string to a number and store it in a variable:

``` {.py}
a = "3490"    # a is a string "3490"
b = int(a)    # b is an integer 3490!

print(b + 5)  # 3495
```

How did that work? We called the built-in `int()` function and passed it
a string `"3490"`. `int()` did all the hard work and converted that
string to an integer and returned it. We then stored the returned value
in `y`. And finally, we printed the value of `b+5` just to show that we
could do math on it.

Perfect!

Here are some of the conversion functions available to you in Python:

|Function|Effect|
|:-:|:-|
|`int()`|Convert argument to an integer and return it|
|`float()`|Convert argument to a floating point number and return it|
|`str()`|Convert argument to a string and return it|


So... given all that we know so far, how can we solve this chapter's
problem: input two numbers from the keyboard and print the sum?

## Input Two Numbers and Print the Sum

Problem solving step: **Make a Plan**

We know:

* How to input strings from the keyboard
* How to convert strings to numbers
* How to add numbers together
* How to print things out

Now---how do we put all that together to write a program that inputs two
numbers from the keyboard and prints their sum?

This is the _Make a Plan_ portion of problem solving. We're not going to
write code to make this happen. We're just going to write an outline of
the individual steps the program must describe in a language called
_pseudocode_ (which is English that looks kinda like code).

Then when we're satisfied it'll work, we can code it up for realsies.

So stop here and take a moment to consider what the step by step might
be to get this done.

Really, take a moment, because I'm about to give spoilers. Thinking
about how to solve problems is 80% of what a software developer gets
paid to do, so you might as well practice right now.

What do we know? What tools do we have at our disposal? What resources?
How do I put all those together to solve this problem, like solving a
puzzle?

Here's some pseudocode that would get the job done, it looks like:

```
read string from keyboard into variable x
convert x to int and store it back in x again
read string from keyboard into variable y
convert y to int and store it back in y again
print the sum of x + y
```

If we're satisfied that our plan is solid, it's time to move to the next
phase.

Problem solving step: **Code It Up**

Now let's convert each of those lines to real Python. I'll throw in the
pseudocode as comments so we can see how they compare.

``` {.py .numberLines}
# read string from keyboard into variable x
x = input("Enter a number: ")

# convert x to int and store it back in x again
x = int(x)

# read string from keyboard into variable y
y = input("Enter another number: ")

# convert y to int and store it back in y again
y = int(y)

# print the sum of x + y
print("The sum of the two numbers is:", x + y)
```

Save that file as `twosum.py` and run it:

```
$ python3 twosum.py
Enter a number: 9
Enter another number: 8
The sum of the two numbers is: 17
```

Too easy! Let's challenge it:

```
$ python3 twosum.py
Enter a number: 235896423496865928659832536289
Enter another number: 94673984675289643982463929238
The sum of the two numbers is: 330570408172155572642296465527
```

Not even breaking a sweat!

Nice. Now, I want you to _think like a villain_. What would a villain
pass into our program for input that would cause it to break?

* Negative numbers?
* Zero?
* Decimal numbers?
* Non-numbers, like "goat"?

Try all those things with your program. What happens when you try it?
Which ones work and which ones don't?

Notice that a big, spewing error message is really the _worst case
scenario_ here. And it's not really that painful. Don't be afraid to
try to break your code. The computer can handle it. Just run it again.

Later, we'll learn techniques to catch errors like this so that the
program doesn't bomb out, and prints a nice message to the user to
please try again with valid input, thank you very much.

> _Notice that when the program crashes, buried in all that output, is
> the line number the program crashed on! Very, very useful! And the
> last line tells you exactly what Python thinks went wrong._

The point is, if you're not sure how something will work, _**just try
it**_. Experiment! Break things! Fix things! Again, the computer can
absolutely handle it. It's just a big sandbox for you to play in.

## Wrapping it Up

Problem solving step: **Postmortem**

This grimly-named step is where we take a look at our code and decide if
there was a better way to attack this problem. It's important to
remember that _coding is a creative endeavor_. There are many ways to
solve the same problem.

Admittedly, right now, you don't have many tools in the toolkit, so your
creativity is limited. But eventually, in the not-too-distant future,
you'll know several ways to solve a problem, and you'll have to weigh
the pros and cons of each, and be creative and choose one!

What could be better?

* We saw earlier that passing in floating point numbers (with a decimal
  point) bombed out. It would be nice if the program would add both
  floating point.

What else could we do?

* What about other math operations?

## Exercises

Some more things to try:

* Have the program print out the sum and the difference between two
  numbers.

* Allow the user to enter 3 numbers and perform the math on those.

* Write a program that allows the user to enter a value for $x$, and
  then computes and prints $x^2$. Remember `**` is the exponentiation
  operator in Python. `3**2` is `9`.

* Write a program that allows the user to enter `a`, `b`, and `c`, and
  the solves [fl[the quadratic
  formula|https://en.wikipedia.org/wiki/Quadratic_formula]] for those
  values.

  A refresher: for equations of the form

  $ax^2+bx+c=0$

  you can solve for $x$ with the quadratic formula:

  $x=\cfrac{-b\pm\sqrt{b^2-4ac}}{2a}$

  This looks terrifying! But you absolutely can do it! Your program
  should plug `a`, `b`, and `c` into the above formula and print out the
  result value in `x`.

  What about that square root? Here's a demo program for computing the
  square root of `2`:

  ``` {.py .numberLines}
  import math      # You need this for access to the sqrt() function

  x = math.sqrt(2)
  print(x)         # 1.4142135623730951
  ```

  Note that there are _two_ solutions to the quadratic formula due to
  the plus-or-minus. Hint: compute it once with `+`, then again with
  `-`. Print both answers.

  * Followup: after computing `x`, go ahead and compute the value of

    $ax^2+bx+c$

    and print it out. The result should be exactly `0`. Is it? Or is it
    just something really close to zero? Lesson: _floating point math
    isn't always exact_. Sometimes it's off by a tiny fraction.

## Summary

