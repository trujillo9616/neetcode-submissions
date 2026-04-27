class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        opening_brackets = list(bracket_map.keys())

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            
            elif len(stack) == 0 or bracket_map[stack.pop()] != bracket:
                return False
    
        return len(stack) == 0