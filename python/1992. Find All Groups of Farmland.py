class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        # print(visited)

        def floodFill(r, c, ls):
            # Boundary condition
            if r == m or c == n or r == -1 or c == -1: return
            # Invalid condition
            if land[r][c] == 0 or visited[r][c] == 1: return

            # Make 1st choice
            visited[r][c] = 1
            # print(r, c)
            ls.append((r, c))
            
            # Make other choices
            floodFill(r+1, c, ls)
            floodFill(r-1, c, ls)
            floodFill(r, c+1, ls)
            floodFill(r, c-1, ls)
            
            # Revert 1st choice
            if ls:
                ls.sort()
                ans.append([ls[0][0], ls[0][1], ls[-1][0], ls[-1][1]])
            ls.clear()

        ans = []
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and land[i][j] == 1: floodFill(i, j, [])

        return ans