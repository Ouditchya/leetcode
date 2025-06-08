class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited, cells_tot = [[0 for _ in range(C)] for _ in range(R)], 2
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: cells_tot += 1
                elif grid[r][c] == 1: start = (r, c)
                elif grid[r][c] == 2: end = (r, c)
        # print(visited)
        # print(cells_tot, start, end)

        def solve(loc, cells, visited):
            nonlocal R, C, cells_tot, end, ans
            r, c = loc[0], loc[1] 
            
            if grid[r][c] == -1: return

            visited[r][c] = 1
            cells += 1

            if cells > cells_tot: return

            # print(path)

            if cells == cells_tot and grid[r][c] == 2: 
                ans += 1
                return

            for i in range(4):
                r1, c1 = r+change[i][0], c+change[i][1]
                if 0 <= r1 < R and 0 <= c1 < C and visited[r1][c1] == 0: 
                    # path.append((r1, c1))
                    solve((r1, c1), cells, visited)
                    # path.pop()
                    visited[r1][c1] = 0
            visited[r][c] = 0

        ans = 0
        change = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        solve(start, 0, visited)

        return ans