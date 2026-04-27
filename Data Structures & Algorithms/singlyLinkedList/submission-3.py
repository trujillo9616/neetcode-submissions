class Node:
    def __init__(self, val: Optional[int] = None, nxt: Optional[Node] = None):
        self.val = val
        self.nxt = nxt


class LinkedList:
    
    def __init__(self):
        self.dummy = Node(-1)
        self.tail = self.dummy

    
    def get(self, index: int) -> int:
        curr = self.dummy.nxt

        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nxt
        return -1
        

    def insertHead(self, val: int) -> None:
        head = self.dummy.nxt
        new_head = Node(val, head)
        self.dummy.nxt = new_head

        if not new_head.nxt:
            self.tail = new_head


    def insertTail(self, val: int) -> None:
        self.tail.nxt = Node(val)
        self.tail = self.tail.nxt


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.dummy
        while i < index and curr:
            i += 1
            curr = curr.nxt
        
        if curr and curr.nxt:
            if curr.nxt == self.tail:
                self.tail = curr
            
            curr.nxt = curr.nxt.nxt
            return True
        return False


    def getValues(self) -> List[int]:
        res = []
        node = self.dummy.nxt
        
        while node:
            res.append(node.val)
            node = node.nxt

        return res

