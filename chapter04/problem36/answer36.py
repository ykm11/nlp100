import sys
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

words_freq = {}
for sentence in sentences:
    for word in sentence:
        words_freq[word["base"]] = words_freq.get(word["base"], 0) + 1

for k, v in sorted(words_freq.items(), key=lambda x:x[1], reverse=True):
    print(f"{k}\t\t{v}回")
