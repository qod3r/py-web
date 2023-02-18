import argparse


parser = argparse.ArgumentParser()

parser.add_argument("file1")
parser.add_argument("file2")
parser.add_argument("--upper", action="store_true",
                    help="make the file uppercase")
parser.add_argument("--lines", help="only copy first N lines",
                    type=int)

args = parser.parse_args()

lines = []
with open(args.file1, 'r') as f:
    lines = f.readlines()

if args.upper:
    for i in range(len(lines)):
        lines[i] = str.upper(lines[i])

if args.lines is not None:
    lines = lines[:args.lines]

# print(''.join(lines))
with open(args.file2, 'w') as f:
    f.writelines(lines)