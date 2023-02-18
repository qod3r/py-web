import os, sys
from datetime import datetime
from zipfile import ZipFile


def make_reserve_arc(src, dest):
    lf = os.path.basename(os.path.normpath(src))
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{lf} {time}.zip"
    
    with ZipFile(os.path.join(dest, filename), 'w') as z:
        for currentdir, dirs, files in os.walk(src):
            for f in files:
                z.write(os.path.join(currentdir, f))


if __name__ == "__main__":
    src = sys.argv[1]
    dest = sys.argv[2]
    make_reserve_arc(src, dest)