import sys
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

for sentence in sentences:
    prev_word = {"surface":None, "base":None, "pos":None, "pos1":None}
    preprev_word = {"surface":None, "base":None, "pos":None, "pos1":None}
    for word in sentence:
        if prev_word["surface"] == "の" and word["pos"] == "名詞" and preprev_word["pos"] == "名詞":
            print(preprev_word["surface"], word["surface"])
        preprev_word = prev_word
        prev_word = word
