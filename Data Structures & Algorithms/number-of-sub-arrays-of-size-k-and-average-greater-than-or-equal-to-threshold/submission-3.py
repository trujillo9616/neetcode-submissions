class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = current_sum = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            if i >= k - 1:
                res += current_sum >= threshold
                current_sum -= arr[i - k + 1]

        return res