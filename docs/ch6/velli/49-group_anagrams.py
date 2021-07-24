from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            sorted_tuple = tuple(sorted(s))
            if mapping.get(sorted_tuple) is not None:
                mapping[sorted_tuple].append(s)
            else:
                mapping[sorted_tuple] = []
                mapping[sorted_tuple].append(s)

        result = []
        for v in mapping.values():
            result.append(v)

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))