class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            currentNum = nums[mid]

            if currentNum == target:
                return mid
            
            elif currentNum < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1