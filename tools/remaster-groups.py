import re
import os
import glob
from natsort import natsorted

files = glob.glob("../subs/Remastered/*.ass")

for file in natsorted(files):
    ep = os.path.basename(file).split(" ")[0].split("-")[0]

    if not os.path.exists(f"../subs/0001-0999/{ep}.ass"):
        print("Missing", ep)
        continue
    with open(file, "r", encoding="utf-8") as r:
        match = re.search(r"^TL Source: ([^\n]+)", r.read(), re.MULTILINE)
        remaster = match.group(1)
    with open(f"../subs/0001-0999/{ep}.ass", "r", encoding="utf-8") as r:
        match = re.search(r"^TL Source: ([^\n]+)", r.read(), re.MULTILINE)
        og = match.group(1)

    print(ep, og, remaster)
