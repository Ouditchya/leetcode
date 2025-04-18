class Solution:
    def isValid(self, s: str) -> bool:
        str_len = len(s)
        s1 = s
        s2 = ''
        para = ['(', '[', '{', '}', ']', ')']

        if str_len % 2 == 1:
            return False

        if s1[-1] == '(' or s1[-1] == '[' or s1[-1] == '{':
            return False

        my_dict = {}
        for i in para:
            my_dict[i] = 0
        for i in range(str_len):
            my_dict[s1[i]] += 1
        
        if (my_dict['('] != my_dict[')']) or (my_dict['['] != my_dict[']']) or (my_dict['{'] != my_dict['}']):
            return False
        print(my_dict)

        j = -1 
        for i in range(str_len-1,-1,-1):
            if (len(s1) == 0):
                break
            if (s1[i] == '(' or s1[i] == '[' or s1[i] == '{') and len(s2) == 0:
                break
            if (s1[i] == ']') or (s1[i] == ')') or (s1[i] == '}'):
                s2 = s2 + s1[i]
                s1 = s1[:-1]
                j += 1
            elif (s1[i] == '[' and s2[j] == ']') or (s1[i] == '(' and s2[j] == ')') or (s1[i] == '{' and s2[j] == '}'):
                s2 = s2[:-1]
                s1 = s1[:-1]
                j -= 1
            # print(i, j, s1, s2)
        
        return len(s1) == 0