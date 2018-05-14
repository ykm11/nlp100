import MeCab

fout = open("neko.txt.mecab", "w")

m = MeCab.Tagger("-Ochasen")
with open("neko.txt") as f:
    for line in f:
        line = line.strip()
        if line == '': continue
        tokens = m.parse(line) 
        #tokens = tokens.rstrip("EOS\n")
        tokens = tokens.rstrip("\n")
        fout.write(tokens.replace("\t", ",") + "\n")

fout.close()
print("OK")
