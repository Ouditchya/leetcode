class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for ls in accounts: ans = max(ans, sum(ls))
        return ans