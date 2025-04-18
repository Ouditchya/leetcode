class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1 = max(z-x, x-z)
        p2 = max(z-y, y-z)
        if p1 == p2:
            return 0
        elif p1 > p2:
            return 2
        else:
            return 1