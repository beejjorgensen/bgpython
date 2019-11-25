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

## Chapter Project

For this chapter, we want to write a program that asks the user for a
number between 5 and 50, inclusive. 

If a number outside that range is entered, an error message is printed
and the user is asked again to enter a valid number.

Once the number is obtained, the program will print out that many `*`
characters in a row. EXCEPT all characters at position 31 and above
should print out an `x`. (Characters before that position will still be
an `x`.)

For example, an input of 10 would result in:

```
**********
```

whereas an input of 37 would result in:

```
******************************xxxxxxx
```

Keep this program in mind as we learn the techniques to implement it.


## What is Flow Control?

Problem solving step: **Understand**.

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
critera you specify. Figuring out which criteria to specify is the job
of a programmer and where most of the hard work comes in.

Eventually we're going to code up things that say "If some condition is
true, do one thing" or "If some condition is false, do another thing".

But before that, we have to meet someone: George Boole.


## Boolean Algebra and Expressions

[fl[George Boole|https://en.wikipedia.org/wiki/George_Boole]] was quite
and interesting character. From humble beginnings in the early 1800s, he
went on to develop the mathematics that became, in many ways, the
foundation of modern computation. Pretty awesome.

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

Now we're about ready to go. Let's learn how to do this in Python.

## Boolean Operations in Python

The comparison operators in Python are:

|Operator|Effect|
|:-:|:-:|
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
Booleans (sometimes called bools for short). Add that to the collewction
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


