class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y: return False
        elif self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        djs = DisjointSet(n)

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1: djs.union(i, j)

        myset = set()
        for x in range(n): myset.add(djs.find(x))
        # print(djs.parent)
        # print(myset)

        return len(myset)