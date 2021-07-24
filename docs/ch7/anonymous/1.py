from typing import List
# https://leetcode.com/problems/two-sum/

class Solution:
    # 536 ms
    # Brute force 방식
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums_len = len(nums)
        if nums_len > 0 :
            for i in range(0, nums_len, 1):
                for j in range(i + 1, nums_len, 1):
                    sum = nums[i] + nums[j] 
                    if sum == target :
                        ans.append(i)
                        ans.append(j)
                        break
                    
        return ans
    
    # 48 ms
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        ans = []
        # a + b = target
        # b = target - a
        for i, num in enumerate(nums):  # n
            tmp = target - num
            if tmp in nums[i + 1:]:  # n 
                return [i, nums[i+1:].index(tmp) + (i + 1)] # O(n^2)

        return ans

    # 44 ms
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        ans = []
        # a + b = target
        # b = target - a
        # 추가로 key로 idx를 찾을 수 있도록 개선
        nums_dict = {}
        # enumerate는 한번 순회할 수 있는 iterator를 반환하므로 이런 식으로 재사용 불가
        for idx, num in enumerate(nums):
            # 조건상 정답은 하나만 있어야 하므로, 같은 수가 3개 이상인데 같은 수를 더해서 target을 구하는 케이스는 없다
            # [1, 3, 3, 3], 6 또는 [1, 3, 3, 3], 4 같은 케이스는 없다
            nums_dict[num] = idx
  
        for idx, num in enumerate(nums):
            tmp = target - num
            if tmp in nums_dict and idx != nums_dict[tmp]:
                ans.append(idx)
                ans.append(nums_dict[tmp])
                break

        return ans

    # 72 ms
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        ans = []
        # a + b = target
        # b = target - a
        # 추가로 key로 idx를 찾을 수 있도록 개선
        nums_dict = {}
        # 반복문을 하나로
        for idx, num in enumerate(nums):
            # 하지만 시간이 더 오래 걸린다
            # [1, 2, 3], 4인 경우
            # tmp = 4 - 1 = 3 없음
            # tmp = 4 - 2 = 2 없음
            # tmp = 4 - 3 = 1 있음
            tmp = target - num
            if tmp in nums_dict:
                return [nums_dict[tmp], idx]
            nums_dict[num] = idx

        return ans
    
    # 포인터 이용하는 경우 시작/끝이 좁혀지는 조건이 있어야 하는데,
    # nums가 정렬되지 않은 상태이므로 작다/크다로는 조건을 줄 수 없다
    # 그리고 nums의 각 요소에 따라 모두 비교한다면, for문을 사용하는 것과 다름이 없다


s = Solution()
case = [2, 7, 11, 15]
target = 9
# case = [3, 2, 4]
# target = 6
# case = [3, 3]
# target = 6
case = [1, 2, 3]
target = 4
ans = s.twoSum4(case, target)
print(ans)

