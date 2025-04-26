class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)
        ctr = 0
        for i in range(n):
            if operations[i][0] == '+' or operations[i][2] == '+':
                ctr += 1
            else:
                ctr -= 1
        return ctr