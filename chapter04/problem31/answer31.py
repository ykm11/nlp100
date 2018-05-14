import sys
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

for sentence in sentences:
    for word in sentence:
        if word["pos"] == "動詞":
            print(word["surface"])
