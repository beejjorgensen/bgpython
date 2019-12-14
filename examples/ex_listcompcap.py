a = ["alice", "beej", "chris", "dave", "eve", "frank"]

b = [x.upper() for x in a if x[0] not in "aeiou"]

print(b)

