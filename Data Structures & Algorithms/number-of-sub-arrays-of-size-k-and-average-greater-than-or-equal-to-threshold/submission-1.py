class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = curSum = 0

        for i, num in enumerate(arr):
            curSum += num
            if i >= k - 1:
                res += curSum >= threshold
                curSum -= arr[i - k + 1]
            
        
        return res