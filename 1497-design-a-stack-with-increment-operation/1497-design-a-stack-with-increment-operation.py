class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [None] * maxSize
        self.maxSize = maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top == self.maxSize - 1:
            return 
        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    def increment(self, k: int, val: int) -> None:
        limit = k if k <= self.top + 1 else self.top + 1
        for i in range(limit):
            self.stack[i] += val