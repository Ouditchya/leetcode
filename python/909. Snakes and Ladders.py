from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        n = len(board) 
        movesLikeJagger = n**2
        flatten, visited = [0], [0]*(n**2+1)
        for i in range(n):
            if i % 2 == 0: 
                for j in range(n): flatten.append(board[i][j])
            else: 
                for j in range(n-1, -1, -1): flatten.append(board[i][j])        
        # print(flatten)

        dq = deque()
        dq.append((1, 0)) # cell, move
        visited[1] = 1

        while dq:
            currCell, moves = dq.popleft()
            if currCell == n**2: movesLikeJagger = min(movesLikeJagger, moves)

            for i in range(1, 7):
                idx = currCell + i
                
                if idx > n**2: break
                
                if visited[idx] == 1: continue
                else: visited[idx] = 1
                
                if flatten[idx] != -1: nextCell = flatten[idx]
                else: nextCell = idx
                
                dq.append((nextCell, moves+1))
        
        return movesLikeJagger if movesLikeJagger < n**2 else -1