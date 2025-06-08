class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        n, maxBOR = len(nums), 0
        for i in range(n): maxBOR |= nums[i]
        
        def solve(idx, curBOR, ls, visited):
            nonlocal n, maxBOR, ans
            
            visited[idx] = 1
            ls.append(nums[idx])
            curBOR = curBOR | nums[idx]
            # print("Curr: ", nums[idx], " ls: ", ls, " curBOR: ", curBOR)
            # print("Visited: ", visited)
            if curBOR == maxBOR: ans += 1

            for i in range(idx, n):
                if visited[i] != 1:
                    solve(i, curBOR, ls, visited)
                    ls.pop()
                    visited[i] = 0
        
        ans = 0
        for j in range(n): solve(j, 0, [], [0]*n)

        return ans