class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize variables
        min_buy_price = prices[0]
        max_profit = 0

        for price in prices:
            min_buy_price = min(min_buy_price, price)
            max_profit = max(max_profit, price - min_buy_price)
        
        return max_profit
        