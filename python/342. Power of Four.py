class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i, ls, ub = 0, [], 2**31

        while True:
            val = 4**i
            if val > ub:
                break
            i += 1
            ls.append(val)

        return n in ls