class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        subsets = []

        def generateSubsets(ls, i):
            subsets.append(ls[:])
            for j in range(i, n): generateSubsets(ls + [nums[j]], j + 1)

        generateSubsets([], 0)
        # print(subsets)

        xorTotal, m = 0, len(subsets)
        for i in range(1, m):
            xorSum = subsets[i][0]
            for j in range(1, len(subsets[i])): xorSum ^= subsets[i][j]    
            xorTotal += xorSum
            # print("subset: ", subsets[i], " xorSum: ", xorSum, " xorTotal: ", xorTotal)

        return xorTotal