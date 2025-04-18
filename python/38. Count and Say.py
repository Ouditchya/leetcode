class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        
        ls = ["0", "1", "11"]

        for i in range(3, n+1):
            str1 = ls[i-1]
            str1_len = len(str1)
            str2 = ''
            cnt = 1
            for j in range(1, str1_len):
                if str1[j] == str1[j-1]:
                    cnt += 1
                else:
                    str2 = str2 + str(cnt) + str1[j-1]
                    cnt = 1
            str2 = str2 + str(cnt) + str1[j]
            ls.append(str2)    

        # print(ls)

        return ls[n]