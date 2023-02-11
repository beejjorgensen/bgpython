# When handling exceptions, the first except clause to match the
# exception is the one that triggers.
#
# Since the Exception class is the base class for all exceptions, it
# effectively means that all exceptions _are_ Exceptions.
#
# So if we handle Exception _before_ ZeroDivisionError, then it's
# Exception's handler than will run (because ZeroDivisionE#rror is an
# Exception).
#
# To fix it, we need to put ZeroDivisionError _before_ Exception in our
# # list of except clauses.

try:
    x = 3490 / 0
except ZeroDivisionError:
    # This will catch it
    print("Division by Zero")
except Exception:
    # This will catch any other exceptions that might have occurred
    print("Exception")