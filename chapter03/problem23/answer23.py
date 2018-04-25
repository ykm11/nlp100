import re

text = open("../uk.txt").read()

pat = r"(==*)(.*==*)"
for mat in re.findall(pat, text):
    print("".join(mat), "\t", len(mat[0]))
