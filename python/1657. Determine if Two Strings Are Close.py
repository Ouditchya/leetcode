class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        
        h1, h2, s1, s2 = {}, {}, set(), set()
        for c in word1: 
            h1[c] = h1.get(c, 0) + 1
            s1.add(c)
        for c in word2: 
            h2[c] = h2.get(c, 0) + 1
            s2.add(c)

        if len(s1) != len(s2): return False

        for c in word1:
            if c not in h2.keys(): return False
        for c in word2:
            if c not in h1.keys(): return False

        ls1, ls2 = [], []
        for v in h1.values(): ls1.append(v)
        for v in h2.values(): ls2.append(v)
        ls1.sort()
        ls2.sort()

        return ls1 == ls2