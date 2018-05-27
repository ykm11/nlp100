

class Morph():

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f"{self.surface}, {self.base}, {self.pos}, {self.pos1}"


def make_morph_list(inFile):

    sentences = []
    sentence = []

    with open(inFile, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split()
            if line_list[0] in ["*", "EOS"]:continue

            line_list = line_list[:1] + line_list[1].split(",")
            if len(line_list) < 8:continue
            morph = Morph(line_list[0], line_list[7], line_list[1], line_list[2])

            sentence.append(morph)
            if morph.pos1 == "句点":
                sentences.append(sentence)
                sentence = []
    return sentences


if __name__ == "__main__":
    sentences = make_morph_list("../neko.txt.cabocha")

    #Printing 3rd morpheme out
    for morph in sentences[2]:
        print(morph)
