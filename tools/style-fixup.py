import os
import re
from natsort import natsorted
#from unidecode import unidecode
#from ocrfixr import spellcheck

for folder in next(os.walk("../subs"))[1]:
    for file in natsorted(os.listdir("../subs/" + folder)):
        if not file.endswith(".ass") or " - TS" in file:
            continue
        out = ""
        ep, ext = file.split(".")
        try:
            ep = int(re.sub("[a-z]", "", ep.split(" ")[0].split("-")[0]))
        except:
            pass
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
                    parts[9] = re.sub(r"(\\be10(?:\\an8)?)(?![\\}])", r"}{\1", parts[9])
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
                    #if parts[1] == parts[2]:
                    #    parts[3] = "Signs"
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
                        print("i", ep, parts[1], parts[9])
                    if r"\b0" not in parts[9] and r"\b1" in parts[9]:
                        print("b", ep, parts[1], parts[9])
                        #parts[9] = parts[9].replace(r"\i1", "")
                    if not parts[9]:
                        continue
                    parts[9] = re.sub(r"(\\be\d+)\}\{(\\an\d+)", r"\1\2", parts[9])
                    parts[9] = re.sub(r"(\\an\d+)\}\{(\\be\d+)", r"\2\1", parts[9])
                    line = ",".join(parts)
                    while r",,\N" in line:
                        line = line.replace(r",,\N", ",,")
                    while r"\N}" in line:
                        line = line.replace(r"\N}", "}")
                    while r"{\N" in line:
                        line = line.replace(r"{\N", "{")
                    line = line.replace(r"\}", "}")
                    #line = line.replace("{ ", "{")
                    #line = line.replace(" }", "}")
                    line = line.replace("}{\\", "\\")
                    line = line.replace("{}", "")
                    line = line.replace(r"\c)", "")
                    line = line.replace(r"\an8\an8", r"\an8")
                    line = line.replace(",, ", ",,")
                    #line = line.replace("l-I", "I-I")
                    line = line.strip()
                    #line = line.replace("— ", r"—\h")
                    line = re.sub(r"—\\h$", "—", line)
                    line = line.strip()
                    parts = line.split(",", 9)
                    #parts[9] = parts[9].replace(" s ", "'s ")
                    parts[9] = parts[9].replace(" . ", ". ")
                    parts[9] = parts[9].replace("..,", "...")
                    #parts[9] = re.sub(r"([^\.A-Z])\. ([a-z])", r"\1, \2", parts[9])
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
                    if style == "Signs":
                        if parts[9].lower() == "look forward to the next episode":
                            continue
                        if parts[9].lower() == "look forward to the next episode!":
                            continue
                        if parts[9].lower() == "60 seconds until the next episode's hint!":
                            continue
                        if parts[9] == "NEXT EPISODE":
                            continue
                        if parts[9] == "Next episode's hint right after this!":
                            continue
                    if parts[9] == "Please look forward to the next episode!":
                        continue
                    line = ",".join(parts)
                out += line + "\n"
            out = re.sub(r"\[Aegisub Project Garbage\].*?^\[", "[", out, flags=re.MULTILINE | re.DOTALL)
            out = re.sub(r"\n+^\[Events\]", "\n\n[Events]", out, flags=re.MULTILINE)
            out = out.replace("﻿", "").replace("‬", "").replace("‭", "").replace("‘", "'")
            #out = re.sub(r"([a-zA-Z])\.\.\.([a-zA-Z])", r"\1... \2", out)
            #out = re.sub(r",,\.\.\. ([a-zA-Z])", r",,...\1", out)
            #out = re.sub("!!+", "!", out)
            out = re.sub(r"([a-zA-Z0-9!])\?\?+", r"\1?", out)
            out = re.sub(r"\.{2}", "...", out)
            out = re.sub(r"\.{4,}", "...", out)
            """
            out = re.sub(r"(,,|\\N|\. )A([a-z])[-] ?[aA]\2", r"\1A\2-A\2", out)
            out = re.sub(r"(,,|\\N|\. )B([a-z])[-] ?[bB]\2", r"\1B\2-B\2", out)
            out = re.sub(r"(,,|\\N|\. )C([a-z])[-] ?[cC]\2", r"\1C\2-C\2", out)
            out = re.sub(r"(,,|\\N|\. )D([a-z])[-] ?[dD]\2", r"\1D\2-D\2", out)
            out = re.sub(r"(,,|\\N|\. )E([a-z])[-] ?[eE]\2", r"\1E\2-E\2", out)
            out = re.sub(r"(,,|\\N|\. )F([a-z])[-] ?[fF]\2", r"\1F\2-F\2", out)
            out = re.sub(r"(,,|\\N|\. )G([a-z])[-] ?[gG]\2", r"\1G\2-G\2", out)
            out = re.sub(r"(,,|\\N|\. )H([a-z])[-] ?[hH]\2", r"\1H\2-H\2", out)
            out = re.sub(r"(,,|\\N|\. )I([a-z])[-] ?[iI]\2", r"\1I\2-I\2", out)
            out = re.sub(r"(,,|\\N|\. )J([a-z])[-] ?[jJ]\2", r"\1J\2-J\2", out)
            out = re.sub(r"(,,|\\N|\. )K([a-z])[-] ?[kK]\2", r"\1K\2-K\2", out)
            out = re.sub(r"(,,|\\N|\. )L([a-z])[-] ?[lL]\2", r"\1L\2-L\2", out)
            out = re.sub(r"(,,|\\N|\. )M([a-z])[-] ?[mM]\2", r"\1M\2-M\2", out)
            out = re.sub(r"(,,|\\N|\. )N([a-z])[-] ?[nN]\2", r"\1N\2-N\2", out)
            out = re.sub(r"(,,|\\N|\. )O([a-z])[-] ?[oO]\2", r"\1O\2-O\2", out)
            out = re.sub(r"(,,|\\N|\. )P([a-z])[-] ?[pP]\2", r"\1P\2-P\2", out)
            out = re.sub(r"(,,|\\N|\. )Q([a-z])[-] ?[qQ]\2", r"\1Q\2-Q\2", out)
            out = re.sub(r"(,,|\\N|\. )R([a-z])[-] ?[rR]\2", r"\1R\2-R\2", out)
            out = re.sub(r"(,,|\\N|\. )S([a-z])[-] ?[sS]\2", r"\1S\2-S\2", out)
            out = re.sub(r"(,,|\\N|\. )T([a-z])[-] ?[tT]\2", r"\1T\2-T\2", out)
            out = re.sub(r"(,,|\\N|\. )U([a-z])[-] ?[uU]\2", r"\1U\2-U\2", out)
            out = re.sub(r"(,,|\\N|\. )V([a-z])[-] ?[vV]\2", r"\1V\2-V\2", out)
            out = re.sub(r"(,,|\\N|\. )W([a-z])[-] ?[wW]\2", r"\1W\2-W\2", out)
            out = re.sub(r"(,,|\\N|\. )X([a-z])[-] ?[xX]\2", r"\1X\2-X\2", out)
            out = re.sub(r"(,,|\\N|\. )Y([a-z])[-] ?[yY]\2", r"\1Y\2-Y\2", out)
            out = re.sub(r"(,,|\\N|\. )Z([a-z])[-] ?[zZ]\2", r"\1Z\2-Z\2", out)
            """
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
