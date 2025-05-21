class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)

        l, r = 0, n-1
        while s[l] == " ": l += 1
        while s[r] == " ": r -= 1

        s1 = ''
        for i in range(l, r+1):
            if i > l and s[i] == s[i-1] and s[i] == " ": continue
            s1 += s[i]
        
        # print("l: ", l, " r: ", r)
        # print("s: ", s, " len(s): ", len(s))
        # print("s1: ", s1, " len(s1): ", len(s1))

        return " ".join(s1.split()[::-1])