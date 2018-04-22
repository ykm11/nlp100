import sys

if len(sys.argv) < 2:
    exit()

f = open(sys.argv[1])
line_num = 0
for line in f:
    line = line.strip()
    line_num += 1
    
print(line_num)
