class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        runningSum = sum(nums[:k])
        maxSum = runningSum
        
        for i in range(k, n):
            runningSum += (nums[i] - nums[i-k])
            maxSum = max(maxSum, runningSum)

        return maxSum/k