class Line: 
    def __init__(self, p1, p2):
        self.points = []
        self.p1 = p1
        self.p2 = p2
        self.get_points()

    def get_points(self):
        if self.p1[0] == self.p2[0]:
            a = 1 if self.p1[1] < self.p2[1] else -1
            i = self.p1[1]
            while i != self.p2[1]+a:
                self.points.append([self.p1[0], i])
                i += a
        else:
            a = 1 if self.p1[0] < self.p2[0] else -1
            i = self.p1[0]
            while i != self.p2[0]+a:
                self.points.append([i, self.p1[1]])
                i += a

    def greatest(self):
        return max(self.p1 + self.p2)

with open("../input.txt") as f:
    z = f.readlines()
    lines = []
    x = 0
    for y in z:
        a, b = y.split(" -> ")
        p1, p2 = list(map(int, a.split(","))), list(map(int, b.split(",")))
        l = Line(p1, p2)
        g = l.greatest()
        if g > x:
            x = g+1
        if (p1[0] == p2[0]) or (p1[1] == p2[1]):
            lines.append(l)
    graph = [[0 for _ in range(x)] for _ in range(x)]
    for t in lines:
        for u in t.points:
            graph[u[0]-1][u[1]-1] += 1
    n = 0
    for g in graph:
        for h in g:
            if h > 1:
                n += 1
    print(n)
