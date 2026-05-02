class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
        

    def isAlphaNum(self, char: str) -> bool:
        char_ord = ord(char.lower())

        return (
            ord('a') <= char_ord <= ord('z') or
            ord('0') <= char_ord <= ord('9')
        )
    
print(Solution().isAlphaNum('o'))