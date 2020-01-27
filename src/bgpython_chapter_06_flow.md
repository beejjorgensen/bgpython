<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# Flow Control and Looping

## Objective

* Understand what flow control is
* Understand what a conditional is 
* Be able to construct Boolean ("BOO-lee-in") expressions
* Implement code that makes decisions with `if` statements
* Implement code that loops with a `while` loop
* Implement code that loops with a `for` loop and `range` iterator

## Chapter Project Specification {#loop-proj-spec}

For this chapter, we want to write a program that asks the user for a
number between 5 and 50, inclusive. 

If a number outside that range is entered, an error message is printed
and the user is asked again to enter a valid number.

Once the number is obtained, the program will print out that many `#`
characters in a row. EXCEPT all characters at position 31 and above
should print out a `*`. (Characters before that position will still be
a `#`.)

For example, an input of 10 would result in:

```
##########
```

whereas an input of 37 would result in:

```
##############################*******
```

Keep this program in mind as we learn the techniques to implement it.


## What is Flow Control?

Problem solving step: **Understanding the Problem**.

What is _flow control_? To understand, let's look at a simple program:

``` {.py .numberLines}
print("Are we not drawn onward")
print("We few")
print("Drawn onward to new era?")
```

When this program runs, Python keeps track of the current instruction,
or line, if you will.

First, Python runs the first line.

Then it goes to the next.

Then it goes to the last.

And then it falls off the end and completes.

Kind of monotonous, right? I mean, it just brainlessly goes to the next
instruction every time.

What if you want to transfer the program flow elsewhere instead of just
blindly going to the next instruction?

This is where you get your first taste of what it means to be a
developer. You can ask the computer to make smart decisions based on
criteria you specify. Figuring out which criteria to specify is the job
of a programmer and where most of the hard work comes in.

Eventually we're going to code up things that say "If some condition is
true, do one thing" or "If some condition is false, do another thing".

But before that, we have to meet someone: George Boole.


## Boolean Algebra and Expressions

Problem solving step: **Understanding the Problem**.

[flw[George Boole|George_Boole]] was quite and interesting character.
From humble beginnings in the early 1800s, he went on to develop the
mathematics that became, in many ways, the foundation of modern
computation. Pretty awesome.

What he developed is what we call today _Boolean Algebra_.

Don't worry--it's easier than that algebra you're thinking of. In fact,
you already know it, just not formally and not by that name.

With Boolean, we're interested in whether or not expressions are _true_
or _false_. And then we can make decisions on whether or not they are.

Let's do some human ones before we get into the computer stuff.

Level: Easy. Are these expressions true or false for you?

* I live in North America.
* It's raining right now.
* Cats are superior to dogs.

Hopefully that wasn't particularly challenging. Let's take it up a notch
by introducing the concept of _AND_. For these, the entire expression is
true _only if all subexpressions are true_.

For example, the statement "I'm over 190 cm tall AND I'm under 30 years
of age" is false. Though I am over 190 cm tall, am I not under 30 years,
so the entire expression is false.

By comparison, "I like dogs AND I like motorcycles" _is_ true, because
both of those subexpressions is true.

And if neither of them are true, the result is also false.

Level: Intermediate. Are these expressions true or false for you?

* I live in Europe AND I'm older than 25.
* It's raining right now AND it's sunny right now.
* Cats are superior to dogs AND dogs are superior to cats.

All right! Let's do a variant on AND, namely _OR_. With OR, the entire
expression is true if _either or both_ of the subexpressions is true.

For example, I _don't_ like running, but I do like bicycling.
Nevertheless, the following statement is true, because at least one of
the subexpressions is true: "I like running OR I like bicycling". True.

> _This is the basis for the smarty-pants answer to the question:_
>
> _"Would you like soup or salad?"_
>
> _"True. I would like soup or I would like salad."_
>
> _"Get out of my restaurant, Boolean fanatic!"_

