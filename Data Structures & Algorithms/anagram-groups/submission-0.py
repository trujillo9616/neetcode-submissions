class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings_by_code = {}

        for s in strs:
            code = "".join(sorted(s))

            if code in strings_by_code:
                strings_by_code[code].append(s)
            else:
                strings_by_code[code] = [s]
        
        return list(strings_by_code.values())