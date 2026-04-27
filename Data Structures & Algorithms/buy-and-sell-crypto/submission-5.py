class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_profit = 0

        for current_price in prices[1:]:
            if current_price < lowest_price:
                lowest_price = current_price
            
            else:
                best_profit = max(best_profit, current_price - lowest_price)
            
        return best_profit