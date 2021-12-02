with open("../input.txt") as f:
    l = list(map(int, f.readlines()))
    W = [l[i:i+3] for i in range(len(l))]
    p = 0
    for i in range(1, len(l)):
        if sum(W[i]) > sum(W[i-1]):
            p += 1
    print(p)

