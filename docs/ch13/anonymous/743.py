# https://leetcode.com/problems/network-delay-time/

from typing import *
import collections
import heapq

class Solution:
    """ 
    [
        [1, 2, 1],
        [2, 1, 3]
    ]
    2
    2
    실패
    """
    def first_failed(self, times: List[List[int]], n: int, k: int) -> int:
        result = [None] * n
        # k를 찾는다
        loop_cnt = 0
        queue = [k]
        while queue and loop_cnt < n:
            node_curr = queue.pop(0)
            for node in times:
                if node[0] == node_curr:
                    queue.append(node[1])
                    if result[loop_cnt]:                        
                        result[loop_cnt].append(node[2])
                    else:
                        result[loop_cnt] = [node[2]]
                    
            loop_cnt += 1
        ans = 0
        print(result)
        for values in result:
            if values is not None:
                ans += max(values)

        if ans == 0:
            return -1
        else:
            return ans


    def second(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        # 인접 리스트 생성
        for node, node_next, time in times:
            # 소요 시간을 계속 추적해야 하므로, tuple로 관리
            if node in graph:
                graph[node].append((node_next, time))
            else:
                graph[node] = [(node_next, time)]
        # print(graph)
        
        loop_cnt = 0
        # 인접한 노드들을 탐색하기 위한 큐
        # (k까지, 소요되는 시간) 튜플로 저장
        queue = [(k, 0)]
        # ~까지의 시간을 저장하기 위한 딕셔너리
        time_to = {k:0} # 시작 지점의 시간은 처음에 셋팅해 둔다
        while queue:
            # 현재 정점
            node_curr = queue.pop(0)
            vertex_curr = node_curr[0]
            # 현재 정점 방문 표시
            time_accumulative = node_curr[1]

            if vertex_curr in graph:
                for node_next in graph[vertex_curr]:
                    # 인접 노드
                    vertex_next = node_next[0]
                    # 방문한 적이 있어도, 축적된 값이 더 작으면 그 값으로 치환할 수 있어야 한다
                    # 그렇다면 "다음 정점이 다시 이전 정점을 가리키면서 무한 반복하는 것 방지"은 어떻게?
                    time_next = node_next[1]
                    # 시간을 축적해 간다
                    time_accumulative_new = time_accumulative + time_next

                    if vertex_next in time_to:
                        # 새로 축적된 시간이 기존 시간보다 작으면 더 작은 값으로 바꾼다
                        if time_accumulative_new < time_to[vertex_next]:
                            time_to[vertex_next] = time_accumulative_new
                            # 더 적은 시간이 발견되면 해당 노드 탐색하도록 추가한다
                            queue.append((vertex_next, time_accumulative_new))
                    else:
                        # 새로 축적된 시간없으면 저장
                        time_to[vertex_next] = time_accumulative_new
                        # 신규 노드 탐색하도록 추가한다
                        queue.append((vertex_next, time_accumulative_new))
        # print(time_to)
        if len(time_to) == n:
            return max(time_to.values())
        else:
            return -1


    def answer(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        """ 
        그래프 인접 리스트 구성
        {
            3: [(1, 5), (2, 2), (4, 1)], 
            2: [(1, 2)], 
            4: [(5, 1)], 
            5: [(6, 1)], 
            6: [(7, 1)], 
            7: [(8, 1)], 
            8: [(1, 1)]
        }
        """
        for node, node_next, time_next in times:
            graph[node].append((node_next, time_next))
        
        # 시작 노드
        start = k
        Q = [(0, start)]
        # 거리를 저장해두 기위한 딕셔너리
        distance = collections.defaultdict(list)
        
        # BFS지만, 최소 힙을 사용하여 시간이 작은 값부터 확인한다
        while Q:
            # https://docs.python.org/3/library/heapq.html
            # time이 가장 작은 원소를 꺼낸다
            time, node_curr = heapq.heappop(Q)
            print('pop: ', (time, node_curr))
            if node_curr not in distance:
                # node까지의 거리에 소요되는 시간
                distance[node_curr] = time
                for node_next, time_next in graph[node_curr]:
                    time_total = time + time_next
                    print('push: ', (time_total, node_next))
                    # https://docs.python.org/3/library/heapq.html#basic-examples
                    # 첫번째 인자 시간(alt)을 최소값으로
                    heapq.heappush(Q, (time_total, node_next))
                # print('distance: ', distance)
        
        # 모든 노드 방문했는지 여부 확인
        if len(distance) == n:
            return max(distance.values())
        else:
            return -1

s = Solution()
case1 = [[2, 1, 1],[2, 3, 1],[3, 4, 1]]
case2 = [[1,2,1],[2,1,3]]
case3 = [[1,2,1],[2,3,2],[1,3,2]]
case4 = [[1,2,1],[2,3,2],[1,3,4]]
case5 = [[3, 1, 5],[3, 2, 2],[2, 1, 2],[3, 4, 1],[4, 5, 1],[5, 6, 1],[6, 7, 1],[7, 8, 1],[8, 1, 1]]
case6 = [[1,2,1],[2,1,3]]
case7 = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
print(s.second(case1, 4, 2)) # expected: 2
print(s.second(case3, 3, 1)) # expected: 2
print(s.second(case3, 3, 2)) # expected: -1
print(s.second(case4, 3, 1)) # expected: 3
print(s.second(case5, 8, 3)) # expected: 5
print(s.second(case6, 2, 2)) # expected: 3
print(s.second(case7, 3, 2)) # expected: 6

"""
{
    3: [(1, 5), (2, 2), (4, 1)], 
    2: [(1, 2)], 
    4: [(5, 1)], 
    5: [(6, 1)], 
    6: [(7, 1)], 
    7: [(8, 1)], 
    8: [(1, 1)]
}

pop:  (0, 3)
push:  (5, 1)
push:  (2, 2)
push:  (1, 4)
distance:  defaultdict(<class 'list'>, {3: 0})
pop:  (1, 4)
push:  (2, 5)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1})
pop:  (2, 2)
push:  (4, 1)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1, 2: 2})
pop:  (2, 5)
push:  (3, 6)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1, 2: 2, 5: 2})
pop:  (3, 6)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1, 2: 2, 5: 2, 6: 3})
pop:  (4, 1)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1, 2: 2, 5: 2, 6: 3, 1: 4})
pop:  (4, 7)
push:  (5, 8)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1, 2: 2, 5: 2, 6: 3, 1: 4, 7: 4})
pop:  (5, 1)
pop:  (5, 8)
push:  (6, 1)
distance:  defaultdict(<class 'list'>, {3: 0, 4: 1, 2: 2, 5: 2, 6: 3, 1: 4, 7: 4, 8: 5})
pop:  (6, 1)
5
"""
