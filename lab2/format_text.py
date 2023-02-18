def format_text_block(h, w, fname):
    text = []
    res = ''
    try:
        with open(fname, 'r') as f:
            text = f.readlines()
    except Exception as e:
        return str(e)

    count = 0
    for line in text[:h]:
        blocks = [line[i:i+w] for i in range(0, len(line), w)]
        count += len(blocks)
        cutoff = len(blocks)
        if len(blocks) > 1 and blocks[-1] == '\n':
            blocks = blocks[:-1]
        
        if count > h:
            cutoff = count - h
        for b in blocks[:cutoff]:
            if b == '\n':
                res += b
            else:
                res += b + '\n'
        if count > h:
            break
    
    return res
