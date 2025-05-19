class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = 2**31-1
        
        # Edge Case
        if amount == 0: return 0

        # Initialize DP array
        dp = [0]*(10001)
        for i in range(n): 
            if coins[i] <= 10000: dp[coins[i]] = 1

        def solve(x):
            if x < 0: return INF
            if x == 0: return 0
            if dp[x] != 0: return dp[x]
            
            minCnt = INF
            for coin in coins:
                minCnt = min(minCnt, solve(x-coin)+1)
            dp[x] = minCnt
            
            return minCnt

        ans = solve(amount)
        # print(dp)    

        return ans if ans != INF else -1
