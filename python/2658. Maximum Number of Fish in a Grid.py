class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal R, C, curr

            if r < 0 or r >= R or c < 0 or c >= C: return
            if visited[r][c] == 1: return
            if grid[r][c] == 0: return

            curr += grid[r][c]
            visited[r][c] = 1

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

        maxFish = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0:
                    visited = [[0 for _ in range(C)] for _ in range(R)]
                    curr = 0
                    dfs(i, j)
                    maxFish = max(maxFish, curr)
        
        return maxFish