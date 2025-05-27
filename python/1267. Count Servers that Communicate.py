from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        adjR, adjC = defaultdict(list), defaultdict(list)
        
        for i in range(R): adjR[i].extend([x for x in grid[i]])
        for i in range(C): adjC[i].extend([grid[r][i] for r in range(R)])

        # print(adjR)
        # print(adjC) 

        myset = set()
        for r, v in adjR.items():
            if sum(v) > 1:
                for j in range(len(v)): 
                    if v[j] == 1: myset.add((r, j))
        for c, v in adjC.items():
            if sum(v) > 1:
                for i in range(len(v)): 
                    if v[i] == 1: myset.add((i, c))
        # print(myset)
        
        return len(myset)