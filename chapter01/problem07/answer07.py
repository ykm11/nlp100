
def make_sentence(x, y, z):
    return f"{x}時の{y}は{z}" # this works on after than 3.6 version, maybe

x = 12
y = "気温"
z = 22.4

print(make_sentence(x, y, z))
