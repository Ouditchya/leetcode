class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        ans, ub = 0, (2*n)//3
        piles.sort(reverse = True)
        for i in range(1, ub, 2): ans += piles[i]
        return ans