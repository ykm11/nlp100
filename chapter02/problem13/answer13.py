f_col1 = open("../problem12/col1.txt")
f_col2 = open("../problem12/col2.txt")

for col1, col2 in zip(f_col1, f_col2):
    col1 = col1.strip()
    col2 = col2.strip()
    print(f"{col1}\t{col2}")
