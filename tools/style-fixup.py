import os
import re
from natsort import natsorted

for folder in next(os.walk("../subs"))[1]:
    for file in natsorted(os.listdir("../subs/" + folder)):
        if not file.endswith(".ass"):
            continue
        out = ""
        ep, ext = file.split(".")
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
                    style = parts[3]
                    parts[9] = re.sub(r"Honorifics - [^}\\]+", "Honorifics - "+style.replace(" Top", ""), parts[9])
                    if r"\be10" in parts[9]:
                        parts[9] = re.sub(r"Honorifics - [^}\\]+", "Honorifics - "+style.replace(" Top", "")+r"\\be10", parts[9])
                        parts[9] = parts[9].replace(r"{\r}", r"{\r\be10}")
                        parts[9] = parts[9].replace(r"\be10\be10", r"\be10")
                    parts[9] = re.sub(r"\\N+$", "", parts[9])
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
                    line = line.strip()
                    line = line.replace("— ", r"—\h")
                    line = re.sub(r"—\\h$", "—", line)
                    line = line.strip()
                    parts = line.split(",", 9)
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                out += line + "\n"
            out = re.sub(r"\[Aegisub Project Garbage\].*?^\[", "[", out, flags=re.MULTILINE | re.DOTALL)
            out = out.replace("﻿", "").replace("‘", "'")
            with open("../subs/" + folder + "/" + ep + ".ass", "w") as fw:
                fw.write(out)
