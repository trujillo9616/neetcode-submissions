class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_to_close = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        for char in s:
            if char in open_to_close.keys():
                stack.append(char)
                continue
            
            if len(stack) == 0 or char != open_to_close[stack.pop()]:
                return False
        
        return len(stack) == 0
