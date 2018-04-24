import sys

if len(sys.argv) < 2:
    exit()

f = open(sys.argv[1])
prefs = []
for line in f:
    line = line.strip()
    prefs.append(line.split()[0]) 

#print(prefs)
set_prefs = set(prefs)
print(set_prefs)
