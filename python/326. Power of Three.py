class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i, ls, ub = 0, [], 2**31

        while True:
            val = 3**i
            if val > ub:
                break
            i += 1
            ls.append(val)

        return n in ls