import os
from natsort import natsorted

known = [
    "Dialogue",
    "Dialogue Top",
    "Signs",
    "Thoughts",
    "Radio",
    "Narration",
    "Narration Off",
    "Flashback",
    "Flashback Thoughts",
    "Honorifics - Dialogue",
    "Honorifics - Signs",
    "Honorifics - Thoughts",
    "Honorifics - Radio",
    "Honorifics - Narration",
    "Honorifics - Narration Off",
    "Honorifics - Flashback",
    "Honorifics - Flashback Thoughts",
    "Masks",
    "Title",
    "OPED",
    "Eyecatch",
    "Character Card",
    "Farewell Card",
]

seen = set()

for folder in next(os.walk("../subs"))[1]:
    for file in natsorted(os.listdir("../subs/" + folder)):
        if not file.endswith(".ass"):
            continue
        with open("../subs/" + folder + "/" + file, encoding="utf8") as f:
            content = f.read()
            lines = content.splitlines()
            for line in lines:
                line = line.rstrip()
                parts = line.split(",", 9)
                if line.startswith("Dialogue: ") or line.startswith("Comment: "):
                    if parts[3] in known:
                        continue
                    if parts[3] in seen:
                        continue
                    seen.add(parts[3])
                    print(parts[3])
