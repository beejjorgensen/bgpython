class InvalidListSize(Exception):
    pass

def listadd(a):
    if len(a) != 3:
        raise InvalidListSize("list must be 3 elements in length")

    return sum(a)

try:
    print(listadd([1, 2, 3]))
    print(listadd([1, 2]))

except InvalidListSize as e:
    print(e.args[0])