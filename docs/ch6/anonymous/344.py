from typing import List

# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

s: Solution = Solution()
case = ["h", "e", "l", "l", "o"]
case = ["h", "e", "l", "x", "l", "o"]
case = [""]
s.reverseString(case)
print(case)
        