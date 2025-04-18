class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            str1 = str(x*-1)
            str2 = '-' + str1[::-1]
            y = int(str1[::-1])
        else:
            str1 = str(x)
            str2 = str1[::-1]
            y = int(str2)
        bits = 0
        while y > 0:
            y = y >> 1
            bits += 1
        print(str2, bits)
        if bits >= 32:
            return 0
        else:
            return int(str2)