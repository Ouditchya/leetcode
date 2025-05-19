class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
    
        if root_x == root_y: return

        if self.size[root_x] >= self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        myset, mydict, disjointSet = set(), defaultdict(list), DisjointSet(n)
        
        for edge in edges: disjointSet.union(edge[0], edge[1])

        # print("parent: ", disjointSet.parent)
        # print("size: ", disjointSet.size)
        
        for edge in edges: 
            parent = disjointSet.parent[edge[0]]
            ls = mydict.get(parent, [0, 0])
            ls[0] = disjointSet.size[parent]
            ls[1] += 1
            mydict[parent] = ls
        # print("mydict: ", mydict)
        
        ans = 0
        for x in disjointSet.parent:
            if disjointSet.parent[x] == x and x not in myset: 
                myset.add(x)
                if mydict.get(x, [0, 0]) == [0, 0]: ans += 1
                else: 
                    ls = mydict.get(x, [0, 0])
                    node, edge = ls[0], ls[1]
                    if edge == node*(node-1)//2: ans += 1

        return ans