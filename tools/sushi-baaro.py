import os
import re
import glob
import subprocess

files = [
    "0301.ass",
    "0302.ass"
]

for file in files:
    ep, group = file.split(".")
    ep = int(re.sub("[^0-9]", "", ep.split(" ")[0].split("-")[0]))
    mkv = glob.glob(glob.escape("Detective Conan - All English Episodes/")+f"*{ep} *[[]Baaro*.mkv")
    if not mkv:
        print("missing src mkv", ep)
        continue
    dst = glob.glob(glob.escape("[RAW Reghost-Fabre] Detective Conan [001-520][DVDR2J][480p][Hi10][AC3]/")+f"**/*Conan {ep}*.mkv")
    if not dst:
        print("missing dst mkv", ep)
        continue
    subprocess.run(["sushi", "--src", mkv[0], "--dst", dst[0], "--script", "subs/0001-0999/"+file, "-o", "subs/0001-0999/"+file])
