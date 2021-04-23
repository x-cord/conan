import os
import re
import glob
import subprocess

files = [
    "0186 (UTB).ass",
    "0187 (UTB).ass",
    "0188 (UTB).ass",
    "0189 (UTB).ass",
    "0190 (UTB).ass",
    "0191 (UTB).ass",
    "0192 (UTB).ass",
    "0193 (UTB).ass",
    "0260 (UTB).ass",
    "0261 (UTB).ass",
    "0262 (UTB).ass",
    "0271 (UTB).ass",
    "0272 (UTB).ass",
    "0273 (UTB).ass",
    "0274 (UTB).ass",
    "0275 (UTB).ass",
    "0277 (UTB).ass",
    "0278 (UTB).ass",
    "0279 (UTB).ass",
    "0280 (UTB).ass",
    "0281 (UTB).ass",
    "0282 (UTB).ass",
    "0283 (UTB).ass",
    "0289 (UTB).ass",
    "0290 (UTB).ass",
    "0294 (UTB).ass",
    "0295 (UTB).ass",
    "0296 (UTB).ass",
    "0299 (UTB).ass",
    "0300 (UTB).ass",
    "0303 (UTB).ass",
    "0309 (UTB).ass",
    "0310 (UTB).ass",
    "0311 (UTB).ass",
    "0312 (UTB).ass",
    "0313 (UTB).ass",
    "0318 (UTB).ass",
    "0319 (UTB).ass",
    "0321 (UTB).ass",
    "0322 (UTB).ass",
    "0323 (UTB).ass",
    "0324 (UTB).ass",
    "0325 (UTB).ass",
    "0326 (UTB).ass",
    "0327 (UTB).ass",
    "0328 (UTB).ass",
    "0331 (UTB).ass",
    "0332 (UTB).ass",
    "0333 (UTB).ass",
    "0334 (UTB).ass",
    "0355 (UTB).ass",
    "0357 (UTB).ass",
    "0358 (UTB).ass",
    "0359 (UTB).ass",
    "0360 (UTB).ass",
    "0361 (UTB).ass",
    "0390 (UTB).ass"
]

for file in files:
    ep, group = file.split(" (")
    ep = int(re.sub("[^0-9]", "", ep.split(" ")[0].split("-")[0]))
    mkv = glob.glob(glob.escape("[UTB] Detective Conan 128-131,150-156,158-420 [English SUB]/")+f"*{ep}*.mkv")
    if not mkv:
        print("missing src mkv", ep)
    dst = glob.glob(glob.escape("[RAW Reghost-Fabre] Detective Conan [001-520][DVDR2J][480p][Hi10][AC3]/")+f"**/*Conan {ep}*.mkv")
    if not dst:
        print("missing dst mkv", ep)
    subprocess.run(["sushi", "--src", mkv[0], "--dst", dst[0], "--script", "subs/0001-0999/"+file])
