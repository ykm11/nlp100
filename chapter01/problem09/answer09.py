import random

def shuffle(s):
    ret = []
    words = s.split()
    for w in words:
        if len(w) > 4:
            shuffled = list(w[1:-1])
            random.shuffle(shuffled)
            ret.append(w[0] + "".join(shuffled) + w[-1])
        else:
            ret.append(w)

    return " ".join(ret)

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(shuffle(s))
