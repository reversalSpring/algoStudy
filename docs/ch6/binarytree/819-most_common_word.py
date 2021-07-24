from typing import List
from collections import defaultdict
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        output = defaultdict(int)

        # 리스트 컴프리헨션으로 축약 가능 
        # word = [word for word in re.sub(r'[^/w]', ' ', paragraph).lower().split() if word not in banned]
        paragraph = paragraph.lower()
        paragraph_to_word = re.sub('[^a-z]',' ',paragraph).split()
        
        for i in paragraph_to_word:
            if i not in banned:
                output[i] += 1

        #count로 가능 
        # ex) counts = collections.Counter(output)
        #     return counts.most_common(1)[0][0]
        return max(output.keys(), key=(lambda k: output[k]))
        

if __name__ == "__main__":
    solution = Solution()

    input_str = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned_list = ["hit"]

    print(solution.mostCommonWord(input_str1, banned))

