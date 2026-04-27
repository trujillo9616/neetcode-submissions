class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.next_idx = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.next_idx == self.capacity:
            self.resize()
        
        self.arr[self.next_idx] = n
        self.next_idx += 1

    def popback(self) -> int:
        n = self.arr[self.next_idx - 1]
        self.arr[self.next_idx - 1] = None
        self.next_idx -= 1
        return n
 

    def resize(self) -> None:
        self.arr += [None] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.next_idx
    
    def getCapacity(self) -> int:
        return self.capacity
