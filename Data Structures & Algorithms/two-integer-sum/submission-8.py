class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in num_hash:
                return [num_hash[diff], i]
            
            num_hash[n] = i
        
        return [0, 0]