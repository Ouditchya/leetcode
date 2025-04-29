class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n, ls = len(nums), [nums[0]]
        for i in range(1, n):
            ls.append(ls[i-1] + nums[i])
        return ls