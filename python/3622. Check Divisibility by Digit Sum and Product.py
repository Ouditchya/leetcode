class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m, ds, dp = n, 0, 1
        while m:
            d = m % 10
            ds += d
            dp *= d
            m = m // 10
        # print(ds, dp)
        # print(n % (ds + dp))
        return (not (n % (ds + dp)))