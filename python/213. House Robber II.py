class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        def solveHR(arr):
            m = len(arr)
            if m == 0: return 0
            if m == 1: return arr[0]
            
            dp = [arr[0]]
            dp.append(max(dp[0], arr[1]))
            
            for i in range(2, m): dp.append(max(dp[i-1], dp[i-2] + arr[i]))
            return dp[m-1]

        return max(solveHR(nums[:-1]), solveHR(nums[1:]))