class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        nums_len = len(nums)
        nums1 = nums[nums_len-3:nums_len]

        val1 = functools.reduce(lambda x, y: x * y, nums1)
        val2 = nums[0] * nums[1] * nums[nums_len-1]
        return max(val1, val2)