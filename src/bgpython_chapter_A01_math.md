# Appendix A: Basic Math for Programmers

I know what you're thinking: _screw this_.

Or maybe your language is even more blue.

But bear with me for just a moment. Knowing a few basic mathematical
operations can really help you be a better developer, as well as help
you understand code that you come across.

This section isn't so much about application of these functions, but is
more about their definition. It'll be up to you to use them as you see
fit.

## Arithmetic

Addition, subtraction, multiplication, and---don't fall asleep on me
already---division. The _Big Four_ of grade school math.

I'm not going to talk about what they do, and will presume you remember
that from however-many years ago.

But I do want to talk about which comes first, because you might have
forgotten.

What do I mean by that?

Take this expression: $1+2\times3$

If we first add $1+2$, we get $3$. And then we multiply it by $3$ and we
get the answer of $9$.

But wait! If we first multiply $2\times3$ and get $6$, then we add $1$
we get an answer of $7$!

So... which is it? $9$ or $7$?

What we need to know is the _order of operations_ or the _precedence_ of
one operator over another. Which happens first, $+$ or $\times$?

For arithmetic, here is the rule: do all the multiplications and
divisions _before_ any additions and subtractions.

So: $1+2\times3=7$

We'll revisit order of operations as we continue on.

In Python, we can just use the operators `+`, `-`, `*`, and `/` for
addition, subtraction, multiplication, and division, respectively.

## Negative numbers

I'm not going to talk much about these here, but negative numbers are
numbers less than 0, and they're indicated by a minus sign in front of
the number. $-7$ means "$7$ less than zero".

And I _know_ that's a crazy concept. Like how can you have $-12$ apples
on the table? It doesn't seem particularly rooted in reality.

But a closer to home example might be me saying, "I owe you $-35!" which
means, in effect, _you_ owe _me_ $35!

Remember some simple rules:

If you multiply a negative number by a negative number, the result is
positive.

$-3\times-7=21$

If you multiply a negative number by a positive number, the result is
negative.

$-3\times7=-21$

If you add a negative number to a positive number, it's just like
subtracting the negative number from the positive number:

$-7+100=93$

or, equivalently:

$100+(-7)=100-7=93$

## The Power of Exponents

Let's say you wanted to multiply the number $7$ by itself, say, 8 times.
We could write this:

$7\times7\times7\times7\times7\times7\times7\times7$

I _guess_ that's not entirely awful.

So let's go all out. I want to multiply $7$ by itself $3490$ times. I'm
going to head to the pub while you work on that. Let me know when you're
done.

Luckily for you, mathematicians are lazy. They hate writing more than
they have to, so they invent new notations out of thin air to avoid the
extra work. Just like how I keep packing the kitchen trash down so I
don't have to run it outside.

Actually, no, it's not really like that at all^[Apart from the lazy
factor, that is.].

So what they invented is another way of saying "3490 7s multiplied by
each other" that didn't involve an endless line of $7$s and $\times$s.
And it looks like this:

$7^{3490}$ (read "7 to the 3490th power")

That means 3490 $7$s multiplied together. We call this _raising to a
power_ or _exponentiation_.

Or, put another way:

$7^8=7\times7\times7\times7\times7\times7\times7\times7$

We have all kinds of fun facts! Ready?

In the example $7^8$, the number $7$ is what we call the _base_ and the
number $8$ we call the _exponent_.

If you want to write that code in Python, you'd write:

``` {.py}
print(7**8)  # prints 5764801
```

The exponent must be non-negative, so zero or larger.

But wait---zero? How do you multiply a number by itself zero times? It's
a valid question, and one that has baffled philosophers for time
immemorial. But not mathematicians! Like power-crazed numerical
dictators, they cried, "We made this up, and we declare that _anything_
to the zeroth power is $1$. End of story!"

So there we have it.  $n^0=1$ for all $n$.

But their unquenchable thirst for power didn't end there. Mathematicians
also decided that there was such a thing as _negative exponents_.

If you have a negative exponent, you need to invert the fraction before
applying the exponent. The following is true:

$4^{-3}=\left(\cfrac{1}{4}\right)^3$

$\left(\cfrac{3}{4}\right)^{-8}=\left(\cfrac{4}{3}\right)^8$

And in case you're wondering how to raise a fraction to an exponent, you
just apply the exponent to the numerator and denominator:

$\left(\cfrac{4}{3}\right)^8=\cfrac{4^8}{3^8}=\cfrac{65536}{6561}$

