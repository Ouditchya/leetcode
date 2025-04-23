class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        dp = [0] * 100001
        cost_max = 0
        for i in range(n):
            cost_max = max(cost_max, costs[i])
            dp[costs[i]] += 1
        ctr, costs_cum = 0, 0
        # print("dp init = ", dp[:cost_max])
        for i in range(cost_max+1):   
            while dp[i] > 0:
                if costs_cum >= coins:
                    break
                ctr += 1
                costs_cum += i
                dp[i] -= 1
            if costs_cum >= coins:
                break
        if costs_cum > coins:
            ctr -= 1
        # print("dp final = ", dp[:cost_max])
        # print("cumulative costs = ", costs_cum)
        return ctr