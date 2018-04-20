text1 = "パトカー"
text2 = "タクシー"

ans = ""
for ch1, ch2 in zip(text1, text2):
    ans += ch1 + ch2
print(ans)
