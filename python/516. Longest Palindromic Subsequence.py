class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n, s1 = len(s), s[::-1]
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s1[j-1]: dp[i][j] = dp[i-1][j-1] + 1
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][n]