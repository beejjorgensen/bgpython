# initialize the list with [0, 1]
fib = [0, 1]

# for 98 times
for _ in range(98):

    # compute the sum of the previous two numbers
    s = fib[-1] + fib[-2]

    # append sum to the list
    fib.append(s)

# print the list
print(fib)
