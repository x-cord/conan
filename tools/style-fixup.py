import os
import re
from natsort import natsorted
#from unidecode import unidecode
#from ocrfixr import spellcheck

for folder in next(os.walk("../subs"))[1]:
    for file in natsorted(os.listdir("../subs/" + folder)):
        if not file.endswith(".ass"):
            continue
        out = ""
        ep, ext = file.split(".")
        ep = int(re.sub("[a-z]", "", ep.split(" ")[0].split("-")[0]))
        with open("../subs/" + folder + "/" + file, encoding="utf8") as f:
            content = f.read()
            lines = content.splitlines()

            for line in lines:
                line = line.rstrip()
                if line.startswith("; "):
                    continue
                parts = line.split(",", 9)
                if line.startswith("Dialogue: ") or line.startswith("Comment: "):
                    parts = line.split(",", 9)
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                    style = parts[3]
                    if style in [
                        "Dialogue",
                        "Dialogue Top",
                        "Signs",
                    ]:
                        line = re.sub(r"\\be\d*", "", line)
                        line = line.replace(r"\}", "}")
                        line = line.replace("{}", "")
                        parts = line.split(",", 9)
                    if style in [
                        "Thoughts",
                        "Radio",
                        "Narration",
                        "Narration Off",
                        "Flashback",
                        "Flashback Thoughts",
                        "Honorifics - Thoughts",
                        "Honorifics - Radio",
                        "Honorifics - Narration",
                        "Honorifics - Narration Off",
                        "Honorifics - Flashback",
                        "Honorifics - Flashback Thoughts",
                    ]:
                        line = re.sub(r"\\be\d*", "", line)
                        line = line.replace(r"\}", "}")
                        line = line.replace("{}", "")
                        parts = line.split(",", 9)
                        parts[9] = r"{\be10}" + parts[9]
                        line = ",".join(parts)
                        parts = line.split(",", 9)
                    if parts[1] == parts[2]:
                        parts[3] = "Signs"
                    style = parts[3]
                    parts[9] = re.sub(r"Honorifics - [^}\\]+", "Honorifics - "+style.replace(" Top", ""), parts[9])
                    if r"\be10" in parts[9]:
                        parts[9] = re.sub(r"Honorifics - [^}\\]+", "Honorifics - "+style.replace(" Top", "")+r"\\be10", parts[9])
                        parts[9] = parts[9].replace(r"{\r}", r"{\r\be10}")
                        parts[9] = parts[9].replace(r"\be10\be10", r"\be10")
                    parts[9] = re.sub(r"(\\N)+$", "", parts[9])
                    #parts[9] = re.sub(r"({[^}{]*?)\s*{\s*", r"\1 / ", parts[9])
                    #parts[9] = re.sub("^SO([ ,.])", r"So\1", parts[9])
                    #parts[9] = re.sub("^sO([ ,.])", r"So\1", parts[9])
                    #parts[9] = re.sub("([^A-Z]{2})SO([ ,.])", r"\1so\2", parts[9])
                    #parts[9] = parts[9].replace("sO", "so")
                    #parts[9] = parts[9].replace("tO", "to")
                    #parts[9] = parts[9].replace("Iike", "like")
                    #parts[9] = parts[9].replace("Iook", "look")
                    #parts[9] = parts[9].rstrip(r"_-\/=°#«»~^ ")
                    #parts[9] = parts[9].rstrip("+")
                    #parts[9] = re.sub(r'Mr\.([^ ,.\\])', r"Mr. \1", parts[9])
                    #parts[9] = re.sub(r'([^\.])\s*=*-+=*$', r"\1—", parts[9])
                    #parts[9] = re.sub(r'Mourn([^a-z]|$)', r"Mouri\1", parts[9])
                    #parts[9] = parts[9].replace("Mr ", "Mr. ")
                    #parts[9] = parts[9].replace("Hey. ", "Hey, ")
                    #parts[9] = parts[9].replace("Huh. ", "Huh, ")
                    parts[9] = parts[9].replace("Mouril", "Mouri!")
                    #parts[9] = parts[9].replace("Oh. ", "Oh, ")
                    #parts[9] = parts[9].replace("'?", "?")
                    parts[9] = parts[9].replace("1.Q", "I.Q")
                    parts[9] = parts[9].replace(r"{\i}", r"{\i0}")
                    if r"\i1" not in parts[9]:
                        parts[9] = parts[9].replace(r"\i0", "")
                    if r"\i0" not in parts[9] and r"\i1" in parts[9]:
                        print(ep, parts[1], parts[9])
                        #parts[9] = parts[9].replace(r"\i1", "")
                    if not parts[9]:
                        continue
                    line = ",".join(parts)
                    while r",,\N" in line:
                        line = line.replace(r",,\N", ",,")
                    while r"\N}" in line:
                        line = line.replace(r"\N}", "}")
                    line = line.replace(r"\}", "}")
                    line = line.replace("}{", "")
                    line = line.replace("{}", "")
                    line = line.replace(r"\c)", "")
                    line = line.replace(r"\an8\an8", r"\an8")
                    line = line.replace(",, ", ",,")
                    #line = line.replace("l-I", "I-I")
                    line = line.strip()
                    line = line.replace("— ", r"—\h")
                    line = re.sub(r"—\\h$", "—", line)
                    line = line.strip()
                    parts = line.split(",", 9)
                    """
                    parts[9] = parts[9].replace(r"\\N", r" \\N ")
                    parts[9] = parts[9].replace("}", "} ")
                    parts[9] = parts[9].replace("{", " {")
                    parts[9] = spellcheck(parts[9]).fix()
                    parts[9] = parts[9].replace(r" \\N ", r"\\N")
                    parts[9] = parts[9].replace("} ", "}")
                    parts[9] = parts[9].replace(" {", "{")
                    """
                    #parts[9] = unidecode(parts[9], errors="preserve")
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                out += line + "\n"
            out = re.sub(r"\[Aegisub Project Garbage\].*?^\[", "[", out, flags=re.MULTILINE | re.DOTALL)
            out = re.sub(r"\n+^\[Events\]", "\n\n[Events]", out, flags=re.MULTILINE)
            out = out.replace("﻿", "").replace("‘", "'")
            out = re.sub(r"([a-zA-Z])\.\.\.([a-zA-Z])", r"\1... \2", out)
            out = re.sub(r",,\.\.\. ([a-zA-Z])", r",,...\1", out)
            #out = re.sub("!!+", "!", out)
            out = re.sub(r"([a-zA-Z0-9!])\?\?+", r"\1?", out)
            out = re.sub(r"\.{4,}", "...", out)
            """
            out = re.sub(r"(,,|\\N|\. )A[,.!-] ?[aA]", r"\1A-A", out)
            out = re.sub(r"(,,|\\N|\. )B[,.!-] ?[bB]", r"\1B-B", out)
            out = re.sub(r"(,,|\\N|\. )C[,.!-] ?[cC]", r"\1C-C", out)
            out = re.sub(r"(,,|\\N|\. )D[,.!-] ?[dD]", r"\1D-D", out)
            out = re.sub(r"(,,|\\N|\. )E[,.!-] ?[eE]", r"\1E-E", out)
            out = re.sub(r"(,,|\\N|\. )F[,.!-] ?[fF]", r"\1F-F", out)
            out = re.sub(r"(,,|\\N|\. )G[,.!-] ?[gG]", r"\1G-G", out)
            out = re.sub(r"(,,|\\N|\. )H[,.!-] ?[hH]", r"\1H-H", out)
            out = re.sub(r"(,,|\\N|\. )I[,.!-] ?[iI]", r"\1I-I", out)
            out = re.sub(r"(,,|\\N|\. )J[,.!-] ?[jJ]", r"\1J-J", out)
            out = re.sub(r"(,,|\\N|\. )K[,.!-] ?[kK]", r"\1K-K", out)
            out = re.sub(r"(,,|\\N|\. )L[,.!-] ?[lL]", r"\1L-L", out)
            out = re.sub(r"(,,|\\N|\. )M[,.!-] ?[mM]", r"\1M-M", out)
            out = re.sub(r"(,,|\\N|\. )N[,.!-] ?[nN]", r"\1N-N", out)
            out = re.sub(r"(,,|\\N|\. )O[,.!-] ?[oO]", r"\1O-O", out)
            out = re.sub(r"(,,|\\N|\. )P[,.!-] ?[pP]", r"\1P-P", out)
            out = re.sub(r"(,,|\\N|\. )Q[,.!-] ?[qQ]", r"\1Q-Q", out)
            out = re.sub(r"(,,|\\N|\. )R[,.!-] ?[rR]", r"\1R-R", out)
            out = re.sub(r"(,,|\\N|\. )S[,.!-] ?[sS]", r"\1S-S", out)
            out = re.sub(r"(,,|\\N|\. )T[,.!-] ?[tT]", r"\1T-T", out)
            out = re.sub(r"(,,|\\N|\. )U[,.!-] ?[uU]", r"\1U-U", out)
            out = re.sub(r"(,,|\\N|\. )V[,.!-] ?[vV]", r"\1V-V", out)
            out = re.sub(r"(,,|\\N|\. )W[,.!-] ?[wW]", r"\1W-W", out)
            out = re.sub(r"(,,|\\N|\. )X[,.!-] ?[xX]", r"\1X-X", out)
            out = re.sub(r"(,,|\\N|\. )Y[,.!-] ?[yY]", r"\1Y-Y", out)
            out = re.sub(r"(,,|\\N|\. )Z[,.!-] ?[zZ]", r"\1Z-Z", out)
            """
            """
            out = re.sub(r"(,,|\\N)A-a", r"\1A-A", out)
            out = re.sub(r"(,,|\\N)B-b", r"\1B-B", out)
            out = re.sub(r"(,,|\\N)C-c", r"\1C-C", out)
            out = re.sub(r"(,,|\\N)D-d", r"\1D-D", out)
            out = re.sub(r"(,,|\\N)E-e", r"\1E-E", out)
            out = re.sub(r"(,,|\\N)F-f", r"\1F-F", out)
            out = re.sub(r"(,,|\\N)G-g", r"\1G-G", out)
            out = re.sub(r"(,,|\\N)H-h", r"\1H-H", out)
            out = re.sub(r"(,,|\\N)I-i", r"\1I-I", out)
            out = re.sub(r"(,,|\\N)J-j", r"\1J-J", out)
            out = re.sub(r"(,,|\\N)K-k", r"\1K-K", out)
            out = re.sub(r"(,,|\\N)L-l", r"\1L-L", out)
            out = re.sub(r"(,,|\\N)M-m", r"\1M-M", out)
            out = re.sub(r"(,,|\\N)N-n", r"\1N-N", out)
            out = re.sub(r"(,,|\\N)O-o", r"\1O-O", out)
            out = re.sub(r"(,,|\\N)P-p", r"\1P-P", out)
            out = re.sub(r"(,,|\\N)Q-q", r"\1Q-Q", out)
            out = re.sub(r"(,,|\\N)R-R", r"\1R-R", out)
            out = re.sub(r"(,,|\\N)S-s", r"\1S-S", out)
            out = re.sub(r"(,,|\\N)T-t", r"\1T-T", out)
            out = re.sub(r"(,,|\\N)U-u", r"\1U-U", out)
            out = re.sub(r"(,,|\\N)V-v", r"\1V-V", out)
            out = re.sub(r"(,,|\\N)W-w", r"\1W-W", out)
            out = re.sub(r"(,,|\\N)X-x", r"\1X-X", out)
            out = re.sub(r"(,,|\\N)Y-y", r"\1Y-Y", out)
            out = re.sub(r"(,,|\\N)Z-z", r"\1Z-Z", out)
            out = re.sub(r"(,,|\\N)A, a", r"\1A-A", out)
            out = re.sub(r"(,,|\\N)B, b", r"\1B-B", out)
            out = re.sub(r"(,,|\\N)C, c", r"\1C-C", out)
            out = re.sub(r"(,,|\\N)D, d", r"\1D-D", out)
            out = re.sub(r"(,,|\\N)E, e", r"\1E-E", out)
            out = re.sub(r"(,,|\\N)F, f", r"\1F-F", out)
            out = re.sub(r"(,,|\\N)G, g", r"\1G-G", out)
            out = re.sub(r"(,,|\\N)H, h", r"\1H-H", out)
            out = re.sub(r"(,,|\\N)I, i", r"\1I-I", out)
            out = re.sub(r"(,,|\\N)J, j", r"\1J-J", out)
            out = re.sub(r"(,,|\\N)K, k", r"\1K-K", out)
            out = re.sub(r"(,,|\\N)L, l", r"\1L-L", out)
            out = re.sub(r"(,,|\\N)M, m", r"\1M-M", out)
            out = re.sub(r"(,,|\\N)N, n", r"\1N-N", out)
            out = re.sub(r"(,,|\\N)O, o", r"\1O-O", out)
            out = re.sub(r"(,,|\\N)P, p", r"\1P-P", out)
            out = re.sub(r"(,,|\\N)Q, q", r"\1Q-Q", out)
            out = re.sub(r"(,,|\\N)R, r", r"\1R-R", out)
            out = re.sub(r"(,,|\\N)S, s", r"\1S-S", out)
            out = re.sub(r"(,,|\\N)T, t", r"\1T-T", out)
            out = re.sub(r"(,,|\\N)U, u", r"\1U-U", out)
            out = re.sub(r"(,,|\\N)V, v", r"\1V-V", out)
            out = re.sub(r"(,,|\\N)W, w", r"\1W-W", out)
            out = re.sub(r"(,,|\\N)X, x", r"\1X-X", out)
            out = re.sub(r"(,,|\\N)Y, y", r"\1Y-Y", out)
            out = re.sub(r"(,,|\\N)Z, z", r"\1Z-Z", out)
            out = re.sub(r"(,,|\\N)A[,.]a", r"\1A-A", out)
            out = re.sub(r"(,,|\\N)B[,.]b", r"\1B-B", out)
            out = re.sub(r"(,,|\\N)C[,.]c", r"\1C-C", out)
            out = re.sub(r"(,,|\\N)D[,.]d", r"\1D-D", out)
            out = re.sub(r"(,,|\\N)E[,.]e", r"\1E-E", out)
            out = re.sub(r"(,,|\\N)F[,.]f", r"\1F-F", out)
            out = re.sub(r"(,,|\\N)G[,.]g", r"\1G-G", out)
            out = re.sub(r"(,,|\\N)H[,.]h", r"\1H-H", out)
            out = re.sub(r"(,,|\\N)I[,.]i", r"\1I-I", out)
            out = re.sub(r"(,,|\\N)J[,.]j", r"\1J-J", out)
            out = re.sub(r"(,,|\\N)K[,.]k", r"\1K-K", out)
            out = re.sub(r"(,,|\\N)L[,.]l", r"\1L-L", out)
            out = re.sub(r"(,,|\\N)M[,.]m", r"\1M-M", out)
            out = re.sub(r"(,,|\\N)N[,.]n", r"\1N-N", out)
            out = re.sub(r"(,,|\\N)O[,.]o", r"\1O-O", out)
            out = re.sub(r"(,,|\\N)P[,.]p", r"\1P-P", out)
            out = re.sub(r"(,,|\\N)Q[,.]q", r"\1Q-Q", out)
            out = re.sub(r"(,,|\\N)R[,.]r", r"\1R-R", out)
            out = re.sub(r"(,,|\\N)S[,.]s", r"\1S-S", out)
            out = re.sub(r"(,,|\\N)T[,.]t", r"\1T-T", out)
            out = re.sub(r"(,,|\\N)U[,.]u", r"\1U-U", out)
            out = re.sub(r"(,,|\\N)V[,.]v", r"\1V-V", out)
            out = re.sub(r"(,,|\\N)W[,.]w", r"\1W-W", out)
            out = re.sub(r"(,,|\\N)X[,.]x", r"\1X-X", out)
            out = re.sub(r"(,,|\\N)Y[,.]y", r"\1Y-Y", out)
            out = re.sub(r"(,,|\\N)Z[,.]z", r"\1Z-Z", out)
            """
            with open("../subs/" + folder + "/" + file, "w") as fw:
                fw.write(out)
