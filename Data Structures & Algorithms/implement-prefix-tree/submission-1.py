class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            
            node = node[ch]
        
        node["*"] = True


    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        if not node:
            return False
        
        return True if node and self._is_end(node) else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return True if node is not None else False
        
    
    def search_prefix(self, prefix: str) -> dict | None:
        node = self.root

        for ch in prefix:
            if ch not in node:
                return None
            
            node = node[ch]
        
        return node

    def _is_end(self, node: dict) -> bool:
        return '*' in node and node['*'] == True
        
        