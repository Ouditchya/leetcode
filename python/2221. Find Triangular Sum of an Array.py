class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ls, n = [], len(nums)
        for i in range(n-1):
            m = len(nums)
            for j in range(m-1): ls.append((nums[j]+nums[j+1])%10)
            # print(ls)
            nums = ls[:]
            ls.clear()
        return nums[0]