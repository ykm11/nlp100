import sys

if len(sys.argv) < 2:
    exit()
f = open(sys.argv[1])

rows = []
for row in f:
    row = row.strip()
    rows.append(row.split())

for row in sorted(rows, key=lambda x:x[2], reverse=True):
    print(" ".join(row))
