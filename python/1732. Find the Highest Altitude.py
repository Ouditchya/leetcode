class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt, n, cum_sum = 0, len(gain), 0
        for i in range(n):
            cum_sum += gain[i]
            max_alt = max(max_alt, cum_sum)
        return max_alt