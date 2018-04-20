text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = text.replace(",", "")
text = text.replace(".", "")

results = []
words = text.split()
for word in words:
    results.append(len(word))
print(results)
