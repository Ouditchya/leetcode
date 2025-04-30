class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1.copy()
        i, j, k = 0, 0, 0

        while i < m and j < n:
            # print(nums1[i], nums2[j], i, j, k)
            if nums3[i] >= nums2[j]:
                nums1[k] = nums2[j]
                j, k = j+1, k+1
            elif nums3[i] < nums2[j]:
                nums1[k] = nums3[i]
                i, k = i+1, k+1
        
        while i != m:
            nums1[k] = nums3[i]
            i, k = i+1, k+1

        while j != n:
            nums1[k] = nums2[j]
            j, k = j+1, k+1

        # print(nums1)
        # print(nums2)
        # print(nums3)