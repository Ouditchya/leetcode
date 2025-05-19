class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ctr, arr = 0, [0]*20002
        
        for num in nums: arr[num+10000] += 1
        
        for i in range(20001, -1, -1):
            ctr += arr[i]
            if ctr >= k: return i-10000