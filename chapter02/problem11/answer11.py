import sys

if len(sys.argv) < 2:
    exit()

f = open(sys.argv[1])
for line in f:
    line = line.strip()
    line = line.replace("\t", " ")
    print(line)
