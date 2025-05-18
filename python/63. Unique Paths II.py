class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]

        # Edge Case
        if obstacleGrid[0][0] == 1: return 0

        # Initialize
        dp[0][0] = 1
        for i in range(r): 
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for j in range(c): 
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1

        # Build paths
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1: dp[i][j] = 0
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # print(dp)

        return dp[r-1][c-1]