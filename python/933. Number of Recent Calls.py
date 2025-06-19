from collections import deque

class RecentCounter:

    def __init__(self):
        self.dq = deque()
        return None

    def ping(self, t: int) -> int:
        self.dq.append(t)
        while self.dq:
            left = self.dq.popleft()
            if (t-3000) <= left:
                self.dq.appendleft(left)
                break
        return len(self.dq)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)