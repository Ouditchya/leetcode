class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        p, n = 0, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]: p += 1
        return p