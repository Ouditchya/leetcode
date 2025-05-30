class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def checkNary(x, n):
            s = ''
            while x:
                d = x % n
                s += str(d)
                x //= n
            return s == s[::-1]
        
        for i in range(2, n-1):
            if not checkNary(n, i): return False
        return True