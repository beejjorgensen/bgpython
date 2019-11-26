input_valid = False  # Assume it's invalid to start

while not input_valid:   # While input invalid
    x = input("Enter a number, 5-50 inclusive: ")
    x = int(x)

    if x >= 5 and x <= 50:
        input_valid = True   # We got a good number!
    else:
        print("The number must be between 5 and 50, inclusive!")

# Print the line
for i in range(x):
    if i < 30:
        print("#", end="")  # Set the end-of-line character to nothing
    else:
        print("*", end="")

print()  # Add a newline to the end of the line

