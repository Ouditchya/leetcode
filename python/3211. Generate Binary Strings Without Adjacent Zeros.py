class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1: return ["0","1"]

        def solve(s):
            nonlocal n
            if len(s) > n: return
            elif len(s) == n: ans.append(s)
            elif s[-1] == "0": solve(s+"1")
            else:
                solve(s+"0")
                solve(s+"1")
        
        ans = []
        solve("0")
        solve("1")

        return ans