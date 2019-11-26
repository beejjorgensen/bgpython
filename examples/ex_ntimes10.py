done = False

while not done:
	x = input('Enter a number (or "quit"): ')
	if x == "quit":
		done = True
	else:
		x = int(x)
		print(x, "times 10 is", x * 10)

