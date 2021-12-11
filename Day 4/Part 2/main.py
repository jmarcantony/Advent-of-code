class Board:
    def __init__(self):
        self.grid = []
        self.marked = []
        self.won = False

    def add_row(self, l):
        self.grid.append(l)
    
    def mark(self, n):
        for i, r in enumerate(self.grid):
            for j, v in enumerate(r):
                if v == n:
                    self.marked.append([i, j])
        return self.check_win()
    
    def check_win(self):
        won = False
        i_count, j_count = [], []
        for p in self.marked:
            i, j = p
            i_count.append(i)
            j_count.append(j)
        for (i, j) in zip(i_count, j_count):
            if i_count.count(i) > 4:
                won = True
                break
            if j_count.count(j) > 4:
                won = True
                break
        if won:
            return self.get_sum()
        return won

    def get_sum(self):
        s = 0
        for i, r in enumerate(self.grid):
            for j, v in enumerate(r):
                if [i, j] not in self.marked:
                    s += v
        return s

with open("../input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    boards = []
    nums = [int(x) for x in lines[0].split(",")]
    i = 2
    while i < len(lines) - 2:
        b = Board()
        for _ in range(5):
            b.add_row([int(x.strip()) for x in lines[i].split()])
            i += 1
        i += 1
        boards.append(b)
    z = 0
    for n in nums:
        for i, board in enumerate(boards):
            if board.won:
                continue
            won = board.mark(n)
            if won:
                board.won = True
                z = won * n
    print(z)
