# https://leetcode.com/problems/cheapest-flights-within-k-stops/

""" 
There are n cities connected by m flights. 
Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. 
If there is no such route, output -1.

m개의 항공편으로 연된 n 개의 도시
각 항송편은 u 도시에서 출발하여 v에 도착(각격은 w)
src에서 시작하여 dst에 도착한다고 할 때 최대 k번 내에 도착하는, 가장 저렴한 가격
"""

from typing import *
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        """
        인접 리스트 생성
        {
            0: [(1, 100), (2, 500)], 
            1: [(2, 100)]
        }
        """
        for city_start, city_arrive, price in flights:
            graph[city_start].append((city_arrive, price))

        layover_cnt = 0
        # (가격, 시작 도시, 경유 수)
        Q = [(0, src, layover_cnt)]
        while Q:
            price, city_arrive, layover_cnt = heapq.heappop(Q)
            if city_arrive == dst:
                return price
            if layover_cnt <= K:
                layover_cnt += 1
                for city_arrive_next, price_next in graph[city_arrive]:
                    price_total = price + price_next
                    heapq.heappush(Q, (price_total, city_arrive_next, layover_cnt))
                    print('from ', city_arrive, ' to ', city_arrive_next, '(', layover_cnt - 1, ')', ' with ', price_total)
        return -1

s = Solution()

case = [[0,1,100],[1,2,100],[0,2,500]]
print(s.findCheapestPrice(3, case, 0, 2, 1))
"""
from  0  to  1 ( 0 )  with  100
from  0  to  2 ( 0 )  with  500
from  1  to  2 ( 1 )  with  200
200
"""
case = [[0,1,100],[1,2,100],[0,2,500]]
print(s.findCheapestPrice(3, case, 0, 2, 0))
"""
from  0  to  1 ( 0 )  with  100
from  0  to  2 ( 0 )  with  500
500
"""
