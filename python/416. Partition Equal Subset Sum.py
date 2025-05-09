class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, totalSum = len(nums), sum(nums)
        targetSum = totalSum// 2
        
        # Edge Cases
        if totalSum % 2 == 1 or n == 1: return False

        nums.sort()
        dp = [False]*(targetSum+1)
        dp[0] = True

        for num in nums:
            for i in range(targetSum, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
            # print(dp)

        return dp[targetSum]