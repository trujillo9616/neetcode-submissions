class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        OPENING_BRACKETS = parenthesis_dict.values()

        sequence_stack = []

        for bracket in s:
            if bracket in OPENING_BRACKETS:
                sequence_stack.append(bracket)
            else:
                if not sequence_stack or parenthesis_dict[bracket] != sequence_stack[len(sequence_stack) - 1]:
                    return False
                sequence_stack.pop()
        
        return len(sequence_stack) == 0

