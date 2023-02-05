import os


def pretty_size(size):
    prefixes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    
    steps = 0
    while size > 1023:
        size = size // 1024
        steps += 1
        
    return f'{size}{prefixes[steps]}'


files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(*[f'{f} {pretty_size(os.path.getsize(f))}' for f in files], sep='\n')