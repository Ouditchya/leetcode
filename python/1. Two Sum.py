class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        len_list = len(nums)
        for i in range(len_list):
            # if nums[i] > target:
            #     continue
            my_dict[nums[i]] = []
        
        for i in range(len_list):
            # if nums[i] > target:
            #     continue
            my_dict[nums[i]].append(i)
        # print(my_dict)
        # print("\n")

        for k in my_dict.keys():
            if my_dict.get(target - k, 0):
                # print(k, my_dict.get(target - k, 0))
                if k == (target - k) and len(my_dict[target - k]) > 1:
                    return [my_dict[k][0], my_dict[target - k][1]]
                elif k != (target - k):
                    return [my_dict[k][0], my_dict[target - k][0]]