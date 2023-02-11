done = False
numbers = []

while not done:
    n = input("Enter a number (or \"done\"): ")

    if n == "done":
        done = True
    else:
        numbers.append(n)

print(max(numbers))

