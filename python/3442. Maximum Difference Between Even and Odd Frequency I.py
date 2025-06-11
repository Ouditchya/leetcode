class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        hMap = [0]*26
        for c in s: hMap[ord(c)-ord("a")] += 1
        
        odd, even = [], []
        for v in hMap:
            if v == 0: continue
            elif v % 2 == 0: even.append(v)
            else: odd.append(v)

        maxDiff = -1000
        for o in odd:
            for e in even: maxDiff = max(maxDiff, o-e)

        return maxDiff