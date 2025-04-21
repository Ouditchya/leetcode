class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        len_emails = len(emails)
        my_dict = {}

        for i in range(len_emails):
            str1 = emails[i]
            len_str1 = len(str1)
            str2 = ''
            flag = 0
            for j in range(len_str1):
                if str1[j] == '.' and flag != 2:
                    continue
                if str1[j] == '+' and flag != 2:
                    flag = 1
                if str1[j] == '@':
                    flag = 2
                if flag != 1:
                    str2 += str1[j]
            # print("str2 = ", str2)
            my_dict[str2] = 1
        
        # print("my_dict = ", my_dict)

        return len(my_dict.keys())