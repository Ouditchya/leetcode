class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subsets = []

        def generateSubsets(ls, i):
            # ls.sort()
            if ls not in subsets: subsets.append(ls[:])
            for j in range(i, n): generateSubsets(ls + [nums[j]], j + 1)

        generateSubsets([], 0)

        return subsets