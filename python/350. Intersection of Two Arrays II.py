class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interset, ls, ls2, n, m = [], [0] * 1001, [0] * 1001, len(nums1), len(nums2)
        for i in range(n): ls[nums1[i]] += 1
        for i in range(m): ls2[nums2[i]] += 1
        for i in range(1001): 
            if ls[i] > 0 and ls2[i] > 0: 
                for j in range(min(ls[i], ls2[i])): interset.append(i)
        return interset