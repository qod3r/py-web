import os
from pretty_size import pretty_size


files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(*[f'{f} {pretty_size(os.path.getsize(f))}' for f in files], sep='\n')