class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in num_hash:
                return [num_hash[diff], i]
            
            num_hash[num] = i
        
        return [-1, -1]