class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while n*n <= x: n += 1
        return n-1