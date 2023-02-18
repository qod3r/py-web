import argparse

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs='*')

args = parser.parse_args().args
if args:
    print(*args, sep='\n')
else:
    print('no args')
    