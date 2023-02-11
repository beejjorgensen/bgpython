class Room:
    """Holds information about a room in the game"""

    def __init__(self, name):
        self.name = name
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def __str__(self):
        return self.name

# All the rooms

hallmist = Room("Hall of Mists")
hallmtking = Room("Hall of the Mountain King")
lowns = Room("Low N/S passage")
y2 = Room("Y2")
winpit = Room("Low Window Overlooking a Pit")
westside = Room("West Side Chamber")
southside = Room("South Side Chamber")

# Connect all the rooms

hallmist.n_to = hallmtking
hallmtking.e_to = hallmist  # This passage turns a corner!

hallmtking.s_to = southside
southside.n_to = hallmtking

hallmtking.w_to = westside
westside.e_to = hallmtking

hallmtking.n_to = lowns
lowns.s_to = hallmtking

lowns.n_to = y2
y2.s_to = lowns

y2.w_to = winpit
winpit.e_to = y2

# Player location

location = hallmtking

done = False

def cant_go():
    print("You can't go that way")

while not done:
    print(location)

    dir = input("Enter a direction (n,s,w,e,q): ")

    if dir == 'q':
        done = True
        continue


    """
    # This code is really repeatingly and redundantly repetitive.
    # So, even though it works, I've commented it out and replaced
    # it with something more concise, below.

    if dir == 'n':
        if location.n_to is None:
            cant_go()
        else:
            location = location.n_to

    elif dir == 's':
        if location.s_to is None:
            cant_go()
        else:
            location = location.s_to

    elif dir == 'w':
        if location.w_to is None:
            cant_go()
        else:
            location = location.w_to

    elif dir == 'e':
        if location.e_to is None:
            cant_go()
        else:
            location = location.e_to
    """

    # Due to a happy coincidence, the name of the direction attribute we
    # want to follow is always what the user entered plus the string
    # "_to". So if they entered "n", we want to look at the attribute
    # "n_to", and so on.
    #
    # So we have a string of the attribute we want to check. This is a
    # prime use case for getattr().

    dir_attr = dir + "_to"
    
    # Get the next room in that direction, or return None if there is no
    # room that way
    next_room = getattr(location, dir_attr, None)

    if next_room is None:
        cant_go()
    else:
        location = next_room

    # Replaced all that stuff, above, with six lines. Not bad!