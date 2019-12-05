x = [1, 2, 3, 4, 5, 6]

# for each element in the list

for i, v in enumerate(x):

    # if that element is even

    if v % 2 == 0: # check if v is even

        # double the value and store it at the same place in the list
        x[i] = v * 2

print(x)  # Print it out, just for fun
