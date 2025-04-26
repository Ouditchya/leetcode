class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False
        else:
            s1 = ''.join(sorted(s))
            t1 = ''.join(sorted(t))
            return s1 == t1