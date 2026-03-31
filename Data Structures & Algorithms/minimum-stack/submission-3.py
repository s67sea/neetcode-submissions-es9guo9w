class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[-1],val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return None
        
        
