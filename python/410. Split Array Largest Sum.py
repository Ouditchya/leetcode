class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lb, ub = max(sum(nums)// k, max(nums)), sum(nums)

        def simulate(capacity):
            currSum, time = 0, 0
            for i in range(n):
                if currSum + nums[i] > capacity: currSum, time = nums[i], time + 1
                else: currSum += nums[i]
            return time+1

        def binarySearch(l, r):
            while l <= r:
                m = (l + r) // 2
                time = simulate(m)
                if time > k: l = m + 1
                else: r = m - 1
            return l

        return binarySearch(lb, ub)