# Starting list
a = ["Chris", "Annie", "Beej", "Aaron", "Charlie"]

# Eventually everything will be in this dict:
d = {}

# You have a couple options for sorting the names in the final sublists.
# You can sort them at the end, when you print them. But you can also
# sort them in advance. If we sort the list with the names, then they'll
# naturally be in sorted order when we append them to the end of the
# sublists.
#
# In this case, it doesn't make that much difference since we have to
# run through all the names to sort them one way or another. But there's
# potentially less overhead calling .sort() once instead of multiple
# times.
#
# But there are a number of places algorithms can be simplified if you
# sort the list up front ahead of time. It takes time to sort, so you
# don't want to do it if it doesn't help you. But every time I see an
# algorithmic problem looping over data, I always ask myself if it buys
# me anything to sort the data ahead of time.

a.sort()  # Sort the list in advance

# Loop through the names
for name in a:
    
    # Get the first letter to use as the key
    first_letter = name[0]

    # If the key doesn't exist in d yet, we need to add it. This is a
    # really common programming pattern:
    if first_letter not in d:
        # Make it an empty list to start
        d[first_letter] = []

    # Now that we're sure there's a list in d for this particular key,
    # let's append the name to the end of the list:
    d[first_letter].append(name)

# Print out the dict sorted by key
for k in sorted(d):
    # We don't have to sort the sublists here because we did it above.
    # If you decided to do it here, instead, that's not really wrong,
    # either. Which way do you like more? Why?
    print(f"{k}: {d[k]}")
