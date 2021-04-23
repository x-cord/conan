import os
import re
import glob
import subprocess

files = [
    "0132 (M-L).ass",
    "0133 (M-L).ass",
    "0134 (M-L).ass",
    "0162 (M-L).ass",
    "0170 (M-L).ass",
    "0171 (M-L).ass",
    "0284 (M-L).ass",
    "0285 (M-L).ass",
    "0286 (M-L).ass",
    "0287 (M-L).ass",
    "0288 (M-L).ass",
    "0304 (M-L).ass",
    "0356 (M-L).ass",
    "0424 (M-L).ass",
    "0453 (M-L).ass",
    "0454 (M-L).ass",
    "0455 (M-L).ass",
    "0456 (M-L).ass"
]

for file in files:
    ep, group = file.split(" (")
    ep = int(re.sub("[^0-9]", "", ep.split(" ")[0].split("-")[0]))
    mkv = glob.glob(glob.escape("Detective Conan - All English Episodes/")+f"*{ep} *[[]M-L*.mkv")
    if not mkv:
        print("missing src mkv", ep)
        continue
    dst = glob.glob(glob.escape("[RAW Reghost-Fabre] Detective Conan [001-520][DVDR2J][480p][Hi10][AC3]/")+f"**/*Conan {ep}*.mkv")
    if not dst:
        print("missing dst mkv", ep)
        continue
    subprocess.run(["sushi", "--src", mkv[0], "--dst", dst[0], "--script", "subs/0001-0999/"+file])
