class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_by_code = defaultdict(list)

        for string in strs:
            code = "".join(sorted(string))
            string_by_code[code].append(string)
        
        return string_by_code.values()