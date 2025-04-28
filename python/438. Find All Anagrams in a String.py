class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, ds, dp = [], {}, {}
        ns, np = len(s), len(p)

        for i in range(np):
            dp[p[i]] = dp.get(p[i], 0) + 1
        
        # print(dp, "\n-----------------------------------")
        for i in range(ns-np+1):
            if i == 0:
                for j in range(i, i+np, 1):
                    ds[s[j]] = ds.get(s[j], 0) + 1
            else:
                ds[s[i+np-1]] = ds.get(s[i+np-1], 0) + 1
            # print("1: ", ds)
            
            if dp == ds:
                ls.append(i)
            ds[s[i]] -= 1
            if ds[s[i]] == 0:
                del ds[s[i]]
            # print("2: ", ds, "\n-----------------------------------")

        return ls