class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans, arr = [], []
        for idx in range(len(nums)): arr.append((nums[idx], idx))
        sorted_arr = sorted(arr, key = lambda x: x[0], reverse = True)[0:k]
        ans_arr = sorted(sorted_arr, key = lambda x: x[1])
        for (k, v) in ans_arr: ans.append(k)
        return ans