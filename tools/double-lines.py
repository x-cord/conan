import os
import re
from natsort import natsorted

last_line = "nope"
last_end = "nope"
last_style = "nope"
this_line = ""

for folder in next(os.walk("../subs"))[1]:
    for file in natsorted(os.listdir("../subs/" + folder)):
        if not file.endswith(".ass"):
            continue
        ep, ext = file.split(".")
        with open("../subs/" + folder + "/" + file, encoding="utf8") as f:
            content = f.read()
            lines = content.splitlines()

            for line in lines:
                line = line.rstrip()
                if line.startswith("; "):
                    continue
                parts = line.split(",", 9)
                if line.startswith("Dialogue: "):
                    parts = line.split(",", 9)
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                    style = parts[3]
                    if style == last_style and parts[9] == last_line and parts[1] == last_end:
                        last_line = parts[9]
                        last_end = parts[2]
                        print(folder, ep, line)
                        continue
                    last_style = style
                    last_line = parts[9]
                    last_end = parts[2]
