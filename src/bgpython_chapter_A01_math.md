# Basic Math for Programmers

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

We'll revisit order of operations as we continue on.

In Python, we can just use the operators `+`, `-`, `*`, and `/` for
addition, subtraction, multiplication, and division, respectively.

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

But wait---zero? How do you multiple a number by itself zero times? It's
a valid question, and one that has baffled philosophers for time
immemorial. But not mathematicians! They said, "We made this up, and we
declare that _anything_ to the zeroth power is $1$. End of story!"

So there we have it.  $n^0=1$ for all $n$.

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

## Square root

Factorial

Shifting

Scientific notation

Logs

Trig?
