class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls = [x for x in range(1, n+1)]
        
        idx_now = k-1
        while len(ls) != 1:
            ls.pop(idx_now)
            idx_next = (idx_now + k - 1) % len(ls)
            # print("idx_now: ", idx_now, " idx_next: ", idx_next, " ls: ", ls)
            idx_now = idx_next

        return ls[0] 