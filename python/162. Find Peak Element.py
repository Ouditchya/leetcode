class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def peakSearch(arr, left, right, n) -> int:
            mid = (left + right)//2
            while mid >= 0 and mid < n:
                if mid == 0 and arr[mid] > arr[mid+1]: return mid
                if mid == n-1 and arr[mid] > arr[mid-1]: return mid
                if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]: return mid
                if arr[mid] < arr[mid+1]: mid += 1
                elif arr[mid] < arr[mid-1]: mid -= 1
            return mid

        n = len(nums)
        if n == 1: return 0
        else: return peakSearch(nums, 0, n-1, n)