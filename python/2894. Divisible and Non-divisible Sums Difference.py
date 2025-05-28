class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = list(range(n+1))
        num2 = [x for x in range(m, n+1, m)]
        return sum(num1) - 2*sum(num2)