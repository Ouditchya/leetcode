class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, r, c = len(word), len(board), len(board[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        word_ctr = 0
        ans = False

        def check():
            if word_ctr == n: return True

        def solve(x, y):
            nonlocal word_ctr, ans

            if ans: return

            # Boundary Condition
            if x < 0 or x >= r or y < 0 or y >= c: return

            # Valid Visit Condition
            if visited[x][y] == 1: return

            # Search Condition
            if board[x][y] != word[word_ctr]: return

            visited[x][y] = 1
            word_ctr += 1
            
            if check(): 
                ans = True
                return

            solve(x, y+1)
            solve(x, y-1)
            solve(x+1, y)
            solve(x-1, y)

            visited[x][y] = 0
            word_ctr -= 1

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    solve(i, j)
                    if ans == True: return ans
                    word_ctr = 0

        return ans