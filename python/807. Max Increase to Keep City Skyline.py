class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]  # Transpose to get columns

        ans = 0
        for i in range(n):
            for j in range(n):
                allowed = min(row_max[i], col_max[j])
                ans += allowed - grid[i][j]

        return ans