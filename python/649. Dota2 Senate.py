from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque()
        for s in senate: dq.append(s)

        while dq:
            if dq.count("D") == 0 and dq.count("R") > 0: return "Radiant"
            elif dq.count("R") == 0 and dq.count("D") > 0: return "Dire"

            s = dq.popleft()

            if s == "R":
                dq.remove("D")
                dq.append("R")
            elif s == "D": 
                dq.remove("R")
                dq.append("D")