<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**.
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**.
-->

# Importing Modules

**WIP**

## Objective

* Learn what a module is
* How to find modules to use
* How to import modules
* Build 
* Splitting projects: Importing your own files

## Chapter Project Specification {#mod-proj-spec}

TODO

## What and Why of Modules

Problem-solving step: **Understanding the Problem**.

Modules are pieces of self-contained code that you can _import_ into
your code and use. Think of them like prefabricated building blocks that
you can put together in your project to accomplish tasks without needing
to write out the details yourself.

This is actually a really powerful concept that you have at your
disposal. Tons of code has already been written, and you can just use it!

Do you want to compute anything to do with date and time? Python has a
module for that.

Do you want to draw graphics on the screen? Python has a module for
that.

Do you want to generate animated GIFs from a sequence of stills?
There's a module for that.

Do you want to download an image from a URL and save it to disk? There
are modules for that.

There are [fl[_tons_ of modules built-in to
Python_|https://docs.python.org/3/library/index.html]]. Give the list a
skim so you know what's there, but you don't need to drill down at all
unless you're dying ot curiosity over a particular module.

Are there are [fl[_zillions_ of third-party modules|https://pypi.org/]]
you can use, as well.

You can import as many modules as you want into an individual project.

## Using a Module

Problem-solving step: **Understanding the Problem**.

You declare your intent to us a module with the `import` keyword. We're
going to do an example with the built-in [fl[`sys`
module|https://docs.python.org/3/library/sys.html]], which contains all
kinds of useful information about the system.

Let's see what platform Python thinks we're running.

But first, some syntax.

When using a function or variable inside a module, you use the dot
operator to get the variable, similar to how you get attributes from
objects. Deep down, it's very similar, indeed, but how we get there is a
little bit different.

Step one is to `import` the module. Then you can access the members of
that module.

Problem-solving step: **Devising a Plan**

Digging through the documentation for the `sys` module, we find there's
something called `sys.platform` that looks really promising.

Let's print it!

Problem-solving step: **Carrying Out the Plan**

``` {.py}
import sys    # Gets us access to all the sys goodies

print(sys.platform)
```

What does it output for you?

For me, on Linux or Windows WSL, it prints "`linux`". On Windows, it
prints "`win32`".

Notice there was nothing we had to do ourselves to make this
determination. (Which is good, because it would be a pain to write!)
Fortunately the `sys` module had everything we needed right there.

## Command Line Arguments

Problem-solving step: **Understanding the Problem**.

I've been hiding something.

In terms of how you run Python programs from the command line.

It turns out you can add things _after_ the Python program name.

Say what?

Let's say you have a program called `foo.py`. You can run it like this,
of course:

```
python foo.py
```

You can also run it like this:

```
python foo.py something another antelopes
```

Those extra words after the program name are called _command line
arguments_.

But _why_ would you do this?

So you can control the behavior of the program from the command line!
When you run it, it's nice to be able to influence behavior this way
instead of having to call `input()` with prompts and everything else.

But _how_ do you get those extra command line arguments?

Our good friendly `sys` module can help us again here.

The variable `sys.argv` is a list that contains the program name
followed by all the command line arguments.

Run this program with a variety of command line arguments and see what
it outputs:

``` {.py}
import sys

print(sys.argv)
```

Example output:

```
$ python foo.py
['foo.py']
```
```
$ python foo.py aa bb cc
['foo.py', 'aa', 'bb', 'cc']
```

So at runtime, we can look in `sys.argv` and make decisions about what
we want to do!

Let's put it to use in the next section.

## Printing Calendars

Print a calendar for any month and year!

Problem-solving step: **Understanding the Problem**.

Your first thought should have been something like, "Holy cow,
Beej---how am I supposed to figure all that out? Was November 12, 1955 a
Friday or a Saturday? I don't know!"

Luckily, we don't have to know! There's a module, `calendar`, that we
can use to do all the dirty work for us.

## Importing Your Own Files

### .pyc