from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict, col_dict = defaultdict(tuple), defaultdict(tuple)
        R, C = len(grid), len(grid[0])
        
        # Build row dict
        for i in range(R):
            mytup = tuple(x for x in grid[i])
            row_dict[mytup] = row_dict.get(mytup, 0) + 1
        
        # Build col dict
        for i in range(C):
            mytup = tuple(grid[r][i] for r in range(R))
            col_dict[mytup] = col_dict.get(mytup, 0) + 1
        
        # print(row_dict)
        # print(col_dict)

        n = 0
        for k, v in row_dict.items():
            if k in col_dict.keys(): n += row_dict[k]*col_dict[k]

        return n