class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = []
        for i in range(n-1):
            for j in range(i+1, n):
                if prices[j] <= prices[i]: break
            if prices[j] <= prices[i]: answer.append(prices[i] - prices[j])
            else: answer.append(prices[i])
        answer.append(prices[n-1])
        return answer