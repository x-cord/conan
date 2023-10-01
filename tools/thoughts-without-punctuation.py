import os
from natsort import natsorted

scan = [
    "Thoughts",
    "Radio",
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
                    if parts[3] not in scan:
                        continue
                    text = parts[9]
                    if "." not in text and "?" not in text and "!" not in text and "," not in text and "—" not in text:
                        print(file, parts[9])
