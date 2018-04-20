text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = text.replace(".", "")

imp_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans_dict = {}

for k, word in enumerate(text.split()):
    if (k+1) in imp_positions:
        ans_dict[word[0]] = k+1
    else:
        ans_dict[word[:2]] = k+1

# to make sure my script worked
for k, v in ans_dict.items():
    print(k, v)
