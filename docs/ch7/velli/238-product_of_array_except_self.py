from typing import List
import collections

class Solution:
    # 312 ms, 21.8 MB (10.08%)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1, len(nums)):
            left.append(nums[i - 1] * left[i - 1])

        right = collections.deque([1])
        for i in range(1, len(nums)):
            right.appendleft(nums[len(nums) - i] * right[0])

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result

    # 228 ms, 21.1 MB (94.07%)
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out



if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    print(s.threeSum([]))
    print(s.threeSum([0]))