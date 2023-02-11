a = [14, 31, 44, 46, 54, 59, 45, 55, 21, 11, 8, 34, 66, 41]

total = 0

for value in a:
    total += value

print(total)

# Python actually has this as a built-in with the sum() function:

print(sum(a))  # Does the same as the loop above
