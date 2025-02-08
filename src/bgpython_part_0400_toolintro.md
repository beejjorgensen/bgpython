<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

# How do I write a program?

## Objectives

* Edit some source code in the IDLE editor.
* Run that program.

## The Problem That Needs Solving

Let's use our problem-solving framework!

1. **Understand the Problem**: We want to write a program that prints a
   neat little message to the screen.

2. **Devise a plan**

   1. Run IDLE.
   2. Open a new file from the File pulldown.
   4. Write code and save it to that file.
   5. Run your program from within the IDE.

3. **Carry out the Plan**: This is where we execute our plan. We'll
   do that in the following sections.

4. **Look Back**: We'll do this, below, as well. In future chapters,
   we'll leave these last two off the number list and just do them in
   subsequent sections.

Let's go!

## Launching your IDE and Opening a File

Run IDLE as discussed in the previous chapter.

Once in there, we're going to make a new file.

> It used to be that everyone who used computers knew what a file was.
> But these days, many people use computers for years without
> encountering the concept.
>
> So! A _file_ is a collection of data with a name. Examples of files
> would be images, movies, PDF documents, music files, and so on.
>
> The name indicates something about the contents of the file.
> Generally. It really can be anything, but that would be misleading,
> like labeling a box of raisins as "Chocolate".
>
> The name is split into two parts, commonly, separated by a period. The
> first part is the name, and the second part is the _extension_.
> Confusingly sometimes people refer to the name and extension together
> as the "name", so you'll have to rely on context.
>
> Sometimes, depending on the system, the extension is optional.
>
> As an example, here's a complete file name and extension:
>
> ``` {.default}
> hello.py
> ```
> <!-- ` -->
>
> There we have a file named `hello` and an extension `.py`. This is a
> common extension that means "this is a Python source code file".

Pull down "File→New" and that'll bring up a blank window.

And let's enter some code!

Type [flx[the following|hello.py]] into the editor (the line numbers,
below, are for reference only and shouldn't be typed in):

``` {.py .numberLines}
print("Hello, world!")
print("My name's Beej and this is (possibly) my first program!")
```

We're (almost) ready to run!

## Running the Program!

Hit `F5` from the editor window (you might have to hit `fn-F5` on the
Mac) to run the code. Alternately, you can pull down the "Run" menu and
select "Run Module".

If you haven't saved the file, it will prompt you to save the file.
(You can pull down "File→Save", or hit `COMMAND-S` or `CTRL-S` to do
this preemptively.)

Give it a good name, like `hello.py`.

And then, in the console window, you'll see the output appear! _[Angelic
Chorus!]_

``` {.default}
Hello, world!
My name's Beej and this is (possibly) my first program!
```

Did you miss it? Hit `F5` again and you'll see it appear again.

You just wrote some instructions and the computer carried it out!

Next up: write a Quake III clone!

Okay, so maybe there might be a small number of _in between_ things that
I skimmed over, but, as Obi-Wan Kenobi once said, "You've taken your
first step into a larger world."

## Exercises

Remember to use the [four problem-solving steps](#problem-solving) to
solve these problems: understand the problem, devise a plan, carry it
out, look back to see what you could have done better.

1. Make another program called `dijkstra.py` that prints out your three
   favorite [fl[Edsger Dijkstra
   quotes|https://en.wikiquote.org/wiki/Edsger_W._Dijkstra]].

## Summary

* Use the problem solving framework!
* Edit some source code in the IDLE editor.
* Run that program from within IDLE.

