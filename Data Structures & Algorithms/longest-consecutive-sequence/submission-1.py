class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr_len = 1

                while num + curr_len in numSet:
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len