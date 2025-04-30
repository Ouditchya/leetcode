class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * 3

        for i in range(n):
            arr[nums[i]] += 1

        j = 0
        for i in range(3):
            while arr[i] != 0:
                arr[i] -= 1
                nums[j] = i
                j += 1

        print(nums)