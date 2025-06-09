class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(s):
            num_str, num = s, int(s)
            if num > n: return
            elif len(num_str) == 1: ans.append(num)

            for i in range(10):
                num_str, num = s+str(i), int(s+str(i))
                if num > n: return
                ans.append(num)
                dfs(num_str)

        ans = []
        for i in range(1, 10): dfs(str(i))

        return ans