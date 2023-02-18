import os, sys
from pprint import pprint
import json
from zipfile import ZipFile


if __name__ == "__main__":
    fname = sys.argv[1]
    data = []
    with ZipFile(fname, 'r') as z:
        for file in z.namelist():
            if file[-5:] == ".json":
                with z.open(file) as f:
                    data.append(json.load(f))
    data = [item for sublist in data for item in sublist]
    filtered = [r for r in data if r['city']=='Moscow']
    print(f"{len(filtered)} people")
    pprint(filtered, sort_dicts=False)