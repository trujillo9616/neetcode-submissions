class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, n - 1
            while j < k:
                triplet = [nums[i], nums[j], nums[k]]
                curr = sum(triplet)

                if curr > 0:
                    k -= 1
                elif curr < 0:
                    j += 1
                
                else:
                    res.append(triplet)
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        
        return res