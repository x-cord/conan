import re
import glob
import subprocess

files = [
    "0126 (Puto).ass",
    "0127 (Puto).ass"
]

for file in files:
    ep, group = file.split(" (")
    ep = int(re.sub("[^0-9]", "", ep.split(" ")[0].split("-")[0]))
    mkv = glob.glob(glob.escape("Detective Conan - All English Episodes/")+f"*{ep}"+glob.escape(" [Puto]")+"*.mkv")
    if not mkv:
        print("missing src mkv", ep)
    dst = glob.glob(glob.escape("[RAW Reghost-Fabre] Detective Conan [001-520][DVDR2J][480p][Hi10][AC3]/")+f"**/*Conan {ep}*.mkv")
    if not dst:
        print("missing dst mkv", ep)
    subprocess.run(["sushi", "--src", mkv[0], "--dst", dst[0], "--script", "subs/0001-0999/"+file])