Level: Intermediate. Are these expressions true or false for you?

* I live in Europe OR I'm older than 25.
* It's raining right now OR it's sunny right now.
* Cats are superior to dogs OR dogs are superior to cats.

All right! Now one more thing to remember: unless there are parentheses
in an expression saying otherwise, AND takes precedence over OR. That
is, do the ANDs first, and then do the ORs.

Level: Advanced.

Let's say it's raining, I'm over 25, and this fish is big. We could
evaluate this expression:

> It's sunny AND this fish is big OR I'm over 25.

We do the AND first. It's not sunny, and the fish is big. So that's
"false AND true", which evaluates to "false".

So replace that AND expression with "false". And then we'll do the OR:

> false OR I'm over 25.

Now I am over 25, so that evaluates to "false OR true", which is "true".

So the entire expression is true.

And you can override with parentheses:

> It's sunny AND (this fish is big OR I'm over 25).

Do the work in parens first. So now we evaluate the OR, which evaluates
to "true OR true" which is "true". _Then_ we evaluate the AND, which is
"It's sunny AND true", which is "false AND true", which is "false".

So the entire expression is false.

Let's do some examples with numeric conditional expressions. Do these
evaluate to true or false?

* 1 < 5
* 5 > 1
* 1 < 5 AND 5 < 10
* 1 > 5 OR 5 < 10
* 1 < 5 AND 5 > 10 OR 10 > 20
* 1 < 5 AND (5 > 10 OR 10 > 20)

Answers:

* True
* True
* True AND True = True
* False OR True = True
* True AND False OR False = False OR False = False
* True AND (False OR False) = True AND False = False

Sometimes developers (but more usually hardware folks) describe these
operations in what are called _truth tables_. A truth table shows what
the result of a Boolean expression will be for some given inputs.

Often these tables use `1` to represent `True` and `0` to represent
`False`^[Ooooo! `1`s and `0`s! Binary! For just a moment, here, we're
getting a glimpse of the deep workings of the machine.].

Here are some truth tables for the operations we've seen so far.

|A|B|A AND B|
|:-:|:-:|:-:|
|`0`|`0`|`0`|
|`0`|`1`|`0`|
|`1`|`0`|`0`|
|`1`|`1`|`1`|

|A|B|A OR B|
|:-:|:-:|:-:|
|`0`|`0`|`0`|
|`0`|`1`|`1`|
|`1`|`0`|`1`|
|`1`|`1`|`1`|

|A|NOT A|
|:-:|:-:|
|`0`|`1`|
|`1`|`0`|

Now we're about ready to go. Let's learn how to do this in Python.

## Boolean Operations in Python

Problem solving step: **Understanding the Problem**.

The comparison operators in Python are:

|Operator|Effect|
|:-:|:-|
|`<`|Less than, e.g. `x < y`|
|`>`|Greater than, e.g. `x > y`|
|`==`|Equal to, e.g. `x == y`|
|`!=`|Not equal to, e.g. `x != y`|
|`<=`|Less than or equal to, e.g. `x <= y`|
|`>=`|Greater than or equal to, e.g. `x >= y`|

So we can take a variable and convert it to a true or false value by
comparing it to numbers or other variables.

What are true and false in Python?

|Boolean|Python Keyword|
|:-:|:-:|
|True|`True`|
|False|`False`|

Easy enough.

Let's try a quick [flx[demo|booltest.py]]:

``` {.py .numberLines}
print(True)     # True
print(False)    # False

x = 10
print(x == 10)  # True
print(x < 5)    # False

# You can store the Boolean result in a variable!
r = x >= 7
print(r)        # True
```

Check that out! You can store the Boolean result of a comparison in a
variable, like we did with `r`, above!

It's important to note that `True` and `False` are not strings. They
represent Boolean values.

So now, for data types, we know about strings, ints, floats, and
Booleans (sometimes called bools for short). Add that to the collection
of tools we have at our disposal.

