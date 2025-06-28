class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        i, s1 = 0, ['']*n
        for idx in indices: 
            s1[idx] = s[i]
            i += 1
        return ''.join(s1) 