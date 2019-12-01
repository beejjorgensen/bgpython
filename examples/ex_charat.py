s = input("Enter a string: ")

valid_input = False

while not valid_input:
	i = input(f"Enter a number (0 to {len(s)-1}): ")

	i = int(i)

	# Set valid_input directly with Boolean expression
	valid_input = i >= 0 and i <= len(s)-1

print(f'Character at index {i} is "{s[i]}"')
