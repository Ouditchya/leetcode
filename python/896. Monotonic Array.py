class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        def checkMonotonic(arr, start, end):
            c1, c2 = 1, 1
            for i in range(start+1, end):
                if arr[i] >= arr[i-1]:
                    c1 += 1
                if arr[i] <= arr[i-1]:
                    c2 += 1
            # print(c1, c2)     
            return c1 == n or c2 == n 

        return checkMonotonic(nums, 0, n)