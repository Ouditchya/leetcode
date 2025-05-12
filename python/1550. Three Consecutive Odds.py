class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ctr, n = 0, len(arr)
        for i in range(n):
            if arr[i] % 2 != 0: ctr += 1
            else: ctr = 0
            if ctr == 3: return True
        return False