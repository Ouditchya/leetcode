class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_p = len(prices)
        
        if len_p == 1:
            return 0
        
        prices_min = 1000000
        profit_max = 0
        for i in range(len_p):
            if prices[i] < prices_min:
                prices_min = prices[i]
            profit_max = max(profit_max, prices[i] - prices_min)

        if profit_max <= 0:
            return 0
        else:
            return profit_max