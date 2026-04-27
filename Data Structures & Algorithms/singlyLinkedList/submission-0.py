class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        current_node = self.head.nxt
        i = 0
        while current_node:
            if i == index:
                return current_node.val
            
            current_node = current_node.nxt
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.nxt)
        self.head.nxt = new_node
        self.size += 1

        if not new_node.nxt:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.nxt = Node(val)
        self.tail = self.tail.nxt
        self.size += 1

    def remove(self, index: int) -> bool:
        i = 0
        current_node = self.head

        while i < index and current_node:
            i += 1
            current_node = current_node.nxt
        
        if current_node and current_node.nxt:
            if current_node.nxt == self.tail:
                self.tail = current_node
            current_node.nxt = current_node.nxt.nxt
            return True
        
        return False

    def getValues(self) -> List[int]:
        res = []
        current_node = self.head.nxt
        while current_node:
            res.append(current_node.val)
            current_node = current_node.nxt
        
        return res

        
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt