class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, n - 1

                while j < k:
                    current = [nums[i], nums[j], nums[k]]
                    current_sum = sum(current)

                    if current_sum == 0:
                        res.append(current)
                        j += 1
                        k -= 1

                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                    
                    elif current_sum < 0:
                        j += 1
                    else:
                        k -= 1

        return res