class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n_candidates = len(candidates)
        candidates.sort()
        
        def solve(idx, tgt, temp):
            nonlocal n_candidates, target

            if tgt == 0:
                myset.append(temp[:])
                return

            if not (0 <= idx < n_candidates): return

            if candidates[idx] > tgt or tgt < 0: return

            for j in range(idx, n_candidates):
                temp.append(candidates[j])
                solve(j, tgt-candidates[j], temp)
                temp.pop() 

        myset = []
        solve(0, target, [])
        # print(myset)

        return myset