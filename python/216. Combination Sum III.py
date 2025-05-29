class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45: return []

        def solve(idx, tgt, ls):
            if tgt == 0 and len(ls) == k:
                ans.append(ls[:])
                return

            if len(ls) > k or tgt < 0: return

            for i in range(idx, 10):
                ls.append(i)
                solve(i+1, tgt-i, ls)
                ls.pop()

        ans = []
        solve(1, n, [])
        # print(ans)

        return ans