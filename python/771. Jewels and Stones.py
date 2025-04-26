class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ctr, n, m, d = 0, len(jewels), len(stones), {}
        for i in range(n):
            d[jewels[i]] = 1
        for i in range(m):
            ctr += d.get(stones[i], 0)
        return ctr