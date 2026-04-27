class DoublyNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.first, self.last = DoublyNode(0,0), DoublyNode(0,0)
        self.first.next, self.last.prev = self.last, self.first

    def _remove_node(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert_node(self, node):
        prev, nxt = self.last.prev, self.last
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self._remove_node(self.cache[key])
        self._insert_node(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
        
        self.cache[key] = DoublyNode(key, value)
        self._insert_node(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.first.next
            self._remove_node(lru)
            del self.cache[lru.key]