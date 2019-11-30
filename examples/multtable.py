valid_input = False

while not valid_input:
	x = input("Enter a number between 1 and 19: ")
	x = int(x)

	if x >= 1 and x <= 19:
		valid_input = True
	
for row in range(1, x + 1):
	for product in range(row, row * (x + 1), row):
		print(f"{product:4}", end="")
	print()
