s = input("Enter a string: ")

valid_input = False

while not valid_input:
	i0 = input(f"Enter a number (0 to {len(s)}): ")

	i0 = int(i0)

	# Set valid_input directly with Boolean expression
	valid_input = i0 >= 0 and i0 <= len(s)

valid_input = False

while not valid_input:
	i1 = input(f"Enter a number ({i0} to {len(s)}): ")

	i1 = int(i1)

	# Set valid_input directly with Boolean expression
	valid_input = i1 >= 0 and i1 <= len(s)

print(f'Slice from {i0} to {i1} is "{s[i0:i1]}"')
