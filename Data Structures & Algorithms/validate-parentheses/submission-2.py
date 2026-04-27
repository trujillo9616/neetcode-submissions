class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        OPENING_BRACKETS = matching_bracket_dict.values()

        sequence_stack = []

        for current_bracket in s:
            if current_bracket in OPENING_BRACKETS:
                sequence_stack.append(current_bracket)
                continue

            if not sequence_stack or matching_bracket_dict[current_bracket] != sequence_stack.pop():
                return False

            # last_opening_bracket = sequence_stack.pop()
            # if matching_bracket_dict[current_bracket] != last_opening_bracket:
            #     return False

        return len(sequence_stack) == 0

