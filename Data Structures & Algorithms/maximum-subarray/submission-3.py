class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0

        for num in nums:
            curSum = max(0, curSum)
            curSum += num
            maxSum = max(maxSum, curSum)
        
        return maxSum