<!--
# vim: ts=4:sw=4:nosi:et:tw=72
-->

# What is Programming, Anyway?

Let's say you're entirely new to this stuff. You have a computer, you
know how to use it, but you don't know how to make it do exactly what
you want it to.

It's the difference between a _user_ and a _programmer_, right?

But what does it mean to _program_ a computer?

In a nutshell, you have a goal (what you want to compute), and
programming is the way you get there.

A _program_ is a description of a series of steps to complete that
computation, blah blah blah...

Okay---instead think of a sequence of steps that you have to do to do
_anything_. Like baking cookies for example.

> _**Fun Computing Fact:** everyone likes yummy cookies._

You often have that sequence of steps, that recipe, written down on a
piece of paper. By itself, it's definitely not cookies. But when you
apply a number of kitchen implements and ingredients and an oven to it,
pretty soon you have some cookies.

Of course, in that case _you_ have to do the work. With programming, the
computer does the work for you. But you have to write down the recipe.

The recipe _is_ the program. Programming is the act of writing down that
recipe so the computer can execute it. And get those cookies baked.

Mmmm. Cookies.

Some programs are simple. "Add up these 12 numbers" is an example. It's
a breeze for the computer to do that.

But others are more complicated. They can extend into millions of lines
long, or even tens of millions, written by large teams over many years.
Think triple-A video game titles, or the Linux operating system.

When you're first starting, large programs like that seem impossible.
But here's the secret: each of those large programs is made up of
smaller, well-designed building blocks. And each of those building
blocks is made up of smaller of the same.

And when you start learning to be a programmer, you start with the
smallest, most basic blocks, and you build up from there.

And you keep building! Writing software is a lifelong learning process.
There are _always_ new things to learn, new technologies, new languages,
new techniques. It's a craft to be developed and perfected over a
lifetime. Sure, at first you won't have that many tools in your toolkit.
But every moment you spend working on software gives you more experience
solving problems, and gives you more methods to attack them.

## What's This Talk About Problem Solving?

In other words, I know what I want to see... how do I get there with the
tools I know?

There's a [fl[great scene in the movie Apollo
13|https://www.youtube.com/watch?v=ry55--J4_VQ]] [ix[Apollo 13]] that I
love. The CO~2~ scrubbers on the command module are spent, and the team
wants to use the scribbers from the lunar module to replace them. But
the former are round, and the latter are square and won't fit. Of
course, the spacecraft has limited resources to repair it---just
miscellaneous stuff on board that was meant for the mission.

On the ground, the team has all those items at hand, and they dump them
on a table. A staff member holds up a square scrubber and a round
scrubber and tells everyone, "We gotta find a way to make _this_ fit
into the hole for _this_," he gestures toward the table, "using nothing
but _that_."

And that's what programming is like, except, obviously and fortunately
no lives are at stake. (Typically.)

You have a limited set of programming techniques at your disposal, and
you have the goal that you want to achieve. How can you get to that goal
using only those tools? It's a puzzle!

## So How To Solve It?

> _**Fun Programming Fact:** Most devs have no idea how to solve a
> problem when they're first presented with it. They have to
> systematically attack it._

Programmers fully intend to use a well-reasoned approach to solving
arbitrary problems. In reality, they often run off in high spirits and
dive right into coding before they've done some of the very important
preliminary work, but since they love programming so much they don't
seem to mind wasting time.

(And it's not really a waste of time, because every second you're
programming, you're learning!)

But lots of _bosses_ do consider unplanned development to be a waste of
time. Time is also known as "money" to the company that hired you. And
the only thing more precious to a company than money is more money.

Imagine that you said, "I want to build an airplane!" and ran off an
bought a pile of tools and metal and rivets and levers and started
bolting it together immediately. You might find after a while that, oh
you should have figured out how big the engine was before you built the
fuselage, but, hey, no problem, you have time. You can just rebuild the
fuselage. So you do. But now the canopy doesn't fit. So you have to
rebuild it again, and so on.

You could have saved a lot of time by actually _planning_ what you were
going to do before you started building.

It's the same with software.

> _**Fun Programming Proverb:** Hours of debugging can save you minutes
> of planning._

There are a number of problem solving frameworks out there. These are
blueprints for how to approach a programming problem and solve it, even
if you have no idea how to solve it when you first see it.

Here's an example of a standard problem-solving framework:

1. **Understand the Problem**. Get clarity on all parts of the problem.
   Break it down into subproblems, and break those subproblems down. If
   you don't understand the problem, any solutions you come up with will
   be solving the wrong problem! You know you understand the problem
   when you can explain it to someone completely.

2. **Make a Plan**. How are you going to attack this with the tools you
   have at your disposal and the techniques you know? You know you're
   done making a plan when you're able to easily convert your plan into
   code.

   Often when planning you realize there's something about the problem
   you don't fully understand. Just for a bit, pop back to Step 1 until
   it's clear, then come back to planning.

3. **Code it up!** Convert your plan into code and get it working.

   Often in this phase, you find that there was either something you
   didn't understand, or something the plan didn't account for. Drop
   back a step or two until it's resolved, then come back here.

4. **Post-mortem**. Look back on the code you got working, and consider
   what went right and what went wrong. What would you do differently
   next time? What techniques did you learn while writing the code? Was
   there any place you could have structured things better, or anyplace
   you could have removed redundant code?

What's neat about this is that developers apply the steps of problem
solving to the _entire program_, and they also apply it to the smaller
problems _within the program_. A big computing problem is always
composed of a number of subproblems! The problem solving framework is
used within the problem solving framework!

An example of a real-life problem might be "build a house". But that's
made up of subproblems, like "build a foundation" and "frame the walls"
and "add a roof". And those are made up of subproblems, like "grade the
lot" and "pour concete".

In programming, we break down problems into smaller and smaller
subproblems until we know how to solve them with the techniques we know.
And if we don't know a technique to solve it, we go and learn one!

Being a developer is the same as being a problem solver. The problems
ain't easy, but that's why it pays the big bucks. 

So you should expect that any time you see a programming problem in this
book, on a programming challenge website, at school, or at work, that
the answer will not be obvious. You're going to have to work hard and
spend a lot of time to get through the first problem solving steps
before you'll even be ready to start coding.

## What is Python?

Python is a _programming language_. This means it's vaguely readable by
humans, and completely readable by a machine. (As long as you don't make
the tiniest mistake!) This is a good combination, since people are bad
at reading the actual `1011010100110` code that machines use. We use
these _higher-level_ langauges to help us get by.

In this case, another piece of software called the Python _interpreter_
takes the code we write in the Python language and runs it, performing
the operations we've requested.

So before we begin, we need to install the Python interpreter. This is
one of the most annoyingly painful parts of the whole book, but luckily
it only has to be done once.

Okay, gang! Let's get it... over with!

...I really need to work on the end of that inspirational speech.
