def pretty_size(size):
    prefixes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    
    steps = 0
    while size > 1023:
        size = size / 1024
        steps += 1
        
    return f'{round(size)}{prefixes[steps]}'