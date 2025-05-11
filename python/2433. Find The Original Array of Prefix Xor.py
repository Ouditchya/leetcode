class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        if n == 1: return pref

        a, ans = 0, []
        for i in range(n):
            ans.append(a ^ pref[i])
            a = pref[i]
        return ans