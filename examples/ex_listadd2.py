def listadd(a, i0, i1):
    return a[i0] + a[i1]

try:
    print(listadd([1, 2, 3], 0, 2))  # 1 + 3 = 4
    print(listadd([1, 2, 3], 0, 3))  # exception--3 out of range

except IndexError as e:
    print(e)  # "list index out of range"