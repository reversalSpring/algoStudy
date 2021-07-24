from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?',;.]", ' ', paragraph.lower())
        word_list = paragraph.replace('  ', ' ').split(' ')
        mapping = Counter(word_list)
        print(mapping)
        for word, count in mapping.most_common():
            if word in banned:
                continue
            return word




if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))