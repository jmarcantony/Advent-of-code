with open("../input.txt") as f:
    l = [(i.split()[0], int(i.split()[1])) for i in f.readlines()]
    h, d = 0, 0
    for (c, v) in l:
        if c == "forward":
            h += v
        elif c == "down":
            d += v
        else:
            d -= v
    print(h * d)
