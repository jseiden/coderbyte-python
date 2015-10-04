def MultiplicativePersistence(num):
    count = 0
    ls = list(str(num))
    while len(ls) > 1:
        n = reduce(lambda x,y: int(x) * int(y), ls)
        ls = list(str(n))
        num = str(n)
        count += 1
    return count

