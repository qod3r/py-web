import sys


args = sys.argv[1:]

lines = []
to_count = False
to_num = False
to_sort = False

while args:
    arg = args.pop(0)
    if arg == "--count":
        to_count = True
    elif arg == "--num":
        to_num = True
    elif arg == "--sort":
        to_sort = True
    else:
        file = arg
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print('ERROR')
        

if to_sort:
    lines = sorted(lines)
if to_num:
    for i in range(len(lines)):
        lines[i] = str(i) + " " + lines[i]
if to_count:
    lines.append(f"rows count: {len(lines)}")

print(''.join(lines))