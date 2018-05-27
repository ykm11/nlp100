import CaboCha

c = CaboCha.Parser()

fout = open("neko.txt.cabocha", "w", encoding="utf-8")
fin  = open("neko.txt", encoding="utf-8")

for line in fin:
    tree = c.parse(line.lstrip())
    fout.write(tree.toString(CaboCha.FORMAT_LATTICE))

fin.close()
fout.close()
