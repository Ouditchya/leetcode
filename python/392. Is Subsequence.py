class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_t = len(t)
        len_s = len(s)

        if len_s == 0:
            return True
        elif len_t == 0:
            return False

        j = 0
        for i in range(len_t):
            if t[i] == s[j]:
                # print("t[i] = ", t[i], " s[j] = ", s[j])
                j += 1
            if j == len_s:
                return True
        
        # print("j = ", j, " len_s = ", len_s)
        # if j == len_s:  

        return False