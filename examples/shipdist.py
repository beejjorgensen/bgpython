import math

def get_ship_locations():
    done = False
    locations = []

    while not done:
        xyz = input('Enter ship location x,y,z (or "done"): ')

        if xyz == "done":
            done = True
        else:
            # Get a list of the x,y,z coordinates
            xyz_list = xyz.split(',')

            # Convert to integers
            for i in range(len(xyz_list)):
                xyz_list[i] = int(xyz_list[i])

            # Build a list of lists
            locations.append(xyz_list)

    return locations

def dist3d(p0, p1):
    dx = p0[0] - p1[0]
    dy = p0[1] - p1[1]
    dz = p0[2] - p1[2]

    return math.sqrt(dx*dx + dy*dy + dz*dz)

def print_grid(locations):

    num_ships = len(locations)
    
    print(" " * 8, end="")

    for i in range(num_ships):
        print(f'{i:8}', end="")

    print()

    for i in range(num_ships):
        print(f'{i:8}', end="")
        for j in range(num_ships):
            dist = dist3d(locations[i], locations[j])
            print(f'{dist:8.2f}', end="")
        print()

locations = get_ship_locations()
print_grid(locations)

