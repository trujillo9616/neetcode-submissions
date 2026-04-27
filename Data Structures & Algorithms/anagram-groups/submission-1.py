class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_by_code = {}

        for string in strs:
            code = "".join(sorted(string))

            if code not in string_by_code:
                string_by_code[code] = []
            
            string_by_code[code].append(string)
        
        return string_by_code.values()