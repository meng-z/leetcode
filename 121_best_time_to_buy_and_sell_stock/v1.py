import numpy as np

# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        np_prices = np.array(prices)
        n = len(prices)
        max_profit = 0
        
        for i, np_price in enumerate(np_prices):
            # cannot sell a stock before buying one
            tmp = [np_price if j <= i else 0 for j in range(n)]
            curr = np.array(tmp)
            diff = curr - np_prices
            candidate_idx = np.argsort(diff)[-1]

            if candidate_idx < i and max_profit < diff[candidate_idx]:
                max_profit = diff[candidate_idx]
                
        return max_profit
