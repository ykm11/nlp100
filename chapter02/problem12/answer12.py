import sys

if len(sys.argv) < 2:
    exit()

f = open(sys.argv[1])

fout1 = open("col1.txt", "w")
fout2 = open("col2.txt", "w")
for line in f:
    line = line.strip()
    cols = line.split()
    fout1.write(cols[0] + "\n")
    fout2.write(cols[1] + "\n")
