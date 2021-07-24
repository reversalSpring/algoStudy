from typing import List
# https://leetcode.com/problems/group-anagrams/
"""
문자열의 배열 strs가 주어졌을 때, 애나그램으로 그룹
순서는 상관 없다
애나그램은 문자를 다른 순서 또는 구로 재정렬한 것으로, 보통 원래 문자를 정확히 한번씩 사용
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        preprocessDict = dict()
        for s in strs:
            tmp = sorted(s)
            tmp = "".join(tmp)
            
            if tmp in preprocessDict:
                preprocessDict[tmp].append(s)
            else :
                preprocessDict[tmp] = [s]

        return preprocessDict.values()


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
ans = s.groupAnagrams(strs = strs)
print(ans)



