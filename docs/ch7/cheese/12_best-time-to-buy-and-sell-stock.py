from typing import List


# Runtime 992ms / Memory 25.2 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], 0
        max_value = 0

        for i, n in enumerate(prices):
            if buy > n:
                buy = n
                sell = 0
            elif i is not 0 and sell < n:
                sell = n

            if max_value < sell - buy:
                max_value = sell - buy

        return max_value

