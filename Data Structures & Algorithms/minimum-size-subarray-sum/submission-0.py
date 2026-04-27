class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = R = 0
        curSum = 0
        res = float('inf')

        for R, num in enumerate(nums):
            curSum += num

            while curSum >= target:
                res = min(res, R - L + 1)

                curSum -= nums[L]
                L += 1
        
        return res if res != float('inf') else 0