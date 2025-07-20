class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = [0] * n
        ans = []
        for num in nums: 
            cnt[num] += 1
            if cnt[num] > 1: ans.append(num)
        return ans