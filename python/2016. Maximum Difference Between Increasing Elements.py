class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefixMin = min(10**9+1, nums[0])
        maxDiff = -10**9
        for i in range(1, len(nums)):
            # print("maxDiff: ", maxDiff, " prefixMin: ", prefixMin)
            maxDiff = max(maxDiff, nums[i]-prefixMin)
            prefixMin = min(prefixMin, nums[i])
        return maxDiff if maxDiff > 0 else -1