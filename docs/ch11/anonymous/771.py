from collections import Counter 
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def first(self, jewels: str, stones: str) -> int:
        # https://docs.python.org/ko/3/library/stdtypes.html?highlight=dict#dict
        jewels_dict = {}
        ans = 0
        for jewel in jewels:
            jewels_dict[jewel] = True

        for stone in stones:
            if stone in jewels_dict:
                ans += 1
        
        return ans

    def second(self, jewels: str, stones: str) -> int:
        # https://docs.python.org/ko/3/library/collections.html?highlight=counter#collections.Counter
        c = Counter(stones)
        ans = 0
        for jewel in jewels:
            if jewel in c:
                ans += c[jewel]

        return ans
    
    def third(self, jewels: str, stones: str) -> int:
        ans = 0
        for stone in stones:
            if stone in jewels:
                ans += 1
        
        return ans
    
    def fourth(self, jewels: str, stones: str) -> int:
        count = 0
        for c in jewels:
            if c in stones:
                count += stones.count(c) 
        return count


s = Solution()
print(s.fourth('aA', 'aAAbbb'))