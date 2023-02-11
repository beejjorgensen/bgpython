a = [1, 2, 3]
#b = a # Copies reference to same list

b = a.copy()  # Makes a new list
#b = list(a)   # Also makes a new list
#b = a[:]      # Also makes a new list

b[0] = 99

print(a[0])

