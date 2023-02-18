import os, sys
from pprint import pprint
from pretty_size import pretty_size

def sizesum(path, filelist):
    s = 0
    for f in filelist:
        s += os.path.getsize(os.path.join(path, f))
    
    return s


sizes = {}
pathoffset = len(sys.argv[1].split('/')) - 1
i = 0
for currentdir, dirs, files in os.walk(sys.argv[1]):
    # print(currentdir, dirs, files)
    
    # if len(currentdir.split('/')) == pathoffset:
    if i == 0:
        for f in files:
            # print(f)
            sizes[f] = sizesum(currentdir, [f])
        i += 1
    else:
        if currentdir.split('/')[pathoffset] not in sizes:
            sizes[currentdir.split('/')[pathoffset]] = 0
        else:
            sizes[currentdir.split('/')[pathoffset]] += sizesum(currentdir, files)


res = sorted(sizes.items(), key=lambda x: x[1])[:-11:-1]
maxlen = len(max(res, key=lambda x: len(x[0]))[0])
for line in res:
    # print(line)
    print(line[0], end='')
    print(" "*(maxlen - len(line[0])), " -", pretty_size(line[1]))