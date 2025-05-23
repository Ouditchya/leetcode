class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        else:
            for i in range(3, n+1):
                ans = t0 + t1 + t2
                t0, t1, t2 = t1, t2, ans
            return t2