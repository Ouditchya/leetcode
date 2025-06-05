class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxAmount = 0
        
        while l < r:
            currAmount = (r - l) * min(height[l], height[r])
            maxAmount = max(maxAmount, currAmount)
            if height[l] < height[r]: l += 1
            else: r -= 1
        
        return maxAmount