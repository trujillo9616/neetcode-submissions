class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            current_num = nums[mid]
            
            if current_num > target:
                right = mid - 1
            elif current_num < target:
                left = mid + 1
            else:
                return mid
        return -1