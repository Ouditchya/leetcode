class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)

        local_max = prices[0]
        local_min = prices[0]
        profit = 0
        for i in range(1, len_prices, 1):
            if prices[i] < prices[i-1]:
                profit += (local_max - local_min)
                # print("i = ", i, " local_min = ", local_min, " local_max = ", local_max, " profit = ", profit)
                local_max = prices[i]
                local_min = prices[i]

            if prices[i] > local_max:
                local_max = prices[i]

            if prices[i] < local_min:
                local_min = prices[i]
        
        if local_max >= local_min:
            profit += (local_max - local_min)

        return profit