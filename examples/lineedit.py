import sys
import os


def read_file(filename):
    """Read a file from disk"""
    lines = []

    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip(os.linesep))

    return lines


def write_file(lines, filename):
    """Write a file to disk"""
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + '\n')


def normalize_start_end(start, end, lines):
    """Make sure start and end values are sane"""
    if end < start:
        end = start

    if start < 1:
        start = 1

    if end > len(lines) + 1:
        end = len(lines) + 1

    return start, end


def command_write(command, lines, filename):
    """Handle the write command"""

    command = command.split(' ')

    if len(command) == 2:
        filename = command[1]
    elif len(command) != 1:
        print("usage: w [filename]")

    if filename is None:
        print("** You must specify a filename")
        return

    write_file(lines, filename)


def command_list(command, cur_line, lines):
    """List lines from the file."""

    command = command.split(' ')

    if len(command) == 1:
        start = cur_line
        end = cur_line + 10

    elif len(command) == 2:
        start = int(command[1])
        end = start + 10

    elif len(command) == 3:
        start = int(command[1])
        end = int(command[2])

    else:
        print("usage: l [start [end]]")
        return

    start, end = normalize_start_end(start, end, lines)

    for i in range(start, end):
        print(f'{i}: {lines[i-1]}')

    return end


def command_edit(command, cur_line, lines):
    """Edit a line in the file."""

    command = command.split(' ')

    if len(command) == 2:
        cur_line = int(command[1])
    elif len(command) != 1:
        print("usage: e [line_num]")
        return

    lines[cur_line - 1] = input()

    return cur_line + 1


def command_delete(command, cur_line, lines):
    """Delete lines in the file."""

    command = command.split(' ')

    if len(command) == 1:
        start = cur_line
        end = start

    elif len(command) == 2:
        start = int(command[1])
        end = start

    elif len(command) == 3:
        start = int(command[1])
        end = int(command[2])

    else:
        print("usage: d [start [end]]")
        return

    start, end = normalize_start_end(start, end, lines)

    for i in range(end, start - 1, -1):
        lines.pop(i)

    return start


def command_append(command, cur_line, lines):
    """Append a line in the file."""

    command = command.split(' ')

    if len(command) == 2:
        cur_line = int(command[1])

    elif len(command) != 1:
        print("usage: a [line_num]")
        return

    done = False

    while not done:
        line = input().rstrip(os.linesep)

        if line == '.':
            done = True
            continue

        lines.insert(cur_line, line)

        cur_line += 1

    return cur_line

# Main


# Parse the command line

if len(sys.argv) == 2:
    filename = sys.argv[1]
elif len(sys.argv) == 1:
    filename = None
else:
    print("usage: lineedit.py [filename]", file=sys.stderr)
    sys.exit(1)


# Read the file (if specified); set up the lines list

if filename is not None:
    lines = read_file(filename)
else:
    lines = []

cur_line = 0

done = False

# Main loop

while not done:
    command = input("> ").strip()

    if command == 'q':
        done = True

    elif command[0] == 'w':
        command_write(command, lines, filename)

    elif command[0] == 'l':
        cur_line = command_list(command, cur_line, lines)

    elif command[0] == 'e':
        cur_line = command_edit(command, cur_line, lines)

    elif command[0] == 'd':
        cur_line = command_delete(command, cur_line, lines)

    elif command[0] == 'a':
        cur_line = command_append(command, cur_line, lines)
