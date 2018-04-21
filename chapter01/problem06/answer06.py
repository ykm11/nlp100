
def n_gram(sequence, n=2): # from ../problem05/answer05.py
    words = []
    text = ""
    if isinstance(sequence, str):
        sequence.replace(".", "")
        sequence.replace(",", "")
        words = sequence.split()
        text = sequence
    elif isinstance(sequence, list):
        if all(map(lambda x : isinstance(x, str), seqence)):
            return 0
        text = " ".join(sequence)
        words = sequence
    else:
        return 0

    word_bi = []
    chr_bi = []

    for k in range(0, len(words)-n+1):
        word_bi.append(tuple(words[k:k+n]))

    for k in range(0, len(text)-n+1):
        chr_bi.append(text[k:k+n])

    return (word_bi, chr_bi)

_, X = n_gram("paraparaparadise", n=2)
_, Y = n_gram("paragraph", n=2)

set_X = set(X)
set_Y = set(Y)

union = set_X.union(set_Y)
diff_set = set_X.difference(set_Y)
inter_set = set_X.intersection(set_Y)


print("Union = {0}\n".format(union))
print("Diffrence set = {0}\n".format(diff_set))
print("Intersection set = {0}\n".format(inter_set))

print("X contains 'se' : {0}\n".format("se" in set_X))
print("Y contains 'se' : {0}\n".format("se" in set_Y))
