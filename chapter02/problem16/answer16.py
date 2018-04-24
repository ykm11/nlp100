import argparse

p = argparse.ArgumentParser(description="ykm")
p.add_argument("-n", )
p.add_argument("-f", "--file")

args = p.parse_args()

n = 1
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

num_lines = len(lines)//n
for i in range(n):
    if i+1 == n:
        print("\n".join(lines[i*num_lines:]))
    else:
        print("\n".join(lines[i*num_lines : (i+1)*num_lines]))
    print("-"*20)
