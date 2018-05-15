import sys
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

cnt = 1
for sentence in sentences:
    cont_words = ""
    for word in sentence:
        if word["pos"] == "名詞":
            cont_words += word["surface"]
        else:
            if cont_words != "":
                print(cont_words)
            cont_words = ""
