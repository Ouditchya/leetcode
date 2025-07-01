class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums: hashMap[num] = hashMap.get(num, 0) + 1
        
        ans = 0
        for k, v1 in hashMap.items():
            v2 = hashMap.get(k+1, 0)
            if v2 > 0: ans = max(ans, v1+v2)
        
        return ans