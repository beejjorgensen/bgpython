import sys


def read_file(filename):
    """Read a file from disk"""
    lines = []

    with open(filename) as f:
        for line in f:
            lines.append(line)

    return lines


def write_file(lines, filename):
    """Write a file to disk"""
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)


def zero_to_one(n):
    """Convert a number from a 0-based index to a 1-based index."""
    return n + 1


def one_to_zero(n):
    """Convert a number from a 1-based index to a 0-based index."""
    return n - 1


def get_num_arg(arg):
    """Helper function to get a numeric argument from a command."""
    v = int(arg)
    v = one_to_zero(v)

    return v


def handle_write(args, lines, filename):
    """Handle the write command"""

    if len(args) == 1:
        filename = args[0]
    else:
        print("usage: w [filename]")

    if filename is None:
        print("** You must specify a filename")
        return

    write_file(lines, filename)


def handle_list(args, lines):
    """List lines from the file."""

    if len(args) == 1:
        # Compute start and end lines
        start = get_num_arg(args[0])
        end = start + 10

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


def handle_edit(args, lines):
    """Edit a line in the file."""

    if len(args) == 1:
        # Get the line number to edit
        line_num = get_num_arg(args[0])
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


def handle_delete(args, lines):
    """Delete a line in the file."""

    if len(args) == 1:
        # Get the line number to delete
        line_num = get_num_arg(args[0])

    else:
        print("usage: d line_num")
        return

    # Make sure we're in range
    if line_num < 0 or line_num >= len(lines):
        print("no such line")
        return

    # Delete the line
    lines.pop(line_num)


def handle_append(args, lines):
    """Append a line in the file."""

    if len(args) == 1:
        # Get the line number to append at. +1 because we want to start
        # adding lines one _after_ the specified line.
        start = get_num_arg(args[0]) + 1

    else:
        print("usage: a line_num")
        return

    done = False

    # We're going to loop until the user enters a single `.` on a line
    while not done:

        # Read a line of input
        line = input()

        # Check if we're done
        if line == '.':
            done = True
            continue  # Jump back to the `while`

        # Otherwise, insert the line, adding a newline to the end (since
        # input() strips it off).
        lines.insert(start, line + '\n')

        # And now on to the next line
        start += 1


# Main


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


# Read the file (if specified); set up the lines list
if filename is not None:
    lines = read_file(filename)
else:
    lines = []

done = False

# Main loop

while not done:
    command = input("> ").strip()

    # If the user entered a blank line, just give them another prompt
    if command == '':
        continue

    # Grab the arguments after the command
    args = command.split(" ")[1:]

    # Quit
    if command == 'q':
        done = True

    # Write (save) the file
    elif command[0] == 'w':
        handle_write(args, lines, filename)

    # List lines
    elif command[0] == 'l':
        handle_list(args, lines)

    # Edit a line
    elif command[0] == 'e':
        handle_edit(args, lines)

    # Delete a line
    elif command[0] == 'd':
        handle_delete(args, lines)

    # Append lines
    elif command[0] == 'a':
        handle_append(args, lines)

    else:
        print("unknown command")
