class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2: return abs(nums[0] - nums[1])
        
        def radix_sort(arr):
            exp, maxNum = 1, max(arr)

            while maxNum // exp > 0:
                count_sort_by_digit(arr, exp)
                exp *= 10

        def count_sort_by_digit(arr, exp):
            n = len(arr)
            temp, count = [0]*n, [0]*10

            for i in range(n):
                idx = (arr[i] // exp) % 10
                count[idx] += 1

            for i in range(1, 10): count[i] += count[i-1]

            for i in range(n-1, -1, -1):
                idx = (arr[i] // exp) % 10
                temp[count[idx]-1] = arr[i]
                count[idx] -= 1
            
            for i in range(n): arr[i] = temp[i]
        
        radix_sort(nums)

        n, maxSum = len(nums), 0
        for i in range(1, n): maxSum = max(maxSum, nums[i] - nums[i-1])

        return maxSum