We also have some shorthand names for certain exponents.

$n^2$ we say "$n$ squared". Anything raised to the power of $2$ is that
number _squared_.

$n^3$ we say "$n$ cubed". Anything raised to the third power is that
number _cubed_.

In casual writing, you'll often see the caret character `^` used to
indicate an exponent. So if someone writes `14^4`, that's the same as
$14^4$.

Lastly, precedence. We know that multiplication and division happen
before addition and subtraction, but what about exponentiation?

Here's the rule: exponentiation happens before arithmetic.

With $2+3^4$, we first compute $3^4=81$, _then_ add $2$ for a total of
$83$.

## Parentheses

So what if you _want_ to change the order of operations, like some kind
of mathematical rebel?

What if you have $1+2^3$ and you want $1+2$ to happen before the
exponentiation?

You can use parentheses to indicate that operation should occur first,
like this:

$(1+2)^3$

With that, we first compute $1+2=3$, and then we raise that to the 3rd
power for a result of $27$.

You could also do this:

$2^{(3+4)}$

Remember: parentheses first! $3+4=7$, so we want to compute $2^7$ which
is $128$. (Good software developers have all the powers of $2$
memorized up through $2^{16}$. Well, crazy ones do, anyway.)

Python uses parentheses, as well. The above expression could be written
in Python like this:

``` {.py}
2**(3+4)
```

Easy peasy.

One final note: if an exponent is a long expression without parentheses,
it turns out the parentheses are _implied_. The following equation is
true:

$2^{(3+4)}=2^{3+4}$

## Square root

Square root is a funny one. It's the opposite of _squaring_, which if
you remember from the earlier section means _raising to a power of 2_.
But, again, _square root_ is the opposite of that.

It's asking the question, "For a given number, which number do I have to
multiply by itself to get that number?"

Let's examplify!

But before we do, the weird lightning bolt line thing is the
mathematical symbol for the square root of a number.

Let's ask for the square root of 9:

$\sqrt9=?$

That's asking, what number multiplied by itself makes $9$? Or, in other
words, what number raised to the 2nd power makes $9$? Or, in other
words, what number squared makes $9$?

Hopefully by now you've determined that:

$3\times3=9$

and, equivalently:

$3^2=9$

so therefore:

$\sqrt9=3$

What about some other ones?

$\sqrt{16}=?$
$\sqrt{25}=?$
$\sqrt{36}=?$
$\sqrt{12180100}=?$

Note that all of those have integer answers. If the square root of
number is an integer, we call that number a _perfect square_. 16, 25,
36... these are all perfect squares.

But you can take the square root of any number.

$\sqrt{17}=4.123105625617661$ approximately.

17 is _not_ a perfect square, since it doesn't have an integer result.

Now, you might be imagining what would happen if you tried to take the
square root of a negative number:

$\sqrt{-100}=?$

After a bit of thought, you might realize that no number multiplied by
itself can ever result in $-100$ so... what can you do?

You might think, "We're doomed," but not mathematicians! They simply
defined:

$\sqrt{-1}=i$

