class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(idx, tgt, ls):
            nonlocal n

            if tgt < 0: return

            if tgt == 0:
                mytup = tuple(x for x in ls[:])
                ans.add(mytup)
                return

            prev = -1
            for i in range(idx, n):
                if prev == candidates[i]: continue
                ls.append(candidates[i])
                solve(i+1, tgt-candidates[i], ls)
                ls.pop()
                prev = candidates[i]

        candidates.sort()
        n, ans = len(candidates), set()
        solve(0, target, [])
        # print(ans)

        return [list(x) for x in ans]