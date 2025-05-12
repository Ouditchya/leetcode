class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n, m = len(s), len(spaces)
        str1, j = '', 0
        for i in range(n):
            if j < m:
                if spaces[j] == i: 
                    str1 += ' '
                    j += 1
            str1 += s[i]
        return str1