But what about our good friends AND and OR?

|Boolean|Python Keyword|
|:-:|:-:|
|AND|`and`|
|OR|`or`|
|NOT|`not`|

Pretty easy, but I threw in a NOT! What is that? It's pretty easy: it
just inverts whatever you give it. "NOT true" is false. And "NOT false"
is true.

``` {.py}
print(not False)  # Prints True
```

Seems mundane, but we'll make good use of it in a minute.


## The Almighty `if` Statement

Problem solving step: **Understanding the Problem**.

It's all well and good for Python to tell me that `1 < 5` is `True`, but
how can we actually use that to make choices in a program?

Let's consider a small program that will let the user input a number and
it will tell the user if the number is between 50 and 59, inclusive.

Before coding, let's think about how to approach it. If the number is
stored in `x`, what would the Boolean expression in Python be that would
be `True` if `x` were between `50` and `59`?

I'm talking `and`s and `or`s and `not`s and `<`s and `>`s... not
necessarily all of them, but the ones needed.

Did you get it? Spoilers ahead!

``` {.py}
x >= 50 and x <= 59  # True if x in that range!
```

Let's take that knowledge and turn it into [flx[a complete
program|ifelse1.py]] using `if`, and then we can take it apart in more
detail:

``` {.py .numberLines}
x = input("Enter a number: ")
x = float(x)

if x >= 50 and x <= 59:
    print(x, "is between 50 and 59, inclusive")
    print("Well done!")
else:
    print(x, "is not between 50 and 59, inclusive")
```

So if `x >=50 and x <= 59` is `True`, then we execute the _block_ that
is indented afterward.

> _Blocks can be indented with any combination of tabs or spaces, as
> long as each line in the block begins with the same pattern of tabs or
> spaces. The official recommendation is to_ **use 4 spaces for
> indentation** _in Python._ 
>
> _Indented blocks in Python are one of the things most devs are pretty
> opinionated about in terms of loving or hating. Personally, I say be a
> good dev in any language, regardless of how you feel about their
> idiosyncrasies._

And then what's this pesky `else`? That's a super-handy feature of `if`.
If the condition is `False`, then the block under the `else` is
evaluated instead. Basically we're saying, "If the condition is true,
then do this, otherwise do this."

There's one more construct we can use in the `if`-`else` family: `elif`.
This is short for `else if` and is used if you need to check multiple
conditions.

``` {.py .numberLines}
if x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is less than 20")
elif x < 30:
    print("x is less than 30")
else:
    print("x is greater than or equal to 30")
```

In that example, first we check if `x` is less than 10. If that's
`False`, the next condition is tested, and so on. If none of them match,
then we get to the `else` case.

The `if` statement is the core of what allows us to use Boolean logic to
control the flow of our program. It's how computers can make decisions
based on input. Without `if`, there would be no computing--that's how
important it is!

And your job as a dev is to come up with that logic, those `if`
statements and conditions, that cause your program to give the proper
output for a given input.


## And Now: `while` Loops!

Problem solving step: **Understanding the Problem**.

We're going to divert ever-so-slightly, and talk about another important
concept in programming: _loops_. A loop is what allows us to execute the
same piece of code repeatedly without repeating ourselves.

Here's a real-life example. Let's say you have to add some shingles to a
roof. The steps to do so are to place a shingle, nail it in place, and
then move to the next spot.

Instructions for four shingles might be:

* Place a shingle
* Nail it on
* Move to the next spot
* Place a shingle
* Nail it on
* Move to the next spot
* Place a shingle
* Nail it on
* Move to the next spot
* Place a shingle
* Nail it on
* Move to the next spot

But that's irksomely verbose. It would be nicer to do something like
this:

* While we haven't yet placed 4 shingles:
  * Place a shingle
  * Nail it on
  * Move to the next spot

That's us _looping_. We're running the same piece of code while a
condition is `True`. At the very least, this can save us a lot of
typing!

