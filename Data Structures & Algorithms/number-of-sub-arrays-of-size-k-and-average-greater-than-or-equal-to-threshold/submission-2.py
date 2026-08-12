class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = 0
        i = 0
        res = 0

        for j in range(len(arr)):
            current_sum += arr[j]

            if j >= k:
                current_sum -= arr[i]
                i += 1

            if j >= k - 1 and current_sum/k >= threshold:
                res += 1

        return res