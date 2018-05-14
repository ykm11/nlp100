import sys
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

for sentence in sentences:
    prev_word = {"surface":None, "base":None, "pos":None, "pos1":None}
    for word in sentence:
        if word["pos"] == "動詞" and word["base"] == "する" and prev_word["pos"] == "名詞":
            print(prev_word["base"])
        prev_word = word
