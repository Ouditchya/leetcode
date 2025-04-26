class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        sum = 0
        for i in range(1, n):
            sum += abs(ord(s[i]) - ord(s[i-1]))
        return sum