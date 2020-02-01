'''
Runtime: 60 ms, faster than 83.33% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 90.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # special case
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        lowest = prices[0]
        
        for price in prices:
            # whether update the lowest price
            if price < lowest:
                lowest = price
            diff = price - lowest
            if diff > max_profit:
                max_profit = diff
                
        return max_profit
