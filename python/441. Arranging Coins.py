class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, ls = 1, []
        while True:
            num = (i*(i+1))/2
            if num > n: break
            ls.append(num)
            i += 1
        return i-1