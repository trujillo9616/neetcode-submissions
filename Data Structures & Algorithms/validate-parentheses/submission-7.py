class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        def stackIsEmpty() -> bool:
            return len(stack) == 0

        opening_brackets = list(bracket_map.keys())

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            
            elif stackIsEmpty() or bracket_map[stack.pop()] != bracket:
                return False
    
        return stackIsEmpty()
    