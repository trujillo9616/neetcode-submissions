class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2
            current_num = nums[mid]

            if current_num == target:
                return mid
            
            if current_num < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return -1