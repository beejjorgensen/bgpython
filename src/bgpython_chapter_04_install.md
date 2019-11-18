<!--
# vim: ts=4:sw=4:nosi:et:tw=72
-->

# How do I install Python?

> _**Note!** Technology changes quickly---this book might already be out
> of date. If you get stuck, Google around for more modern answers.

## A note on Python2 versus Python3

Back in the day, Python version 2.x was king. Everything was written
using it. But it had a few shortcomings that couldn't be addressed
without major surgery. This surgery resulted in what we call _breaking
changes_ to the language. That is, old programs written for Python2
would be broken when trying to run them on Python3. They had to be
updated.

After only 37,600 years^[I always exaggerate.], the old Python2 code was
dragged kicking and screaming into the glorious future of Python3 and
now Python3 is finally the go-to version for all Python developers.

Not to say there's not tons of Python2 code out there, because there is,
but everything we'll be doing here will be in Python 3.6 and later.
(Google for `python2 vs python3` for more information on the differences
if you happen to cruelly find yourself in a Python2 environment.

## Checking to see if you already have Python installed

There are a number of different ways on different platforms.

As long as you can bring up a terminal and type on of the following and
get it to report version 3.6 or higher, you're set:

```
python3 --version
python --version
py --version
```

If those aren't installed, or none of them report version 3.6 or higher,
then read on for an install. (Or google for instructions to upgrade.)


## Windows WSL (recommended)

TODO

## Windows native

TODO -- is there a way to streamline this with Windows WSL?

## Mac

There are a few third-party package managers for command line tools for
the Mac, including [fl[Homebrew|https://brew.sh/]] and
[fl[MacPorts|https://www.macports.org/]]. We're only going to cover
Homebrew here.

Visit the Homebrew home page, and install it.

Then run this in the bash shell:

```
brew install python
```

After that, `python3 --version` should work.

You can also install Python straight from the official website, but lots
of people on the web recommend using brew to manage it instead.

## Linux/Unix-likes

The Linux community tends to be pretty supportive of people looking to
install things. Google for something like `ubuntu install python3`,
replacing `ubuntu` with the name of your distribution.
