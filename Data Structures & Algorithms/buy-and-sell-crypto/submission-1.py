class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_difference = 0
        start = 0

        for end in range(len(prices)):
            if prices[start] > prices[end]:
                start = end
                next
            
            current_difference = prices[end] - prices[start]
            max_difference = max(max_difference, current_difference)

        return max_difference

        
        