class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans, c, n = 1, 1, len(word)
        for i in range(1, n): 
            if word[i] == word[i-1]: c += 1
            elif word[i] != word[i-1] and c > 1: 
                ans += (c - 1)
                c = 1
            else: c = 1
        if c > 1: ans += (c - 1)
        return ans  