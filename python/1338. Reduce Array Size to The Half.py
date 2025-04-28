class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d, n = {}, len(arr)

        for i in range(n):
            d[arr[i]] = d.get(arr[i], 0) + 1
        
        ls = [v for v in d.values()]
        ls.sort()
        ctr, cumSum, m, lm = 0, 0, len(ls), n//2
        for i in range(m-1, -1, -1):
            cumSum += ls[i]
            ctr += 1
            if cumSum >= lm:
                break
        # print(d)
        # print(ls)
        # print(cumSum)
        return ctr