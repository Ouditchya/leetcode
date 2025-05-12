from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n

        dq = deque()
        dq.append(0)

        while dq:
            key = dq.popleft()
            visited[key] = 1

            for i in rooms[key]:
                if visited[i] == 0: dq.append(i)
        
        # print(visited)

        return sum(visited) == n