import sys

if len(sys.argv) < 2:
    exit()
f = open(sys.argv[1])

rows = []
for row in f:
    row = row.strip()
    rows.append(row.split())
    
freq_prefs = {}
for row in rows:
    freq_prefs[row[0]] = freq_prefs.get(row[0], 0) + 1

for pref, freq in sorted(freq_prefs.items(), key=lambda x:x[1], reverse=True):
    print(pref, freq) 
