class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_freq = Counter(s)

        for char in t:
            if char not in word_freq:
                return False
            
            word_freq[char] -= 1

            if word_freq[char] == 0:
                del word_freq[char]

        return len(word_freq) == 0
