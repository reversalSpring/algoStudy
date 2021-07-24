# https://leetcode.com/problems/longest-palindromic-substring/
"""
Given a string s, return the longest palindromic substring in s.
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        # 가장 긴 팰린드롬 부분 문자열.
        # 1. 부분 문자열에서 팰린드롬 있는지 파악해야 하고
        #   - 팰린드롬: 각 첫부분과 끝부분부터 시작하여 서로 같음
        # 2. 그게 가장 긴지 알아야 한다


        return ans

    def my_longestPalindrome(self, s: str) -> str:
        ans = ''
        s = "".join(s.split())
        print(s)
        s_len = len(s)
        longestPalindrome = s[0]
        longestPalindromeEnd = s_len - 1
        longestPalindromeMax = 0
        longestPalindromeStart = 0

        for i, c in enumerate(s):
            start = i
            start_old = start
            end = s_len - 1
            end_old = 0
            is_palindrome = False
            is_started = False
            loop_cnt = 0
            if end - start < longestPalindromeMax:
                break 
            
            while start < end:
                first = s[start]
                last = s[end]

                if first != last:
                    if is_started:
                        end = end_old
                        start = start_old
                        loop_cnt = 0
                        is_started = False
                        is_palindrome = False
                        longestPalindromeEnd = s_len - 1
                        longestPalindromeStart = 0
                    else:
                        end -= 1

                    continue
                else :
                    if loop_cnt == 0:
                        longestPalindromeStart = start
                        longestPalindromeEnd = end 
                        is_started = True
                        # 다음에 다시 시작할 end 지점
                        end_old = end - 1

                    if is_started: 
                        is_palindrome = True
                        loop_cnt += 1
                        start += 1
                        end -= 1

            if is_palindrome:
                if longestPalindromeMax < (longestPalindromeEnd - longestPalindromeStart):
                    longestPalindromeMax = longestPalindromeEnd - longestPalindromeStart
                    longestPalindrome = "".join(s[longestPalindromeStart:longestPalindromeEnd+1])

        return longestPalindrome

    def second(self, s: str) -> str:
        ans = ''
        s_len = len(s)
        mid = s_len // 2
        if mid == 0:
            return s
        
        s_sub_palindrome = ''
        s_sub_palindrome_len = 0
        loop_cnt = 0
        # 중앙을 기점으로 하지 말고 제일 앞에서부터 끝까지 모두 훑어보자
        target = s[loop_cnt]
        while loop_cnt < s_len:
            '''
            baaaabb -> baaaab
            baaabb -> baaab
            '''
            print('target: ', target, ', loop_cnt: ', loop_cnt)
            idx_curr = loop_cnt
            # `aba`: 좌/우에 문자 있고 left와 right는 같고 start는 다른 경우
            if idx_curr - 1 >= 0 and idx_curr + 1 < s_len:
                loop_cnt_to_add = 1
                idx_left = idx_curr - 1
                idx_right = idx_curr + 1
                is_palindrome = False
                while idx_left >= 0 and idx_right < s_len:
                    if s[idx_left] == s[idx_right]:
                        idx_left -= 1
                        idx_right += 1
                        is_palindrome = True
                    else:
                        break
                tmp_len = idx_right - idx_left + 1
                print('[case1] idx_right: ', idx_right, ', idx_left: ', idx_left, 'tmp_len: ', tmp_len, ', sub str: ', s[idx_left:idx_right + 1])
                if is_palindrome and s_sub_palindrome_len < tmp_len:
                    s_sub_palindrome_len = tmp_len
                    s_sub_palindrome = s[idx_left + 1:idx_right]
                    target = s[loop_cnt]

                idx_left = idx_curr
                idx_right = idx_curr + 1
                is_palindrome = False
                while idx_left >= 0 and idx_right < s_len:
                    if s[idx_left] == s[idx_right]:
                        idx_left -= 1
                        idx_right += 1
                        is_palindrome = True
                    else:
                        break
                
                tmp_len = idx_right - idx_left + 1
                print('[case2] idx_right: ', idx_right, ', idx_left: ', idx_left, 'tmp_len: ', tmp_len, ', sub str: ', s[idx_left:idx_right + 1])
                if is_palindrome and s_sub_palindrome_len < tmp_len:
                    s_sub_palindrome_len = tmp_len
                    s_sub_palindrome = s[idx_left + 1:idx_right]
                    loop_cnt_to_add = 2

                loop_cnt += loop_cnt_to_add
                target = s[loop_cnt]
            else:
                if s_sub_palindrome_len == 0:
                    s_sub_palindrome = target
                loop_cnt += 1
                if loop_cnt < s_len:
                    target = s[loop_cnt]
        ans = s_sub_palindrome

        return ans

    def third(self, s: str) -> str:
        ans = ''
        s_len = len(s)
        # 문자열이 1개면 굳이 아래 로직 따를 필요 없다
        if s_len == 1:
            return s

        palindrome_len = 0
        loop_cnt = 0
        # 중앙을 기점으로 하지 말고 제일 앞에서부터 끝까지 모두 훑어보자
        target = s[loop_cnt]
        while loop_cnt < s_len:
            # 초기값 설정. 이걸 하지 않으면 아래에서 `ac` 같은 경우 빈 값으로 나온다
            if palindrome_len == 0 and loop_cnt == 0:
                ans = target

            idx_left = loop_cnt - 1
            idx_right = loop_cnt + 1
            is_palindrome = False
            while idx_left >= 0 and idx_right < s_len:
                if s[idx_left] == s[idx_right]:
                    is_palindrome = True
                    idx_left -= 1
                    idx_right += 1
                else:
                    break
            
            if is_palindrome:
                tmp_len = idx_right - idx_left + 1
                if palindrome_len < tmp_len:
                    palindrome_len = tmp_len
                    # while문 안에서 is_palindrome 체크하고 left 및 right로 이동하므로, 
                    # break된 후에는 각각 이전 포인터를 인덱스로 삼아야 한다
                    ans = s[idx_left + 1:idx_right]

            idx_left = loop_cnt
            idx_right = loop_cnt + 1
            is_palindrome = False
            while idx_left >= 0 and idx_right < s_len:
                if s[idx_left] == s[idx_right]:
                    is_palindrome = True
                    idx_left -= 1
                    idx_right += 1
                else:
                    break
            
            if is_palindrome:
                tmp_len = idx_right - idx_left + 1
                if palindrome_len < tmp_len:
                    palindrome_len = tmp_len
                    ans = s[idx_left + 1:idx_right]

            loop_cnt += 1
            if loop_cnt < s_len:
                target = s[loop_cnt]
            else:
                break

        return ans


s = Solution()

test_cases = [
    {'case': 'babad', 'extected': 'bab'},
    {'case': 'cbbd', 'extected': 'bb'},
    {'case': 'a', 'extected': 'a'},
    {'case': 'ac', 'extected': 'a'},
    {'case': 'bb', 'extected': 'bb'},
    {'case': 'xaabacxcabaaxcabaax', 'extected': 'xaabacxcabaax'},
    {'case': 'abbbddedssdeeaaas', 'extected': 'edssde'},
    {'case': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'extected': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'},
]

print(s.third('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))



