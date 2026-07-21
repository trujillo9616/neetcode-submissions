class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = set()
        j = 0

        for i, n in enumerate(nums):
            if i > k:
                my_set.remove(nums[j])
                j += 1
            
            if n in my_set:
                return True
            
            my_set.add(n)
        
        return False