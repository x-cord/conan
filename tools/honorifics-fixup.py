import os
import re
from natsort import natsorted

honorifics = [
    "san",
    "sama",
    "kun",
    "chan",
    "tan",
    "senpai",
    "sensei",
    "kohai",
    "hakase",
    "neechan",
    "oneesan",
    "oneesama",
    "oneechan",
    "onichan",
    "onisan",
    "obasan",
    "oobasan",
    "neesan",
    "aneki",
    "aniki",
    "zeki",
    "han",
    "niichan",
    "dono",
    "ojosama",
    "niisan",
    "oniisama",
    "ojisan",
    "nee",
    "nii",
]

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
                    parts = line.split(",", 9)
                    for honorific in honorifics:
                        if honorific in line:
                            if r"\be10" in line:
                                line = re.sub(
                                    "(?:{[^}]*})?(-)(?:{[^}]*})?"
                                    + honorific
                                    + "(?:{[^}]*})?(?:([][.,()?!'\" \\\\—:;…~]|$)|{[^}]*})",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"\\be10}\1"
                                    + honorific
                                    + r"{\\r\\be10}\2",
                                    line,
                                )
                            else:
                                line = re.sub(
                                    "(?:{[^}]*})?(-)(?:{[^}]*})?"
                                    + honorific
                                    + "(?:{[^}]*})?(?:([][.,()?!'\" \\\\—:;…~]|$)|{[^}]*})",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"}\1"
                                    + honorific
                                    + r"{\\r}\2",
                                    line,
                                )
                            line = re.sub(
                                r"({[^\\{}]*[^\\{}]){[^{}]*}(-[^\\{}]*){[^{}]*}([^\\{}]*})",
                                r"\1\2\3",
                                line,
                            )
                            parts = line.split(",", 9)
                        elif honorific.capitalize() in line:
                            if r"\be10" in line:
                                line = re.sub(
                                    "(?:{[^}]*})?(-)(?:{[^}]*})?"
                                    + honorific.capitalize()
                                    + "(?:{[^}]*})?(?:([][.,()?!'\" \\\\—:;…~]|$)|{[^}]*})",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"\\be10}\1"
                                    + honorific.lower()
                                    + r"{\\r\\be10}\2",
                                    line,
                                )
                            else:
                                line = re.sub(
                                    "(?:{[^}]*})?(-)(?:{[^}]*})?"
                                    + honorific.capitalize()
                                    + "(?:{[^}]*})?(?:([][.,()?!'\" \\\\—:;…~]|$)|{[^}]*})",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"}\1"
                                    + honorific.lower()
                                    + r"{\\r}\2",
                                    line,
                                )
                            line = re.sub(
                                r"({[^\\{}]*[^\\{}]){[^{}]*}(-[^\\{}]*){[^{}]*}([^\\{}]*})",
                                r"\1\2\3",
                                line,
                            )
                            parts = line.split(",", 9)
                        elif honorific.upper() in line:
                            if r"\be10" in line:
                                line = re.sub(
                                    "(?:{[^}]*})?(-)(?:{[^}]*})?"
                                    + honorific.upper()
                                    + "(?:{[^}]*})?(?:([][.,()?!'\" \\\\—:;…~]|$)|{[^}]*})",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"\\be10}\1"
                                    + honorific.upper()
                                    + r"{\\r\\be10}\2",
                                    line,
                                )
                            else:
                                line = re.sub(
                                    "(?:{[^}]*})?(-)(?:{[^}]*})?"
                                    + honorific.upper()
                                    + "(?:{[^}]*})?(?:([][.,()?!'\" \\\\—:;…~]|$)|{[^}]*})",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"}\1"
                                    + honorific.upper()
                                    + r"{\\r}\2",
                                    line,
                                )
                            line = re.sub(
                                r"({[^\\{}]*[^\\{}]){[^{}]*}(-[^\\{}]*){[^{}]*}([^\\{}]*})",
                                r"\1\2\3",
                                line,
                            )
                            parts = line.split(",", 9)
                    if r"\be10" in line:
                        line = re.sub(
                            r"-{\\i1}([^{ ]*){\\i0}|{\\i1}-([^{ ])*{\\i0}",
                            r"{\\rHonorifics - "
                            + (style.replace(" Top", ""))
                            + r"\\be10}-\1\2"
                            + r"{\\r\\be10}",
                            line,
                        )
                    else:
                        line = re.sub(
                            r"-{\\i1}([^{ ]*){\\i0}|{\\i1}-([^{ ])*{\\i0}",
                            r"{\\rHonorifics - "
                            + (style.replace(" Top", ""))
                            + r"}-\1\2"
                            + r"{\\r}",
                            line,
                        )
                    for honorific in honorifics:
                        if honorific in line:
                            if r"\be10" in line:
                                line = re.sub(
                                    r"{\\i1}"
                                    + honorific
                                    + r"{\\i0}",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"\\be10}"
                                    + honorific
                                    + r"{\\r\\be10}",
                                    line,
                                )
                            else:
                                line = re.sub(
                                    r"{\\i1}"
                                    + honorific
                                    + r"{\\i0}",
                                    r"{\\rHonorifics - "
                                    + (style.replace(" Top", ""))
                                    + r"}"
                                    + honorific
                                    + r"{\\r}",
                                    line,
                                )
                    parts = line.split(",", 9)
                    parts[9] = parts[9].strip()
                out += line + "\n"
            out = re.sub(r"\[Aegisub Project Garbage\].*?^\[", "[", out, flags=re.MULTILINE | re.DOTALL)
            out = re.sub(r"\n+^\[Events\]", "\n\n[Events]", out, flags=re.MULTILINE)
            out = out.replace("﻿", "").replace("‘", "'")
            out = re.sub(r"([a-zA-Z])\.\.\.([a-zA-Z])", r"\1... \2", out)
            out = re.sub(r",,\.\.\. ([a-zA-Z])", r",,...\1", out)
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
            """
            with open("../subs/" + folder + "/" + ep + ".ass", "w") as fw:
                fw.write(out)
