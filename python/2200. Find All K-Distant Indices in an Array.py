class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n, arr_idx = len(nums), []
        for i in range(n):
            if nums[i] == key: arr_idx.append(i)

        ans = []
        for i in range(n):
            for j in range(len(arr_idx)):
                if abs(i-arr_idx[j]) <= k: 
                    ans.append(i)
                    break
        
        return ans