import textwrap

matrix = """The Matrix is everywhere. It is all around us. Even
now, in this very room. You can see it when you look out your window,
or when you turn on your television. You can feel it when you go to
work, when you go to church, when you pay your taxes."""

# Get a list of lines of max width 40
lines = textwrap.wrap(matrix, width=40)

# We could do this to print out each line
#for l in lines:
#    print(l)

# Or I could just join them together by newlines and print the whole
# thing

print("\n".join(lines))