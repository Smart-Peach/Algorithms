class MinStack:

    def __init__(self):
        self.stack_min = []
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not len(self.stack_min) or val <= self.stack_min[-1]:
            self.stack_min.append(val)

    def pop(self) -> None:
        if self.data[-1] == self.stack_min[-1]:
            self.stack_min.pop(-1)
        self.data.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
