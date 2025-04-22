class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        expected = heights.copy()
        expected.sort()
        ctr = 0
        for i in range(n):
            if heights[i] != expected[i]:
                ctr += 1
        return ctr