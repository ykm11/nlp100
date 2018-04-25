import re

text = open("../uk.txt").read()

pat = r"\[\[Category:(.*)\]\]"
for mat in re.findall(pat, text):
    print(mat)
