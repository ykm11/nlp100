import json

articles = {}

def extract_article(country=""):
    f = open("../jawiki-country.json")
    for line in f:
        line = line.strip()
        data = json.loads(line)
        if data['title'] == country:
            return data['text']
    f.close()

print(extract_article("イギリス"))
