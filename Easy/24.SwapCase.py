def SwapCase(str):
    res = []
    for l in list(str):
        if l == l.upper():
            res.append(l.lower())
        else:
            res.append(l.upper())
    return ''.join(res)
