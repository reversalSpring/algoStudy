# https://leetcode.com/problems/array-partition-i/
from typing import List

"""
Given an integer array nums of 2n integers, 
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. 
Return the maximized sum.

Constraints:
- 1 <= n <= 104
- nums.length == 2 * n
- -104 <= nums[i] <= 104

"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 정렬된 후에는 항상 짝수번째에 작은 값이 위치한다 
        sum = 0
        nums.sort()
        nums_len = len(nums)
        
        for i in range(0, nums_len, 2):
            sum += nums[i]
        
        return sum

s = Solution()
case = [1, 4, 3, 2]
print(s.arrayPairSum(case))