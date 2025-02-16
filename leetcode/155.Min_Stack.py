class MinStack:

    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.history) > 0:
            self.history.append(min(self.history[-1], val))
        else:
            self.history.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.history.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.history[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
