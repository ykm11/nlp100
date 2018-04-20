
def n_gram(sequence, n=2):
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
        chr_bi.append(tuple(text[k:k+n]))

    return (word_bi, chr_bi)

text = "I am an NLPer"
w_bi, c_bi = n_gram(text)
print(w_bi)
print(c_bi)
