def get_ship_locations():
    done = False
    locations = []

    while not Done:
        xyz = input('Enter ship location x,y,z (or "done"): ')

        if xyz == "done":
            done = True
        else:
            # Get a list of the x,y,z coordinates
            xyz_list = xyz.split(',')

            # Build a list of lists
            locations.append(xyz_list)

    return locations


locations = get_ship_locations()
print_grid(locations)

