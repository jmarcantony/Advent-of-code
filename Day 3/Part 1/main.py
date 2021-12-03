def get_decimal(b):
    l, a = len(b), 0
    for c in b:
        l -= 1
        a += int(c) * (2 ** l)
    return a

with open("../input.txt") as f:
    a = [a.strip() for a in  f.readlines()]
    m = len(a[0])
    g = e = ""
    for i in range(m):
        c = []
        for j in a:
            c.append(j[i])
        if c.count("1") > c.count("0"):
            g += "1"
            e += "0"
        else:
            g += "0"
            e += "1"
    g, e = get_decimal(g), get_decimal(e)
    print(g * e)
