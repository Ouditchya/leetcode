class Solution:
    def countVowelStrings(self, n: int) -> int:
        m = n + 4
        return m*(m-1)*(m-2)*(m-3)//24