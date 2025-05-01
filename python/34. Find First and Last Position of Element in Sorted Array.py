class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(arr, left, right, val) -> int:
            while left <= right:
                mid = (left + right)// 2
                if arr[mid] == val: return mid
                if arr[mid] > val: right = mid - 1    
                else: left = mid + 1      
            return left
        
        n = len(nums)
        idx = binarySearch(nums, 0, n-1, target)
        # print(idx)

        if idx < 0 or idx >= n:
            return [-1, -1]
        if nums[idx] != target:
            return [-1, -1]
        
        lb, ub = idx, idx
        while lb >= 0 and lb < n and nums[lb] == target: lb -= 1
        while ub >= 0 and ub < n and nums[ub] == target: ub += 1

        return [lb+1, ub-1]