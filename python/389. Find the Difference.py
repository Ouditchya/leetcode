class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)
        if n == 0:
            return t
        
        d1, d2 = {}, {}
        for i in range(n):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        d2[t[n]] = d2.get(t[n], 0) + 1

        # print(d1)
        # print(d2)

        for i in range(n+1):
            if d2[t[i]] != d1.get(t[i], 0):
                return t[i]
        return None