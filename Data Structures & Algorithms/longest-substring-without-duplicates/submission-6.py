class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in char_hash:
                l = max(char_hash[s[r]] + 1, l)
            
            char_hash[s[r]] = r
            res = max(res, r - l + 1)
        
        return res