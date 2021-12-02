with open("../input.txt") as f:
    l = [(i.split()[0], int(i.split()[1])) for i in f.readlines()]
    h = d = a = 0
    for (c, v) in l:
        if c == "forward":
            h += v
            d += a * v
        elif c == "down":
            a += v
        else:
            a -= v
    print(h * d)
