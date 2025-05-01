class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ctr, n = 0, len(nums)
        for i in range(n):
            dg, val = 0, nums[i]
            while val != 0:
                val = val//10
                dg += 1
            if dg % 2 == 0:
                ctr += 1
            # print(nums[i], dg, ctr)    
        return ctr