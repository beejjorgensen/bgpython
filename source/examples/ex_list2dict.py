# Starting list
a = ["Chris", "Annie", "Beej", "Aaron", "Charlie"]

# Eventually everything will be in this dict:
d = {}

# Loop through the names
for name in a:
    
    # Get the first letter to use as the key
    first_letter = name[0]

    # If the key doesn't exist in d yet, we need to add it
    if first_letter not in d:
        # Make it an empty list to start
        d[first_letter] = []

    # Now that we're sure there's a list in d for this particular key,
    # let's append the name to the end of the list:
    d[first_letter].append(name)

# Print out the dict
for k, v in d.items():
    print(f"{k}: {v}")
