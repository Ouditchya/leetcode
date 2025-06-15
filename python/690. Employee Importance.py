"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict, deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = defaultdict(list)
        for employee in employees: adj[employee.id] = [employee.importance, employee.subordinates]
        
        dq = deque()
        dq.append(adj[id])
        total_imp = 0

        while dq:
            curr = dq.popleft()
            total_imp += curr[0]
            for x in curr[1]: dq.append(adj[x])

        return total_imp