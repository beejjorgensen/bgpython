import sys

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} filename")
    sys.exit(1)

filename = sys.argv[1]

word_count = 0

with open(filename) as f:
    for line in f:
        words = line.split()
        word_count += len(words)

print(word_count)