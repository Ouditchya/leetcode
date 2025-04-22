class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(0, n, 2):
            max_sum += nums[i]
        # print(nums)
        return max_sum