x = input("Enter a number: ")
x = int(x)

y = input("Enter a second number, bigger than that: ")
y = int(y)

# If x is even, bump it up to the next odd
if x % 2 == 0:
	x += 1

for i in range(x, y + 1, 2):
	print(i)
