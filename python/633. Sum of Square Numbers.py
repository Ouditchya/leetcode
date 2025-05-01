import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        lb, ub = 0, int(math.sqrt(c-1))+1
        while True:
            val = lb**2 + ub**2
            # print(lb, ub, val)
            if val == c: return True
            elif val > c: ub -= 1
            elif val < c: lb += 1
            if lb > ub: break
        return False