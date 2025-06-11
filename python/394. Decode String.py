class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_cnt, stack_char = [], []
        cache_int = ""
        for c in s:
            if 0 <= ord(c) - ord("0") <= 9: cache_int += c
            
            elif c == "[":
                if len(cache_int) > 0:
                    stack_cnt.append(int(cache_int))
                    cache_int = ""
                stack_char.append(c)
            
            elif c == "]":
                cache_char = ""
                while stack_char[-1] != "[":
                    cache_char = stack_char[-1] + cache_char
                    stack_char.pop()
                stack_char.pop()
                
                cache_char *= stack_cnt[-1]
                stack_cnt.pop()

                stack_char.append(cache_char)

            else: stack_char.append(c)

        # print(stack_char)
        # print(stack_cnt)

        return "".join(x for x in stack_char)