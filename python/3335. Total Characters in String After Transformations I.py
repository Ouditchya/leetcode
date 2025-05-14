class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ls, temp, n = [0] * 26, [0] * 26, len(s)
        INT_MAX = 10**9+7
        for i in range(n): ls[ord(s[i])-97] += 1
        
        for i in range(t):
            temp = ls.copy()
            for j in range(26):    
                if j == 25 and temp[25] > 0: 
                    ls[0] += temp[25] 
                    ls[1] += temp[25]
                    ls[25] -= temp[25] 
                elif temp[j] > 0: 
                    ls[j] -= temp[j]
                    ls[j+1] += temp[j]
            # print(temp)
            # print(ls, "\n---------------------------------------")

        return sum(ls) % INT_MAX