class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        d1, d2 = defaultdict(set), defaultdict(set)

        len_p = len(pattern)
        strs = s.split(" ")
        len_s = len(strs) 

        # print(strs)
        # print(len_p, len_s)

        if len_s != len_p:
            return False

        for i in range(len_p):
            d1[pattern[i]].add(strs[i])
            d2[strs[i]].add(pattern[i])
            if len(d1[pattern[i]]) > 1 or len(d2[strs[i]]) > 1:
                return False

        # print(d1)
        # print(d2)

        return True