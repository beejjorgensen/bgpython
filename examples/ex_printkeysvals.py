d = {
    "key1": "value1",
    "key2": "value1",
    "key3": "value1",
    "key4": "value1",
}

for k, v in d.items():
    print(f"{k}: {v}")

# This also works. Which do you like more? Why?

for k in d:
    print(f"{k}: {d[k]}")