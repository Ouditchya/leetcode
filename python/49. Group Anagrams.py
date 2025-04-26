class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ls, d = [], {}

        for i in range(n):
            str1 = strs[i]
            str2 = ''.join(sorted(str1))
            d[str2] = []
            # print(str1, str2)

        for i in range(n):
            str1 = strs[i]
            str2 = ''.join(sorted(str1))
            d[str2].append(str1)
            # print(str1, str2)

        for v in d.values():
            ls.append(v)

        # print(d)
        # print(ls)

        return ls