class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        opening_brackets = bracket_dict.keys()

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            
            elif len(stack) == 0 or bracket != bracket_dict[stack.pop()]:
                return False
        
        return len(stack) == 0