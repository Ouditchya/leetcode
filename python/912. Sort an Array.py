class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp, ln = [0] * 50001, [0] * 50001
        fn = 0
        p_max, n_max = 0, 100000
        for i in range(n):
            if nums[i] >= 0:
                lp[nums[i]] += 1
            else:
                ln[-1 * nums[i]] += 1
                fn = 1
            p_max, n_max = max(p_max, nums[i]), min(n_max, nums[i])

        k = 0
        if fn == 1:
            for i in range(-1*n_max, 0, -1):
                while ln[i] != 0:
                    nums[k] = -1 * i
                    k += 1
                    ln[i] -= 1
        for i in range(0, p_max+1):
            while lp[i] != 0:
                nums[k] = i
                k += 1
                lp[i] -= 1
        # print(p_max, n_max)

        return nums