class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans, temp = '', ''
        for c in command:
            if c == 'G': ans += c
            elif c == ')':
                temp += c
                # print(temp)
                if temp == '()': ans += 'o'
                elif temp == '(al)': ans += 'al'
                else: ans += temp
                temp = ''
            else: temp += c
        return ans