class MinStack:

    def __init__(self):
        self.main = []
        self.mins = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if self.mins:
            self.mins.append(min(val,self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.main.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.mins[-1]
