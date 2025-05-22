class Solution:
    def compress(self, chars: List[str]) -> int:
        ctr, ans, n = 1, [], len(chars)
        
        # Loop for chars in list
        for i in range(n):
            if i > 0 and chars[i] == chars[i-1]: ctr += 1
            elif i > 0 and chars[i] != chars[i-1]:
                ans.append(chars[i-1])
                if ctr > 1: 
                    s_ctr = str(ctr)
                    for j in range(len(s_ctr)): ans.append(s_ctr[j])
                ctr = 1
        
        # Account for last character
        ans.append(chars[n-1])
        if ctr > 1: 
            s_ctr = str(ctr)
            for j in range(len(s_ctr)): ans.append(s_ctr[j])

        chars[:] = ans
        # print("ans: ", ans, " chars: ", chars)

        return len(ans)