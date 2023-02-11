import sys

# Make sure the user has entered enough stuff on the command line
if len(sys.argv) < 4:
    # If not, tell them how to use this program
    print(f'usage: {sys.argv[0]} filename count word1 [word2 ...]')
    # Exiting with a non-zero code indicates failure to the shell, and
    # is conventional:
    sys.exit(1)

# Let's get some decent names for these values to make our code easier
# to read
filename = sys.argv[1]
count = int(sys.argv[2])

# Now build up the lines. We'll join all the remaining arguments with
# spaces, and add a newline to the end:
line = " ".join(sys.argv[3:]) + '\n'

# Open the file
with open(filename, "w") as f:
    # Loop through the count and write lines that many times. "_" as a
    # variable name indicates to readers that you're not interested in
    # the value from the range() iterator---you're merely using it to
    # loop a number of times.
    for _ in range(count):
        f.write(line)
