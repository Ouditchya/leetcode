class Solution:
    def longestPalindrome(self, s: str) -> int:
        mydict = {}
        for x in s: mydict[x] = mydict.get(x, 0) + 1
        
        m, n = 0, 0
        for k, v in mydict.items():
            if v > 1:
                cnt = v//2
                v -= cnt*2
                n += cnt*2
            if v == 1: m = 1
        
        return m + n