class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0]*(5001)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1): dp[i] += dp[i - coin]
        # print(dp[:amount+1])

        return dp[amount]