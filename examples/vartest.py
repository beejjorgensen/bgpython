a = 34      # Variable a is assigned value 34
print(a)
a = 90      # Variable a is assigned value 90
print(a)

b = a + 40  # b is assigned a + 40 which is 90 + 40, or 130
print(a)    # Still 90! Nothing changed here
print(b)    # Prints "130"

a = 1000
print(b)    # Still 130!
