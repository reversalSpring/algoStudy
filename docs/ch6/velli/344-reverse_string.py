from typing import List


class Solution:
    # 208ms
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    # 188ms
    def reverseString2(self, s: List[str]) -> None:
        s.reverse()


if __name__ == "__main__":
    solution = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    solution.reverseString(s1)
    print(s1)

    s2 = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s2)
    print(s2)