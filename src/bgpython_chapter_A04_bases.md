# Appendix D: Number Bases

## How to Count like a Boss

You all have figured out by now how much I love numbers. So I'm going to
keep talking about them! Yay!

At some point, you might have heard that computers run on a bunch of 1s
and 0s. That they're binary. But what does that mean?

As humans, we're used to numbers. We use them all the time. 7 Dwarves.
Speed limit 55. 99 bottles of [your favorite beverage] on the wall.

We use the digits 0-9. And we use them repeatedly.

Computers, though, only have two digits: 0 and 1.

That seems kind of limiting. What happens if you want to go higher than
1, to say, 2?

Fortunately, there is a workaround. When computers want to go higher
than 1, they do the same thing we humans do when we want to go higher
than 9: we all add another _place_.

As a human counting apples on a table, you start with 0, 1, and keep
going... 7, 8, 9... and then you're out of digits for the _ones place_,
which represents the number of individual items (1s of items) we've seen
so far.

So you add another place, the _tens place_, which represents the number
of 10s of items we've seen so far.

If we count to 27 apples, a number made up of 2 and 7, we know we have 2
10s of apples, and 7 1s of apples. Let that sink in. Every value in the
10s place is worth 10 apples. And every value in the 1s place is worth 1
apple.

Therefore for 27 apples, we have

$2\times10+7\times1=27$

apples.

Let's do the same thing with $100. With that, I'm saying there's a 1 in
the 100s place, a 0 in the 10s place, and a 0 in the 1s place. This
means the value is

$1\times100+0\times10+0\times1$

or $100.

Computers go through this same process when they run out of digits,
except they run out of digits a lot sooner, since they only have two of
them.

Let's count apples in binary.

0, 1... oh no! We're out of digits. We have to add another place. Except
this time, in binary, it's not the 10s place... it's the 2s place.

0, 1, 10, 11... out of digits again! We have to add another place. This
time it's the 4s place:

0, 1, 10, 11, 100.

Let's look at that last number. In binary, that's saying we have 1 4, 0
2s, and 0 1s. For a total value of 4. For 5, we just have to put a 1 in
the 1s place: 101.

In fact, we can take any number and digest it that way. Take the human
number 7. That's made up of one 4, one 2, and one 1. $4+2+1=7$. So in
binary, we need a 1 in the 4s place, the 2s place, and the 1s place.
Which looks like this in binary: 111.

We've written the number 7 in two "languages". In human language, it
looks like $7$. In computer language it looks like $111$.

But, and this is important: _human 7 and computer 111 are the same
number_. They're just written in a different language, of sorts.

## Number Bases

These "number languages" actually have names for convenience. Human
numbers are called Jeff, and computer numbers, Alice.

I'm kidding. That's completely false---they're not named that.

Human numbers are called _decimal_ numbers.

Computer 1-and-0 numbers are called _binary_ numbers.

We also refer to these numbers by something called their _base_. This
basically means "the number of digits this number system has".

In decimal, we have 10 digits: 0-9. So decimal is a _base 10_ numbering
system.

In binary, we have 2 digits: 0 and 1. So binary is a _base 2_ numbering
system.

As we saw in the previous section, 7 in decimal (base 10) is the same as
111 in binary (base 2).

And we also saw that as we counted up in any numbering system, when we
ran out of digits, we had to add another place to create higher-valued
numbers.

There are other number bases in use. In fact, for any number you can
think of, you can use that as a base for a numbering system. Base 3.
Base 3490. Base 27. Whatever you want. Of course, a base 3490 numbering
system will have 3490 different digits, so I don't know what you're
going to use for those... you'll have to come up with a lot of new
shapes to draw numbers with.

Base 8, AKA _octal_, isn't that common any longer, but used to be used
by programmers consistently. Since it's base 8, it has the digits 0-7
available to use. When you use them up, you have to add another place,
the 8s place.

Notice how when you add a second place when you're adding up, the value
of that place is the base!

When you run out of digits with decimal (base 10), you add the 10s
place.

When you run out of digits with binary (base 2), you add the 2s place.

When you run out of digits with octal (base 8), you add the 8s place.

More generally, the place value is the base to the power of how many
digits you are from the right of the number, just counting up.

With the decimal number 1234, we have 1 in the thousands place, 2 in the
hundreds, 3 in the tens place, and 4 in the ones place. But the place
values 1000, 100, 10, and 1 are all powers of 10:

$10^0=1$
$10^1=10$
$10^2=100$
$10^3=1000$

And it's the same in binary. If we have the binary number 1011, that's 1
in the 8s place, 0 in the 4s place, 1 in the 2s place, and 1 in the 1s
place.

$2^0=1$
$2^1=2$
$2^2=4$
$2^3=8$

So the base is also tied into the value that any place in a number
represents. Which makes sense, since we have to add a new place when we
run out of digits, and if we have digits 0-9, that next place must
represent the number of 10s, because that's what comes after 9.

## Hexadecimal, Base 16

Hexadecimal, or _hex_ for short, is a really common number base for
programmers. And it's an interesting one to look at because, at base 16,
it has more digits than base 10. With base 10, we have 0-9. But with
base 16, we have 0 through... what?

Since we need more symbols to represent digits in base 16 than then
normal arabic numerals we use for 0-9, we've gone ahead and co-opted the
first part of the latin alphabet. We have 10 digits in 0-9, and we
grabbed 6 more "digits" with A-F to get up to 16 total digits.

That means when counting apples on the table in hex, we count:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12 ...

(Upper and lower case don't matter when writing numbers in hex.)

Look what happened when we got to F and ran out of digits: we added a
new place. What value does that place have?

Since this is base 16, it has to be the 16s place.

TODO

## Specifying the Number Base in Python

When you write down a number in your code, you have to tell Python what
the base is, or it'll assume you mean decimal (base 10).

For example, if I write

``` {.py}
x = 10101011
```

Is that binary? I mean, it looks like it!

But it's not! Because we didn't indicate otherwise, Python assumes this
is the decimal number ten million one hundred one thousand eleven.

We have some options
## Writing Numbers Down

Throughout all this, it's important to remember that number bases are
just other languages for representing the same number. You might write
number in code as



