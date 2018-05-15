import sys
import matplotlib.pyplot as plt
sys.path.append('../problem30/')
from answer30 import *

sentences = extract_analysed_neko()

words_freq = {}
for sentence in sentences:
    for word in sentence:
        words_freq[word["base"]] = words_freq.get(word["base"], 0) + 1

high_freq_words = sorted(words_freq.items(), key=lambda x:x[1], reverse=True)[:10]

print(high_freq_words)

x = [data[0] for data in high_freq_words]
y = [data[1] for data in high_freq_words]

plt.bar(range(10), y, tick_label=x) # matplotlib doesn't print larger than 2bytes character.
# change x-axis labels
plt.show()
