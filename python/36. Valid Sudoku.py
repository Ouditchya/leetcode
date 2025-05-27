class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            hashMap = {}
            for x in board[i]: 
                hashMap[x] = hashMap.get(x, 0) + 1
                if hashMap[x] > 1 and x != '.': return False
        
        # Check columns
        for i in range(9):
            hashMap = {}
            for r in range(9): 
                hashMap[board[r][i]] = hashMap.get(board[r][i], 0) + 1
                if hashMap[board[r][i]] > 1 and board[r][i] != '.': return False

        # Check 3x3
        grid = [
            [(0, 3), (0, 3)], [(0, 3), (3, 6)], [(0, 3), (6, 9)],
            [(3, 6), (0, 3)], [(3, 6), (3, 6)], [(3, 6), (6, 9)],
            [(6, 9), (0, 3)], [(6, 9), (3, 6)], [(6, 9), (6, 9)]
        ]
        for i in range(9):
            r_lb, r_ub = grid[i][0][0], grid[i][0][1]
            c_lb, c_ub = grid[i][1][0], grid[i][1][1]
            hashMap = {}
            for i in range(r_lb, r_ub):
                for j in range(c_lb, c_ub):
                    hashMap[board[i][j]] = hashMap.get(board[i][j], 0) + 1
                    if hashMap[board[i][j]] > 1 and board[i][j] != '.': return False

        return True