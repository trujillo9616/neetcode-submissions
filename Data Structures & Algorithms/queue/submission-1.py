class Node:
    def __init__(
        self,
        value: int = -1,
        prev: Optional[Node] = None,
        next: Optional[Node] = None
    ):
        self.value = value
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
    

    def append(self, value: int) -> None:
        last_node = self.tail.prev
        new_node = Node(value, prev=last_node, next=self.tail)
        last_node.next = new_node
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        first_node = self.head.next
        new_node = Node(value, prev=self.head, next=first_node)
        first_node.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last_node = self.tail.prev
        prev_node = last_node.prev
        self.tail.prev, prev_node.next = prev_node, self.tail

        return last_node.value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first_node = self.head.next
        next_node = first_node.next
        self.head.next, next_node.prev = next_node, self.head

        return first_node.value
        
