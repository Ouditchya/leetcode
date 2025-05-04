class MinStack:

    def __init__(self):
        self.stack = []
        self.stackTop = -1
        self.minstack = []
        self.minstackTop = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackTop += 1
        if self.minstackTop == -1:
            self.minstack.append(val)
            self.minstackTop += 1
        elif self.minstack[-1] >= val:
            self.minstack.append(val)
            self.minstackTop += 1

    def pop(self) -> None:
        if self.stackTop == -1: return None
        val = self.stack[self.stackTop]
        self.stack.pop()
        self.stackTop -= 1
        if self.minstack[self.minstackTop] == val:
            self.minstack.pop()
            self.minstackTop -= 1
        return val

    def top(self) -> int:
        if self.stackTop == -1: return None
        return self.stack[self.stackTop]

    def getMin(self) -> int:
        if self.minstackTop == -1: return None
        return self.minstack[self.minstackTop]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()