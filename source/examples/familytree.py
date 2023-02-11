tree = {
    "Beej Jorgensen": {
        "born": 1990,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": ["Brother Jorgensen", "Sister Jorgensen", "Little Sister Jorgensen"]
    },
    "Mom Jorgensen": {
        "born": 1970,
        "mother": "Grandma Jorgensen",
        "father": "Grandpa Jorgensen",
        "siblings": ["Auntie Jorgensen"]
    },
    "Dad Jorgensen": {
        "born": 1965,
        "mother": "Granny Jorgensen",
        "father": "Grandad Jorgensen",
        "siblings": ["Uncle Jorgensen"]
    },
    "Brother Jorgensen": {
        "born": 1989,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": ["Beej Jorgensen", "Sister Jorgensen", "Little Sister Jorgensen"]
    },
    "Sister Jorgensen": {
        "born": 1991,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": ["Beej Jorgensen", "Brother Jorgensen", "Little Sister Jorgensen"]
    },
    "Little Sister Jorgensen": {
        "born": 1992,
        "mother": "Mom Jorgensen",
        "father": "Dad Jorgensen",
        "siblings": ["Beej Jorgensen", "Brother Jorgensen", "Sister Jorgensen"]
    },
    "Grandma Jorgensen": {
        "born": 1950,
        "mother": "Great Grandma Jorgensen",
        "father": "Great Grandpa Jorgensen",
        "siblings": []
    },
    "Grandpa Jorgensen": {
        "born": 1945,
        "mother": "Great Granny Jorgensen",
        "father": "Great Grandad Jorgensen",
        "siblings": []
    }
}

done = False

while not done:
    name = input("Enter a name (or q to quit): ")

    if name == "q":
        done = True
        continue

    record = tree.get(name)

    if record is None:
        print(f'No record for "{name}"')
        continue

    mother_name = record["mother"]
    father_name = record["father"]

    mother_record = tree.get(mother_name)
    father_record = tree.get(father_name)

    if mother_record is not None:
        mother_born_date = mother_record["born"]
    else:
        mother_born_date = "no record"

    if father_record is not None:
        father_born_date = father_record["born"]
    else:
        father_born_date = "no record"

    print("Parents:")
    print(f'    {mother_name} ({mother_born_date})')
    print(f'    {father_name} ({father_born_date})')
    