Python has a number of looping statements, but for this section, we'll
concentrate on what's called the `while`-loop. It does something while a
condition is true.

[flx[Here's an example|while.py]] that counts from 1200 to 1210:

``` {.py .numberLines}
x = 1200

while x <= 1210:
    print(x)
    x += 1

print("All done!")
```

It repeats the body of the loop (everything that's indented) as long as
the condition `x <= 1210` is `True`.

You see inside the body of the loop, we _increment_ (add one to) `x`
every iteration so that it increases toward `1210`.

What would happen if we didn't increment `x`? In that case, it would
loop forever. We call this an _infinite loop_. If your program's running
for a long time with no output (or repeating output), it might be in an
infinite loop.

How do you get out of your program if it's caught in an infinite loop?
You hit `CTRL-C` (AKA "break"). That'll get you back to your shell
prompt.

Remember one of our goals for this chapter's program is to ask the user
for a number between 5 and 50. And we need to ask them again if they
enter a number outside that range. That is, we need to loop while the
user has not given us valid input. Give that some thought now, and we'll
come back to it later.


## Looping: `for` Loops

Problem solving step: **Understanding the Problem**.

In addition to `while` loops, we also have a beast called a `for` loop.
These are actually quite powerful as we'll find out later, but for now I
just want to talk about looping for a certain number of times. (As
opposed to looping while a condition is true.)

Here's an example of printing out the numbers from `0` to `9` using a
`for` loop and a function called `range()`. (`range()` returns something
called an _iterator_. More on iterators in upcoming chapters---for now,
just look at how they can be used with `for` loops.)

``` {.py}
for i in range(10):  # loop from 0 to 9
    print(i)
```

Notice a few things:

* `i` is the classic variable name for a looping _index_.
* If you have a _nested loop_ (a loop inside a loop---more on that
  later) you can use `j`, then `k`, etc.
* We loop until we get to one before the argument to `range()`. Up to
  but not including.

But wait, there's more! `range()` is multi-talented! Not only can it
count up from zero to almost-a-number, but you could give it another
starting point, as well:

``` {.py}
for i in range(5, 10):  # loop from 5 to 9
    print(i)
```

_Now_ how much would you pay? It slices, it dices! But we're not done
yet! You can also tell `range()` how far to skip each step!

Let's print out only the even numbers between 4 and 18 (that is, print
from 4 to 18, stepping by 2 each time):

``` {.py}
for i in range(4, 20, 2):  # loop from 5 to 9, skipping by 2 each time
    print(i)
```

Question: let's say I wanted to count down from 10 to 1 using `range()`.
How would I do that?

``` {.py}
for i in range(???, ???, ???):
    print(i)
```

What do you think? Spoilers upcoming!

You can give `range()` a negative "step" to make it walk backward:

``` {.py}
for i in range(10, 0, -1): # Step backward from 10 to 1
    print(i)
```

Like before, the final value isn't included in the results.

> _Python2 had an additional function called `xrange()`. Python3 doesn't
> have that. If you're ever reading old Python2 code and see `xrange()`,
> know that it's the same as `range()` in Python3._

Now, `for` does a lot more than just looping for a range, but that's a
story for another time.


## When `while` and When `for`?

Problem solving step: **Understanding the Problem**.

Which of these looping constructs should you use, and when?

Generally speaking, whichever one is the easiest for the problem. Or
makes the easiest-to-read code.

Okay, I know that's not much to go on.

If you want to loop a number of times that you know in advance, like 10
times, or the number stored in `x` times, then use a `for` loop with
`range()`.

If you just want to loop until some condition is `True` or `False`, but
you don't know when that'll be, use a `while` loop.


## Chapter Project

Let's jump into that project from the beginning of the chapter. [Revisit
the project spec](#loop-proj-spec) if you need a refresher.

Problem solving step: **Devising a Plan**.

Let's break this program into to two parts, and tackle them
individually.

1. We want to get some valid user input in the range 5-50, inclusive.
2. We want to print out some `#` and `x`s based on the input.

By _breaking down the problem_, we make it more approachable. We can
even break down step 1 into more:

```
While user input isn't valid:
    Ask user for input
    If input invalid, print an error message
```

Don't look now, but our "plan" is looking like really good pseudocode
at this point.

Let's go ahead and code up the user input portion. We'll do printing
asterisks later.

Problem solving step: **Carrying out the Plan**.

Asking the user for input, we already know.

But how do we ask them repeatedly until they enter something valid? We
need to loop! How about looping while the input is invalid? Sure!

``` {.py .numberLines}
input_valid = False  # Assume it's invalid to start

while not input_valid:   # While not input valid ("while input invalid")
    x = input("Enter a number, 5-50 inclusive: ")
    x = int(x)

    if x >= 5 and x <= 50:
        input_valid = True   # We got a good number!
```

Let's study that pattern, because it's a common use of `while`.

We start by assuming that the success condition _isn't_ met. And then we
check every iteration of the loop, with `if`, to see if it is met. And
we loop while the success condition is `not` true.

Now, we're also supposed to print an error if the input is out of range.
How? We can do it in two lines.

If the `if` condition is `True`, then we have good input. Otherwise we
have bad input and should print a message... `if`... `else`! 

(_Note: the code below is a continuation of the program, above. Pay
attention to the line numbers!_)

``` {.py .numberLines startFrom="7"}
    if x >= 5 and x <= 50:
        input_valid = True   # We got a good number!
    else:
        print("The number must be between 5 and 50, inclusive!")
 
```

If you haven't already, code that up and run it. No, it's not the
complete program, but it's the complete first step of the program, and
we can test it before moving on just to be confident that this part
works.

Run it and try it with some numbers. If you enter an invalid number, it
should tell you so and ask again. If you enter a valid number,
`input_valid` becomes `True` and the `while` loop exits (because the
continuation condition is `not input_valid`).

Once you're satisfied it's working correctly, let's move back to the
spec and concentrate on printing out the asterisks.

Problem solving step: **Devising a Plan**.

If the user enters `x`, we want to print out `x` count of characters,
total. The first 30 of these will be `#`, and any after that will be
`*`.

Before we start things out, let's use a different planning technique:
_simplify the problem_.

Let's forget about the `*` for now and just print out `#` characters,
however many the user specified. Later we'll add the code for `*`.

> _Simplifying the problem allows you to more easily tackle it, and
> leads you to see ways to add the missing features later._

The plan for this simplified phase isn't that tough:

```
For however many numbers the user inputs:
   Print a `#`.
```

Problem solving step: **Carrying out the Plan**.

Since we know how many `#`s we want to print (the user entered the
number!) this would be a great place for a `for` loop. Let's print
those:

``` {.py .numberLines startFrom="12"}
# Print the line
for i in range(x):
    print("#")
```

Run it! How did it do?

Hmmm. Looks like it's printing a hash on each line. The `print()`
function puts a _newline_ at the end of the line. We need to override
that behavior, and there's an easy way to do it.


``` {.py .numberLines startFrom="12"}
# Print the line
for i in range(x):
    print("#", end="")  # Set the end-of-line character to nothing

print()  # Add a newline to the end of the line
```

We did a bit of magic there. We passed another argument to `print()`
that told it we wanted it to put nothing (an empty string, `""`) at the
end of the line instead of the newline character it noramlly tacks on.

You could go crazy and say `end="Beej"` and it would put the word "Beej"
after every hashmark. Do it. Go crazy.

Getting there! But we're not out of the woods yet. We need to make it so
that for character more than 30 characters out, we print a `*` instead
of a `#`.

Problem solving step: **Devising a Plan**.

This is like the plan for printing the line from before, but we
simplified that, remember? So we have to add some complexity in to mett
the spec.

```
For however many numbers the user inputs:
    If we're at the 30th character or earlier:
        Print a `#`.
    Otherwise:
        Print a `*`.
```

And that's looking like a good case for `if` _inside_ our `for` loop!

Problem solving step: **Carrying out the Plan**.

Let's add that `if` logic to the `for` loop at the end:

``` {.py .numberLines startFrom="12"}
# Print the line
for i in range(x):
    if i < 30:
        print("#", end="")  # Set the end-of-line character to nothing
    else:
        print("*", end="")

print()  # Add a newline to the end of the line
```

There's something here to note that's subtle and important:

* If the user enters `40`, the value of `i` runs from `0` to `39`,
  because the body of the `for` loop does not execute when `i` reaches
  its maximum value.
* But `0` to `39` is still 40 iterations, right? Just like 0,1,2,3 is a
  total of 4 iterations. So we're still getting all 40 characters even
  though the counter is running from `0` to `39`.
* However, since the counter is running from `0`, that means the
  highest character that will be a `#` occurs when `i` is `29`, not when
  `i` is `30`. This is why we test `i < 30`^[We could have also tested
  `i <= 29`.] and not `i < 31`.

But there we have it!

Be sure to test with the _edge cases_. These are inputs that are at the
edges of conditions in your program.

For example, we have conditions testing input against 5 and 50. So test
with `4`, `5`, `50`, and `51`, both sides of those conditions.

Where else do we have an edge case in the code? That right: the `if`
when printing. The first 30 are supposed to be `#` with `*` after that.
So test with `30` and make sure it's all `#`s, and then test with `31`
and make sure there's a single `*`.

_Testing the edge cases_ is an all-powerful programming technique that
all devs use to great effect.

And, while you're at it, test a bunch of other numbers to make sure it
behaves like you'd expect.

**Bonus Question:** Can you think of another way to draw the line of
characters without using an `if` inside the loop? (There's a hint at
this footnote^[Have two loops!].) _Coding is creative!_ There's more
than one way to do these things. Try them and see which you like better.


## Exercises

**Remember: to get your value out of this book, you have to do these
exercises.** After 20 minutes of being stuck on a problem, you're
allowed to look at the solution.

1. Print out the sum of the numbers from `1` to (and including) `10000`.
   ([flx[Solution|ex_10ksum.py]].)

2. Print out values for `x` and `x**4` for all `x` between 0 and 99,
   inclusive. ([flx[Solution|ex_xfourth.py]].)

3. Ask the user to input a number, or the word `quit`. If the user
   enters a number, print out that number times 10. If the user enters
   `quit`, the program should complete.
   ([flx[Solution|ex_ntimes10.py]].)

4. Prompt the user for two numbers. Print out all the odd numbers
   between and including those two numbers.
   ([flx[Solution|ex_oddsbetween.py]].)

5. Print out the numbers from `1` to `100`. Except if the number is
   divisible by `3`^[A number `x` is divisible by `3` if `x % 3 == 0`.],
   print `Fizz` instead. If the number is divisible by `5`, print `Buzz`
   instead. And if the number is divisible by 3 and divisible by 5,
   print `FizzBuzz`^[This is a famous interview problem for junior
   devs.]. There are a lot of ways to solve this one.
   ([flx[Solution|ex_fizzbuzz.py]].)

6. Make up two more exercises and code them up.


## Summary

We covered all kinds of super-important things this chapter.

* Flow Control
* Boolean algebra, conditional expressions, `True`, `False`
* `if`-`else`
* `while` loops and `for` loops
* A bit about testing edge cases

Guess what! You now know enough Python syntax to solve any computing
problem! [flw[I'm not kidding|Turing_completeness]]!

See, it's not knowing all the syntax that's important; it's the ability
to figure out how to put it all together in the right way.

That said, we haven't learned enough Python syntax to necessarily make
solving every computing problem _easy_. In the upcoming chapters, we'll
learn more tools that Python gives you to increase the size of your
problem-solving toolkit.


