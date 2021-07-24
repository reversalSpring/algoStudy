# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        sLen = len(s)
        if sLen == 0:
            return True
        
        a: bool = False
        s = s.lower()
        start = 0
        end = sLen - 1
        loopCnt: int = 0 
        while start <= end :
            if not s[start].isalnum():
                start += 1
                continue
            elif not s[end].isalnum():
                end -= 1
                continue
            else :
                if s[start] == s[end]:
                    a = True
                    loopCnt += 1
                    start += 1
                    end -= 1
                else :
                    loopCnt += 1
                    a = False
                    break
        
        if loopCnt == 0: 
            a = True

        return a

s= Solution()
case: str = "1b1"
a = s.isPalindrome(s = case)
print(a)
