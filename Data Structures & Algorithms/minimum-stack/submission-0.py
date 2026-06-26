class MinStack:

    def __init__(self):
        self.stack = []
        self.premin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.premin:
            self.premin.append(val)
        else:
            self.premin.append(min(val, self.premin[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.premin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.premin[-1]
