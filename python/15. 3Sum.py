class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, myset = len(nums), set()
        nums.sort()
        # print("-------------------------------------------")
        # print(nums)
        # print("-------------------------------------------")
        for i in range(n-2):
            tgt = -1 * nums[i]
            left = i+1
            right = n-1
            # print("1: ", tgt, nums[left], nums[right])
            if left >= right:
                continue
            while left < right:
                s = nums[left] + nums[right]
                if s == tgt:
                    myset.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s > tgt:
                    right -= 1
                elif s < tgt:
                    left += 1
            #     print("2: ", tgt, nums[left], nums[right])
            # print("-------------------------------------------")
                
        return [list(triplet) for triplet in myset]