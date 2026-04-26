class MinStack:    
    def __init__(self):
        self.stack = []
        self.minIndexes = [0]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minIndexes:
            self.minIndexes = [0]
        elif self.stack[self.minIndexes[-1]] > val:
            self.minIndexes.append(len(self.stack) - 1)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) - 1 < self.minIndexes[-1]:
            self.minIndexes.pop()
                
    def top(self) -> int:     
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minIndexes[-1]]