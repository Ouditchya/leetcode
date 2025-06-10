class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for q in queries:
            x, y, r = q[0], q[1], q[2]
            cnt = 0
            for p in points:
                x1, y1 = p[0], p[1]
                if (x-x1)**2 + (y-y1)**2 <= r**2: cnt += 1
            ans.append(cnt)
        return ans