class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums, ans, visited = [], [], [0] * n
        for i in range(n): nums.append(i+1)
        # print(nums)

        def generateCombinations(ls, i):
            # Make 1st choice
            visited[i] = 1
            ls.append(nums[i])
            if len(ls) == k: ans.append(ls[:])
            else:
                # Make all choices
                for j in range(i+1, n):
                    if visited[j] != 1:
                        generateCombinations(ls, j)
            # Backtrack 1st choice
            visited[i] = 0
            ls.pop()
            
        for i in range(n): generateCombinations([], i)

        return ans