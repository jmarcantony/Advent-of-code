with open("../input.txt") as f:
    p = 0
    l = list(map(int, f.readlines()))
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            p += 1
    print(p)
