class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_freq = {}

        for char in s:
            char_freq[char] = 1 + char_freq.get(char, 0)

        for char in t:
            if char not in char_freq:
                return False
            
            char_freq[char] -= 1

            if char_freq[char] == 0:
                del char_freq[char]
        
        return len(char_freq) == 0