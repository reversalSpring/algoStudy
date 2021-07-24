import timeit
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        
        def recursion(nums, start, end):
            if end < start:
                return -1

            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1
            
            mid = start + ((end - start) // 2)

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                return recursion(nums, mid + 1, end)
            else:
                return recursion(nums, start, mid - 1)
        
        ans = recursion(nums, 0, len(nums) - 1)

        return ans

    # 책 풀이
    def search_recursion(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target: 
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)
    
    def search_loop(self, nums: List[int], target: int) -> int:
        ans = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target: # 우측에 있다
                left = mid + 1
            elif nums[mid] > target: # 좌측에 있다
                right = mid - 1
            else:
                return mid

        return -1

    def search_module(self, nums: List[int], target: int) -> int:
        ans = -1
        import bisect
        # target을 삽입할 인덱스를 반환
        # target이 이미 존재하면, 이미 존재하는 가장 좌측의 target 앞에 삽입
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1

    def search_by_index(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

s = Solution()

print(timeit.timeit(lambda: s.search([-1,0,3,5,9,12], 9), number=10000)) # 0.009751099999999999
print(timeit.timeit(lambda: s.search_recursion([-1,0,3,5,9,12], 9), number=10000)) # 0.008811400000000011
print(timeit.timeit(lambda: s.search_loop([-1,0,3,5,9,12], 9), number=10000)) # 0.008394699999999991
print(timeit.timeit(lambda: s.search_module([-1,0,3,5,9,12], 9), number=10000)) # 0.007204000000000002
print(timeit.timeit(lambda: s.search_by_index([-1,0,3,5,9,12], 9), number=10000)) # 0.0043739. 하지만 O(n)