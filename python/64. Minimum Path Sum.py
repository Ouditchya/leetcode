class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        
        # Initialize
        dp[0][0] = grid[0][0]
        for i in range(1, r): dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, c): dp[0][j] = grid[0][j] + dp[0][j-1]

        # Build min path sum
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # print(dp)

        return dp[r-1][c-1]