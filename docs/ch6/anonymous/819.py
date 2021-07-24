import re
from typing import List
from collections import Counter
# https://leetcode.com/problems/most-common-word/
"""
문장과 금지된 단어 목록이 주어졌을 때, 금지되지 않은 단어중 가장 흔한 단어 반환
금지된 단어 목록에서 단언느 소문자이며, 구두점이 없다.
문장에서 단어는 대소문자 구별하지 않으며, 소문자로 반환
# 조건
1 <= paragraph.length <= 1000.
0 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase 
(even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ans = ''
        # 1. 알파벳 아닌 것 삭제
        regex = re.compile(r'[^\w]')
        pragraphCleaned = regex.sub(' ', paragraph).lower().split()
        wordsList = []
        for word in pragraphCleaned:
            if word not in banned:
                wordsList.append(word)

        c = Counter(wordsList)

        return c.most_common(1)[0][0]

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
ans = s.mostCommonWord(paragraph = paragraph, banned = banned)
print(ans)