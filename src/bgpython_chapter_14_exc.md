<!--
vim: ts=4:sw=4:nosi:et:tw=72:spell:nojs
-->

<!--
Problem-solving step: **Understanding the Problem**
Problem-solving step: **Devising a Plan**
Problem-solving step: **Carrying Out the Plan**
Problem-solving step: **Looking Back**
-->

# Exceptions

**WIP**

## Objective

* Learn about different ways of handling errors
* Understand what exceptions are
* Write programs that catch exceptions
* Throw your own exceptions

## Project {#exc-proj-spec}

TODO

## Errors in Programs

Problem-solving step: **Understanding the Problem**

Let's stop and think about this from a conceptual standpoint for just a
minute.

Normally, a program produces data in the way you've asked for it. Unless
something goes wrong. In which case, it produces "bad" data.

Now, computers don't really have much of sense of right and wrong. So
how can we differentiate between good and bad data?

How can we tell that something's gone wrong?

## Classic Error Handling

Problem-solving step: **Understanding the Problem**

There's one way we've been using so far: the return value from a
function. If it's a particular _sentinel value_ that we're on the
lookout for, we can use that to determine success or failure.

For example, let's check out the `.find()` method on strings. This
returns the index in a string that a given substring can be found. For
example:

``` {.py}
s = 'Bears, beets, Battlestar Galactica'

x = s.find('beets')

print(x)  # 7, because that's the index 'beets' starts at in the string
```

The return value there of `7` is "good" data. We asked for a thing and
we got it. But what if something goes wrong?


``` {.py}
s = 'Bears, beets, Battlestar Galactica'

x = s.find('Dwight')

print(x)  # -1, because the substring isn't found
```

`-1` here is the sentinel value we're looking for to tell us if there's
an error.

We can make decisions on it. This is what I'd call "classic" error
handling. This is the way people used to handle errors when Stonehenge
was built. And, like Stonehenge, this method of handling errors is still
in use to this day. If it ain't broke, don't fix it.

OK, yes, I admit Stonehenge is broke. Allow me my analogy!

``` {.py}
s = 'Bears, beets, Battlestar Galactica'

x = s.find(substring)

if x == -1:
    print(f"Couldn't find {substring}")
else:
    print(f"Found {substring} at index {x}")
```

There! We successfully handled an error the classic way.

But now let's learn another way.


## Exceptions
