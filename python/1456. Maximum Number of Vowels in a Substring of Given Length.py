class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        def isVowel(c): return 1 if c in ["a", "e", "i", "o", "u"] else 0

        currWindow = 0
        for i in range(k): currWindow += isVowel(s[i])
        
        n, maxWindow = len(s), currWindow
        for i in range(k, n):
            currWindow += (isVowel(s[i]) - isVowel(s[i-k]))
            maxWindow = max(maxWindow, currWindow)
            if maxWindow == k: return maxWindow

        return maxWindow