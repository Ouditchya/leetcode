class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ctr = [0] * 100001
        for num in nums: ctr[num] += 1

        nums.sort()
        ub, ans = nums[-1], 0
        itr = nums[0]
        while itr <= ub:
            if ctr[itr] > 0:
                itr += k
                ans += 1
            itr += 1
        
        return ans