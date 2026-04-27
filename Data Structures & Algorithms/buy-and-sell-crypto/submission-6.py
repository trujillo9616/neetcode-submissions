class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = prices[0]
        max_profit = 0

        for current_price in prices:
            if current_price < min_buy_price:
                min_buy_price = current_price
            
            else:
                max_profit = max(max_profit, current_price - min_buy_price)
        
        return max_profit
