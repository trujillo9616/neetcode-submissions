class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        start = 0
        max_len = 0

        for end in range(n):
            current_char = s[end]

            while current_char in char_set:
                initial_char = s[start]
                char_set.remove(initial_char)
                start += 1
            
            char_set.add(current_char)
            max_len = max(max_len, end - start + 1)
        
        return max_len
