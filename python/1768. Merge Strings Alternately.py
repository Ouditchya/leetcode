class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        str1 = ''
        i, j = 0, 0

        for k in range(2*n):
            if i == n or j == m: break
            elif k % 2 == 0: 
                str1 += word1[i]
                i += 1
            else:
                str1 += word2[j]
                j += 1
        
        while i < n:
            str1 += word1[i]
            i += 1
        while j < m:
            str1 += word2[j]
            j += 1
        
        return str1