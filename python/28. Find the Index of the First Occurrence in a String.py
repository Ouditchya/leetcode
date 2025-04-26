class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)

        if ln > lh:
            return -1
        
        flag = -1
        for i in range(lh):
            # print("needle = ", needle, " haystack[i:i+ln] = ", haystack[i:i+ln])
            if needle == haystack[i:i+ln]:
                flag = i
                break

        return flag