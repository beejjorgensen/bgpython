import sys

if len(sys.argv) != 3:
    print("usage: head.py filename count")
    sys.exit(1)

filename = sys.argv[1]

try:
    # Convert the line count to an int--this might raise an exception
    total_count = int(sys.argv[2])

    # If the count is a valid number, let's check to see if it's
    # invalid:
    if total_count < 1:
        # And if it is, let's force the exception handler to run
        raise ValueError()

except ValueError:
    # This handler gets called if either the call to int() fails, or if
    # we detect that count is less than 1

    print("head.py: count must be a positive integer")

    # exit with a different error code just in case the shell wants to
    # do something more specific  with this error
    sys.exit(2)

line_count = 0  # Number of lines we've read so far

try:
    # Open the file
    with open(filename) as f:

        # Read lines one at a time
        for line in f:

            # Keep track of the number of lines we've read
            line_count += 1

            # If it's greater than our target amount, bail out
            if line_count > total_count:
                break

            # Otherwise, print the line (suppressing the newline, since
            # there's already one at the end of the line)
            print(line, end="")

except IOError as e:
    # I know that IOError objects have a useful message stored in the
    # `sterror` attribute, so we'll print that.
    #
    # This will give us output like
    #
    # head.py: filename.txt: No such file or directory
    #
    print(f'head.py: {filename}: {e.strerror}')
