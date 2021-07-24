# https://leetcode.com/problems/permutations/

'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from typing import *
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = [nums[:]]
        # https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        def do_permutation(nums_curr, nums_len):
            # 오름차순인 부분이 있는지 탐색
            # 1. 1 6 7 3 5 4 2
            idx1 = nums_len - 1
            while idx1 > 0 and nums_curr[idx1 - 1] >= nums_curr[idx1]:
                idx1 -= 1

            # 2. idx1이 0보다 작으면 모두 내림차순으로 종료 케이스
            if idx1 <= 0:
                return False

            # 3. 찾아낸 오름차순인 수보다 큰 수가 우측에 있으면, `다음 내림차순` 준비
            idx2 = nums_len - 1
            while nums_curr[idx2] <= nums_curr[idx1 - 1]:
                idx2 -= 1

            # 다음 내림차순 위한 치환
            # 4. 1 6 7 4 5 3 2
            nums_curr[idx1 - 1], nums_curr[idx2] = nums_curr[idx2], nums_curr[idx1 - 1]

            # 다음 내림차순이 시작된 후 idx1과 idx2 사이의 숫자는 다시 정순으로 정렬되어야 다음 순열이 진행되므로, 뒤집는다
            # 5. 1 6 7 4 2 3 5
            idx2 = nums_len - 1
            while idx1 < idx2:
                nums_curr[idx1], nums_curr[idx2] = nums_curr[idx2], nums_curr[idx1]
                idx1 += 1
                idx2 -= 1
                
            ans.append(nums_curr[:])
            
            return True
        
        while result := do_permutation(nums, len(nums)):
            continue
        
        return ans
    
    def second(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_len = len(nums)
        '''
        nums: 원본 배열. 요소를 계속 붙여 나가야 하므로 계속 전달
        permutaion: 순열을 만들어 나갈 배열
        depth: 백 트래킹 조건
        '''
        def dfs(nums, permutaion, depth):
            # 배열의 길이만큰 깊어지면 종료
            if depth == nums_len:
                ans.append(permutaion[:])
                return

            for num in nums:
                if not num in permutaion:
                    """
                    permutaion.append(num) (X) 
                        - append를 하면 기존 permutation에 추가되고, 유지된다. 
                        - 리프 노드에서 백 트래킹 후 기존 permutation 배열이 있어야 하므로, 전달 시에는 새로운 배열로 넘긴다
                    """
                    dfs(nums, permutaion + [num], depth + 1)

        dfs(nums, [], 0)

        return ans

    def third(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))        

s = Solution()
case = [1, 2, 3, 4]

print(s.permute(case))
print(s.second(case))
print(s.third(case))