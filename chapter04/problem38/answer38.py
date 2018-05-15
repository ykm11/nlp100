import sys
import matplotlib.pyplot as plt
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

words_freq = {}
for sentence in sentences:
    for word in sentence:
        words_freq[word["base"]] = words_freq.get(word["base"], 0) + 1

freq = {}
for cnt in words_freq.values():
    freq[cnt] = freq.get(cnt, 0) + 1

x = [data[0] for data in sorted(freq.items())]
y = [data[1] for data in sorted(freq.items())]

plt.bar(x, y)
plt.ylim(ymax=5200, ymin=0)
plt.xlabel("Appeared x times")
plt.ylabel("Number of words")
plt.show()
