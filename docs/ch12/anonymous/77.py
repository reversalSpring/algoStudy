# https://leetcode.com/problems/combinations/
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
'''
from typing import *
import collections
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        numbers = [i for i in range(1, n + 1)]

        def dfs(numbers, combination, depth):
            # 조합하려는 k개가 완성되면 종료
            if len(combination) == k:
                ans.append(combination)
                return
            
            # 숫자들을 비워 나간다
            while numbers:
                number = numbers.pop(0)
                # 참조로 넘어가지 않도록 새로운 배열 생성하여 전달
                dfs(numbers[:], combination + [number], depth + 1)

        dfs(numbers, [], 0)
        return ans

    def combine2(self, n: int, k: int) -> List[List[int]]:
        numbers = [i for i in range(1, n + 1)]
        return list(itertools.combinations(numbers, k))

s = Solution()

print(s.combine(4, 2))
print(s.combine(5, 3))
print(s.combine2(5, 3))