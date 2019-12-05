a = [5, 2, 8, 4, 7, 4, 0, 9]

print(len(a))   # 8, the number of elements in the list

a.append(100)

print(a)  # [5, 2, 8, 4, 7, 4, 0, 9, 100]

print(a.count(4))  # 2, the number of 4s in the list

print(a.index(4))  # 3, the index of the first 4 in the list

v = a.pop()  # Remove the 100 from the end of the list

print(v)   # 100
print(a)   # [5, 2, 8, 4, 7, 4, 0, 9]

a.reverse()   # Reverse the list

print(a)   # [9, 0, 4, 7, 4, 8, 2, 5]

a.insert(2, 999)  # insert 999 before index 2

print(a)   # [9, 0, 999, 4, 7, 4, 8, 2, 5]

b = [1, 2, 3]

a.extend(b)  # Add contents of b to end of a

print(a)   # [9, 0, 999, 4, 7, 4, 8, 2, 5, 1, 2, 3]

a.sort()   # Sort all elements

print(a)   # [0, 1, 2, 2, 3, 4, 4, 5, 7, 8, 9, 999]

a.clear()  # Remove all elements

print(a)   # [], an empty list of length 0
