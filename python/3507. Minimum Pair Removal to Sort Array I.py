class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:  
        ops = 0
        while True:
            min_sum = 1000000
            pos = -1
            len_nums = len(nums)

            check = 0
            for i in range(1, len_nums, 1):
                if nums[i] < nums[i-1]:
                    check = 1
            if check == 0:
                break

            for i in range(1, len_nums, 1):
                curr_sum = nums[i] + nums[i-1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    pos = i
            if pos == -1:
                break
            else:
                nums.pop(pos)
                nums.pop(pos-1)
                nums.insert(pos-1, min_sum)
                ops += 1

            # print(ops, pos, min_sum)
            # print(nums)

        return ops