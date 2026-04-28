class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        lo = 0
        max_len = 0

        for hi, char in enumerate(s):
            if char in char_map:
                lo = max(lo, char_map[char] + 1)
            
            char_map[char] = hi
            max_len = max(max_len, hi - lo + 1)
        
        return max_len