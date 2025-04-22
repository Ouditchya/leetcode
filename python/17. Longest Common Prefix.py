class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        my_dict = {}
        len_strs = len(strs)

        for i in range(len_strs):
            len_str = len(strs[i])
            # print(strs[i])
            for j in range(len_str+1):
                str1 = strs[i][0:j]
                my_dict[str1] = my_dict.get(str1, 0) + 1
        #         print(str1)
        #     print("------------------------------------")

        # print(my_dict)

        max_prefix = 0
        for k, v in my_dict.items():
            if v == len_strs:
                max_prefix = k

        return max_prefix