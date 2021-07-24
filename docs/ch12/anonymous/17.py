# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

- 조건
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
from typing import *

class Solution:
    digits = ""
    result = []
    numbers = {
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': ['+'],
        '*': [],
        '#': []
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.result = []
        if not self.digits:
            return self.result    

        self.dfs(0, "")

        return self.result

    def dfs(self, idx, path):
        if len(path) == len(self.digits):
            self.result.append(path)
            return

        for i in range(idx, len(self.digits)):
            for j in self.numbers[self.digits[i]]:
                self.dfs(i + 1, path + j)


s = Solution()
digits = "23"
print(s.letterCombinations(digits))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]


digits = ""
# []

digits = "2"
# ["a","b","c"]
print(s.letterCombinations(digits))
