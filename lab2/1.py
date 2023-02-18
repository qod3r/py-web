import sys


args = sys.argv[1:]
kvs = []
to_sort = False
while args:
    arg = args.pop(0)
    if arg == "--sort":
        to_sort = True
    else:
        k, v = arg.split('=')
        kvs.append(f"Key: {k} Value: {v}")

if to_sort:
    kvs = sorted(kvs)
print('\n'.join(kvs))