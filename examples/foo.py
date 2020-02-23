import sys

# Parse the command line

if len(sys.argv) == 2:
    filename = sys.argv[1]

elif len(sys.argv) == 1:
    # We'll use this as a sentinel value later if we need to prompt for
    # a filename when writing the file.
    filename = None

else:
    print("usage: lineedit.py [filename]", file=sys.stderr)
    sys.exit(1)


def read_file(filename):
    """Read a file from disk"""
    lines = []

    with open(filename) as f:
        for line in f:
            lines.append(line)

    return lines


def one_to_zero(n):
    """Convert a number from a 1-based index to a 0-based index."""
    return n - 1

def zero_to_one(n):
    """Convert a number from a 0-based index to a 1-based index."""
    return n + 1


def handle_list(args, lines):

    if len(args) == 1:
        # Compute start and end lines
        start = one_to_zero(int(args[0]))
        end = start + 10  # print 10 lines

    else:
        print("usage: l line_num")
        return

    # Make sure start isn't before the beginning of the list
    if start < 0:
        start = 0

    # Make sure end isn't past the end of the list
    if end > len(lines):
        end = len(lines)

    # Print all the lines
    for i in range(start, end):
        # end="" to suppress newlines (since lines already have them)
        print(f'{zero_to_one(i)}: {lines[i]}', end="")


def handle_delete(args, lines):
    """Delete a line in the file."""

    if len(args) == 1:
        # Get the line number to delete
        line_num = one_to_zero(int(args[0]))

    else:
        print("usage: d line_num]")
        return

    # Make sure we're in range
    if line_num < 0 or line_num >= len(lines):
        print("no such line")
        return

    # Delete the line
    lines.pop(line_num)

def handle_edit(args, lines):
    """Edit a line in the file."""

    if len(args) == 1:
        # Get the line number to edit
        line_num = one_to_zero(int(args[0]))
    else:
        print("usage: e line_num")
        return

    # Make sure we're in range
    if line_num < 0 or line_num >= len(lines):
        print("no such line")
        return

    # Edit the line, adding a newline to the end (since input() strips
    # it off).
    lines[line_num] = input() + '\n'


if filename is not None:
    lines = read_file(filename)
else:
    lines = []


# Main loop

done = False

while not done:
    command = input("> ").strip()

    # If the user entered a blank line, just give them another prompt
    if command == '':
        continue

    # Grab the arguments after the command
    args = command.split(" ")[1:]

    if command[0] == 'q':
        done = True

    # List lines
    elif command[0] == 'l':
        handle_list(args, lines)

    # Delete a line
    elif command[0] == 'd':
        handle_delete(args, lines)

    # Edit a line
    elif command[0] == 'e':
        handle_edit(args, lines)

    else:
        print("unknown command")
