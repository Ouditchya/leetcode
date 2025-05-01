class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 1: return 0
        
        ctr, l, r = 0, 0, n-1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] >= target: r -= 1
            else: ctr, l = ctr + (r - l), l+1

        return ctr