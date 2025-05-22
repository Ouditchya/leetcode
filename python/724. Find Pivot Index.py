class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans, n = -1, len(nums)
        prefixSum = [0, nums[0]]
        for i in range(1, n): prefixSum.append(prefixSum[i] + nums[i])
        # print(prefixSum)

        for i in range(1, n+1):
            if prefixSum[i-1] == prefixSum[n]-prefixSum[i]:
                ans = i-1
                break
        
        return ans