class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0 or val <= self.getMin():
            self.minStack.append(val)
        
        return None

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.getMin():
            self.minStack.pop()
        
        return val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
