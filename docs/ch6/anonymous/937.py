from typing import Optional, Any, List, Tuple
# https://leetcode.com/problems/reorder-data-in-log-files/
"""
logs: 공백으로 구별되는 문자열
1. 식별자 다음의 각 단어는 소문자로 구성되거나: letter-logs
2. 식별자 다음의 각 단어는 숫자로만 구성된다: digit-logs
식별자 다음에 최소한 한 단어 있다

로그를 재정렬하여 문자 로그가 앞에 오도록 한다
문자 로그는 식별자 무시하고 사전순으로 정렬
모두 같은 순서일 경우에는 식별자로 정렬
숫자 로그는 원래 순서대로 유지
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        # 1. 숫자 로그인지 문자 로그인지 구별하여 정리
        for log in logs:
            logSplitted = log.split()
            
            if logSplitted[1].isnumeric() :
                digitLogs.append(log)
            else :
                letterLogs.append(log)

        # python3에서 cmp 함수는 deprecated
        letterLogs.sort(key = self.sortLog)

        return letterLogs + digitLogs
    

    # 2. 우선 로그 내용으로 정렬하고, 차순위로 식별자로 정렬
    def sortLog(self, log: str) -> Tuple[List[str], str] :
        logSplitted = log.split()

        return logSplitted[1:], logSplitted[0]
    

s = Solution()
logs =  ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs =  ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
a = s.reorderLogFiles(logs)
print(a)
