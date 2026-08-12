class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        left = 0
        min_length = float('inf')

        for right, num in enumerate(nums):
            current_sum += num

            while left <= right and current_sum >= target:
                min_length = min(min_length, right - left + 1)

                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0