class Node:
    def __init__(self, value: int, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        current_last_node = self.tail.prev
        new_last_node = Node(value, next=self.tail, prev=current_last_node)

        current_last_node.next = new_last_node
        self.tail.prev = new_last_node
        self.length += 1

    def appendleft(self, value: int) -> None:
        current_first_node = self.head.next
        new_first_node = Node(value, next=current_first_node, prev=self.head)

        current_first_node.prev = new_first_node
        self.head.next = new_first_node
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        deleted_node = self.tail.prev
        new_last_node = deleted_node.prev
        self.tail.prev = new_last_node
        new_last_node.next = self.tail
        self.length -= 1

        return deleted_node.value
    
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        deleted_node = self.head.next
        new_first_node = deleted_node.next
        self.head.next = new_first_node
        new_first_node.prev = self.head
        self.length -= 1

        return deleted_node.value
