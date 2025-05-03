class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n, ls = len(nums), []
        nums.sort()
        for i in range(n):
            if nums[i] == target: ls.append(i)
        return ls