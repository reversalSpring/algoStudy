from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in strs:
            output[''.join(sorted(i))].append(i)
        
        # list 불필요
        # ex) output.values()
        return list(output.values())

if __name__ == "__main__":
    solution = Solution()

    input_str_list1 = ["eat","tea","tan","ate","nat","bat"]

    print(solution.groupAnagrams(input_str_list1))

