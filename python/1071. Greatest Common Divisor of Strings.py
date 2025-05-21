import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        if n1 > n2: 
            s1, s2 = str1, str2
            m1, m2 = n1, n2
        else: 
            s1, s2 = str2, str1
            m1, m2 = n2, n1

        c1, c2, c3 = [0]*26, [0]*26, [0]*26
        gcd = ''

        for i in range(m1): c1[ord(s1[i])-65] += 1
        for i in range(m2): c2[ord(s2[i])-65] += 1

        for i in range(26):
            if (c1[i] == 0 and c2[i] != 0) or (c1[i] != 0 and c2[i] == 0): return ""
            else: c3[i] = math.gcd(c1[i], c2[i])

        for i in range(m2):
            if c3[ord(s2[i])-65] == 0: continue
            gcd += s2[i]
            c3[ord(s2[i])-65] -= 1

        m3 = len(gcd)
        if m1 % m3 != 0 or m2 % m3 != 0: return ""
        
        if gcd*(m1//m3) != s1 or  gcd*(m2//m3) != s2: return ""

        return gcd