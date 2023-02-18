import argparse


parser = argparse.ArgumentParser()
parser.add_argument("nums", nargs='*')
args = parser.parse_args()
nums = []
if len(args.nums) < 2:
    print('TOO FEW PARAMS')
elif len(args.nums) > 2:
    print('TOO MANY PARAMS')
else:
    try:
        nums = list(map(int, args.nums))
        print(sum(nums))
    except Exception as e:
        print(type(e).__name__)