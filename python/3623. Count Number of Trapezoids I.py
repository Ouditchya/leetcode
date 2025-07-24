from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        N = 10**9+7
        hm, pairs = defaultdict(set), []
        for point in points: hm[point[1]].add(point[0])
        for k, v in hm.items(): pairs.append((len(v)*(len(v)-1))//2)

        n, s, ss = len(pairs), sum(pairs), 0
        for i in range(n): ss = (ss + pairs[i]*pairs[i]) 
        ans = ((s*s - ss)//2) % N
        return ans