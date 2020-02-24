class Game:
    def __init__(self, title, year, studio, publisher):
        self.title = title
        self.year = year
        self.studio = studio
        self.publisher = publisher

    def __str__(self):
        # There's a lot of stuff to unpack on the next line.
        #
        # A colon followed by a number is the field width that will
        # display this value. (That is, it will pad with spaces to make
        # it that big, and we use this to align columns.)
        #
        # When you specify a field width, strings justify to the left by
        # default, and numbers to the right. I want them all to justify
        # left, so I force the year to justify left with a less-than
        # sign.
        #
        # Now, this line goes longer than I want it to aesthetically (80
        # columns is my max). So I split the line and put a backslash at
        # the very end. In this context the backslash is referred to as
        # an "escape". It's a way to telling Python, "Hey, pretend
        # there's no newline here."
        #
        # Finally, I take advantage of the fact that in Python, two
        # strings next to each other are treated as a single string.
        #
        # Example:
        #
        # s = 'foo' 'bar'
        # print(s)   # foobar
        return f'{self.title:25} {self.year:<6} {self.studio:22} ' \
            f'{self.publisher:22}'

    def __repr__(self):
        # We don't use the repr, but it's good practice to include it in
        # all your classes just in case.
        return f'Game({repr(self.title)},{repr(self.year)},' \
            f'{repr(self.studio)},{repr(self.publisher)})'


# List of games that we read from the CSV file
games_list = []

with open("games.csv") as f:

    # Call next() right away to get and discard the first line of the
    # file (the header line)
    next(f)

    # Go through every line in the file
    for line in f:
        # Extract the fields
        title, year, studio, publisher = line.strip().split(",")

        # Make a new Game object with that data in it
        g = Game(title, int(year), studio, publisher)

        # Append the new object to the games list
        games_list.append(g)

# Sort the list
#
# In the following like, the keyword arg "key" is set to a function that
# returns the value that should be used as a key when determining the
# sort order. We want to sort by year, so we pass it a function that
# returns the year for any given game.
games_list.sort(key=lambda g: g.year)

# Lambda is like a small, anonymous function. g is the parameter. And
# the thing after the : is the return value. The above line is
# equivalent to:
#
#    def get_game_sort_key(g):
#       return g.year
#
#    games_list.sort(key=get_game_sort_key)
#
# Same thing, but the lambda function makes it far more concise.

# Print all the games
for g in games_list:
    print(g)
