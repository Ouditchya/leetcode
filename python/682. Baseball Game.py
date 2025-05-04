class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        stack = []

        for i in range(n):
            if operations[i] == 'C': stack.pop()
            elif operations[i] == 'D': 
                v1 = stack[-1]
                stack.append(v1*2)
            elif operations[i] == '+':
                v1, v2 = stack[-1], stack[-2]
                stack.append(v1+v2)
            else: stack.append(int(operations[i]))

        return sum(stack)