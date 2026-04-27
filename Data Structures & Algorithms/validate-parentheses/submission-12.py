class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_opening = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        opening_brackets = closing_to_opening.values()
        stack = []

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
                continue
            
            if len(stack) == 0 or closing_to_opening[bracket] != stack.pop():
                return False
        
        return len(stack) == 0
                

            