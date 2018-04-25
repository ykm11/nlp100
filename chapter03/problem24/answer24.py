import re

text = open("../uk.txt").read()

#pat = r"([0-9a-zA-Z]+-*[0-9a-zA-Z]*-*[0-9a-zA-Z]*\.(jpeg|png|jpg))"
pat = r"((-*[0-9a-zA-Z]){1,}\.(jpeg|png|jpg))"

for mat in re.findall(pat, text):
    print(mat[0])
