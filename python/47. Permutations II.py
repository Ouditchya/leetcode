class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, visited = [], [0] * n

        def generatePermutations(ls, i):
            # Make 1st choice
            visited[i] = 1
            ls.append(nums[i])
            if len(ls) == n: 
                if ls[:] not in ans:
                    ans.append(ls[:])
            else:
                # Make all choices
                for j in range(n):
                    if visited[j] != 1:
                        generatePermutations(ls, j)
            # Backtrack 1st choice
            visited[i] = 0
            ls.pop()
            
        for i in range(n): generatePermutations([], i)

        return ans