import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        len_points = len(points)

        for i in range(len_points):
            v1 = points[i]
            for j in range(i+1, len_points):
                v2 = points[j]
                # a = math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)
                for k in range(j+1, len_points):
                    v3 = points[k]
                    # b = math.sqrt((v1[0] - v3[0])**2 + (v1[1] - v3[1])**2)
                    # c = math.sqrt((v3[0] - v2[0])**2 + (v3[1] - v2[1])**2)
                    # s = (a + b + c)/ 2
                    # area = math.sqrt(s*(s-a)*(s-b)*(s-c))
                    area = abs(v1[0]*(v2[1]-v3[1]) + v2[0]*(v3[1]-v1[1]) + v3[0]*(v1[1]-v2[1]))/ 2
                    max_area = max(area, max_area)

        return max_area 