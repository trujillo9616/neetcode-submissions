class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            current_word = strs[i]
            j = 0

            while j < min(len(prefix), len(current_word)):
                if prefix[j] != current_word[j]:
                    break
                
                j += 1
            
            prefix = prefix[:j]
        
        return prefix

                