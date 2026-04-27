class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique_nums = set()
        L = 0

        for R, num in enumerate(nums):
            if R - L > k:
                unique_nums.remove(nums[L])
                L += 1
            
            if nums[R] in unique_nums:
                return True
            
            unique_nums.add(nums[R])
        
        return False