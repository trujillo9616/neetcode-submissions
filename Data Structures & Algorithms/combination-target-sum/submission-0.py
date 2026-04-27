class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            current.append(nums[i])
            total += nums[i]

            # Try again with same num
            dfs(i, current, total)

            # Backtrack
            current.pop()
            total -= nums[i]

            # Continue with following nums
            dfs(i+1, current, total)
        
        dfs(0, [], 0)
        return res