and invented an entire mathematical system around what they called
[fl[_imaginary numbers_|https://en.wikipedia.org/wiki/Imaginary_number]]
that actually have some amazing applications. But that's something you
can look up on your own.

In addition to square roots, there are also cube roots. This is asking,
"What number cubed results in this number?" This is indicated by a small
$3$ above the root symbol:

$\sqrt[3]{27}=x$

which is the inverse of the equation:

$x^3=27$

Can you figure out what $x$ is?

What about how to do this in Python?

For square roots, the preferred way is to use the `sqrt()` function in
the `math` module that you `import`:

``` {.py}
import math

print(math.sqrt(12180100))  # prints 3490.0
```

What about cube roots? Well, for that, we're going to jump back to
exponents and learn a little secret. You can raise numbers to _fractional_
powers. Now, there are a lot of rules around this, but the short of it
is that these equations are true:

$\sqrt{x}=x^\frac{1}{2}$\ \ \ \ $\sqrt[3]{x}=x^\frac{1}{3}$\ \ \ \ $\sqrt[4]{x}=x^\frac{1}{4}$

and so on. Raising a number to the $\frac{1}{3}$ power is the same as
taking the cube root!

Like if we wanted to compute the cube root of $4913$, we could compute:

$\sqrt[3]{4913}=4913^\frac{1}{3}=17$

And you can do that in Python with the regular exponent operator `**`:

``` {.py}
print(4913**(1/3))  # prints 16.999999999999996
```

Hey---wait a second, that's not $17$! What gives?

Well, turns out that floating point numbers in computers aren't exact.
They're close, but not exact. It's something developers need to be aware
of and either live with or work around.

Lastly, because square root, cube root, and all the other roots are just
exponents in disguise, they have the same precedence as exponents: they
happen _before_ arithmetic.

## Factorial

Factorial is a fun function.

Basically if I ask for something like "5 factorial", that means that I
want to know the answer when we multiply 5 by all integers less than 5,
down to 1.

So I'd want to know:

$5\times4\times3\times2\times1$

the answer to which is $120$.

But writing "factorial" is kind of clunky, so we have special notation
for it: the exclamation point: $!$. "5 factorial" is written $5!$.

Another example:

$6!=6\times5\times4\times3\times2\times1=720$

As you can imagine, factorial grows very quickly.

$40!=815915283247897734345611269596115894272000000000$

In Python, you can compute factorial by using the `factorial()` function
in the `math` module.

``` {.py}
import math

print(math.factorial(10))  # prints 3628800
```

Factorial, being multiplication in disguise, has the same precedence as
multiplication. You do it before addition and subtraction.

## Scientific notation

For really large floating point numbers, you might see things like this
appear:

``` {.py}
print(2.7**100)  # 1.3689147905858927e+43
```

What's that `e+43` at the end?

This is what we call _scientific notation_. It's a shorthand way of
writing really large (or small) numbers.

The number above, `1.3689147905858927e+43`, is saying this,
mathematically:

$1.3689147905858927\times10^{43}$

Now, $10^{43}$ is a _big_ number. So multiplying $1.3689$ etc. by it
results in a very large number, indeed.

But that's not all. We can use it to represent very small numbers, too.

``` {.py}
print(3.6/5000000000000000000)   # 7.2e-19 
```

`7.2e-19` means:

$7.2\times10^{-19}$

And $10^{-19}$ is a very small number (very close to 0---remember that
$10^{-19}=\frac{1}{10^{19}}$), so multiplying $7.2$ by it results in a
very small number as well.

Remember this:

* If you see `e-something` at the end, it's a very small number (close
  to 0).
* If you see `e+something` at the end, it's a very large number (far
  from 0).

## Logarithms

Hang on, because things are about to get weird.

Well, not _too_ weird, but pretty weird.

Logarithms, or _logs_ for short, are kind of the opposite of exponents.

But not opposite in the same way square roots are opposite.

That's convenient, right?

With logs, we say "log base x of y". For example, "log base 2 of 32",
which is written like this:

$\log_2{32}$

What that is asking is "2 to the what power is 32?" Or, in math:

These are both true:

$x=\log_2{32}$

$2^x=32$

So what's the answer? Some trial and error might lead you to realize
that $2^5=32$, so therefore:

$x=\log_2{32}=5$

There are three common bases that you see for logs, though the base can
be any number: 2, 10, and $e$.

Base 2 is super common in programming.

$e$ is the base of the [fl[_natural
logarithm_|https://en.wikipedia.org/wiki/Natural_logarithm]], common in
math, and uncommon in computing.

So what are they good for?

The main place you see logarithms in programming is when using Big-O
notation to indicate [fl[computational
complexity|https://en.wikipedia.org/wiki/Big_O_notation]].

The big thing to remember there is that a number gets large, the log of
the number remains small. Here are some examples:

|_x_|log~2~_x_|
|-------:|-------------------------------:|
|1|0.0000|
|10|3.3219|
|100|6.6439|
|1000|9.9658|
|10000|13.2877|
|100000|16.6096|
|1000000|19.9316|
|10000000|23.2535|

The log-base-2 of a big number tends to be a much smaller number.

## Large Numbers

Python is really good with large integer numbers. In fact, it has what
we call _arbitrary precision integer math_. That means we can hold
numbers as big as memory can handle, which is large.

So if you ask Python to compute $100000!$, it will do it. The result,
incidentally, is 465,575 digits long. No problem.

But the same is _not_ true for floating point numbers (numbers with a
decimal point). Python generally uses 64 bits to represent floating
point numbers, which means there's a limit to the amount of
precision---you can only have 16 digits in your number, though you can
raise that number to huge positive or negative powers to get very large
or very small numbers.

Floating point is brilliant because it can represent really huge and
really small numbers, but the number of digits you have at your
disposal is limited.
