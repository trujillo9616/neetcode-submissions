class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start_price = prices[0]
        max_profit = -float('inf')

        for price in prices[1:]:
            if price < start_price:
                start_price = price
            else:
                current_profit = price - start_price
                max_profit = max(max_profit, current_profit)
        
        return max_profit if max_profit != -float('inf') else 0