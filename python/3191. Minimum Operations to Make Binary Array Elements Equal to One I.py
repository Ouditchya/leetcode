class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops, n = 0, len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                ops += 1
            # print(nums)
        return -1 if sum(nums) != n else ops