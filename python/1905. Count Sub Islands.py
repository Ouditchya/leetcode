class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R, C = len(grid2), len(grid2[0])

        def dfs(r, c):
            nonlocal R, C, curr, flag, visited

            if r < 0 or r >= R or c < 0 or c >= C: return
            if visited[r][c] == 1: return
            if grid2[r][c] == 0: return

            curr += 1
            visited[r][c] = 1
            # print("(r, c): (", r, ", ", c, ") curr: ", curr)
            if grid1[r][c] == 0: flag = False

            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

            return True

        numIslands = 0
        visited = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid2[i][j] == 1 and visited[i][j] == 0:
                    flag, curr = True, 0
                    dfs(i, j)
                    if flag: numIslands += 1
        
        return numIslands