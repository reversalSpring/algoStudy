from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMax = 0
        result = 0

        for i in range(len(prices) - 1):
            localMax += prices[i + 1] - prices[i]
            localMax = max(localMax, 0)
            result = max(localMax, result)

        return result

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit
