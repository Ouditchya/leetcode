class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n, x, y = len(moves), 0, 0
        d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        for i in range(n):
            tup = d.get(moves[i], (0, 0))
            # print(tup)
            x, y = x + tup[0], y + tup[1]
            # print(x, y)
        return x == 0 and y == 0