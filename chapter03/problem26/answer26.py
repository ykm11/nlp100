import re

text = open("../uk.txt").read()

pat = r"\|(.*) = (.*)"

basics_info = {}
for key, value in re.findall(pat, text): #mat[0], mat[1] = KEY, VALUE
    value = re.sub(r"'{1,3}", "", value)
    basics_info[key] = value

for k, v in basics_info.items():
    print(k, '\t', v)
