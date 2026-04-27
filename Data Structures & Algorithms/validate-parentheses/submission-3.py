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
            
            elif len(stack) == 0:
                return False
            
            else:
                opening = stack.pop()
                if matching_parenthesis[opening] != char:
                    return False
        
        return len(stack) == 0