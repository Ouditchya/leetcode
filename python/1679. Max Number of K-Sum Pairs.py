class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashMap = {}
        for num in nums: hashMap[num] = hashMap.get(num, 0) + 1
        
        ans = 0
        for key in hashMap.keys(): 
            if key == k - key:
                val = hashMap[key]//2
                hashMap[key] -= val
                ans += val
            else:
                val = min(hashMap[key], hashMap.get(k - key, 0))
                if val > 0:
                    hashMap[key] -= val
                    hashMap[k - key] -= val
                    ans += val

        return ans