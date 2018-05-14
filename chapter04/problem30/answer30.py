
def ret_sentence():
    data = open("../neko.txt.mecab").read()
    for sentences in data.split("EOS"):
        yield sentences

def extract_analysed_neko():
    #analysed_sentence = []
    ss = ret_sentence()
    for line in ss:
        line = line.rstrip("\n")
        morphemes_words = line.split("\n")

        sentence = []
        for word in morphemes_words:
            s = {}
            word = word.split(",")
            if len(word) < 4 : continue
            s["surface"] = word[0]
            s["base"] = word[2]

            pos = word[3].split("-")
            s["pos"] = pos[0]
            if len(pos) == 2:
                s["pos1"] = pos[1]
            else:
                s["pos1"] = None

            sentence.append(s)

        #analysed_sentence.append(sentence)
        yield sentence
