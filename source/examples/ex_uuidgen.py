import sys
import uuid

if len(sys.argv) != 2:
    print("usage: py_uuidgen.py count")
    sys.exit(1)

count = int(sys.argv[1])

for _ in range(count):
    print(uuid.uuid4())