import math   # Needed for sqrt

# Input all values
a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")

# Convert from string to float
a = float(a)
b = float(b)
c = float(c)

# Compute the square root part
sqrt_part = math.sqrt(b**2 - 4*a*c)

# Compute plus and minus answers
x_plus  = (-b + sqrt_part) / (2*a)
x_minus = (-b - sqrt_part) / (2*a)

# Print the result
print("x is", x_plus, "or", x_minus)
