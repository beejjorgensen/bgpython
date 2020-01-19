d = {
    "key1": "value1",
    "key2": "value1",
    "key3": "value1",
    "key4": "value1",
}

for key in d:
    print(key)

# This also works, but is less idiomatic:
for key in d.keys():
    print(key)