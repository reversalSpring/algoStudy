# [7-11] 238. Product of Array Except Self

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(nums[i-1] * left[i-1])
        
        
        right = collections.deque([1])
        for i in range(1, len(nums)):
            right.appendleft(nums[len(nums)-i] * right[0])
        
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        
        return result
```
a   b   c   d

| 1     | a   | a*b | a*b*c |
|-------|-----|-----|-------|
| b*c*d | c*d | d   | 1     |



# [7-12] 121. Best Time to Buy and Sell Stock
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMax = 0
        result = 0
        
        for i in range(len(prices)-1):
            localMax += prices[i+1] - prices[i]
            localMax = max(localMax, 0)
            result = max(localMax, result)
            
        return result
```
풀이에서는 최저점을 찾고 그 안에서 최대 수익을 찾는 방식
비슷하지만 수익과 손실을 계속 계산해가는 방식으로 풀이. 그러나 수익이 -(마이너스)가 되면 다시 시작하는 방식이다.


## 책 풀이
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit
```
