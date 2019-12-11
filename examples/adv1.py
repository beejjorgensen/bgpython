# The map

map_data = [
	"#####################",
	"#...#...............#",
	"#...#..........#....#",
	"#...#..........#....#",
	"#...#..........#....#",
	"#...#..........#....#",
	"#..............#....#",
	"#..............#....#",
	"#####################"
]

# Player position

player_row = 4
player_column = 9

quit = False

while not quit:

	# Print map and player indicator

	for row_index, row in enumerate(map_data):  # for each row
		for col_index, map_character in enumerate(row):  # for each col
			if row_index == player_row and col_index == player_column:
				print("@", end="")  # end="" no newline
			else:
				print(map_character, end="")
		print()

	# Get input

	command = input("Enter a move (n,s,w,e,q): ")

	# Figure out the new row and column of the player
	# Make sure input is valid
	if command == "n":
		new_row = player_row - 1
		new_column = player_column
	elif command == "s":
		new_row = player_row + 1
		new_column = player_column
	elif command == "w":
		new_row = player_row
		new_column = player_column - 1
	elif command == "e":
		new_row = player_row
		new_column = player_column + 1
	elif command == "q":
		quit = True
		continue
	else:
		print(f'Unknown command {command}')

	if map_data[new_row][new_column] == "#":
		print("You can't move that way!")
	else:
		# Set the current position to the new position
		player_row = new_row
		player_column = new_column

