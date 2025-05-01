class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, farthest = len(nums), 0
        for i in range(n):
            if i > farthest:
                return False  # i is unreachable
            farthest = max(farthest, i + nums[i])
        return True