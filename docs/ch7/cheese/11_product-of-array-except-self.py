from typing import List


# Runtime 284ms / Memory 22.2MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, end, result = [], [], []
        mul_front, mul_end = 1, 1;

        for i in range(len(nums) - 1):
            mul_front *= nums[i];
            mul_end *= nums[len(nums) - i - 1]
            front.append(mul_front)
            end.append(mul_end)

        for i in range(len(nums)):
            mul = 1
            if i > 0:
                mul *= front[i - 1]
            if len(nums) - i - 1 > 0:
                mul *= end[len(nums) - i - 2]
            result.append(mul)

        return result

