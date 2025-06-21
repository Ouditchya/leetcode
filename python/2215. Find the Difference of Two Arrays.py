class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ls1, ls2 = [0]*2001, [0]*2001
        for num in nums1: ls1[num+1000] = 1
        for num in nums2: ls2[num+1000] = 1

        a1, a2 = [], []
        for i in range(2001): 
            if ls1[i] > 0 and ls2[i] == 0: a1.append(i-1000)
            if ls2[i] > 0 and ls1[i] == 0: a2.append(i-1000)

        return [a1, a2]