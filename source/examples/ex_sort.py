import sys

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} filename")
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    lines = list(f)

lines.sort()

for l in lines:
    print(l, end="")