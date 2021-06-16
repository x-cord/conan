import glob
import subprocess
from natsort import natsorted

files = glob.glob("../subs/**/*.ass")

for file in natsorted(files):
    out = subprocess.run(["prass", "sort", file, "--by", "time", "--by", "layer"], capture_output=True).stdout

    with open(file, "wb") as fw:
        fw.write(out)
