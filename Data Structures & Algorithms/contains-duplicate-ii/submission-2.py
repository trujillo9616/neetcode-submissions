class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_in_window = set()
        j = 0

        for i in range(len(nums)):
            if nums[i] in nums_in_window:
                return True
            
            nums_in_window.add(nums[i])

            if len(nums_in_window) > k:
                nums_in_window.remove(nums[j])
                j += 1
        
        return False
