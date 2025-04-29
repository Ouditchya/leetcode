class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n, ls1, ls2, ls3 = len(nums), [], [], []
        for i in range(n):
            if nums[i] < pivot:
                ls1.append(nums[i])
            elif nums[i] == pivot:
                ls2.append(nums[i])
            else:
                ls3.append(nums[i])
        # print(ls1)
        # print(ls2)
        # print(ls3)
        ls1.extend(ls2)
        ls1.extend(ls3)
        return ls1