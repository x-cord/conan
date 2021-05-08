import os
import re
from natsort import natsorted

approved = [
    "Dialogue",
    "Dialogue Top",
    "Signs",
    "Thoughts",
    "Radio",
    "Narration",
    "Narration Off",
    "Flashback",
    "Flashback Thoughts",
    "Honorifics - Dialogue",
    "Honorifics - Signs",
    "Honorifics - Thoughts",
    "Honorifics - Radio",
    "Honorifics - Narration",
    "Honorifics - Narration Off",
    "Honorifics - Flashback",
    "Honorifics - Flashback Thoughts",
    "Masks",
    "Title",
    "OPED",
    "Eyecatch",
    "Character Card",
    "Farewell Card",
]
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

shown = set()

for folder in next(os.walk("../og"))[1]:
    for file in natsorted(os.listdir("../og/" + folder)):
        if not file.endswith(".ass"):
            continue
        out = ""
        ep, group = file.split(" (")
        group = group.split(")")[0]
        with open("../og/" + folder + "/" + file, encoding="utf8") as f:
            content = f.read()
            content = content.replace("WrapStyle: ", "TL Source: " + group + "\nWrapStyle: ")
            lines = content.splitlines()
            remove = set()
            rename = {}
            seen = set()
            skip_empty = False
            remove.add("RMLyrics")
            remove.add("RMLyrics2")
            remove.add("TLLyrics")
            remove.add("TLLyrics2")
            remove.add("Credit")
            remove.add("Credits")
            remove.add("CreditsRole")
            remove.add("EpisodeTitle")
            remove.add("NextEpTitle1")
            remove.add("NextEpTitle2")
            remove.add("NextEp")
            remove.add("OP")
            remove.add("OP-R")
            remove.add("OP-EN")
            remove.add("OP-R-furigana")
            remove.add("OP-EN-furigana")
            remove.add("ED-R-furigana")
            remove.add("ED-EN-furigana")
            remove.add("ED")
            remove.add("ED-R")
            remove.add("ED-EN")
            remove.add("OPRomaji")
            remove.add("OPTL")
            remove.add("EDRomaji")
            remove.add("EDTL")
            remove.add("EDCredit")
            remove.add("SongsEnglish")
            remove.add("Kanji")
            remove.add("karaoke")
            remove.add("Title")
            remove.add("TitleCard")
            remove.add("Eyecatch")
            remove.add("EyeCatcher")
            remove.add("Song")
            remove.add("Songs")
            remove.add("InsSong")
            remove.add("InsertTL")
            remove.add("InsertRom")
            remove.add("Romaji")
            remove.add("Blank")
            remove.add("Credits2")
            remove.add("OP Eng")
            remove.add("OP/ED Romaji")
            remove.add("OP/ED Translation")
            remove.add("ED Romaji")
            remove.add("ED Translation")
            remove.add("Title of Episode")
            remove.add("FBI")
            remove.add("OPEDBottom")
            remove.add("OPEDTop")
            remove.add("Preview")
            remove.add("DC_Logo")
            remove.add("DC Opening Romaji")
            remove.add("Detective Conan Ending Karaoke Romaji")
            remove.add("Detective Conan Ending Karaoke Eng")
            remove.add("Detective Conan Ending Karaoke Eng2")
            remove.add("BOX")
            remove.add("NEPTitle")
            remove.add("Title001")
            remove.add("Karaoke (English)")
            remove.add("Editor's Note Box")
            remove.add("Next Episode Title")
            remove.add("Person's name box")
            remove.add("NEPCard")
            remove.add("NEPShort")
            remove.add("EDCred")
            remove.add("OPCred")
            remove.add("box")
            remove.add("box2")
            remove.add("Copyright")
            remove.add("notebox")
            remove.add("Next Ep Title")
            remove.add("Next Conan Hint")
            remove.add("half time")
            remove.add("Conan Hint")
            remove.add("DC Name Back")
            remove.add("OP_51_Romaji")
            remove.add("ED_61_Romaji")
            remove.add("romaji")
            remove.add("romaji_flickering")
            remove.add("RMLyrics2FX")
            remove.add("Song-Artist Title")
            remove.add("Thinking (Girl) (Bottom)")
            remove.add("Thinking (Guy) (Bottom)")
            remove.add("OPTL_old")
            remove.add("Muteki na Heart")
            remove.add("DCEpPreview")
            remove.add("HappyEnd")
            remove.add("GGC-TL")
            remove.add("GiriGiriRomaji")
            remove.add("GiriGiriRomaji2")
            remove.add("FreeMagicRomaji")
            remove.add("FreeMagicRomaji2")
            remove.add("FreeMagic-TL")
            remove.add("EyecatchSD")
            remove.add("MysteriousEyesTL")
            remove.add("MysteriousEyesTL2")
            remove.add("MERomaji")
            remove.add("MERomaji2")
            remove.add("FreeMagicTL")
            remove.add("OPKara")
            remove.add("OPKara2")
            remove.add("OPKara3")
            remove.add("ShoudouRomaji")
            remove.add("ShoudouTL")
            remove.add("EDTLKanashii")
            remove.add("EDRomaji")
            remove.add("EDRomaji - Copy")
            remove.add("ButterflyCore")
            remove.add("ButterflyCore2")
            remove.add("AitakuteRomaji")
            remove.add("MysteriousEyesRomajiOLD")
            remove.add("OPTop")
            remove.add("OPBottom")
            remove.add("Icant")
            remove.add("Icant - Copy")
            remove.add("ED304")
            remove.add("ED304-2")
            remove.add("ED304-3")
            remove.add("ED304-TL")
            remove.add("Detective Conan - end song eng")
            remove.add("StartROM")
            remove.add("StartTL")
            remove.add("NemuruRomaji")
            remove.add("NemuruTL")
            remove.add("Title10 - 1")
            remove.add("Title11 - 1")
            remove.add("Title12 - 1")
            remove.add("Title13 - 1")
            remove.add("Title14 - 1")
            remove.add("TLLyrics 2")
            remove.add("EDBottom")
            remove.add("EDTop")
            remove.add("TST")
            remove.add("Adds")
            remove.add("Otanoshimi")
            remove.add("MKED")
            remove.add("OPTLTextless")
            remove.add("HitomiRomaji")
            remove.add("Massugu Yuku TL")
            remove.add("Massugu Yuku Romaji")
            remove.add("Poodles")
            remove.add("RainMan")
            remove.add("EDTLBox1")
            remove.add("EDTLBox2")
            remove.add("OPTL_BL")
            remove.add("ED_53_Romaji")
            remove.add("OP_44_Romaji")
            remove.add("Romaji_Insert")
            remove.add("TL_Insert")
            remove.add("Romaji-ED")
            remove.add("ED-TL")
            remove.add("ED_61_TL")
            remove.add("RMLyrics3")
            remove.add("OPRom")
            remove.add("o-tanoshimi")

            rename["Default"] = "Dialogue"
            rename["DCMain"] = "Dialogue"
            rename["English"] = "Dialogue"
            rename["JSub"] = "Dialogue"
            rename["Default 2"] = "Dialogue"
            rename["Default-furigana"] = "Signs"
            rename["DCMain-furigana"] = "Signs"
            rename["Comment"] = "Signs"
            rename["T.N"] = "Signs"
            rename["Police"] = "Signs"
            rename["Pachinko"] = "Signs"
            rename["Press"] = "Signs"
            rename["Artist"] = "Signs"
            rename["BeikaPolice"] = "Signs"
            rename["BeikaTheater"] = "Signs"
            rename["Comedian"] = "Signs"
            rename["Pocke1"] = "Signs"
            rename["President"] = "Signs"
            rename["Tendo"] = "Signs"
            rename["atorie"] = "Signs"
            rename["Phone01"] = "Signs"
            rename["phone1"] = "Signs"
            rename["phone2"] = "Signs"
            rename["phone3"] = "Signs"
            rename["Ei"] = "Signs"
            rename["Eternity"] = "Signs"
            rename["Honoo"] = "Signs"
            rename["Flame"] = "Signs"
            rename["Ryuu"] = "Signs"
            rename["Dragon"] = "Signs"
            rename["Flame 2"] = "Signs"
            rename["Awa"] = "Signs"
            rename["Eternity 2"] = "Signs"
            rename["Swimming"] = "Signs"
            rename["Dragon 2"] = "Signs"
            rename["StpTitle01"] = "Signs"
            rename["gtitle"] = "Signs"
            rename["gtitle02"] = "Signs"
            rename["gtitle03"] = "Signs"
            rename["Xtitle001"] = "Signs"
            rename["Xtitle02"] = "Signs"
            rename["title03"] = "Signs"
            rename["title001"] = "Signs"
            rename["title01"] = "Signs"
            rename["title04"] = "Signs"
            rename["title002"] = "Signs"
            rename["title003"] = "Signs"
            rename["title004"] = "Signs"
            rename["title005"] = "Signs"
            rename["title006"] = "Signs"
            rename["title000"] = "Signs"
            rename["Title002"] = "Signs"
            rename["Title003"] = "Signs"
            rename["Title004"] = "Signs"
            rename["Title005"] = "Signs"
            rename["Title006"] = "Signs"
            rename["Title007"] = "Signs"
            rename["Title008"] = "Signs"
            rename["Title009"] = "Signs"
            rename["Title010"] = "Signs"
            rename["Title011"] = "Signs"
            rename["Title012"] = "Signs"
            rename["Title013"] = "Signs"
            rename["Title02"] = "Signs"
            rename["Title03"] = "Signs"
            rename["Title04"] = "Signs"
            rename["Title05"] = "Signs"
            rename["Title06"] = "Signs"
            rename["Title07"] = "Signs"
            rename["Title08"] = "Signs"
            rename["Title09"] = "Signs"
            rename["Title10"] = "Signs"
            rename["Title11"] = "Signs"
            rename["Title12"] = "Signs"
            rename["Title13"] = "Signs"
            rename["Title14"] = "Signs"
            rename["Title15"] = "Signs"
            rename["Title16"] = "Signs"
            rename["Title17"] = "Signs"
            rename["Title18"] = "Signs"
            rename["Title19"] = "Signs"
            rename["Title20"] = "Signs"
            rename["Title21"] = "Signs"
            rename["PlaceCard"] = "Signs"
            rename["NoPosition01"] = "Signs"
            rename["Special01"] = "Signs"
            rename["JBNotes2"] = "Signs"
            rename["Warning01"] = "Signs"
            rename["Warning02"] = "Signs"
            rename["Warning03"] = "Signs"
            rename["Warning04"] = "Signs"
            rename["Warning05"] = "Signs"
            rename["Warning06"] = "Signs"
            rename["NightBaronessTypeset"] = "Signs"
            rename["Editor's Note"] = "Signs"
            rename["Not"] = "Signs"
            rename["TLnote"] = "Signs"
            rename["Note"] = "Signs"
            rename["TL Note"] = "Signs"
            rename["Top Italic"] = "Signs"
            rename["ScreenText"] = "Signs"
            rename["Def_alt"] = "Dialogue Top"
            rename["Alternative"] = "Dialogue"
            rename["Default360"] = "Dialogue"
            rename["Main"] = "Dialogue"
            rename["Def_tv"] = "Radio"
            rename["Main - Phone"] = "Radio"
            rename["Phone"] = "Radio"
            rename["Electronic Voice"] = "Radio"
            rename["Movie"] = "Radio"
            rename["Mic"] = "Radio"
            rename["def_it"] = "Radio"
            rename["Transmitter"] = "Radio"
            rename["Character Cards"] = "Character Card"
            rename["Name cards"] = "Character Card"
            rename["CharCar02"] = "Character Card"
            rename["Name"] = "Character Card"
            rename["DCThoughts"] = "Thoughts"
            rename["Thinking"] = "Thoughts"
            rename["BCPrologue"] = "Narration Off"
            rename["MENarration"] = "Narration Off"
            rename["DCNarrator"] = "Narration Off"
            rename["NarrationOP"] = "Narration Off"
            rename["Intro"] = "Narration Off"
            rename["Narration360"] = "Narration Off"
            rename["Prolog"] = "Narration Off"
            rename["Opening Lines"] = "Narration Off"
            rename["Prologue"] = "Narration Off"
            rename["PrologueText"] = "Narration Off"
            rename["GreedNarr"] = "Narration Off"
            rename["Narration"] = "Narration Off"
            rename["Narr"] = "Narration Off"
            rename["Thoughts360"] = "Narration Off"
            rename["ProlTrans"] = "Narration Off"
            rename["Kaitei"] = "Narration"
            rename["Hubuki - Normal"] = "Dialogue"
            rename["Hubuki - Thought"] = "Thoughts"
            rename["CharCard"] = "Character Card"
            rename["Place"] = "Character Card"
            rename["Info Box"] = "Character Card"
            rename["CharCards"] = "Character Card"
            rename["Charcards 2"] = "Character Card"
            rename["Üst yazı"] = "Dialogue Top"
            rename["Üst yazi"] = "Dialogue Top"
            rename["Üstyazı"] = "Dialogue Top"
            rename["Üstyazi"] = "Dialogue Top"
            rename["Title01"] = "Character Card"
            rename["Flashback - 01"] = "Flashback"
            rename["DCFlashback"] = "Flashback"
            rename["Thought"] = "Thoughts"
            rename["KudoLocker"] = "Signs"
            rename["RemWord"] = "Signs"
            rename["Italic"] = "Signs"
            rename["Copy of Default"] = "Signs"
            rename["N-E-Title"] = "Signs"
            rename["Sign"] = "Signs"
            rename["Typeset"] = "Signs"
            rename["Somesigns"] = "Signs"
            rename["title02"] = "Character Card"
            rename["CharCard02"] = "Character Card"
            rename["CharCard03"] = "Character Card"
            rename["CharCard04"] = "Character Card"
            rename["DC Name"] = "Character Card"
            rename["Thinking (Guy)"] = "Thoughts"
            rename["Thoughts (Female)"] = "Thoughts"
            rename["Thinking (Girl)"] = "Thoughts"
            rename["Thinking (Girl) (Top)"] = "Thoughts"
            rename["Thinking (Guy) (Top)"] = "Thoughts"
            rename["Def_it"] = "Thoughts"
            rename["Def_up"] = "Dialogue Top"
            rename["Episode Introduction"] = "Narration Off"
            rename["Recap"] = "Narration Off"
            rename["ThoughtsF"] = "Thoughts"
            rename["Memory"] = "Flashback"
            rename["Memory2"] = "Flashback"
            rename["Memory3"] = "Flashback"
            rename["DCItalic"] = "Flashback"
            rename["DCItalic1"] = "Flashback"
            rename["Def_past"] = "Flashback"
            rename["Case history"] = "Flashback"
            rename["Jokes"] = "Dialogue Top"
            rename["Top"] = "Dialogue Top"
            rename["Def2"] = "Dialogue Top"
            rename["Post-NEP Talk"] = "Dialogue Top"
            rename["DCEpTitle"] = "Title"
            rename["HintKara"] = "Signs"
            rename["Woman"] = "Signs"
            rename["DCNextEp"] = "Signs"
            rename["Don'tMiss"] = "Farewell Card"
            rename["MovieDerpsub"] = "Flashback"
            rename["Thoughts2"] = "Thoughts"
            rename["Giris"] = "Thoughts"
            rename["Default Sign"] = "Signs"
            rename["Mail"] = "Signs"
            rename["Text"] = "Signs"
            rename["default01"] = "Dialogue"
            rename["Default2"] = "Dialogue"
            rename["Next time"] = "Dialogue Top"

            if "YZS " in content:
                remove.add("EpisodePreview")

            wait = True
            for line in lines:
                line = line.rstrip()
                if line.startswith("["):
                    wait = False
                if wait:
                    continue
                if line == "[Events]":
                    skip_empty = True
                if line.startswith("Video File: ") or line.startswith("Audio File: "):
                    continue
                parts = line.split(",", 9)
                if line.startswith("Dialogue: ") or line.startswith("Comment: "):
                    if r"\p1" in line:
                        continue
                    if "BAARO RELEASE" in line:
                        continue
                    if ",Effector [fx]," in line:
                        continue
                    if ",Episode Introduction,Typesetting," in line:
                        continue
                    if r"\fn" in line:
                        continue
                    line = line.replace(r"\h", " ")
                    line = line.replace("sempai", "senpai")
                    line = line.replace("ojōsama", "ojosama")
                    line = line.replace("ojousama", "ojosama")
                    line = line.replace("nêchan", "neechan")
                    line = line.replace("néechan", "neechan")
                    line = line.replace("-nee-chan", "-neechan")
                    line = line.strip()
                    line = line.replace("ı", "i")
                    line = line.replace(r"\a6", r"\an8")
                    line = line.replace(r"{\blur1.2", "{")
                    line = line.replace(r"{\be3", "{")
                    line = line.replace(r"{\be10", "{")
                    line = line.replace(r" \N", r"\N")
                    line = line.replace(r" \N", r"\N")
                    line = re.sub(r"\\r[^\\}]*", "", line)
                    line = line.replace("{}", "")
                    line = line.replace("Dialogue: 1,", "Dialogue: 0,")
                    parts = line.split(",", 9)
                    parts[5] = "0"
                    parts[6] = "0"
                    parts[7] = "0"
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                    if ",Thoughts,Comment," in line and r"\fs" in line:
                        parts[3] = "Signs"
                        line = ",".join(parts)
                    if parts[9].startswith("Note:") or r"{\an8\fad(200,200)}" in line:
                        parts[3] = "Signs"
                        line = ",".join(parts)
                        line = line.replace(r"{\an8\fad(200,200)}", "")
                        parts = line.split(",", 9)
                    style = parts[3]
                    if style == "ScreenText" and (r"\fs" in line or ",OP JP," in line):
                        continue
                    if ",OP EN," in line:
                        continue
                    if (r"\a5\fs24\c&H00&\3c&HFFFFFF&\blur2}" in line or r"\a7\fs22\blur2\c&H000000&\3c&HFFFFFF&}" in line):
                        continue
                    if style in remove:
                        continue
                    elif style in rename:
                        style = rename[style]
                        parts[3] = style
                        line = ",".join(parts)
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
                        line = re.sub(r"\\blur[^\\}]*", "", line)
                        line = re.sub(r"\\be[^\\}]*", "", line)
                        line = re.sub(r"\\pos[^\\}]*", "", line)
                        line = re.sub(r"\\frx[^\\}]*", "", line)
                        line = re.sub(r"\\fry[^\\}]*", "", line)
                        line = re.sub(r"\\frz[^\\}]*", "", line)
                        line = re.sub(r"\\xshad[^\\}]*", "", line)
                        line = re.sub(r"\\move[^\\}]*", "", line)
                        line = re.sub(r"\\fad[^\\}]*", "", line)
                        line = re.sub(r"\\alpha[^\\}]*", "", line)
                        line = re.sub(r"\\bord[^\\}]*", "", line)
                        line = re.sub(r"\\shad[^\\}]*", "", line)
                        line = re.sub(r"\\fs[^\\}]*", "", line)
                        line = re.sub(r"\\c&[^\\}]*", "", line)
                        line = re.sub(r"\\t\([^\\}]*", "", line)
                        line = re.sub(r"\\[0-9]a[^\\}]*", "", line)
                        line = re.sub(r"\\[0-9]c[^\\}]*", "", line)
                        line = re.sub(r"\\an[0-7]", "", line)
                        line = line.replace(r"\}", "}")
                        line = line.replace("{}", "")
                        line = line.replace(r"\c)", "")
                        parts = line.split(",", 9)
                        parts[9] = r"{\be10}" + parts[9]
                        line = ",".join(parts)
                        parts = line.split(",", 9)
                    style = parts[3]
                    if (r"\pos" in line or r"\move" in line) and style not in remove:
                        if style != "Character Card":
                            parts[3] = "Signs"
                            if r"\move" in line:
                                continue
                        line = ",".join(parts)
                        line = re.sub(r"{[^}]*}", "", line)
                        parts = line.split(",", 9)
                    style = parts[3]
                    if r"\an8" in line and style == "Dialogue":
                        parts[3] = "Dialogue Top"
                        line = ",".join(parts)
                        line = line.replace(r"\an8", "")
                        line = line.replace("{}", "")
                        parts = line.split(",", 9)
                    style = parts[3]
                    if parts[9].startswith("Note:"):
                        parts[3] = "Signs"
                        line = ",".join(parts)
                    style = parts[3]
                    if (style == "Dialogue" and line.startswith("Comment: ") and "YZS " in content):
                        parts[3] = "Character Card"
                        line = ",".join(parts)
                        line = line.replace("Comment: ", "Dialogue: ")
                        parts = line.split(",", 9)
                    elif "YZS" in line:
                        continue
                    elif style in remove:
                        continue
                    elif style in rename:
                        style = rename[style]
                        parts[3] = style
                        line = ",".join(parts)
                    elif (
                        style.startswith("encoded by ")
                        or style.startswith("PrologueText")
                        or style.startswith("OPED")
                        or style.startswith("Hubuki - ")
                        or style.startswith("Conan Title")
                        or style.startswith("Opening")
                        or style.startswith("Ending")
                        or style.startswith("NextEpTitle")
                        or style.startswith("MAINTITLE")
                    ):
                        continue
                    if style in ["FlashbackThoughts", "FlashThoughts"]:
                        style = "Flashback Thoughts"
                        parts[3] = "Flashback Thoughts"
                        line = ",".join(parts)
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
                        line = re.sub(r"\\blur[^\\}]*", "", line)
                        line = re.sub(r"\\be[^\\}]*", "", line)
                        line = re.sub(r"\\pos[^\\}]*", "", line)
                        line = re.sub(r"\\frx[^\\}]*", "", line)
                        line = re.sub(r"\\fry[^\\}]*", "", line)
                        line = re.sub(r"\\frz[^\\}]*", "", line)
                        line = re.sub(r"\\xshad[^\\}]*", "", line)
                        line = re.sub(r"\\move[^\\}]*", "", line)
                        line = re.sub(r"\\fad[^\\}]*", "", line)
                        line = re.sub(r"\\alpha[^\\}]*", "", line)
                        line = re.sub(r"\\bord[^\\}]*", "", line)
                        line = re.sub(r"\\shad[^\\}]*", "", line)
                        line = re.sub(r"\\fs[^\\}]*", "", line)
                        line = re.sub(r"\\c&[^\\}]*", "", line)
                        line = re.sub(r"\\t\([^\\}]*", "", line)
                        line = re.sub(r"\\[0-9]a[^\\}]*", "", line)
                        line = re.sub(r"\\[0-9]c[^\\}]*", "", line)
                        line = re.sub(r"\\an[0-7]+", "", line)
                        line = line.replace(r"\}", "}")
                        line = line.replace("{}", "")
                        line = line.replace(r"\c)", "")
                        parts = line.split(",", 9)
                        parts[9] = r"{\be10}" + parts[9]
                        line = ",".join(parts)
                        parts = line.split(",", 9)
                    if (
                        style == "Dialogue"
                        or style == "Dialogue Top"
                        or style == "Signs"
                        or style == "Farewell Card"
                    ):
                        line = re.sub(r"\\blur[^\\}]*", "", line)
                        line = re.sub(r"\\be[^\\}]*", "", line)
                        line = re.sub(r"\\pos[^\\}]*", "", line)
                        line = re.sub(r"\\frx[^\\}]*", "", line)
                        line = re.sub(r"\\fry[^\\}]*", "", line)
                        line = re.sub(r"\\frz[^\\}]*", "", line)
                        line = re.sub(r"\\xshad[^\\}]*", "", line)
                        line = re.sub(r"\\move[^\\}]*", "", line)
                        line = re.sub(r"\\fad[^\\}]*", "", line)
                        line = re.sub(r"\\alpha[^\\}]*", "", line)
                        line = re.sub(r"\\bord[^\\}]*", "", line)
                        line = re.sub(r"\\shad[^\\}]*", "", line)
                        line = re.sub(r"\\fs[^\\}]*", "", line)
                        line = re.sub(r"\\c&[^\\}]*", "", line)
                        line = re.sub(r"\\t\([^\\}]*", "", line)
                        line = re.sub(r"\\[0-9]a[^\\}]*", "", line)
                        line = re.sub(r"\\[0-9]c[^\\}]*", "", line)
                        line = line.replace(r"\}", "}")
                        line = line.replace("{}", "")
                        line = line.replace(r"\c)", "")
                        parts = line.split(",", 9)
                    if r"\an8" in line and style == "Dialogue":
                        parts[3] = "Dialogue Top"
                        line = ",".join(parts)
                        line = line.replace(r"\an8", "")
                        line = line.replace("{}", "")
                        parts = line.split(",", 9)
                    else:
                        line = re.sub(r"\\an[0-7]+", "", line)
                        parts = line.split(",", 9)
                    if parts[9].startswith("Note:"):
                        parts[3] = "Signs"
                        line = ",".join(parts)
                    style = parts[3]
                    line = re.sub(
                        r"[.\s]{3,}$",
                        "...",
                        line.strip()
                        .replace("|", "!")
                        .replace("…", "...")
                        .replace("’", "'")
                        .replace("“", "")
                        .replace("”", "")
                        .replace("﻿", ""),
                    )
                    line = line.replace("…", "...")
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
                    parts[9] = re.sub(r"^\.([^\.])", r"\1", parts[9])
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                    line = re.sub(
                        r"[.\s]{3,}$",
                        "...",
                        line.strip()
                        .replace("|", "!")
                        .replace("…", "...")
                        .replace("’", "'")
                        .replace("“", "")
                        .replace("”", "")
                        .replace("﻿", ""),
                    )
                    line = line.replace(" !", "!")
                    line = line.replace("…", "...")
                    line = re.sub(r"  +", " ", line)
                    line = re.sub(r"^[lI1]-[lI1]", "I-I", line)
                    line = re.sub(r"^l(?=\w+)", "I", line)
                    line = re.sub(r"^lt", "It", line)
                    line = re.sub(r"\s+!", "!", line)
                    line = line.replace("-.", ".")
                    line = line.replace("-,", ",")
                    line = line.replace(r"\/V", "W")
                    line = line.replace(" ", " ")
                    line = line.strip()
                    line = line.replace(r" \N", r"\N")
                    line = line.replace(r" \N", r"\N")
                    line = line.replace(r"\N ", r"\N")
                    line = line.replace(r"\N ", r"\N")
                    parts = line.split(",", 9)
                    parts[9] = (
                        parts[9].replace(r"\N", "\n").strip().replace("\n", r"\N")
                    )
                    line = ",".join(parts)
                    while r",,\N" in line:
                        line = line.replace(r",,\N", ",,")
                    line = line.replace(r"\}", "}")
                    line = line.replace("}{", "")
                    line = line.replace("{}", "")
                    line = line.replace(r"\c)", "")
                    line = line.replace(r"\N}", "}")
                    line = line.replace(",, ", ",,")
                    line = line.strip()
                    line = line.replace("— ", r"—\h")
                    line = re.sub(r"—\\h$", "—", line)
                    line = line.strip()
                    parts = line.split(",", 9)
                    if group == "UTB":
                        parts[9] = re.sub(r"^,+", "", parts[9])
                        parts[9] = re.sub(r"\s*\\N\s*([a-z])", r" \1", parts[9])
                        parts[9] = re.sub(r"\s*,", ",", parts[9])
                        parts[9] = re.sub(r",,+", ",", parts[9])
                        parts[9] = re.sub(r",([a-z])", r", \1", parts[9])
                    parts[9] = re.sub(r"[,.]{3}", "...", parts[9])
                    parts[9] = parts[9].replace(" ,", ",")
                    parts[9] = parts[9].replace(r"{}", "")
                    parts[9] = parts[9].replace(r"{\N}", "")
                    parts[9] = re.sub(r"\.{3,}$", "...", parts[9])
                    parts[9] = parts[9].strip()
                    line = ",".join(parts)
                    if (
                        not re.sub(r"{[^}]*}", "", ",".join(parts[9:]))
                        .strip()
                        .strip("  .")
                        .strip()
                    ):
                        continue
                    if style == "Radio" and " over phone," in line:
                        line = (
                            ",".join(parts[:9])
                            + ","
                            + re.sub(r"^{", r"{\\an8", ",".join(parts[9:]))
                        )
                    if line.startswith("Comment: "):
                        continue
                    elif re.sub(r"Base\d+", "", style) == "":
                        style = "Dialogue"
                        parts[3] = style
                        line = ",".join(parts)
                        if r"\an8" in line and style == "Dialogue":
                            style = "Dialogue Top"
                            parts[3] = style
                            line = ",".join(parts)
                            line = line.replace(r"\an8", "")
                            line = line.replace("{}", "")
                            parts = line.split(",", 9)
                elif line.startswith("Style: "):
                    style = parts[0].split(": ")[1]
                    if style in remove:
                        continue
                    elif style in rename:
                        style = rename[style]
                        parts[0] = "Style: " + style
                        line = ",".join(parts)
                    elif style.startswith("title0") or style.startswith("Title0"):
                        style = "Signs"
                        parts[0] = "Style: " + style
                        line = ",".join(parts)
                    elif style.startswith("CharCard"):
                        style = "Character Card"
                        parts[0] = "Style: " + style
                        line = ",".join(parts)
                    elif re.sub(r"Base\d+", "", style) == "":
                        style = "Dialogue"
                        parts[0] = "Style: " + style
                        line = ",".join(parts)
                    elif (
                        style.startswith("encoded by ")
                        or style.startswith("PrologueText")
                        or style.startswith("OPED")
                        or style.startswith("Hubuki - ")
                        or style.startswith("Conan Title")
                        or style.startswith("Opening")
                        or style.startswith("Ending")
                        or style.startswith("NextEpTitle")
                        or style.startswith("MAINTITLE")
                    ):
                        continue
                    if style in seen:
                        continue
                    if style not in approved:
                        if style.startswith("Guest"):
                            style = "Character Card"
                            parts[0] = "Style: " + style
                            line = ",".join(parts)
                    seen.add(style)
                if skip_empty and not line:
                    continue
                out += line + "\n"
            if folder == "0001-0999" or folder == "Remastered":
                out = re.sub(r"\[Aegisub Project Garbage\][^\[]*", "", out, re.DOTALL)
                out = re.sub(r"\[Script Info\][^\[]*", "", out, re.DOTALL)
                hd_era = False
                if int(re.sub("[^0-9]", "", ep.split(" ")[0].split("-")[0])) > 453:
                    hd_era = True
                if hd_era:
                    out = (
                        "[Script Info]\nTitle: Detective Conan - "
                        + ep
                        + "\nTL Source: "
                        + group
                        + "\nScriptType: v4.00+\nWrapStyle: 3\nPlayResX: 1920\nPlayResY: 1080\nScaledBorderAndShadow: yes\nYCbCr Matrix: TV.601\n\n"
                        + out
                    )
                else:
                    out = (
                        "[Script Info]\nTitle: Detective Conan - "
                        + ep
                        + "\nTL Source: "
                        + group
                        + "\nScriptType: v4.00+\nWrapStyle: 3\nPlayResX: 1440\nPlayResY: 1080\nScaledBorderAndShadow: yes\nYCbCr Matrix: TV.601\n\n"
                        + out
                    )
                out2 = ""
                lines = out.splitlines()
                for line in lines:
                    line = line.rstrip()
                    if line.startswith("Style: "):
                        parts = line.split(",", 9)
                        style = parts[0].replace("Style: ", "")
                        if "," + style + "," not in out:
                            continue
                        elif style not in approved and style not in shown:
                            shown.add(style)
                            print(ep, "unknown", style)
                    out2 += line + "\n"
                out = out2
                styleres = "Style: Dialogue,FrancophilSans,74,&H00FFFFFF,&H00FFFFFF,&H00401311,&HC0313134,-1,0,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Dialogue Top,FrancophilSans,74,&H00FFFFFF,&H00FFFFFF,&H00401311,&HC0313134,-1,0,0,0,100,100,0,0,1,4,2.5,8,30,30,55,1\nStyle: Signs,FrancophilSans,74,&H14FFFFFF,&H00FFFFFF,&H46101010,&HC0313134,-1,0,0,0,100,100,0,0,1,4,2.5,8,30,30,55,1\nStyle: Thoughts,FrancophilSans,74,&H46360001,&H00FFFFFF,&H00FFFFFF,&HC0313134,-1,0,0,0,100,100,0,0,1,3,2.5,2,30,30,55,1\nStyle: Radio,FrancophilSans,74,&H00BEE1FF,&H00FFFFFF,&H000B2A42,&HC0313134,-1,0,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Narration,FrancophilSans,74,&H00FFFFFF,&H00FFFFFF,&H00BF6F00,&HC0313134,-1,0,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Narration Off,FrancophilSans,74,&H6E8C6F00,&H00FFFFFF,&H00FFFFFF,&HC0313134,-1,0,0,0,100,100,0,0,1,3,2.5,2,30,30,55,1\nStyle: Flashback,FrancophilSans,74,&H00CDFAFF,&H00FFFFFF,&H00373737,&HC0313134,-1,0,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Flashback Thoughts,FrancophilSans,74,&H46360001,&H00FFFFFF,&H00CCFFFF,&HC0313134,-1,0,0,0,100,100,0,0,1,3,2.5,2,30,30,55,1\nStyle: Honorifics - Dialogue,FrancophilSans,74,&H00FFFFFF,&H00FFFFFF,&H00401311,&HC0313134,-1,-1,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Honorifics - Signs,FrancophilSans,74,&H14FFFFFF,&H00FFFFFF,&H46101010,&HC0313134,-1,-1,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Honorifics - Thoughts,FrancophilSans,74,&H46360001,&H00FFFFFF,&H00FFFFFF,&HC0313134,-1,-1,0,0,100,100,0,0,1,3,2.5,2,30,30,55,1\nStyle: Honorifics - Radio,FrancophilSans,74,&H00BEE1FF,&H00FFFFFF,&H000B2A42,&HC0313134,-1,-1,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Honorifics - Narration,FrancophilSans,74,&H00FFFFFF,&H00FFFFFF,&H00BF6F00,&HC0313134,-1,-1,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Honorifics - Narration Off,FrancophilSans,74,&H6E8C6F00,&H00FFFFFF,&H00FFFFFF,&HC0313134,-1,-1,0,0,100,100,0,0,1,3,2.5,2,30,30,55,1\nStyle: Honorifics - Flashback,FrancophilSans,74,&H00CDFAFF,&H00FFFFFF,&H00373737,&HC0313134,-1,-1,0,0,100,100,0,0,1,4,2.5,2,30,30,55,1\nStyle: Honorifics - Flashback Thoughts,FrancophilSans,74,&H46360001,&H00FFFFFF,&H00CCFFFF,&HC0313134,-1,-1,0,0,100,100,0,0,1,3,2.5,2,30,30,55,1\nStyle: Masks,FrancophilSans,74,&H00000000,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,2,0,0,0,1\nStyle: Title,Conan Episode Title,74,&H00E1E4E3,&H000000FF,&HC8DBDAE1,&HC0000000,-1,0,0,0,100,100,0,0,1,1,0,5,0,0,0,1\nStyle: OPED,A-OTF Shin Go Pro M,63,&H14F3FCFE,&H000000FF,&H96171717,&H00141414,-1,0,0,0,100,100,0,0,1,0,0,2,0,0,65,1\nStyle: Eyecatch,Calibri,45,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,9,16,16,16,1\nStyle: Character Card,A-OTF Shin Go Pro B,63,&H0FFFFFFF,&H000000FF,&H00B46E0E,&H00000000,-1,0,0,0,90,100,0,0,1,3.4,0,2,90,90,45,1\nStyle: Farewell Card,Calibri,70,&H14DAEFEB,&H000000FF,&H46101010,&H641B1B1B,-1,0,0,0,100,100,0,0,1,0.5,0,2,90,90,80,1"
                for appr in approved:
                    out = re.sub(r"^Style: STYLEREMOVE,.*\s*", "", out.replace("Style: " + appr + ",", "Style: STYLEREMOVE,"))
                out = re.sub(r"Style: STYLEREMOVE,.*\n", "", out)
                out = out.replace("[V4+ Styles]", "[V4+ Styles]\n" + styleres)
                out = out.replace("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n", "")
                out = out.replace("[V4+ Styles]", "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding")
            out = out.replace("﻿", "").replace("‘", "'")
            out = out.replace("[Events]", "\n[Events]")
            out = out.replace("\n\n\n[Events]", "\n\n[Events]")
            with open("../subs/" + folder + "/" + ep + ".ass", "w") as fw:
                fw.write(out)
