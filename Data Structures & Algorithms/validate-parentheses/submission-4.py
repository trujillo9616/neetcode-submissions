class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_parenthesis = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        OPENING = matching_parenthesis.keys()

        for char in s:
            if char in OPENING:
                stack.append(char)
                continue
            
            if not stack or matching_parenthesis[stack.pop()] != char:
                return False
        
        return len(stack) == 0