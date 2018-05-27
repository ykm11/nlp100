import sys
sys.path.append('../problem40/')
from answer40 import Morph

class Chunk():

    def __init__(self, morphs, dst, src):
        self.morphs = morphs
        self.dst = int(dst)
        self.src = int(src)

    def __str__(self):
        return "dst({0})\nsrc({1})\nmorphs({2})\n".format(self.dst, self.src, " / ".join(str(morph) for morph in self.morphs))
    
    def add_morph(self, morph):
        self.morphs.append(morph)

def make_chunk(inFile):

    sentences = []
    sentence = []
    chunk = None

    with open(inFile, "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip().split()
            if line_list[0] == "EOS":
                if not chunk is None:
                    sentence.append(chunk)
                if len(sentence) > 0:
                    sentences.append(sentence)
                chunk = None
                sentence = []

            elif line_list[0] == "*":
                if not chunk is None:
                    sentence.append(chunk)
                line_list[2] = line_list[2][:line_list[2].find("D")]
                chunk = Chunk(morphs=[], dst=line_list[2], src=line_list[1])

            else:
                line_list = line_list[:1] + line_list[1].split(",")
                if len(line_list) < 8:continue
                morph = Morph(line_list[0], line_list[7], line_list[1], line_list[2])
                chunk.add_morph(morph)

    return sentences

if __name__ == "__main__":

    sentences = make_chunk("../neko.txt.cabocha")
    for chunk in sentences[10]:
        print(chunk)
