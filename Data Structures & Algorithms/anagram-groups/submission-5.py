class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity -> O(n)
        # space complexity -> O(n)
        res, strs_hash = [], defaultdict(list)

        for s in strs:
            strs_hash[str(sorted(s))].append(s)
        
        return list(strs_hash.values())
    