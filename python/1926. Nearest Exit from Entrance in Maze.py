from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        visited = [[0 for _ in range(C)] for _ in range(R)]
        
        dq = deque()
        dq.append((entrance[0], entrance[1], 0))
        ans = 1000000

        while dq:
            r, c, steps = dq.popleft()

            if (r == 0 or r == R-1 or c == 0 or c == C-1) and (r, c) != (entrance[0], entrance[1]): 
                ans = min(ans, steps)
                break
            else:
                delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for d in delta:
                    r1, c1 = r+d[0], c+d[1]
                    if (0 <= r1 < R and 0 <= c1 < C) and maze[r1][c1] == "." and visited[r1][c1] == 0: 
                        visited[r1][c1] = 1
                        dq.append((r1, c1, steps+1))
                        # visited[r1][c1] = 0

        return ans if ans != 1000000 else -1