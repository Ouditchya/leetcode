from collections import defaultdict, deque

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n, hMap, lMap = len(s1), defaultdict(set), {}
        for i in range(n):
            hMap[s1[i]].add(s2[i])
            hMap[s2[i]].add(s1[i])
        # print(hMap)

        dq = deque()
        for k, v in hMap.items():
            for c in v: dq.append(c)
            visited, currMin = [0]*26, 1000
            # print(dq)
            while dq:
                curr = dq.popleft()
                idx = ord(curr)-ord("a")
                visited[idx] = 1
                currMin = min(currMin, ord(curr))
                if hMap.get(curr, False):
                    for c1 in hMap.get(curr, False): 
                        idx1 = ord(c1)-ord("a")
                        if visited[idx1] == 0: dq.append(c1)
            lMap[k] = chr(currMin)
        # print(lMap)
        
        ans = ''
        for c in baseStr: ans += lMap.get(c, c)

        return ans