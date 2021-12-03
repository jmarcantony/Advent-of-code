def get_decimal(b):
    l, a = len(b), 0
    for c in b:
        l -= 1
        a += int(c) * (2 ** l)
    return a

def get_oxygen(c, n=0):
    if len(c) == 1:
        return c[0]
    temp = [x for x in c]
    p = [a[n] for a in c]
    m = "1" if p.count("1") > p.count("0") or p.count("1") == p.count("0") else "0"
    for x in c:
        if x[n] != m:
            temp.remove(x)
    return get_oxygen(temp, n+1)

def get_co2(c, n=0):
    if len(c) == 1:
        return c[0]
    temp = [x for x in c]
    p = [a[n] for a in c]
    m = "0" if p.count("1") > p.count("0") or p.count("1") == p.count("0") else "1"
    for x in c:
        if x[n] != m:
            temp.remove(x)
    return get_co2(temp, n+1)

with open("../input.txt") as f:
    l = [a.strip() for a in f.readlines()]
    o, c = get_decimal(get_oxygen(l)), get_decimal(get_co2(l))
    print(o * c)
