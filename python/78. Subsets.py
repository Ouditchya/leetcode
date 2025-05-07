class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []

        def generateSubsets(ls, i):
            subsets.append(ls[:])
            for j in range(i, n): generateSubsets(ls + [nums[j]], j + 1)

        generateSubsets([], 0)

        return subsets