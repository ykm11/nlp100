import argparse

p = argparse.ArgumentParser(description="ykm")
p.add_argument("-n", )
p.add_argument("-f", "--file")

args = p.parse_args()

n = 10
if args.n != None:
    n = int(args.n)
if args.file != None:
    _file = args.file
else: exit()

f = open(_file)

lines = []
for line in f:
    line = line.rstrip()
    lines.append(line)

print("\n".join(lines[-n:]))
