# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import * 
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 원점에서 K 번 가까운 점 목록을 순서대로 출력
        # 거리 순으로 정렬

        heap = []
        for x, y in points:
            # dist = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
            # 거리 계산을 모두 정확하게 할 필요는 없다
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        
        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result

    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]*x[0]+x[1]*x[1])[:K]

    def kClosest3(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y) # 음수로 확인
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]

s = Solution()
print(s.kClosest3([[1,3],[-2,2]], 1))
print(s.kClosest3([[3,3],[5,-1],[-2,4]], 2))