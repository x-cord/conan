import json
import requests
from selectolax.parser import HTMLParser

r = requests.get("https://www.detectiveconanworld.com/wiki/Anime")

doc = HTMLParser(r.text)

def ranges(s):
    return sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))]))
        if '-' in i else [int(i)]) for i in s.split(',')), [])

int_to_jpn = {}

for row in doc.css(".wikitable tr:not(:first-child)"):
    cells = row.css("td")
    jpn = cells[0].text(strip=True)
    inter = cells[1].text(strip=True)
    title = cells[2].text(strip=True)
    if "Remastered" in title:
        continue
    if not jpn.split("-")[0].isnumeric() or not inter.split("-")[0].isnumeric():
        continue
    jpn = ranges(jpn)
    inter = ranges(inter)
    if len(jpn) == 1:
        if len(inter) > 1:
            l = "a"
            for intr in inter:
                int_to_jpn[intr] = f"{jpn[0]}{l}"
                l = chr(ord(l) + 1)
        else:
            int_to_jpn[inter[0]] = str(jpn[0])
    else:
        for i, intr in enumerate(inter):
            int_to_jpn[intr] = str(jpn[i])

with open("int_to_jpn.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(int_to_jpn))
