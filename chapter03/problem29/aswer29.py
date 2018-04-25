import re, json
import requests

def rm_internal_link(text):
    text = re.sub(r"\[", "", text)
    text = re.sub(r"]", "", text)
    text = re.sub(r"{", "", text)
    text = re.sub(r"}", "", text)
    return text

text = open("../uk.txt").read()

pat = r"\|(.*) = (.*)"

basics_info = {}
for key, value in re.findall(pat, text): #mat[0], mat[1] = KEY, VALUE
    value = re.sub(r"'{1,3}", "", value)
    value = rm_internal_link(value)
    value = re.sub(r"<.*>", "", value)
    basics_info[key] = value

for k, v in basics_info.items():
    print(k, '\t', v)


url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(basics_info["国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

res = requests.get(url, params=payload)
dt = json.loads(res.text)

print("\nURL =", dt['query']['pages']['23473560']['imageinfo'][0]['url'])
