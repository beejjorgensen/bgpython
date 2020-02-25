import sys

if len(sys.argv) != 3:
    print(f'usage: {sys.argv[0]} size filename')
    sys.exit(1)

size = int(sys.argv[1])
filename = sys.argv[2]

with open(filename, "w") as f:
    for row in range(1, size + 1):
        for product in range(row, row * (size + 1), row):
            f.write(f"{product:4}")
        f.write('\n')
