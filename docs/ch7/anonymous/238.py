from typing import List
# https://leetcode.com/problems/product-of-array-except-self/
"""
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Constraint: 
It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) 
fits in a 32 bit integer.

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        p = 1
        for i in range(0, len(nums)):
            left.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            left[i] = left[i] * p
            p = p * nums[i]
        
        return left
    
s = Solution()
case = [1,2,3,4]
print(s.productExceptSelf(case))