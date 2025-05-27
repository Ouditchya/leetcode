class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal R, C, curr, visited

            if r < 0 or r >= R or c < 0 or c >= C: return
            if visited[r][c] == 1: return
            if grid[r][c] == "0": return

            curr += 1
            visited[r][c] = 1

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

            return True

        numIslands = 0
        visited = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    curr = 0
                    if dfs(i, j): numIslands += 1
        
        return numIslands