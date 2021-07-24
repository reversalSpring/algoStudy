class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            if not str.isalnum(s[i]):
                i += 1
                continue

            if not str.isalnum(s[j]):
                j -= 1
                continue

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        import collections
        dequeue = collections.deque()

        for char in s:
            if char.isalnum():
                dequeue.append(char)

        while len(dequeue) > 1:
            if dequeue.pop() != dequeue.popleft():
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome("0P"))
