class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        dgt1, dgt2 = num_str[0], num_str[0]
        for c in num_str:
            if c != "9":
                dgt1 = c
                break
        # print(int(num_str.replace(dgt1, "9")), int(num_str.replace(dgt2, "0")))
        return int(num_str.replace(dgt1, "9")) - int(num_str.replace(dgt2, "0"))