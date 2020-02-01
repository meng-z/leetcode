# Time Limit Exceeded
class SolutioN:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        
        for i, price in enumerate(prices):
            # cannot sell a stock before buying one
            if i == 0:
                continue
                
            diff = [price-prices[prev] for prev in range(i)]
            max_diff = max(diff)
            if max_profit < max_diff:
                max_profit = max_diff
                
        return max_profit
